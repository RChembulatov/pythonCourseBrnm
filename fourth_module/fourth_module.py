# Уровень 1 (бинарный поиск)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

print("Уровень 1 (бинарный поиск): ", binary_search(arr, target))  # 4


# Уровень 2 (сортировка вставками)
def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array


print("Уровень 2 (сортировка вставками): ", insertion_sort([12, 11, 13, 5, 6]))
# [5, 6, 11, 12, 13]


# Уровень 3 (Поиск в ширину)
graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3']),
}


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited


print("Уровень 3 (Поиск в ширину): ", bfs(graph, '3'))
# ['3', '1', '0', '4', '2']
