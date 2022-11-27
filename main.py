from funcoes import enviar_email, consulta_preco, msg_whatsapp

mensagem = consulta_preco()
enviar_email(mensagem)
msg_whatsapp(mensagem)

