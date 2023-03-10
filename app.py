from flask import Flask, request, render_template
from mensaje import enviar_ubicacion



app = Flask(__name__)

# @app.before_first_request
# def enviar_ubicacion_automaticamente():
#     # Llamar a la función que envía la ubicación por WhatsApp

@app.route("/")
def index():
    # enviar_ubicacion()
    return "Hello, World!"

@app.route('/location')
def location():
    # Verificar si la aplicación tiene permiso para acceder a la ubicación
    if 'geolocation' in request.headers.get('User-Agent'):
        # Se puede acceder a la ubicación
        latitude = request.headers.get('X-Forwarded-For')
        longitude = request.headers.get('X-Forwarded-Proto')
        return f"Latitud: {latitude}, Longitud: {longitude}"
    else:
        # No se puede acceder a la ubicación
        return "La aplicación no tiene permiso para acceder a la ubicación", 403
    

@app.route('/mi_ruta', methods=['POST'])
def mi_funcion():
    if request.headers.get('sec-ch-ua') and 'Google' in request.headers['sec-ch-ua']:
        # Verificar si el navegador es Google Chrome para acceder a la ubicación.
        if request.headers.get('sec-ch-ua-mobile') != '?0':
            # Si el dispositivo es móvil y el usuario ha permitido el acceso a la ubicación.

            # Obtener la ubicación del dispositivo a través de JSON
            datos = request.get_json()
            latitud = datos['latitud']
            longitud = datos['longitud']
            print(latitud)
            print(longitud)

            return enviar_ubicacion(latitud, longitud)
        else:
            # Si el dispositivo es una computadora y se requiere acceso a la ubicación.
            return render_template('solicitar_permiso.html')
    else:
        # Si el navegador no es Google Chrome, el usuario no puede compartir su ubicación.
        return "Lo siento, esta función solo está disponible en Google Chrome."


@app.route('/solicitud')
def solicitud():
    return render_template('solicitar_permiso.html')


# hacer la app accesible desde el puerto  en la red local
if __name__ == "__main__":
    app.run(debug=True)
