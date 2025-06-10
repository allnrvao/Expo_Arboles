import heapq
def heapsort(arr):
    h = []
    for x in arr:                
        heapq.heappush(h, x)    # O(log n)
    return [heapq.heappop(h) for _ in range(len(h))]  # O(n log n)
print(heapsort([4,1,7,3,8,5]))