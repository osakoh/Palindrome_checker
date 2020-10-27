class Deque:
    """
    Deque (pronounced as 'deck'):A hybrid(stack & queue) ordered collection of items.
    Items can be added/removed from either the front or the rear(end) of the deque.
    rear -->[2, 4, 5, 6]<-- front
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ return True if empty otherwise False """
        return self.items == []

    def add_front(self, item):
        """
        adds item to the front of the deque (.append() method add elements to the end of the list)
        """
        return self.items.append(item)

    def add_rear(self, item):
        """ adds item to the end of the deque """
        return self.items.insert(0, item)

    def remove_front(self):
        """
        removes items from the front of the deque (.pop() method removes elements from the end of the list)
        """
        return self.items.pop()

    def remove_rear(self):
        """
        removes items from the rear/end of the deque
        :return:
        """
        return self.items.pop(0)

    def size(self):
        return len(self.items)
