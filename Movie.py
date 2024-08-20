import os

open("bookings.txt", "w").close()

movies = {
    1: {
        'a': {'morning': 100, 'evening': 100},
        'b': {'morning': 100, 'evening': 100}
    },
    2: {
        'a': {'morning': 100, 'evening': 100},
        'b': {'morning': 100, 'evening': 100}
    },
    3: {
        'a': {'morning': 100, 'evening': 100},
        'b': {'morning': 100, 'evening': 100}
    }
}

def book_ticket(name, email, date, movie, show_time, num_seats):
    if movies[date][movie][show_time] >= num_seats:
        movies[date][movie][show_time] -= num_seats
        booking_details = f"Name: {name}\nEmail: {email}\nDate: {date}\nMovie: {movie}\nShow Time: {show_time}\nSeats Booked: {num_seats}"
        with open("bookings.txt", "a") as f:
            f.write(booking_details + "\n")
        print("Booking successful!")
    else:
        print("Not enough seats available for the selected movie and show time.")


def check_available_seats(date, movie, show_time):
    available_seats = movies[date][movie][show_time]
    print(f"Available seats for {movie} on {date} ({show_time}): {available_seats}")

def check_booking_status(email):
    with open("bookings.txt", "r") as f:
        bookings = f.readlines()
    user_bookings = [booking for booking in bookings if email in booking]
    if user_bookings:
        print(f"Booking details for {email}:")
        for booking in user_bookings:
            print(booking)
    else:
        print(f"No bookings found for {email}")


while True:
    print("\nWelcome to the Movie Ticket Booking System!")
    choice = input("Enter 1 to book a ticket, 2 to check available seats, or 3 to check booking status: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        date = int(input("Enter the date (1, 2, or 3): "))
        movie = input("Enter the movie (a or b): ")
        show_time = input("Enter the show time (morning or evening): ")
        num_seats = int(input("Enter the number of seats to book: "))
        book_ticket(name, email, date, movie, show_time, num_seats)

    elif choice == '2':
        date = int(input("Enter the date (1, 2, or 3): "))
        movie = input("Enter the movie (a or b): ")
        show_time = input("Enter the show time (morning or evening): ")
        check_available_seats(date, movie, show_time)

    elif choice == '3':
        email = input("Enter your email: ")
        check_booking_status(email)

    else:
        print("Invalid choice. Please try again.")

    continue_booking = input("Do you want to perform another action? (y/n): ")
    if continue_booking.lower() != 'y':
        break