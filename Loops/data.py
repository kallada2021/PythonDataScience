num_seq = range(0, 10)
num_list = list(num_seq)
print(num_list)

num_seq = range(3, 20, 3)
print(list(num_seq))

world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
world_cup_winners.append([2022, "Argentina"])
world_cup_winners.append([2026, "India"])
print(world_cup_winners)
world_cup_winners.remove([2026, "India"])
print(world_cup_winners)

num_list = [1, 2, 3, 4, 5]
num_list.insert(3,["India", "USA"])
num_list.insert(2,list(range(4, 10,2)))    
print(num_list)


part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)
part_B.extend(part_A)
print(part_B)

def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged_list = []
    
    while i < len(list1) and j < len(list2):
        print(i, j)
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
            print(merged_list)
        else:
            merged_list.append(list2[j])
            j+=1
            print(merged_list)
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
        
    return merged_list
    
list1 = [4, 6, 8, 10]
list2 = [3, 7, 11, 12]
print(merge_sorted_lists(list1, list2))

#List Slicing
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list[2:7])
print(num_list[:5])
print(num_list[5:-1])
print(num_list[2:9:2])
print(num_list[::2])
print(num_list[::-1])

cities = ["London", "Paris", "Los Angeles", "Beirut", "Beirut"]
print(cities.index("Los Angeles"))
cities.remove("Paris")
print(cities)
print("London" in cities)
print("NewYork" not in cities)
print(cities.count("Beirut"))
print(cities.copy())
