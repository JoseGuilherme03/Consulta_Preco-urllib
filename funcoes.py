# A função abaixo abre um arquivo texto através da "urllib", lê seus dados, considerando que são do formato UTF-8 e retorna uma string com os dados. Após isso, utiliza o find para encontrar a posição do valor do preço e retorna o valor do preço.
def identifica_preco(url):
    import urllib.request

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

        # Nessa exeção ele verifica se o valor esta acima do valor de comprar, se estiver ele continua o loop.
        if cliente_comum >= valor_minino and cliente_fidelidade >= valor_minino:
            print("\nEspere...")
            print(f"\033[31mPreço Fidelidade: U${cliente_fidelidade:.2f}\033[m")
            print(f"\033[31mPreço Comum: U${cliente_comum:.2f}\033[m\n\033[m")
            sleep(4)  # Espera 4 segundos para fazer a próxima verificação

        # Se estiver no preço adequado de compra ele indicado a página e o valor de compra.
        else:
            print(f"\nCompre agora na pagina do {pagina}.")
            print(f"\033[32mPreço: U${menor_valor:.2f}\033[m\n")
            break

    return f"Preço Baixou!! - Preço: U${menor_valor:.2f} - Acesse a página do {pagina}."


def enviar_email(txt):
    import os
    import dotenv
    import smtplib
    import email.message


    corpo_email = f"""
    <p>Olá segue abaixo o preço de compra do café</p>
    <p>{txt}</p>
    """

    arquivo_env = dotenv.find_dotenv()  # procura o arquivo .env
    dotenv.load_dotenv(arquivo_env)  # adiciona o arquivo na variavel
    usuario = os.getenv("email")  # pega a variavel email no arquivo .env
    senha = os.getenv("senha")  # pega a senha na variavel senha no arquivo .env

    msg = email.message.Message()  # cria a mensagem do email
    msg["Subject"] = "Preço do Café"
    msg["From"] = usuario
    msg["To"] = usuario
    msg.add_header("Content-Type", "text/html") # define o tipo de conteudo do email
    msg.set_payload(corpo_email) # define o corpo do email

    s = smtplib.SMTP("smtp.gmail.com: 587")  # Servidor do Gmail
    s.starttls()  # Inicia a conexão com o servidor
    s.login(msg["From"], senha)  # Faz o login no servidor
    s.sendmail(
        msg["From"], [msg["To"]], msg.as_string().encode("utf-8")
    )
    s.quit()  # Fecha a conexão com o servidor

    print("\033[32mEmail enviado\033[m")


def msg_whatsapp(mensagem):
    from pywhatkit import sendwhatmsg
    from datetime import datetime

    # Pega a hora atual e adiciona 1 minuto
    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute + 1

    # Envia a mensagem para o número informado e aguarda 2 segundos para fechar o navegador
    sendwhatmsg("+554799161-6278", mensagem, hora, minuto,20,True,2)
    print("\033[32mMensagem enviada no whatsapp\033[m")
    

