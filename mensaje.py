from twilio.rest import Client
from flask import request
import os

# Datos de la cuenta de Twilio
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def enviar_ubicacion():
    print("Enviando ubicación...")
    # Obtener la ubicación del dispositivo a través de request.args.get()
    latitud = request.args.get('latitud')
    longitud = request.args.get('longitud')

    # Construir el mensaje de ubicación
    ubicacion = "geo:{},{}".format(latitud, longitud)
    print(ubicacion)
    # Enviar el mensaje de ubicación a través de Twilio
    message = client.messages.create(
        from_='+15672352765',
        to='+595994256673',
        body='Mi ubicación actual:'
        # , media_url=ubicacion
    )

    # Imprimir la respuesta de Twilio
    print(message.sid)