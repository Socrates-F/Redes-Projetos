# Traceroute com GeoIP

Este projeto implementa uma ferramenta de traceroute em Python que não apenas traça a rota para um destino de rede, mas também fornece informações geográficas sobre cada salto (hop) ao longo do caminho.

## Funcionalidades

- **Traceroute tradicional**: Utiliza pacotes UDP e respostas ICMP para mapear a rota até o destino
- **Geolocalização**: Integração com banco de dados GeoLite2 para identificar a localização geográfica de cada IP intermediário
- **Tempo de resposta**: Calcula e exibe o tempo de ida e volta para cada salto
- **Interface interativa**: Permite ao usuário especificar o host de destino e número máximo de saltos

## Como funciona

1. O programa envia pacotes UDP com TTL (Time to Live) incremental
2. Cada roteador ao longo do caminho decrementa o TTL e, quando chega a zero, retorna um pacote ICMP Time Exceeded
3. O programa captura essas respostas e extrai o endereço IP do roteador
4. Consulta o banco de dados GeoIP para obter informações de localização
5. Exibe os resultados formatados com IP, tempo de resposta e localização

## Pré-requisitos

- Python 3.x
- Biblioteca `geoip2`: `pip install geoip2`
- Banco de dados GeoLite2-City (disponível gratuitamente em MaxMind)

## Instalação

1. Clone o repositório ou baixe o arquivo `redes2Pj1.py`
2. Instale a dependência necessária:
   ```bash
   pip install geoip2
3. Baixe o banco de dados GeoLite2-City do site da MaxMind e coloque-o no mesmo diretório do script

## Uso
Execute o script e siga as instruções:

  ```bash
  python redes2Pj1.py
  ```
## Estrutura do código
- `Tracer`: Classe principal que gerencia todo o processo

- `create_receiver()`: Cria socket para receber respostas ICMP

- `create_sender()`: Cria socket para enviar pacotes UDP

- `get_geoip()`: Consulta localização geográfica do IP

- `run()`: Executa o traceroute principal

## Exemplo de saída
```text
traceroute to example.com (93.184.216.34), 30 hops max
1    192.168.1.1    5.23 ms    São Paulo, Brazil (Lat: -23.5, Lon: -46.6)
2    10.0.0.1       12.45 ms   Rio de Janeiro, Brazil (Lat: -22.9, Lon: -43.2)
3    201.20.64.1    25.67 ms   Brasília, Brazil (Lat: -15.8, Lon: -47.9)
...
```
## Limitações
- Requer privilégios de administrador/root para criar sockets raw

- A precisão da geolocalização depende do banco de dados GeoIP utilizado

- Alguns roteadores podem não responder a pacotes ICMP, resultando em saltos não identificados
