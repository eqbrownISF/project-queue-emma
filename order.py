# orders.py
# by Jacob Wolf
#
# Class implementation of the Order object, for use in the cs10 ADT challenge

class Order():
    """ Object class representing an order to an online shopping platform.
    Must be initialized with a unique order_id. Optional parameters for
    buyer, shipping_address, and contents.
    """

    def __init__(self, order_id, buyer=None, shipping_address=None, content=None):
        self.order_id = order_id
        self.buyer = buyer
        self.shipping_address = shipping_address
        self.content = content

    def __str__(self):
        return f"id: {self.order_id}, buyer: {self.buyer}, address: {self.shipping_address}, content: {self.content}"
