class Airline:
    # Class to represent an airline, with a name and a list of flights
    def __init__(self, name, flight_list):
        self.name = name
        self.flight_list = flight_list
        
class Flight:
    # Class to represent a flight, with a flight number, departure and arrival cities, departure time, and number of seats
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.seats = seats
        
class Booking:
    # Class to represent a booking, with a flight and the number of seats booked
    def __init__(self, flight, seats_booked):
        self.flight = flight
        self.seats_booked = seats_booked
        
def make_booking(flight, seats_booked):
    # Function to make a booking for a given flight, if enough seats are available
    if flight.seats >= seats_booked:
        flight.seats -= seats_booked
        return Booking(flight, seats_booked)
    else:
        return None
        
def cancel_booking(booking):
    # Function to cancel a booking, by adding the seats back to the flight's available seats
    booking.flight.seats += booking.seats_booked
    return True

# Create an airline with some example flights
airline = Airline("Example Airline", [
    Flight("F001", "New York", "London", "10:00", 50),
    Flight("F002", "London", "Paris", "12:00", 40),
    Flight("F003", "Paris", "New York", "14:00", 30)
])

# Allow the user to interact with the flight booking system
while True:
    print("Welcome to the flight booking system!")
    print("[1] Search for flights")
    print("[2] Make a booking")
    print("[3] Cancel a booking")
    print("[4] Quit")
    
    # Get the user's choice
    choice = input("Enter your choice: ")
    
    if choice == "1":
        # Option 1: Search for flights
        print("Search for flights:")
        departure_city = input("Enter departure city: ")
        arrival_city = input("Enter arrival city: ")
        
        # Search for flights that match the user's departure and arrival cities
        matching_flights = [flight for flight in airline.flight_list if flight.departure_city == departure_city and flight.arrival_city == arrival_city]
        
        # Print the matching flights
        if matching_flights:
            print("Matching flights:")
            for i, flight in enumerate(matching_flights):
                print("[{}] {} - {} ({})".format(i + 1, flight.departure_city, flight.arrival_city, flight.departure_time))
        else:
            print("No matching flights found.")

    elif choice == "2":
        # Option 2: Make a booking
        print("Make a booking:")
        flight_number = input("Enter flight number: ")
        seats_booked = int(input("Enter number of seats booked: "))
        
        # Search for the flight with the given flight number
        flight = next((flight for flight in airline.flight_list if flight.flight_number == flight_number), None)
        
        if flight:
            # Make a booking for the flight, if enough seats are available
            booking = make_booking(flight, seats_booked)
            if booking:
                print("Booking successful!")
            else:
                print("Booking failed: not enough seats available.")
        else:
            print("Booking failed: no flight found with that flight number.")

    elif choice == "3":
        # Option 3: Cancel a booking
        print("Cancel a booking:")
        flight_number = input("Enter flight number: ")
        seats_booked = int(input("Enter number of seats booked: "))
        
        # Search for the flight with the given flight number
        flight = next((flight for flight in airline.flight_list if flight.flight_number == flight_number), None)
        
        if flight:
            # Cancel the booking for the flight
            booking = Booking(flight, seats_booked)
            cancel_booking(booking)
            print("Booking cancelled.")
        else:
            print("Booking not found.")
