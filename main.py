import json
import CreacionDatos as cd
flightStatus = ['Scheduled', 'Cancelled', 'Delayed']
prop = [0.80, 0.05, 0.15]
i = 0

conn, c = cd.create_database_connection()

def tableCreation():
    cd.create_departure_table(c)
    cd.create_iata_table(c)
    cd.create_names_table(c)
    cd.create_airlines_table(c)
    cd.create_destinations_table(c)
    cd.create_flightstatus_table(c)
    cd.create_longitude_table(c)
    cd.create_latitude_table(c)
    cd.create_routeids_table(c)
    cd.create_flights_table(c)

def main(route, i, flightStatus, prop):
    
    for i in range (100):
        conn, c = cd.create_database_connection()
        tableCreation()
        
        with open('routes.json') as routes_file:
            route = json.load(routes_file)
        
        plane = cd.get_random_flight(flightStatus, prop, route)
        print(plane)
        cd.insert_flight_data(plane, c, conn)
        i = i + 1

# Cargar los datos del archivo JSON
with open('routes.json') as routes_file:
    route = json.load(routes_file)

# Llamar a main() con los datos cargados
main(route, i, flightStatus, prop)