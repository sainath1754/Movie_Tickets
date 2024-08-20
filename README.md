# Movie Ticket Booking System

A simple command-line interface (CLI) application for booking movie tickets, checking seat availability, and viewing booking status.

## Features

1. Book movie tickets
2. Check available seats for a specific movie, date, and show time
3. View booking status for a given email

## Requirements

- Python 3.x

## Usage

1. Run the script
2. Follow the on-screen prompts to interact with the system:
- Enter '1' to book a ticket
- Enter '2' to check available seats
- Enter '3' to check booking status

3. Provide the requested information when prompted:
- Name
- Email
- Date (1, 2, or 3)
- Movie (a or b)
- Show time (morning or evening)
- Number of seats (when booking)

4. The system will display the results of your action.

5. Choose whether to perform another action or exit the program.

## Data Storage

- Booking information is stored in a file named `bookings.txt`.
- The file is created when the script runs and is updated with each successful booking.

## Limitations

- The system currently supports only 3 dates, 2 movies, and 2 show times per day.
- Each movie has a fixed capacity of 100 seats per show time.
- Data persistence is limited to the `bookings.txt` file. Seat availability is reset each time the script is run.

## Future Improvements

- Implement a database for more robust data storage and retrieval.
- Add more dates, movies, and show times.
- Implement a graphical user interface (GUI) for easier interaction.
- Add error handling for invalid inputs.
- Implement user authentication and account management.

## Contributing

Feel free to fork this project and submit pull requests with any improvements or bug fixes.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
