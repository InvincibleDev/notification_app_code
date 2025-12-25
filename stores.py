from utils import load_json, save_json

class UserStore:
    def __init__(self, path):
        self.path = path
        self.data = load_json(path, {"users": []})

    def find_user_by_username(self, username):
        for user in self.data["users"]:
            if user.get("username") == username:
                return user
        return None
    
    def save(self):
        save_json(self.path, self.data)

    def add_user(self, user):
        self.data["users"].append(user)
        self.save()
    
    
class NotificationStore:
    def __init__(self, path):
        self.path = path
        self.data = load_json(path, {"notifications": []})

    def find_notification_by_id(self, notification_id):
        for index, notification in enumerate(self.data['notifications']):
            if notification.get("notification_id") == notification_id:
                return index, notification
        return None, None

    # [{1}, {2}, {3}, {4}]

    def update_notifications_list(self, notification):
        index, notifcation_ = self.find_notification_by_id(notification.get("notification_id"))
        self.data['notifications'].pop(index)
        self.data['notifications'].insert(index, notification)

        self.save()

    def print_notifications(self, notifications_to_print):
        for index, notification in enumerate(notifications_to_print, start=1):
            status = "Read" if notification.get("is_read") else "Unread"
            print(f"{index}. {notification.get('message')} [{status}]")

    def save(self):
        save_json(self.path, self.data)

    def view_notifications(self, user_id):
        print("\n All Notifications: ")

        user_notifications = [notification for notification in self.data if notification.get("user_id") == user_id]
        self.print_notifications(user_notifications)
        
    def view_unread_notifications(self, user_id):
        print("\n Unread Notifications: ")

        unread_notifications = [notification for notification in self.data if notification.get("user_id") == user_id and not notification.get("is_read")]
        self.print_notifications(unread_notifications)
    
    def mark_notification_as_read(self, user_id):
        print("Enter the notification id that you want to mark read")
        self.view_unread_notifications(user_id)
        
        notification_id = input("Notification ID: ")
        index, notification = self.find_notification_by_id(notification_id)

        if not notification:
            print("Notification not found.")
            return
        
        notification["is_read"] = True
        self.update_notifications_list(notification)

print(__name__)