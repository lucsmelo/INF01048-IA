from queue import PriorityQueue

q = PriorityQueue()

q.put((1, "A"))
q.put((2, "B"))
q.put((401, "E"))
q.put((3, "C"))
q.put((61, "D"))
q.put((5, "F"))

while not q.empty():
    next_item = q.get() 
    print(next_item)
