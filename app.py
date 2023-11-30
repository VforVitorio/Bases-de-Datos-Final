from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/aviones'
db = SQLAlchemy(app)


class Departures(db.Model):
    __tablename__ = 'Departures'
    id_departure = db.Column(db.Integer, primary_key=True)
    departure_code = db.Column(db.String(255))


class IataCodes(db.Model):
    __tablename__ = 'IataCodes'
    id_iata = db.Column(db.Integer, primary_key=True)
    iataCode = db.Column(db.String(255))


class Airlines(db.Model):
    __tablename__ = 'Airlines'
    id_air = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(255))


class Destinations(db.Model):
    __tablename__ = 'Destinations'
    id_destination = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(255))


class FlightStatuses(db.Model):
    __tablename__ = 'FlightStatuses'
    id_status = db.Column(db.Integer, primary_key=True)
    flightStatus = db.Column(db.String(255))


class routeIds(db.Model):
    __tablename__ = 'routeIds'
    id_route = db.Column(db.Integer, primary_key=True)
    routeId = db.Column(db.String(255))


class names(db.Model):
    __tablename__ = 'names'
    id_name = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


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

# Paso 5: Crear una ruta para mostrar los vuelos y de inicio


@app.route('/', methods=['GET'])
def buscar_avion():
    route_id = request.args.get('route_id')
    vuelo = None
    if route_id is not None:
        vuelo = db.session.query(Flights, Departures, IataCodes, Airlines, Destinations, FlightStatuses, routeIds, names).join(Departures, Flights.id_departure == Departures.id_departure).join(IataCodes, Flights.id_iata == IataCodes.id_iata).join(Airlines, Flights.id_air == Airlines.id_air).join(
            Destinations, Flights.id_destination == Destinations.id_destination).join(FlightStatuses, Flights.id_status == FlightStatuses.id_status).join(routeIds, Flights.id_route == routeIds.id_route).join(names, Flights.id_name == names.id_name).filter(routeIds.routeId == route_id).first()
    return render_template('SeleccionVuelos.html', vuelo=vuelo)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
