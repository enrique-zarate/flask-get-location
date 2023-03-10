from twilio.rest import Client
from flask import request
import os
from dotenv import load_dotenv

# import credentials dotenv
load_dotenv()


# Datos de la cuenta de Twilio
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def enviar_ubicacion(lat, long):
    print("Enviando ubicación...")
    # Construir el mensaje de ubicación
    ubicacion = "geo:{},{}".format(lat, long)
    print(ubicacion)
    # crear objeto mensaje
    mensaje = {
        "body":"Aqui estoy!",
        "location": {
            "latitud": lat,
            "longitud": long
        }
    
    }
    # Enviar el mensaje de ubicación a través de Twilio
    message = client.messages.create(
        body=f"Estoy aqui bro: https://www.google.com/maps/search/?api=1&query={lat},{long}",
        from_='+15672352765',
        to='+595994256673'
    )

    # Imprimir la respuesta de Twilio
    print(message.sid)