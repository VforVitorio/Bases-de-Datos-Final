import random
import time
import mysql.connector


# Conexion a la base de datos
def create_database_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="aviones"
    )
    c = conn.cursor()

    return conn, c

# Creacion de la tablas

# Creacion tabla departure


def create_departure_table(c):
    c.execute('''
        CREATE TABLE IF NOT EXISTS Departures (
            id_departure INTEGER AUTO_INCREMENT PRIMARY KEY,
            departure_code VARCHAR(255)
        )
    ''')


# Creacion de la tabla iatacodes

def create_iata_table(c):
    c.execute('''
        CREATE TABLE IF NOT EXISTS IataCodes (
            id_iata INTEGER AUTO_INCREMENT PRIMARY KEY, 
            iataCode VARCHAR(255)
        )
    ''')


# Creacion de la tabla names

def create_names_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS names (
            id_name INTEGER AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255)
            )
                ''')
# Creacion de la tabla airlines


def create_airlines_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS Airlines (
            id_air INTEGER AUTO_INCREMENT PRIMARY KEY, 
            airline VARCHAR(255)
            )
                ''')


# Creacion de la tabla destinations

def create_destinations_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS Destinations (
            id_destination INTEGER AUTO_INCREMENT PRIMARY KEY, 
            destination VARCHAR(255)
            )
                ''')


# Creacion de la tabla FlightStatus

def create_flightstatus_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS FlightStatuses (
            id_status INTEGER AUTO_INCREMENT PRIMARY KEY, 
            flightStatus VARCHAR(255)
            )
                ''')


# Creacion de la tabla routeIds

def create_routeids_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS routeIds (
            id_route INTEGER AUTO_INCREMENT PRIMARY KEY, 
            routeId VARCHAR(255)
            )
                ''')


# Creación tabla longitude

def create_longitude_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS longitude (
            id_longitude INTEGER AUTO_INCREMENT PRIMARY KEY, 
            longitude FLOAT
            )
                ''')


# Creacion de la tabla latitude

def create_latitude_table(c):
    c.execute(''' 
            CREATE TABLE IF NOT EXISTS latitude (
            id_latitude INTEGER AUTO_INCREMENT PRIMARY KEY, 
            latitude FLOAT
            )
                ''')


# Creacion de la tabla Flights

def create_flights_table(c):
    c.execute('''
        CREATE TABLE IF NOT EXISTS Flights (
            id_flight INTEGER AUTO_INCREMENT PRIMARY KEY,
            id_departure INTEGER DEFAULT NULL,
            id_iata INTEGER DEFAULT NULL,
            id_name INTEGER DEFAULT NULL,
            id_air INTEGER DEFAULT NULL,
            id_destination INTEGER DEFAULT NULL,
            id_status INTEGER DEFAULT NULL,
            id_route INTEGER DEFAULT NULL,
            id_longitude INTEGER DEFAULT NULL,
            id_latitude INTEGER DEFAULT NULL,
            FOREIGN KEY (id_departure) REFERENCES Departures (id_departure),
            FOREIGN KEY (id_iata) REFERENCES IataCodes (id_iata),
            FOREIGN KEY (id_name) REFERENCES names (id_name),
            FOREIGN KEY (id_air) REFERENCES Airlines (id_air),
            FOREIGN KEY (id_destination) REFERENCES Destinations (id_destination),
            FOREIGN KEY (id_status) REFERENCES FlightStatuses (id_status),
            FOREIGN KEY (id_route) REFERENCES routeIds (id_route),
            FOREIGN KEY (id_longitude) REFERENCES longitude (id_longitude),
            FOREIGN KEY (id_latitude) REFERENCES latitude (id_latitude)
            
        )
    ''')


def get_random_flight(flightStatus, prop, route):
    randomAirport = random.choice(route['airports'])
    randomRoute = random.choice(randomAirport['routes'])
    randomStatus = random.choices(flightStatus, weights=prop, k=1)[0]

    plane = {
        "Departure": randomAirport['departure'],
        "iataCode": randomAirport['iataCode'],
        "name": randomAirport['name'],
        "longitude": randomAirport['longitude'],
        "latitude": randomAirport['latitude'],
        "Airline": randomRoute['airline'],
        "Destination": randomRoute['destination'],
        "Id": randomRoute['routeId'],
        "flightStatus": randomStatus

    }

    return plane


def insert_flight_data(plane, c, conn):
    time.sleep(5)

    try:
        c.execute("INSERT INTO Departures (departure_code) VALUES (%s)",
                  (plane['Departure'],))
        id_departure = c.lastrowid

        c.execute("INSERT INTO IataCodes (iataCode) VALUES (%s)",
                  (plane['iataCode'],))
        id_iata = c.lastrowid

        c.execute("INSERT INTO names (name) VALUES (%s)", (plane['name'],))
        id_name = c.lastrowid

        c.execute("INSERT INTO Airlines (airline) VALUES (%s)",
                  (plane['Airline'],))
        id_air = c.lastrowid

        c.execute("INSERT INTO Destinations (destination) VALUES (%s)",
                  (plane['Destination'],))
        id_destination = c.lastrowid

        c.execute("INSERT INTO FlightStatuses (flightStatus) VALUES (%s)",
                  (plane['flightStatus'],))
        id_status = c.lastrowid

        c.execute("INSERT INTO routeIds (routeId) VALUES (%s)", (plane['Id'],))
        id_route = c.lastrowid

        c.execute("INSERT INTO Flights (id_departure, id_iata, id_name, id_air, id_destination, id_status, id_route) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (id_departure, id_iata, id_name, id_air, id_destination, id_status, id_route))

    except mysql.connector.Error as e:
        print(
            f"Se produjo un error al insertar datos en la base de datos: {e}")

    # Guardamos los cambios
    conn.commit()
    conn.close()
