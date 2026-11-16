# Hotel Booking System

A small menu-driven program that manages hotel rooms, built with Python classes.

## What it does
- Shows the rooms that are available
- Books the first free room of a type (Standard, Deluxe or Suite)
- Checks a room out by its number
- Refuses to book a room that is already booked, and handles wrong input without crashing

## How it is built
- `Room` class: stores a room's number, type, price and whether it is booked, with `book`, `check_out` and `total_cost` methods
- `Hotel` class: holds a list of `Room` objects and manages them

## How to run
`python hotel_booking.py`

## Sample session
 ```
 1. Show available rooms
2. Book a room by type
3. Check out a room
4. Quit
Choose 1-4: 2
Room type (Standard, Deluxe, Suite): standard
Room 101 has been booked.
```

## What I learned
I learned that a class is a blueprint and each object keeps its own data, so booking one room does not affect another. I also learned to test the "nothing to do" cases: checking out a room that was never booked gave a misleading message until I fixed it. The same pattern could be reused for other systems, such as products in a shop or students in a school.

## Tools used
Python
