class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist.")

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            print(f"{name} added to the end of the waitlist.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{name} added to the end of the waitlist.")

    def remove(self, name):
        if not self.head:
            print(f"{name} not found. The waitlist is empty.")
            return
        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist.")
            return
        current = self.head
        while current.next and current.next.name != name:
            current = current.next
        if current.next is None:
            print(f"{name} not found in the waitlist.")
        else:
            current.next = current.next.next
            print(f"Removed {name} from the waitlist.")

    def print_list(self):
        if not self.head:
            print("The watlist is empty.")
            return
        print("Current waitlist:")
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_manager():
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
        elif choice == "4":
            waitlist.print_list()
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    waitlist_manager()

"""
For this assignment, I made a program that uses a linked list to handle a customer waitlist. 
Instead of using Python’s normal list, I built my own version to see how the pieces work. 
A linked list is made up of nodes. Each node has two parts: the customer’s name and a link 
(pointing) to the next customer. 

The waitlist starts with the “head,” which is just the first person in the list. 
If the head is None, that means the list is empty. When I add someone to the front, 
I make a new node and set it as the new head. That new node points to the old head, 
so nothing gets lost. When I add someone to the end, I walk through the whole list 
until I find the last node, and then I attach the new person there.

Removing someone works by searching through the list until I find their name. 
When I do, I update the “next” link so that the list skips over that person. 
If the name is not found, the program says so.

This program is good for small or medium waitlists. If I had thousands of names, 
it would still work but might be slower since it has to go through each person one by one. 
A real eng

"""