## <h1 align="center">App de Vendas de Açaí e Cupuaçu <img align="center" alt="Nickson-Python" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /></h1>


Este é um aplicativo simples para pedidos de açaí e cupuaçu. Os usuários podem escolher o sabor e o tamanho desejados, e o aplicativo calcula o total a pagar.

## Funcionalidades

1. **Escolha do Sabor:**
   - Os usuários podem escolher entre **Cupuaçu (CP)** e **Açaí (AC)**.
   - Se o sabor escolhido não for válido, o aplicativo exibirá uma mensagem de erro.

2. **Escolha do Tamanho:**
   - Os tamanhos disponíveis são **P (Pequeno)**, **M (Médio)** e **G (Grande)**.
   - Se o tamanho escolhido não for válido, o aplicativo exibirá uma mensagem de erro.

3. **Cálculo do Total:**
   - O aplicativo mantém um registro do total a pagar com base nas escolhas do usuário.
   - O preço é determinado pela combinação de sabor e tamanho.

4. **Pedidos Adicionais:**
   - Os usuários podem fazer pedidos adicionais ou finalizar o pedido.
   - O aplicativo pergunta se o usuário deseja pedir mais alguma coisa.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o arquivo `app_vendas_acai_cupuacu.py`.
3. Siga as instruções no terminal para fazer seu pedido.

## Observações

- O aplicativo trata exceções, como interrupção pelo usuário ou erros inesperados.
- Os preços dos sabores estão definidos no dicionário `precos`.
