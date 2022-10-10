class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        self.next: Order = None

def sort(orders):
    
    def merge(arr, left, m, right):
        n1 = m - left + 1
        n2 = right - m

        arrayLeft = [0] * (n1)
        arrayRight = [0] * (n2)

        for i in range(0, n1):
            arrayLeft[i] = arr[left + i]

        for j in range(0, n2):
            arrayRight[j] = arr[m + 1 + j]

        i = 0	 
        j = 0	 
        indexMerged = left

        while i < n1 and j < n2:
            if (arrayLeft[i].selection_time + arrayLeft[i].shipping_time) <= (arrayRight[j].selection_time + arrayRight[j].shipping_time):
                    arr[indexMerged] = arrayLeft[i]
                    i += 1
            else:
                    arr[indexMerged] = arrayRight[j]
                    j += 1
            indexMerged += 1

        while i < n1:
            arr[indexMerged] = arrayLeft[i]
            i += 1
            indexMerged += 1

        while j < n2:
            arr[indexMerged] = arrayRight[j]
            j += 1
            indexMerged += 1

    def mergeSort(arr, l, r):
        if l < r:
            m = l+(r-l)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

    n = len(orders)
    mergeSort(orders, 0, n-1)
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
    
    sort(orders)
    for order in orders:
        print(order.id, end=" ")
    print("\n")
