# Hotel Booking System: a small menu program built with classes


class Room:
    """One hotel room."""

    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_booked = False  # every new room starts free

    def book(self):
        # Book the room, unless it is already taken
        if self.is_booked:
            print("Room", self.number, "is already booked.")
        else:
            self.is_booked = True
            print("Room", self.number, "has been booked.")

    def check_out(self):
        # Free the room, if it was booked
        if self.is_booked:
            self.is_booked = False
            print("Room", self.number, "is now free.")
        else:
            print("Room", self.number, "was not booked.")

    def total_cost(self, nights):
        # Price for a stay of this many nights
        return self.price * nights


class Hotel:
    """A hotel that holds a list of rooms."""

    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_available(self):
        # List every room that is not booked
        print("Available rooms at", self.name)
        for room in self.rooms:
            if not room.is_booked:
                print(room.number, room.room_type, room.price)

    def book_type(self, room_type):
        # Book the first free room of the requested type
        for room in self.rooms:
            if room.room_type == room_type and not room.is_booked:
                room.book()
                return
        print("Sorry, no", room_type, "room is available.")

    def check_out_room(self, number):
        # Free a room by its number
        for room in self.rooms:
            if room.number == number:
                room.check_out()
                return
        print("No room with number", number)


# Create the hotel and its rooms
hotel = Hotel("Immaculate Golden Hotels")
hotel.add_room(Room(101, "Standard", 35000))
hotel.add_room(Room(102, "Standard", 35000))
hotel.add_room(Room(210, "Deluxe", 55000))
hotel.add_room(Room(305, "Suite", 90000))

# The menu loop: show the options, ask, act, repeat until the user quits
running = True
while running:
    print("\n1. Show available rooms")
    print("2. Book a room by type")
    print("3. Check out a room")
    print("4. Quit")
    choice = input("Choose 1-4: ").strip()

    if choice == "1":
        hotel.show_available()
    elif choice == "2":
        room_type = input("Room type (Standard, Deluxe, Suite): ").strip().title()
        hotel.book_type(room_type)
    elif choice == "3":
        try:
            number = int(input("Room number: "))
        except ValueError:
            print("Please type a number.")
        else:
            hotel.check_out_room(number)
    elif choice == "4":
        running = False
        print("Goodbye!")
    else:
        print("Please choose 1, 2, 3 or 4.")