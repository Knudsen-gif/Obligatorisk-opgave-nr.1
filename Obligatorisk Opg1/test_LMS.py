from LibraryManagementSystem import Library, Book, DVD, Member

def test_cases():
    print("\n" + "=" * 130)
    print("STARTING SYSTEM TEST:".center(130))
    print("="* 130)
    
    lib = Library()
    test_book = Book(111, "Python test case book", "Test Case book", 1)
    test_dvd = DVD(111, "Python test case dvd", "Test Case dvd", 1)
    test_member = Member(111, "Test Case")

    lib.add_book(test_book)
    lib.add_dvd(test_dvd)
    lib.add_member(test_member)
    
# 1.Testing borrwing successfully:
# 1.1 Book
    print("Testing Successful Borrow:".center(130))
    success_book = lib.issue_book(111, 111) 
    
    if success_book and test_book.copies == 0:
        print("\n Success: Item issued and count decreased.")
    else:
        print("Fail: Issue logic error...")
        
# 1.2 DVD
    success_dvd = lib.issue_dvd(111, 111)
    
    if success_dvd and test_dvd.copies == 0:
          print("\n Success: Item issued and count decreased.")
    else:
        print("Fail: Issue logic error...")
    
    
        
# 2. Testing borrowing where copies is out-of-stock:
    print("\n" + "=" * 130)
    print("Testing Out of stock (Copies = 0)".center(130))
    print("="* 130)
    
    second_attempt = lib.issue_book(member_id = 111, book_id = 111)
    
    if not second_attempt:
        print("System have corrctly blocked borrowing out-of-stock item.")
    else:
        print("Fail: System have borrowed out-of-stock item...")

# 3. Testing Invaild id in both book_id & dvd_id
# 3.1 book_ID
    print("\n" + "=" * 130)
    print("Testing Invaild id".center(130))
    print("="* 130)
    
    invalid_bookid = lib.issue_book(member_id = 1, book_id = 123)
    
    if not invalid_bookid:
        print("The Sytem have successfully handled Invaild book_id")
    else: 
        print("Fail: The System did not catch the inviald book_id")
        
# 3.2 DVD_ID
    invalid_dvd_id = lib.issue_dvd(member_id = 2, dvd_id = 123)
    
    if not invalid_dvd_id:
        print("The Sytem have successfully handled Invaild DVD_ID")
    else:
        print("Fail: The System did not catch the inviald DVD_ID")

# 4. Testing the searching functionality:
    print("\n" + "=" * 130)
    print("Testing The Searching Functionality".center(130))
    print("="* 130)
    
    Search_result = lib.search_inventory("Python")
    if len(Search_result) > 0:
        print("The Searching Function Works!")
    else:
        print("Fail: The Search failed to find an item in the inventory...")

    print("\n" + "=" * 130)
    print("TESTING COMPLETE".center(130))
    print("="* 130)

if __name__ == "__main__":
    test_cases()


