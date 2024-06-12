def nome_do_programa():
    print("""𝗚𝗢𝗡𝗡𝗘 - 𝗖𝗢𝗡𝗧𝗥𝗢𝗟𝗘 𝗗𝗘 𝗘𝗦𝗧𝗢𝗤𝗨𝗘\n""")

def escolher_opcao():
    print('Escolha uma opcao: ')

def cadastro_item():
    print('1. Cadastrar um novo item')

def estoque_atual():
    print('2. Consultar o estoque atual')

def realizar_baixa():
    print('3. Realizar baixa do item')

def inserir_item_estoque():
    print('4. Inserir item no estoque')

def movimentacao_item():
    print('5. Verificar movimentação do item')


def main():
    nome_do_programa()
    escolher_opcao()
    cadastro_item()
    estoque_atual()
    realizar_baixa()
    inserir_item_estoque()
    movimentacao_item()

if __name__ == '__main__':
    main()