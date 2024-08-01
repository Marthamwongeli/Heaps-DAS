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

# QUESTION 1

# Given an integer array nums and an integer k, return the k most frequent elements.

def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    return heapq.nlargest(k, count.keys(), key=count.get)


# QUESTION 2

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.Merge all the linked-lists into one sorted linked-list and return it.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    dummy = ListNode()
    curr = dummy
    
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        node = node.next
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    return dummy.next



# QUESTION 3

#  Implement heap sort using a heap.

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Example usage
array = [12, 11, 13, 5, 6, 7]
heap_sort(array)
print(array)  # Output: [5, 6, 7, 11, 12, 13]




# QUESTION 4

# Check if a given array represents a min-heap.

def is_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

# Example usage
array = [1, 3, 5, 7, 9, 8]
print(is_min_heap(array))  # Output: True




# QUESTION 5

# How do you insert a new element into a heap?

def insert(heap, value):
    # Add the new value at the end of the heap
    heap.append(value)
    # Sift up the inserted value to its proper place
    siftUp(heap, len(heap)-1)

def siftUp(heap, index):
    parentIndex = (index - 1) // 2
    if index == 0:
        return
    elif heap[parentIndex] < heap[index]:
        heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
        siftUp(heap, parentIndex)

heap = [12, 11, 13, 5, 6, 7]
insert(heap, 10)
print("After insertion:", heap)




