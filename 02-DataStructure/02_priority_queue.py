import heapq

def order_tasks(tasks):
    heap = []
    for number, task in enumerate(tasks):
        priority, name = task

        heapq.heappush(heap, (priority, number, name))

    result = []
    while heap:
        priority, number, name = heapq.heappop(heap)
        result.append((priority, name))
    return result
