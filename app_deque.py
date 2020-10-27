from deque import Deque


# rear(pushes items forward) -->[2, 4, 5, 6]<-- front(pushes items backwards)
d = Deque()

d.add_rear(4)  # [4]
d.add_rear(1)  # [1, 4]
d.add_rear(12)  # [12, 1, 4]
print(d.items)  # [12, 1, 4]

d.add_front(5)  # [12, 1, 4, 5]
d.add_front(8)  # [12, 1, 4, 5, 8]
d.add_front(7)  # [12, 1, 4, 5, 8, 7]
print(d.items)  # [12, 1, 4, 5, 8, 7]
print(d.is_empty())  # False
print(d.size())  # 6

print(d.remove_front())  # 7
print(d.remove_front())  # 8
print(d.remove_front())  # 5

print(d.remove_rear())  # 12
print(d.remove_rear())  # 1
print(d.remove_rear())  # 4
print(d.is_empty())  # True