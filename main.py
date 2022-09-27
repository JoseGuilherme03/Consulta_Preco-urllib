import urllib.request


# A função abaixo abre um arquivo texto através da "urllib", lê seus dados, considerando que são do formato UTF-8 e retorna uma string com os dados. Após isso, utiliza o find para encontrar a posição do valor do preço e retorna o valor do preço.
def identifica_preco(url):
    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode("utf-8")
    inicio = texto.find(">$") + 2
    fim = texto.find("</", inicio)
    preco = texto[inicio:fim]
    return float(preco)


def consulta_preco():
    from time import sleep

    valor_minino = 4.70  # Valor mínimo que o produto deve custar para que seja comprado

    while True:
        cliente_comum = identifica_preco("http://beans.itcarlow.ie/prices-loyalty.html")
        cliente_fidelidade = identifica_preco("http://beans.itcarlow.ie/prices.html")

        # Verifica qual o menor valor entre os dois clientes
        menor_valor = (
            cliente_comum if cliente_comum <= cliente_fidelidade else cliente_fidelidade
        )
        # Verifica qual pagina possui o menor valor
        pagina = (
            "cliente comum" if menor_valor == cliente_comum else "cliente fidelidade"
        )

        if cliente_comum >= valor_minino and cliente_fidelidade >= valor_minino:
            print("\nEspere...")
            print(f"\033[31mPreço Fidelidade: U${cliente_fidelidade:.2f}\033[m")
            print(f"\033[31mPreço Comum: U${cliente_comum:.2f}\033[m\n\033[m")
            sleep(4) # Espera 4 segundos para fazer a próxima verificação

        else:
            print(f"\nCompre agora na pagina do {pagina}.")
            print(f"\033[32mPreço: U${menor_valor:.2f}\033[m\n")
            break


# Programa Principal
consulta_preco()
