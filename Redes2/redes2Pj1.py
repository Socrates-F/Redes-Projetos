import socket           # Utilizar sockets de rede
import random           # Gerar números aleatórios para as portas
import struct           # Manipulação dos dados binários
import time             # Manipulação de tempo
import geoip2.database  # Acesso ao banco de dados GeoIP


__all__ = ['Tracer']

class Tracer(object):
    def __init__(self, dst, hops=30, geoip_db_path='GeoLite2-City.mmdb'):
        """
        Identificando Args:
            dst (str): Host de destino.
            hops (int): Número máximo de saltos.
            geoip_db_path (str): Caminho para o banco de dados GeoIP.
        """
        self.dst = dst
        self.hops = hops
        self.ttl = 1
        self.geoip_db_path = geoip_db_path

        # É escolhido uma porta aleatório num intervalo:    
        self.port = random.choice(range(33434, 33535))

        # Inicializando o leitor GeoIP
        try:
            print(f"Tentando abrir o banco de dados GeoIP em {self.geoip_db_path}")  # Depuração
            self.geoip_reader = geoip2.database.Reader(self.geoip_db_path)
            print(f"Banco de dados GeoIP carregado com sucesso de {self.geoip_db_path}")  # Depuração
        except FileNotFoundError:
            raise IOError(f"Não foi possível encontrar o banco de dados GeoIP no caminho: {self.geoip_db_path}")

    def run(self):
        """
        Execuçao do tracer.
        É criada uma exceção para tratar a conversão do nome do host para um endereço IP.
        A mensagem inicial com o destino, IP e o número de saltos e mostrada na tela (print)
        Um loop é executado para enviar os pacotes UDP e receber as respostas ICMP.
        Calcula-se o tempo de resposta e e demonstra-se o resultado para cada salto(print).
        O TTL é incrementado e verifica-se o destino já foi alcançado ou ao máximo de saltos.
        """
        try:
            dst_ip = socket.gethostbyname(self.dst)
        except socket.error as e:
            raise IOError('Não foi possível encontrar o destino {} : {}'.format(self.dst, e))

        text = 'traceroute to {} ({}), {} hops max'.format(
            self.dst,
            dst_ip,
            self.hops
        )

        print(text)

        while True:
            start_time = time.time()
            receiver = self.create_receiver()
            sender = self.create_sender()
            sender.sendto(b'', (self.dst, self.port))

            addr = None
            try:
                data, addr = receiver.recvfrom(1024)
                end_time = time.time()
            except socket.error:
                pass
            finally:
                receiver.close()
                sender.close()

            if addr:
                time_cost = round((end_time - start_time) * 1000, 2)
                location = self.get_geoip(addr[0])
                print('{:<4} {} {} ms {}'.format(self.ttl, addr[0], time_cost, location))
                if addr[0] == dst_ip:
                    break
            else:
                print('{:<4} *'.format(self.ttl))

            self.ttl += 1

            if self.ttl > self.hops:
                break

    def create_receiver(self):
        """
        É criado um socket ICMP receptor.
        E espera o retorno uma instância de socket.
        """
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_RAW,
            proto=socket.IPPROTO_ICMP
        )

        timeout = struct.pack("ll", 5, 0)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        try:
            s.bind(('', self.port))
        except socket.error as e:
            raise IOError('Não foi possível encontrar socket receptor: {}'.format(e))

        return s

    def create_sender(self):
        """
        Cria um socket UDP para envio dos pacotes.
        Retorna também uma instância de socket.
        """
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM,
            proto=socket.IPPROTO_UDP
        )

        s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, self.ttl)

        return s

    def get_geoip(self, ip):
        """
        Obtém a localização geográfica para um endereço IP.
        """
        try:
            response = self.geoip_reader.city(ip)
            country = response.country.name
            city = response.city.name
            latitude = response.location.latitude
            longitude = response.location.longitude
            return f"{city}, {country} (Lat: {latitude}, Lon: {longitude})" if city else f"{country} (Lat: {latitude}, Lon: {longitude})"
        except geoip2.errors.AddressNotFoundError:
            return "Localização desconhecida"
        except Exception as e:
            return f"Erro ao obter localização: {e}"

def main():
    host = input("Digite o host de destino: ")
    max_hops = input("Digite o número máximo de saltos (padrão é 30): ")

    if not max_hops:
        max_hops = 30
    else:
        max_hops = int(max_hops)

    tracer = Tracer(host, max_hops)
    tracer.run()

if __name__ == "__main__":
    main()