def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("What item would you like to append to the list?: ").strip()
            shopping_list.append(item)
            print("\n")
            pass

        elif choice == '2':
            item = input("What item would you like to remove from the list?: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print("\n")
            else:
                print(f"{item} is not in the list")
                print("\n")
            pass
        

        elif choice == '3':
            if shopping_list:
                print(f"This is your current shopping list: ")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("\n")
            else:
                print("Your shopping list is empty.")
                print("\n")
            pass
        
        elif choice == '4':
            print("Goodbye!")
            print("\n")
            break
        else:
            print("Invalid choice. Please try again.")
            print("\n")
            
if __name__== "__main__":
    main()