# 🌐 Servidor TCP com Página HTML

## 📖 Sobre o Projeto
Este projeto implementa um **servidor TCP simples em Python** que responde a requisições HTTP enviando uma página HTML estática (`index.html`).  
O objetivo é demonstrar como funciona a comunicação básica entre cliente e servidor, utilizando **sockets** e servindo conteúdo web sem necessidade de servidores como Apache ou Nginx.

---

## 🎯 Objetivo
- Entender o funcionamento de **sockets TCP/IP** em Python.  
- Implementar um **servidor web minimalista** que responda a requisições GET.  
- Exibir uma **página HTML personalizada** no navegador do cliente.  

---

## 🛠️ Estrutura do Projeto

### 🔹 `ServerTCP.py`
- Cria um servidor TCP que escuta na porta **60000**.  
- Lê o conteúdo do arquivo `index.html`.  
- Responde com **código 200 OK** e o conteúdo da página quando o cliente acessa `/`.  
- Fecha a conexão após o envio da resposta.  
- Inclui tratamento de exceções para encerrar o servidor com segurança.  

### 🔹 `index.html`
- Página HTML exibida pelo servidor.  
- Estrutura estilizada com **CSS embutido**.  
- Conteúdo: informações sobre o **histórico e situação da internet no Brasil**.  
- Inclui cards com ícones (Font Awesome) e descrições, como:
  - Chegada da internet ao Brasil.  
  - Estatísticas de acesso da população.  
  - Velocidade média da internet.  
  - Papel da ANATEL.  

---

## 🚀 Tecnologias Utilizadas
- **Python 3** (módulo `socket`)  
- **HTML5 + CSS3**  
- **Font Awesome** (ícones)  

---

## 📊 Finalidade
Este projeto tem caráter **educacional e didático**, permitindo:  
- Compreender como funciona um servidor TCP básico.  
- Ver na prática a resposta HTTP enviada para o navegador.  
- Aprender a estruturar e servir uma página HTML sem frameworks adicionais.  

É um exemplo introdutório de como a **camada de aplicação da Internet** pode ser construída a partir de sockets simples.

---

