class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key 
        self.value = value 
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size: int = 10):
        self.size = size
        self.data =[None] * size
    def hash_function(self, key: str) -> int:
        total = 0 
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key:str, value: str) -> None:
        index = self.hash_function(key)
        current = self.data[index]
        if current is None:
            self.data[index] = Node(key, Contact(key, value))
            return
        while True:
            if current.key == key:
                current.value.number = value
                return
            if current.next is None:
                break
            current = current.next 
        new_node = Node(key, Contact(key, value))
        new_node.next = self.data[index]
        self.data[index] = new_node
   
    def search(self,key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next 
        return None
    
    def print_table(self) -> None:
        for index, head in enumerate(self.data): 
            if head is None:
                print(f"Index {index}: Empty")
                continue
            line = f"Index {index}:"
            current = head
            while current is not None:
                line += f" - {current.value}"
                current = current.next 
                print(line)

# Test your hash table implementation here.
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")

    print()
    table.print_table()

    contact = table.search("John")
    print("\nSearch result:", contact)

if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    print()
    table.print_table()

    contact = table.search("John")
    print("\nSearch result:", contact)

    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    print("\nAfter collision test:")
    table.print_table()

    table.insert("Rebecca", "999-444-9999")
    print("\nAfter duplicate test:")
    table.print_table()

    print("\nSearch for Chris:", table.search("Chris"))