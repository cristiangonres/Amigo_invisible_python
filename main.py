#Programa para hacer el "amigo invisible". 
# Tras introducir los participantes, los empareja aleatoriamente y envía email a cada participante con los datos del amigo, conservando el anonimato y la sorpresa
import smtplib 
import re
from random import shuffle
from datetime import datetime
from datetime import timedelta

lista_participantes = []
fecha = datetime.now() 
asignaciones = {}

def add_members():
    continuar = ''
    nparticipante = 1
    while not continuar.startswith('n'):
        nombre = input(f'Introduzca el nombre del participante n {nparticipante}: ')
        email = input( f'Introduzca el email de {nombre}: ')
        regex = re.compile(r'([A-Za-z0-9\.\-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email):
            print(f'La dirección de correo de {nombre} es incorrecta. El participante no ha sido guardado.')
            continue
        nparticipante += 1
        lista_participantes.append({nombre:email})
        if nparticipante > 3:
            continuar = input('¿Desea añadir otro participante? (Si/No)').lower()

        
        
def emparejar_amigo():
    # Mezcla la lista de manera aleatoria
    shuffle(lista_participantes)
    # Crea el diccionario de asignación
    for i in range(len(lista_participantes)):
        for nombre, mail in lista_participantes[i].items():
            if 'nombre_anterior' in locals():
                asignaciones[mail] = nombre_anterior
            else:
                nomb = str(lista_participantes[len(lista_participantes)-1].keys())
                asignaciones[mail] = nomb[12:-3]
            nombre_anterior = nombre
    return asignaciones
    
def enviar_mail(asignaciones):
    print(asignaciones)
    for mail, amigo in asignaciones.items():
        remitente = 'amigoinvisible@satecma.com' 
        destinatario = mail 
        asunto = 'AMIGO INVISIBLE' 
        mensaje = f"""Debes darle un regalo a {amigo} de un importe del rango {importe_min} - {importe_max}"""
        email = """From: %s 
        To: %s 
        MIME-Version: 1.0 
        Content-type: text/html 
        Subject: %s 
        %s
        """ % (remitente, destinatario, asunto, mensaje)
        smtp = smtplib.SMTP('mail.server.com', 25)
        smtp.sendmail(remitente, destinatario, email)
    
    

add_members()
emparejar_amigo()
importe_min = int(input('¿Cuál es el importe mínimo de cada regalo? '))
importe_max = int(input('¿Cuál es el importe máximo de cada regalo? '))
enviar_mail(emparejar_amigo())


