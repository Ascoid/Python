import os
import smtplib
import requests
from email.message import EmailMessage

# Configurar email, senha 
EMAIL_ADDRESS = 'rafahove2@gmail.com'
EMAIL_PASSWORD = 'Astnfvwo426842'
# Criar um e-mail 
msg = EmailMessage() 
msg['Subject'] = 'Carga #35 chegou ao porto'
msg['From'] = 'rafahove2@gmail.com'
msg['To'] = 'rafahove@gmail.com'
msg.set_content('Favor buscar a carga #35 que acaba de chegar na portaria'),

# Enviar um e-mail 
with smtplib. SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

""" 
Link de pesquisa - https://www.youtube.com/watch?v=pJP6ruTiKX4 
Codigo de envio por Gmail.com

"""