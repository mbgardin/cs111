class Person:
    def __init__(self, name):
        self.name = name
        self.energy = 10
        self.understanding = 10

    def read(self, time):
        self.understanding += 2 * time
        self.energy -= 2 * time

    def sleep(self, time):
        self.energy += 2 * time

class Student(Person):
    max_slip_days = 3  # Class variable shared by all students

    def __init__(self, name, major):
        super().__init__(name)  # Initialize using Person's constructor
        self.major = major
        self.understanding = 0
        self.energy = 10
        print("Added", self.name)

    def do_homework(self):
        if self.energy <= 0:
            print("Too tired!")
            self.understanding -= 1
        else:
            print("Wow, that was interesting!")
            self.understanding += 1
            self.energy -= 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

    @staticmethod
    def study_group(student_list):
        for student in student_list:
            student.understanding += 2

    def __str__(self):
        return f"{self.name} is a {self.major} major."

    def __repr__(self):
        return f"Student('{self.name}', '{self.major}')"


# Derived Class: Professor (inherits from Person)
class Professor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days


# Class: Book
class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0

    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.author}')"

    def __str__(self):
        return f"{self.title} by {self.author}"


# Class: Library
class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    """

    def __init__(self, *args):
        self.books = {}
        for book in args:
            self.books[book.id] = book

    def read_book(self, id):
        if id in self.books:
            book = self.books[id]
            book.times_read += 1
            return f"{book.title} has been read {book.times_read} time(s)"

    def read_author(self, author):
        result = []
        for book in self.books.values():
            if book.author == author:
                book.times_read += 1
                result.append(f"{book.title} has been read {book.times_read} time(s)")
        return '\n'.join(result)

    def add_book(self, book):
        if book.id not in self.books:
            self.books[book.id] = book

    def __repr__(self):
        books_repr = ', '.join(repr(book) for book in self.books.values())
        return f"Library({books_repr})"

    def __str__(self):
        books_str = ' | '.join(str(book) for book in self.books.values())
        return books_str

callahan = Professor("Callahan")
elle = Student("Elle", "Law")

callahan.add_student(elle)

elle.visit_office_hours(callahan)  # Expected output: "Thanks, Callahan"

elle.visit_office_hours(Professor("Paulette"))  # Expected output: "Thanks, Paulette"

print(elle.understanding)  # Expected output: 2

print([name for name in callahan.students])  # Expected output: ['Elle']

x = Student("Vivian", Professor("Stromwell")).name
print(x)  # Expected output: "Vivian"

print([name for name in callahan.students])  # Expected output: ['Elle']

print(elle.max_slip_days)  # Expected output: 3

callahan.grant_more_slip_days(elle, 7)
print(elle.max_slip_days)  # Expected output: 7

print(Student.max_slip_days)  # Expected output: 3

b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")

l = Library(b1, b2, b3)

print(l.books[0].title)  # Expected output: 'A Tale of Two Cities'
print(l.read_book(1))  # Expected output: 'The Hobbit has been read 1 time(s)'
print(l.read_author("Charles Dickens"))  # Expected output: 'A Tale of Two Cities has been read 1 time(s)'

l.add_book(Book(3, "The Silmarillion", "J.R.R. Tolkien"))
print(str(l))  # Expected output: 'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien | The Fellowship of the Ring by J.R.R. Tolkien | The Silmarillion by J.R.R. Tolkien'

print(repr(b1))  # Expected output: "Book(0, 'A Tale of Two Cities', 'Charles Dickens')"
print(str(b1))  # Expected output: 'A Tale of Two Cities by Charles Dickens'
print(repr(l))  # Expected output: "Library(Book(0, 'A Tale of Two Cities', 'Charles Dickens'), Book(1, 'The Hobbit', 'J.R.R. Tolkien'), ...)"

isaih = Student("Isaih", "Computer Science")
print(isaih.name)  # Expected output: 'Isaih'
print(isaih.energy)  # Expected output: 10

isaih.sleep(2)
print(isaih.energy)  # Expected output: 14

stephens = Professor("Stephens")
print(stephens.understanding)  # Expected output: 50

stephens.read(2)
print(stephens.understanding)  # Expected output: 54
