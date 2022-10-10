class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time

        '''
        Remove me if you don't need me.
        Add a method to assign to me.
        '''
        self.next: Order = None



def bubbleSort(orders):
    n = len(orders)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if  (orders[j].selection_time + orders[j].shipping_time) > (orders[j+1].selection_time + orders[j+1].shipping_time):
                swapped = True
                orders[j], orders[j + 1] = orders[j + 1], orders[j]
        if not swapped:
            return


if __name__ == '__main__':
    '''
    Retrieves and splits the input
    '''
    data = input()
    data = data.split('; ')
    orders = []
    for d in data:
        id, selection_t, shipping_t = d.split(', ', 2)
        order: Order = Order(int(id), int(selection_t), int(shipping_t))
        orders.append(order)
    
    bubbleSort(orders)
    for order in orders:
        print(order.id, end=" ")
    print("\n")
