from stores import UserStore, NotificationStore
from auth import signup, login


def initial_options():
    print("\n Options")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

def after_login_menu():
    print("\n After Login Menu")
    print("1. View notifications")
    print("2. View unread notifications only")
    print("3. Mark notification as read")
    print("4. Clear all notifications")
    print("5. Logout")

def main():

    user_store = UserStore('data/users.json')
    notification_store = NotificationStore('data/notifications.json')

    while True:
        
        initial_options()
        choice = input("Enter your choice: ")

        if choice == '1':
            signup(user_store)
        
        elif choice == '2':
            user = login(user_store)
            if not user:
                continue

            while True:
                after_login_menu()
                c = input("Enter your choice: ")

                if c == '1':
                    notification_store.view_notifications()  # View notifications logic here

                elif c == '2':
                    notification_store.view_unread_notifications()  # View unread notifications logic here

                elif c == '3':
                    notification_store.mark_notification_as_read()
                
                elif c == '4':
                    pass  # Clear all notifications logic here
                
                elif c == '5':
                    print("Logging out...")
                    break
                else:
                    print("Invalid Choice. Please try again.")

        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":    
    main()
