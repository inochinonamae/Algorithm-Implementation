class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data


# Example usage
todo_list = LinkedList()

todo_list.insert_at_end("Complete project report")
todo_list.insert_at_end("Finish coding tasks")
todo_list.insert_at_end("Prepare presentation")
todo_list.insert_at_end("Submit deliverables")

print("Todo List:")
todo_list.traverse()

todo_list.delete("Finish coding tasks")

print("Updated Todo List:")
todo_list.traverse()

todo_list.reverse()

print("Reversed Todo List:")
todo_list.traverse()

print("Middle item of Todo List:")
print(todo_list.find_middle())
