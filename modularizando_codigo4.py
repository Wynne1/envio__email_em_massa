# tornar o código inteiro em um módulo para que a interação entre 2 arquivos python seja mais dinâmica e poupe tempo e código. Como exemplo : app.py  e app2.py , fazer uma importação do módulo app.py dentro do app2.py

'''Seguindo o Email_Sender4.py como o modularizador'''

from Email_Sender4 import Emailer

email = Emailer('seuemail@email.comcom','senha_token_email') # email e senha gerada

lista_contato = ['emaildestino1@email.com','emaildestino1@email.com']

mensagem = '''Oi seu pedido acabou de chegar nos correios'''

email.definir_conteudo(topico='Seu pacote chegou!', email_remetente='douglas.devhoje@gmail.com', lista_contatos= lista_contato, conteudo_email= mensagem)

#enviar as imagens
imagens = ['bluesky3.jpg','retro3.jpg']
email.anexar_imagem(imagens)

#anexar arquivos
arquivos = ['csv_exemplo3.csv','xlsx_exemplo3.xlsx','pdf_exemplo3.pdf', 'csv_exemplo3.csv']
email.anexar_arquivos(arquivos)

#enviar email
email.enviar_email(intervalo_em_segundos=30)