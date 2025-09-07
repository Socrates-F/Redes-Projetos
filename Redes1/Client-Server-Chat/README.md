# 💬 Sistema de Chat em Rede – Python (Sockets + Tkinter)

## 📖 Sobre o Projeto
Este projeto implementa um **sistema de chat cliente-servidor** em Python utilizando **sockets TCP/IP** para comunicação e **Tkinter** para a interface gráfica do cliente.  
Ele permite que múltiplos usuários se conectem a um servidor central e troquem mensagens em tempo real.

---

## 🎯 Objetivo
- Criar um ambiente de **comunicação em rede** via **protocolo TCP**.  
- Permitir **mensagens entre múltiplos clientes**, incluindo mensagens privadas direcionadas a um usuário específico.  
- Oferecer uma interface gráfica simples e intuitiva para envio e recebimento de mensagens.  

---

## 🛠️ Estrutura do Projeto

### 🔹 `serverP2.py` – Servidor
- Gerencia todas as conexões de clientes.  
- Recebe e distribui mensagens para os usuários conectados.  
- Mantém dicionários com:
  - **`clients`** → lista de clientes ativos.  
  - **`enderecos`** → endereços IP e portas dos clientes.  
- Implementa:
  - **Broadcast** (mensagem enviada a todos).  
  - **Gerenciamento de saída** ({quit}).  
- Funciona em **multi-thread**, permitindo que vários clientes interajam simultaneamente.

### 🔹 `cliente1.py` – Cliente
- Interface gráfica construída em **Tkinter**.  
- Permite:
  - Informar o **nome de usuário**.  
  - Definir **destinatário, assunto e mensagem**.  
  - Enviar mensagens públicas ou privadas.  
  - Receber e exibir mensagens em uma **caixa de entrada**.  
- Botões para:
  - **Enviar nome**.  
  - **Enviar mensagem**.  
  - **Sair do chat**.  
- Cria uma **thread dedicada para receber mensagens** sem travar a interface.

---

## 🚀 Tecnologias Utilizadas
- **Python 3**  
- **Sockets (TCP/IP)** – comunicação cliente-servidor  
- **Threading** – suporte a múltiplas conexões  
- **Tkinter** – interface gráfica do cliente  

---

## 📊 Finalidade
O projeto serve como exemplo prático de:
- **Comunicação em rede com Python** usando sockets.  
- **Integração entre back-end (servidor)** e **front-end (interface gráfica)**.  
- **Chat multiusuário** com suporte a mensagens privadas.  

É uma base que pode ser expandida para sistemas de mensagens mais complexos, como chats em grupo, envio de arquivos e aplicações colaborativas.

---
