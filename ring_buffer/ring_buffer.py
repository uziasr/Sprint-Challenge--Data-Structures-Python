from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            # print(self.storage.length == self.capacity)
            # print(self.current['current'].next,' this is the item ', item)
            if self.current['count'] == self.storage.length:
                self.current['current'] = self.storage.head
                self.current['count'] = 0
            if self.current['current'].next:
                new_current = self.current['current'].next
                self.current['current'].insert_after(item)
                self.storage.delete(self.current['current'])
                self.current['current'] = new_current
                self.current['count'] +=1
        self.storage.add_to_tail(item)
        if self.current == None:
            self.current = {"current":self.storage.head, "count":0}

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        for i in range(self.storage.length):
            if node:
                list_buffer_contents.append(node.value)
                node = node.next

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
