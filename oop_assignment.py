# --- Assignment 1: Design Your Own Class! ---

# 1. Create a class representing a Book
class Book:
    """
    A class to represent a book with a title, author, and page count.
    """
    
    # 3. Use a constructor to initialize each object
    def __init__(self, title, author, pages):
        """Initializes a new Book object."""
        # 2. Add attributes to the class
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = False

    # 2. Add methods to the class
    def open_book(self):
        """Marks the book as open."""
        if not self.is_open:
            self.is_open = True
            print(f"📖 You have opened '{self.title}'.")
        else:
            print(f"'{self.title}' is already open.")

    def close_book(self):
        """Marks the book as closed."""
        if self.is_open:
            self.is_open = False
            print(f"덮 You have closed '{self.title}'.")
        else:
            print(f"'{self.title}' is already closed.")

    def get_summary(self):
        """Returns a summary of the book's details."""
        return f"'{self.title}' by {self.author} has {self.pages} pages."

# 4. Add an inheritance layer
class EBook(Book):
    """
    An EBook is a specific type of Book with a file format.
    This demonstrates inheritance.
    """
    def __init__(self, title, author, pages, file_format):
        # Call the constructor of the parent class (Book)
        super().__init__(title, author, pages)
        self.file_format = file_format # Add a new attribute specific to EBook

    # Overriding the parent's method to add more detail
    def get_summary(self):
        """Returns a more detailed summary for the EBook."""
        return f"'{self.title}' by {self.author}, {self.pages} pages, Format: {self.file_format}."


# --- Activity 2: Polymorphism Challenge! ---

class Vehicle:
    """A general base class for all vehicles."""
    def __init__(self, name):
        self.name = name

    def move(self):
        """A generic move method that should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    """A Car class that defines its own move behavior."""
    def move(self):
        print(f"{self.name} is Driving 🚗")

class Plane(Vehicle):
    """A Plane class that defines its own move behavior."""
    def move(self):
        print(f"{self.name} is Flying ✈️")

class Boat(Vehicle):
    """A Boat class that defines its own move behavior."""
    def move(self):
        print(f"{self.name} is Sailing ⛵")


# --- Demonstration ---

if __name__ == "__main__":
    print("--- Demonstrating Assignment 1: Book Class ---")
    # Create an instance of the Book class
    my_book = Book("The Hobbit", "J.R.R. Tolkien", 310)
    print(my_book.get_summary())
    my_book.open_book()
    my_book.close_book()

    print("\n--- Demonstrating Inheritance with EBook ---")
    my_ebook = EBook("A Game of Thrones", "George R.R. Martin", 694, "EPUB")
    print(my_ebook.get_summary())
    my_ebook.open_book()

    print("\n\n--- Demonstrating Activity 2: Polymorphism ---")
    # Create instances of the vehicle classes
    my_car = Car("Toyota Camry")
    my_plane = Plane("Boeing 747")
    my_boat = Boat("Sailboat")

    # Create a list of different vehicle objects
    vehicles = [my_car, my_plane, my_boat]

    # Loop through the list and call the same .move() method on each object.
    # Python automatically calls the correct version of .move() for each object.
    # This is polymorphism in action!
    for vehicle in vehicles:
        vehicle.move()
