import heapq

heap=[5,9,8,3]
#  a list with initial values
heapq.heapify(heap)
# Transform the list into a heap
heapq.heappop(heap)
#  Remove and return the smallest element from the heap

# Add another new element to the heap
heapq.heappush(heap,6)
heapq.heappush(heap,9)

# Remove and return the smallest element from the heap again
node=heapq.heappop(heap)
minNode=heapq.heappop(heap)

# Print the smallest element that was just removed
print(minNode)

maxNode=heapq.heappop(heap)
print(maxNode)
print(heap)

# Initialize a new list with names
heap2=["Martha","Lewis","Derrick"]
heapq.heapify(heap2)
heapq.heappop(heap2)
heapq.heappush(heap2,"Jina")
print(heap2)
# Print the final state of the heap after all operations