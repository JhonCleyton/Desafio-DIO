## README - Sistema Bancário DIO

**Descrição**

Este projeto simula um sistema bancário simples, permitindo que os usuários realizem operações de depósito, saque e consulta de extrato. O sistema também possui algumas funcionalidades extras, como:

* Validação de entrada de dados para garantir que apenas números sejam inseridos nos campos de conta e valor.
* Limite de saques por dia para evitar transações excessivas.
* Exibição de data e hora da transação no extrato.
* Mensagens personalizadas para cada tipo de operação.

**Funcionalidades**

* **Depósito:** Permite depositar qualquer valor positivo na conta do cliente.
* **Saque:** Permite sacar dinheiro da conta do cliente, respeitando o saldo disponível e o limite de saques diário.
* **Extrato:** Mostra o histórico de todas as transações realizadas na conta, incluindo data, hora, tipo de operação e valor.

**Requisitos**

* Python 3 ou superior

**Como usar**

1. Clone o repositório para sua máquina.
2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute o script principal:

```
python main.py
```

4. Siga as instruções na tela para realizar as operações desejadas.

**Exemplo de uso**

```
Digite sua conta: 123456
Digite seu nome Completo: João Silva

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 1

Informe o valor do depósito: 100

Depósito realizado com sucesso!

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 2

Informe o valor do saque: 50

Saque realizado com sucesso!

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 3

20/07/2023 15:44:55

Conta Nº: 123456 - Cliente: João Silva

********************** EXTRATO *************************

Depósito: R$ 100.00
Saque: -R$ 50.00

Saldo: R$ 50.00

_____________________ BANCO DIO __________________________

**Qualquer irregularidade constatada procure o seu gerente

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 0

Obrigado por usar nosso sistema bancário.Tenha um Exelente dia!
```

**Observações**

* Este é um projeto simples para fins didáticos. Não deve ser usado em um ambiente de produção real.
* O sistema não possui mecanismos de segurança para proteger as informações dos usuários.
* O limite de saques e outras configurações podem ser facilmente modificados no código.

**Melhorias**

* Implementar mecanismos de segurança para proteger as informações dos usuários.
* Adicionar mais funcionalidades, como transferências entre contas, pagamento de contas e investimentos.
* Criar uma interface gráfica para facilitar o uso do sistema.

**Contribuições**

Se você tiver sugestões de melhorias ou encontrar algum problema com o sistema, por favor, abra uma issue no repositório do projeto.
