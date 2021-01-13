# queue.py
#
# Base queue implementation for teh cs10 ADTs unit
#
# Our initial implementation will use a singly linked list. But, if you
# want to make a faster queue, you will need to implement the data structue
# in a different way. To do this, you will need to change the class definitions
# below.
#
# IMPORTANT: If you change the class constructions, make sure you DO NOT change the
# name of the Queue class. The testing harnesses expect your queue implementation to
# be named Queue in this file.

class ListElem:
    """An element of the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """A queue made from a linked list.
    """
    def __init__(self):
        self.head = None

    # Add your queue implementation here!

