rooms = [1,2,3,4,5,6,7]
rooms_assi = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

set1 = set(rooms_assi)
set2 = set(rooms)
captain = set1-set2
print(captain.pop())
