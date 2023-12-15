# Importación de las librerías necesarias
# render_template: para renderizar las plantillas html
# request: para obtener los datos de la petición
# redirect: para redirigir a otra página
# url_for: para obtener la url de una página
# jsonify: para convertir los datos a formato json
# Flask: para crear la aplicación: framework usado para crear aplicaciones web
# SQLAlchemy: para la conexión con la base de datos
# joinedload: para realizar consultas con joins
# pymysql: para la conexión con la base de datos en algunas máquinas, dicha líneas es
# pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
import pymysql

# Creación de la aplicación
# Configuración de la base de datos: nombre de la base de datos, usuario, contraseña y puerto
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/aviones'
db = SQLAlchemy(app)

# Necesitamos volver a definir las tablas de la base de datos SQL en el código Python
# para que SQLAlchemy pueda trabajar con ellas. Para ello, creamos una clase por cada
# tabla de la base de datos. En cada clase, definimos los atributos de la tabla como
# variables de la clase y los tipos de datos como parámetros de la función Column.
# Además, definimos la clave primaria de la tabla con el parámetro primary_key=True.
# Por último, definimos las relaciones entre tablas con el parámetro ForeignKey.
# En este caso, usamos el parámetro backref para definir la relación inversa.


class Departures(db.Model):
    __tablename__ = 'Departures'
    id_departure = db.Column(db.Integer, primary_key=True)
    departure_code = db.Column(db.String(255))

# La clase Departures representa la tabla Departures de la base de datos. En esta
# clase, definimos los atributos id_departure y departure_code y la relación con
# la tabla Flights con el parámetro db.relationship.


class IataCodes(db.Model):
    __tablename__ = 'IataCodes'
    id_iata = db.Column(db.Integer, primary_key=True)
    iataCode = db.Column(db.String(255))
# La clase IataCodes representa la tabla IataCodes de la base de datos. En esta
# clase, definimos los atributos id_iata y iataCode y la relación con la tabla
# Flights con el parámetro db.relationship.


class Airlines(db.Model):
    __tablename__ = 'Airlines'
    id_air = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(255))
# La clase Airlines representa la tabla Airlines de la base de datos. En esta
# clase, definimos los atributos id_air y airline y la relación con la tabla
# Flights con el parámetro db.relationship.


class Destinations(db.Model):
    __tablename__ = 'Destinations'
    id_destination = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(255))
# La clase Destinations representa la tabla Destinations de la base de datos. En
# esta clase, definimos los atributos id_destination y destination y la relación
# con la tabla Flights con el parámetro db.relationship.


class FlightStatuses(db.Model):
    __tablename__ = 'FlightStatuses'
    id_status = db.Column(db.Integer, primary_key=True)
    flightStatus = db.Column(db.String(255))
# La clase FlightStatuses representa la tabla FlightStatuses de la base de datos.
# En esta clase, definimos los atributos id_status y flightStatus y la relación
# con la tabla Flights con el parámetro db.relationship.


class routeIds(db.Model):
    __tablename__ = 'routeIds'
    id_route = db.Column(db.Integer, primary_key=True)
    routeId = db.Column(db.String(255))
# La clase routeIds representa la tabla routeIds de la base de datos. En esta
# clase, definimos los atributos id_route y routeId y la relación con la tabla
# Flights con el parámetro db.relationship.


class names(db.Model):
    __tablename__ = 'names'
    id_name = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
# La clase names representa la tabla names de la base de datos. En esta clase,
# definimos los atributos id_name y name y la relación con la tabla Flights con
# el parámetro db.relationship.


class Longitude(db.Model):
    __tablename__ = 'longitude'
    id_longitude = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
# La clase Longitude representa la tabla longitude de la base de datos. En esta
# clase, definimos los atributos id_longitude y longitude y la relación con la
# tabla Flights con el parámetro db.relationship.


class Latitude(db.Model):
    __tablename__ = 'latitude'
    id_latitude = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
# La clase Latitude representa la tabla latitude de la base de datos. En esta
# clase, definimos los atributos id_latitude y latitude y la relación con la
# tabla Flights con el parámetro db.relationship.


class Flights(db.Model):
    __tablename__ = 'Flights'
    id_flight = db.Column(db.Integer, primary_key=True)
    id_departure = db.Column(
        db.Integer, db.ForeignKey('Departures.id_departure'))
    id_iata = db.Column(db.Integer, db.ForeignKey('IataCodes.id_iata'))
    id_air = db.Column(db.Integer, db.ForeignKey('Airlines.id_air'))
    id_destination = db.Column(
        db.Integer, db.ForeignKey('Destinations.id_destination'))
    id_status = db.Column(
        db.Integer, db.ForeignKey('FlightStatuses.id_status'))
    id_route = db.Column(db.Integer, db.ForeignKey('routeIds.id_route'))
    id_name = db.Column(db.Integer, db.ForeignKey('names.id_name'))

    id_longitude = db.Column(
        db.Integer, db.ForeignKey('longitude.id_longitude'))
    id_latitude = db.Column(db.Integer, db.ForeignKey('latitude.id_latitude'))

    departure = db.relationship(
        'Departures', backref=db.backref('flights', lazy=True))
    iatacode = db.relationship(
        'IataCodes', backref=db.backref('flights', lazy=True))
    airline = db.relationship(
        'Airlines', backref=db.backref('flights', lazy=True))
    destination = db.relationship(
        'Destinations', backref=db.backref('flights', lazy=True))
    status = db.relationship(
        'FlightStatuses', backref=db.backref('flights', lazy=True))
    route = db.relationship(
        'routeIds', backref=db.backref('flights', lazy=True))
    name = db.relationship('names', backref=db.backref('flights', lazy=True))

    longitude = db.relationship(
        'Longitude', backref=db.backref('flights', lazy=True))
    latitude = db.relationship(
        'Latitude', backref=db.backref('flights', lazy=True))

# Por ejemplo, en la clase Flights, definimos la relación con la tabla Departures
# con el parámetro db.Column(db.Integer, db.ForeignKey('Departures.id_departure'))
# y la relación inversa con el parámetro departure = db.relationship('Departures',
# backref=db.backref('flights', lazy=True)). De esta forma, podemos acceder a los
# datos de la tabla Departures desde la tabla Flights con la variable departure y
# desde la tabla Departures podemos acceder a los datos de la tabla Flights con la
# variable flights. Además, con el parámetro lazy=True, indicamos que la relación
# se cargará cuando se acceda a ella por primera vez. Si no se indica este parámetro,
# la relación se cargará siempre que se acceda a la tabla Flights.


# En Flask, necesitamos definir las rutas de la aplicación. Para ello, usamos el
# decorador route. En este caso, definimos la ruta /, que es la ruta de inicio de
# la aplicación. En la función asociada a la ruta, renderizamos la plantilla menu.html.
# El renderizado de plantillas se realiza con la función render_template, que recibe
# como parámetro el nombre de la plantilla a renderizar.

# Necesitamos tener las plantillas html en la carpeta templates. En este caso, tenemos
# la plantilla menu.html en la carpeta templates.


@app.route('/', methods=['GET'])
def menu():
    return render_template('menu.html')
# La función menu renderiza la plantilla menu.html, que es nuestra página de inicio en la web


@app.route('/buscar_avion', methods=['GET'])
def buscar_avion():
    route_id = request.args.get('route_id')
    error = None
    vuelo = None
    if route_id is not None:
        vuelo = db.session.query(Flights, Departures, IataCodes, Airlines, Destinations, FlightStatuses, routeIds, names, Latitude, Longitude).join(Departures, Flights.id_departure == Departures.id_departure).join(IataCodes, Flights.id_iata == IataCodes.id_iata).join(Airlines, Flights.id_air == Airlines.id_air).join(
            Destinations, Flights.id_destination == Destinations.id_destination).join(FlightStatuses, Flights.id_status == FlightStatuses.id_status).join(routeIds, Flights.id_route == routeIds.id_route).join(names, Flights.id_name == names.id_name).join(Latitude, Flights.id_latitude == Latitude.id_latitude).join(Longitude, Flights.id_longitude == Longitude.id_longitude).filter(routeIds.routeId == route_id).first()
        if vuelo is None:
            error = "No se encontró ningún vuelo con el routeId proporcionado"
    return render_template('SeleccionVuelos.html', vuelo=vuelo, error=error)
# En la plantilla SeleccionVuelos.html, tenemos un formulario
# con el método GET y un campo de texto con el nombre route_id. Cuando se envía el
# formulario, se envía una petición GET a la ruta /buscar_avion con el parámetro
# route_id.

# En la función buscar_avion, obtenemos el parámetro route_id con la función
# request.args.get('route_id'). Si el parámetro route_id no es None, realizamos
# la consulta a la base de datos con la función db.session.query. En esta consulta,
# usamos la función join para realizar un join entre las tablas Flights, Departures,
# IataCodes, Airlines, Destinations, FlightStatuses, routeIds, names, Latitude y
# Longitude. Además, usamos la función filter para filtrar los resultados por el
# parámetro routeIds.routeId == route_id. Por último, usamos la función first para
# obtener el primer resultado de la consulta. Si el resultado es None, mostramos
# un mensaje de error en la plantilla SeleccionVuelos.html. Si el resultado no es
# None, mostramos los datos del vuelo en la plantilla SeleccionVuelos.html.


@app.route('/borrar_avion', methods=['GET'])
def borrar_avion():
    return redirect(url_for('buscar_avion'))

# La función borrar avión redirige a la función buscar_avion. Para ello, usamos la
# función redirect, que recibe como parámetro la función a la que queremos redirigir.
# En este caso, redirigimos a la función buscar_avion con la función url_for, que
# recibe como parámetro el nombre de la función a la que queremos redirigir.


@app.route('/informacion-de-los-aeropuertos', methods=['GET'])
def ver_rutas_aerolineas():
    aeropuerto = request.args.get('aeropuerto')
    resultados = None
    busqueda_realizada = False

    if aeropuerto:
        vuelos = db.session.query(Flights).options(joinedload(Flights.airline), joinedload(
            Flights.route)).filter(Flights.name.has(name=aeropuerto)).all()
        busqueda_realizada = True

        if vuelos:
            resultados = [(vuelo.route.routeId, vuelo.airline.airline)
                          for vuelo in vuelos]

    return render_template('destinos.html', resultados=resultados, aeropuerto=aeropuerto, busqueda_realizada=busqueda_realizada)
# La funcion ver_rutas_aerolineas recibe como parámetro el nombre del aeropuerto
# y realiza una consulta a la base de datos para obtener los vuelos que salen de
# ese aeropuerto. Para ello, usamos la función db.session.query. En esta consulta,
# usamos la función options para realizar un join entre las tablas Airlines y
# routeIds. Además, usamos la función filter para filtrar los resultados por el
# parámetro Flights.name.has(name=aeropuerto). Por último, usamos la función all
# para obtener todos los resultados de la consulta. Si la consulta devuelve algún
# resultado, mostramos los resultados en la plantilla destinos.html. Si la consulta
# no devuelve ningún resultado, mostramos un mensaje de error en la plantilla destinos.html.


@app.route('/borrar_aerolinea', methods=['GET'])
def borrar_aerolineas():
    return redirect(url_for('ver_rutas_aerolineas'))

# La función borrar aerolinea redirige a la función ver_rutas_aerolineas. Para ello, usamos la
# función redirect, que recibe como parámetro la función a la que queremos redirigir.
# En este caso, redirigimos a la función ver_rutas_aerolineas con la función url_for, que
# recibe como parámetro el nombre de la función a la que queremos redirigir.


@app.route('/grafico')
def grafico():
    return render_template('diagrama.html')
# La función grafico renderiza la plantilla diagrama.html, que es una pagina donde se muestra
# un diagrama entidad relacion de la base de datos
# En el futuro intentaremos hacer este diagrama en tiempo real, para que se vayan añadiendo periodicamente
# los datos a cada tabla


# La funcion de flask que ibamos a usar para el diagrama en tiempo real

# @app.route('/dataGraph')
# def get_graph():
#     flights_with_departures = Flights.query.options(
#         joinedload(Flights.departure)).all()
#     flights_with_destinations = Flights.query.options(
#         joinedload(Flights.destination)).all()

#     nodes = [{'name': flight.departure.departure_code, 'group': 1}
#              for flight in flights_with_departures]  # Iterate over all flights
#     links = [{'source': flight.departure.departure_code, 'target': flight.destination.destination}
#              for flight in flights_with_destinations]

#     graph = {'nodes': nodes, 'links': links}

#     return jsonify(graph)

# La ultima funcion de flask que usamos es la que nos permite ejecutar la aplicacion
# en el puerto 5000, y en modo debug, para que se actualice automaticamente.
# Ademas, creamos la base de datos con la funcion db.create_all()
# Por ultimo, ejecutamos la aplicacion con la funcion app.run()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
