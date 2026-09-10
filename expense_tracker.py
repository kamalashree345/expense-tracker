def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Show total")
    print("5. Add category")
    print("6. View categories")
    print("7. Delete category")
    print("8. Quit")
    choice = input("Choose an option number: ")
    return choice


def add_category(categories):
    """Function asks fo a new category name, checks that it does not already exist and it appends the new category to a list of categories. 
    The program must make the categories case insensitive and ignore any spaces at the start or end of the string in order to avoid replicas.
    """
    new_category = input("Enter the name of the new category: ").strip()

    if len(new_category) == 0:
        print("category name cannot be empty")
        return

    for c in categories:
        if new_category.lower() == c.lower():
            print (f"'{new_category}' already exists as a category ")
            return

    categories.append(new_category)
    print(f"new category '{new_category}' has been added")


def view_categories(categories):
    """The function checks if the list of categories is empty or not.
     If it is empty, it says that there are no existing categories 
     and the return statement stops the program from running the code that returns the 
     categories in a numbered format as there are no categories.
     The enumerate function assigns an index to each category in the list starting with 1 and prints the numbered categories.
     """
    
    if len(categories) == 0: 
        print("No existing categories: ")
        return 

    print("\n----Categories----")
    for i, category in enumerate(categories,start=1):
        print(f"{i}. {category}")



def delete_category(categories, expenses):
    """If categories is empty, function prints a message stating that.
    Categories are displayed using view_categories() so that user can see what they want to delete.
    Program asks which category number to delete.
    If there are any expenses in that category, program asks user to confirm whether they want the category to be deleted or not
    If there are no expenses in that category, category is deleted with no confirmation needed from user."""
    pass


def add_expense(expenses, categories):
    """If category is expensive, then program tells user to add a category first.
    Show all the categories and ask user to choose a category number to add expense to.
    Make sure that category number exists.
    Ask for an expense and append it to expense list as a dictionary of category and amount
    """
    pass


def view_expenses(expenses):
    """If expense list is empty, print a message stating that.
    Print a table with a row for category and amount. 
    """
    pass


def delete_expense(expenses):
    """Expenses are displayed with indexing and grouped into categories.
    Program asks which expense number to delete and deletes it after making sure the expense exists."""
    pass


def total_expenses(expenses):
    """If expenses list is empty, print a message stating that.
    Loop through expenses (list of dictionaries) to fill a new dictionary of category totals.
    The grand total of expenses is displayed.
    """
    pass


def load_expenses(filename):
    """Opens file if it exists, reads it line-by-line and rebuilds list of dictionaries.
    If a file does not exist, then an empty list of expenses is returned"""
    pass


def save_expenses(filename, expenses):
    """Opens the file for writing.
    Writes each expense as category and amount in a single line.
    """
    pass


def load_categories(filename):
    """Reads category names line by linr from file and returns a list of categories.
    An ampty list is returned if file does not exist"""
    pass


def save_categories(filename, categories):
    """Opens the file for writing.
    Each category is written in a single line.
    """
    pass


def main(): #function that can run the whole program/functions written in the whole program.
    expenses_file = "expenses.txt"
    categories_file = "categories.txt"

    expenses = []  #switch to load_expenses(expenses_file) once that's working
    categories = [] #switch to load_categories(categories_file) once that's working

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses, categories)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            total_expenses(expenses)
        elif choice == "5":
            add_category(categories)
        elif choice == "6":
            view_categories(categories)
        elif choice == "7":
            delete_category(categories, expenses)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


main()

