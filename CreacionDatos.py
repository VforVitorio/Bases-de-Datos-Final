import json
import random
import time
import mysql.connector

# Conexion a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="aviones"
)
c = conn.cursor()

# Creacion de la tablas

# Creacion tabla departure
c.execute('''
    CREATE TABLE IF NOT EXISTS Departures (
        id_departure INTEGER AUTO_INCREMENT PRIMARY KEY,
        departure_code VARCHAR(255)
    )
''')
# Creacion de la tabla iatacodes
c.execute(''' 
          CREATE TABLE IF NOT EXISTS IataCodes (
          id_iata INTEGER PRIMARY KEY, 
          iataCode VARCHAR(255)
          )
            ''')
# Creacion de la tabla names
c.execute(''' 
          CREATE TABLE IF NOT EXISTS names (
          id_name INTEGER PRIMARY KEY, 
          name VARCHAR(255)
          )
            ''')
# Creacion de la tabla airlines
c.execute(''' 
          CREATE TABLE IF NOT EXISTS Airlines (
          id_air INTEGER PRIMARY KEY, 
          airline VARCHAR(255)
          )
            ''')
# Creacion de la tabla destinations
c.execute(''' 
          CREATE TABLE IF NOT EXISTS Destinations (
          id_des INTEGER PRIMARY KEY, 
          destination VARCHAR(255)
          )
            ''')
# Creacion de la tabla FlightStatus
c.execute(''' 
          CREATE TABLE IF NOT EXISTS FlightStatuses (
          id_status INTEGER PRIMARY KEY, 
          flightStatus VARCHAR(255)
          )
            ''')

# Creacion de la tabla Flights
c.execute(''' 
          CREATE TABLE IF NOT EXISTS Flights (
          id_flight INTEGER PRIMARY KEY, 
          id_departure INTEGER DEFAULT NULL,
          id_iata INTEGER,
          id_name INTEGER,
          id_air INTEGER,
          id_des INTEGER,
          id_status INTEGER,
          FOREIGN KEY (id_departure) REFERENCES Departures (id_departure),
          FOREIGN KEY (id_iata) REFERENCES IataCodes (id_iata),
          FOREIGN KEY (id_name) REFERENCES names (id_name),
          FOREIGN KEY (id_air) REFERENCES Airlines (id_air),
          FOREIGN KEY (id_des) REFERENCES Destinations (id_des),
          FOREIGN KEY (id_status) REFERENCES FlightStatuses (id_status)
          )
            ''')

flightStatus = ["The flight is on time",
                "The flight is delayed", "The flight is cancelled"]
prop = [0.85, 0.10, 0.05]

with open('routes.json', 'r') as route_file:
    route = json.load(route_file)

# Añadimos un contador para limitar el número de iteraciones del bucle
counter = 0
while counter < 100:  # Por ejemplo, detenemos el bucle después de 100 iteraciones
    randomAirport = random.choice(route['airports'])
    randomRoute = random.choice(randomAirport['routes'])
    randomStatus = random.choice(flightStatus)

    plane = {
        "Departure": randomAirport['departure'],
        "iataCode": randomAirport['iataCode'],
        "name": randomAirport['name'],
        "Airline": randomRoute['airline'],
        "Destination": randomRoute['destination'],
        "Id": randomRoute['routeId'],
        "flightStatus": randomStatus
    }

    print(plane)

    # Espera 10 segundos antes de repetir el proceso
    time.sleep(10)

    try:
        # Insertar datos en las tablas
        # Insertar datos en las tablas relacionadas antes de la tabla Flights
        c.execute("INSERT INTO Departures (departure_code) VALUES (%s)",
                  (plane['Departure'],))
        id_departure = c.lastrowid  # Obtener el ID asignado automáticamente

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
        id_des = c.lastrowid

        c.execute("INSERT INTO FlightStatuses (flightStatus) VALUES (%s)",
                  (plane['flightStatus'],))
        id_status = c.lastrowid

        # Insertar una nueva fila en la tabla Flights
        c.execute("INSERT INTO Flights (id_departure, id_iata, id_name, id_air, id_des, id_status) VALUES (%s, %s, %s, %s, %s, %s)",
                  (id_departure, id_iata, id_name, id_air, id_des, id_status))

    except mysql.connector.Error as e:
        print(
            f"Se produjo un error al insertar datos en la base de datos: {e}")

    # Guardar los cambios
    conn.commit()

    # Incrementamos el contador
    counter += 1

# Cerrar la conexión a la base de datos
conn.close()
