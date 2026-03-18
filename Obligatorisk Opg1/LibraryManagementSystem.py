############################################################
#                  OBLIGATORISK OPGAVE NR. 1               #
#                  LIBRARY MANAGEMENT SYSTEM               #
############################################################

#LibraryEntity is the base class for all entities in the library system:
class LibraryEntity: 
    def display_info(self):
    # display_info is defined here, but the implementation is left to the subclasses. 
    
    # NotImplementedError is used as safety measure so the program would crash, if i forgot to display_info about an item,
    # which in a management system isnt very good, if you can watch what is in it, so it makes "invisible" items:
        raise NotImplementedError("Subclasses must implement this method")

#This class defines what a book is in the library system:
class Book(LibraryEntity):
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        
# Prints formatted information about the book:
    def display_info(self):
        print(f"ID: {self.book_id:<1} | Title: {self.title:<60} | Author: {self.author:<26} | Copies: {self.copies:<1}")
        
    def __str__(self):
        return f"{self.title} written by {self.author}"

#This class defines what a DVD is in the library system:
class DVD (LibraryEntity):
    def __init__(self, dvd_id, title, director, copies):
        self.dvd_id = dvd_id
        self.title = title
        self.director = director
        self.copies = copies

# Prints formatted information about the DVD:    
    def display_info(self):
        print(f"ID: {self.dvd_id:<1} | Title: {self.title:<60} | Director: {self.director:<24} | Copies: {self.copies:<1}") 
               
class Member(LibraryEntity):
# This class represents a library member and tracks their borrowed items:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []
        
# Adds an item to the member's borrowed list:
    def borrow_item(self, item): 
        self.borrowed_items.append(item)

# Removes an item from the member's borrowed list, if they have it:
    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            return True
        return False
 
# Displays member details and currently their borrowed items:   
    def display_info(self):
        item_titles = ",  ".join([item.title for item in self.borrowed_items]) or "None"
        print(f"Member: {self.name:<20} | ID: {self.member_id:<5} | Borrowed: {item_titles}")

# Main controller class that manages Books, DVDs, and Members:  
class Library:
    def __init__(self):
        self.books = {}
        self.dvds = {}
        self.members = {}
        
# Add Book: 
    def add_book(self, book):
        self.books[book.book_id] = book 
        
# Remove Book: 
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            print(f"Error: The Book ID {book_id} could not be found...")

#Update Book:       
    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title: book.title = title 
            if author: book.author = author 
            if copies is not None: book.copies = copies
            print("\n" + "=" * 130)
            print(f" The Book ID {book_id} has been successfully updated.")
            print("=" * 130)
        else:
            print(f"Error: Could not find The Book ID {book_id} to update.")
                 
# Add DVD:      
    def add_dvd(self, dvd):
        self.dvds[dvd.dvd_id] = dvd
    
# Remove DVD:
    def remove_dvd(self, dvd_id):
        if dvd_id in self.dvds:
            removed_item = self.dvds.pop(dvd_id)
            print(f"The DVD '{removed_item.title}' was successfully removed.")
        else:
            print(f"Error: The DVD ID {dvd_id} could not be found...")
         
# Update DVD:   
    def update_dvd(self, dvd_id, title= None, director= None, copies= None):
        if dvd_id in self.dvds:
               dvd = self.dvds[dvd_id]
               if title: dvd.title = title
               if director: dvd.director = director
               if copies is not None: dvd.copies = copies
               print(f" The DVD ID {dvd_id} has been succesfully updated.")
        else:
            print(f"Error: Could not find the DVD ID {dvd_id} to update.")

# Add Member:
    def add_member(self, member):
        self.members[member.member_id] = member
        
# Remove Member:
    def remove_member(self,member_id):
        self.members.pop(member_id, None)
    
# Update Member:   
    def update_member(self, member_id, name):
        if member_id in self.members:
            self.members[member_id].name = name
            
# Issuing Books & Returning:
    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        
        if book and member and book.copies > 0:
            book.copies -=1
            member.borrow_item(book)
            print("\n" + "=" * 130)
            print("ISSUED BOOKS:".center(130))
            print(f"\n The Book '{book.title}' has successfully been issued to {member.name}.")
            print("=" * 130)
        
            return True
        else:
            print(f"\nError: Issued failed...")
            return False
            
    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        
        if member and book and member.return_item(book):
            book.copies += 1
            print("\n" + "=" * 130)
            print("RETURNED BOOKS:".center(130))
            print(f"\n The Book '{book.title}' has successfully been returned by {member.name}.")
            print("=" * 130)
        else:
            print(f"Error: Returned failed...")
            
# Issuing DVDs & Returning:
    def issue_dvd(self, dvd_id, member_id):
        dvd = self.dvds.get(dvd_id)
        member = self.members.get(member_id)
        
        if dvd and member and dvd.copies > 0:
            dvd.copies -= 1
            member.borrow_item(dvd)
            
            print("\n" + "=" * 130)
            print("ISSUED DVD:".center(130))
            print(f"\n The DVD '{dvd.title}' has successfully been issued to {member.name}.")
            print("=" * 130)
            
            return True
        else:
            print(f"\nError: The DVD Issue failed...") 
            
            return False
            
    def return_dvd(self, dvd_id, member_id):
        dvd = self.dvds.get(dvd_id)
        member = self.members.get(member_id)
        
        if member and dvd and member.return_item(dvd):
            dvd.copies += 1 
            
            print("\n" + "=" * 130)
            print("RETURNED DVD:".center(130))
            print(f"\n The DVD '{dvd.title}' has successfully been returned by {member.name}.")
            print("=" * 130)
        else:
            print(f"Error: DVD return failed...")
            
# Displaying books:      
    def display_books(self):
        print("\n" + "=" * 130)
        print("LIBRARY BOOKS".center(130))
        print("=" * 130)
        
        for book in self.books.values():
            book.display_info()
        
        print("=" * 130 + "\n")

# Displaying DVDs:
    def display_dvds(self):
        print("\n" + "=" * 130)
        print("LIBRARY DVDS".center(130))
        print("=" * 130)     
        
        for dvd in self.dvds.values():
            dvd.display_info()
        print("=" * 130 + "\n")
        
# Displaying Members:   
    def display_members(self):
        print("\n" + "=" * 130)
        print("LIBRARY MEMBERS".center(130))
        print("=" * 130)
        
        for member in self.members.values():
            member.display_info()
            
        print("=" * 130 + "\n")   
        
# Searching Feature: 
    def search_inventory(self, keyword):
        print("\n" + "=" * 130)
        print(f"SEARCH RESULTS FOR: '{keyword}'".center(130))
        print("=" * 130)
        
        found_items = []
        keyword = keyword.lower()
        
    # Search for Books:
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                book.display_info()
                found_items.append(book)
                
    # Search for DvDs:
        for dvd in self.dvds.values():
            if keyword in dvd.title.lower() or keyword in dvd.director.lower():
                dvd.display_info()
                found_items.append(dvd)
                
    # If there is no result:    
        if not found_items:
            print(f"There were no result for '{keyword}'".center(130))
        print("=" * 130 + "\n")
        
        return found_items

############################################################
#                  Functional Requirements:                #
############################################################
if __name__ == "__main__":
    my_library = Library()

#Book Management: 
# Adding books:
    book1 = Book(1, "The Pragmatic Programmer", "Andy Hunt & Dave Thomas", 1)
    book2 = Book(2, "Clean Code", "Robert Martin", 3)
    book3 = Book(3, "Code Complete: A Practical Handbook of Software Construction", "Steve McConnell", 2)
    book4 = Book(4, "Refactoring", "Martin Fowler & Kent Beck", 7)
    book5 = Book(5, "Python Crash Course", "Eric Matthes", 9)
    book6 = Book(6, "Automate the Boring Stuff with Python", "Al Sweigart", 4)

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)
    my_library.add_book(book5)
    my_library.add_book(book6)

# Removing books: 
    my_library.remove_book(1)

# Update Book Details: 
    my_library.update_book(2, title = "Clean Code: A Handbook of Agile Software Craftsmanship", author = "Robert Cecil Martin", copies = 5)

# Adding DVDs:
    dvd1 =DVD(1, "Interstellar", "Christopher Nolan", 3)
    dvd2 =DVD(2, "The Dark Knight", "Christopher Nolan", 2)
    dvd3 =DVD(3, "Darkest Hour", "Joe Wright", 5)
    dvd4 =DVD(4, "War Machine", "Patrick Hughes", 1)
    dvd5 =DVD(5, "The Man Who Knew Infinity", "Matthew Brown", 7)
    dvd6 =DVD(6, "Python", "Richard Clabaugh", 2)

    my_library.add_dvd(dvd1)
    my_library.add_dvd(dvd2)
    my_library.add_dvd(dvd3)
    my_library.add_dvd(dvd4)
    my_library.add_dvd(dvd5)
    my_library.add_dvd(dvd6)
    
#Member Management:
# Adding Members:
    member1 = Member(1, "Thomas Nielsen")
    member2 = Member(2, "Mette Hansen")
    member3 = Member(3, "Hanne Jensen")
    member4 = Member(4, "Lars Pedersen")
    member5 = Member(5, "Emil Skov")

    my_library.add_member(member1)
    my_library.add_member(member2)
    my_library.add_member(member3)
    my_library.add_member(member4)
    my_library.add_member(member5)

# Removing Members:
    my_library.remove_member(3)

# Updating Members:
    my_library.update_member(5, "Emil Kristensen")

# Issuing and Returning books:
# Issuing books:
    my_library.issue_book(2,4)
    my_library.issue_book(4,2)
    my_library.issue_book(5,1)
    my_library.issue_book(5,5)

# Returning books:
    my_library.return_book(2,4)
    my_library.return_book(5,5)

# Issuing and returning dvds:
    my_library.issue_dvd(2,4)
    my_library.issue_dvd(3,5)
    my_library.issue_dvd(4,5)

# Displaying all books: 
    my_library.display_books()

# Displaying all DvDs:
    my_library.display_dvds()

# Displaying All Members
    my_library.display_members()

#Additional Features  
# Searching Feature:
    my_library.search_inventory("python")

    
    
