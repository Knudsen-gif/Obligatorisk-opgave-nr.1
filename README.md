# OBLIGATORISK OPGAVE NR. 1

## LIBRARY MANAGEMENT SYSTEM

### Description: 
The program is a python-based system ment for managing items, members & transactions.   
This program was developed to demonstrate understanding of OOP concept such as classes, objects, inheritance & polymorphism.  

### Features: 
1.Inventory Mangement: You are able to add, update & remove items(books & DVDs).  
2.Member Tracking: You are able to Register members, and track which items they currently have borrowed.   
3.Transaction Logic: The inventory is automated, so when an item is issued or returned form a member the copies will decrease or increase.   
4.Serach Funktion: Keyword-based searchs across titles, authors & directors.   
5.Console Output: The console output is formatted as tabular data presentation, which makes it easy to read & clean. This is also done by using f-string alignment.   

### Testing:
To check if the systems functions work correctly, there have been made a test_LMS.py.
In the test_LMS.py file. There done 4. different test cases on the systems features, where all the test cases gave the desired result.
#### Test Cases
1. Succesful Borrwing: Verified that items can be issued to members, and that the inventory copies decreased correctly with both Books & DvDs.
2. Out-Of-Stock Handling: Verified that the system blocked borrwing items that is not longer in stock (copies == 0).
3. Invalid ID Handling: Verified that the system correctly identifies and handles non-existent book_id & dvd_id inputs without crashing.
4. Seach Functionality: Verified that the search function worked correctly, by retrieving items from the inventory based on "keywords" and return the expected data.   
