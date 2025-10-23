for value in range(1, 21):
  print(value)
 
for value in range(1, 1000001):
  print(value)
  
lists = list(range(1, 1000001))
print(min(lists))
print(max(lists))
print(sum(lists))

odd_numbers = list(range(1, 21, 2))    
for value in odd_numbers:
  print(value)

divisible_by_3 = list(range(3, 31, 3))
for value in divisible_by_3:
  print(value)

cubes = []
for value in range(1, 11):
  cubes.append(value ** 3)
print(cubes)

cubes_list = [value ** 3 for value in range(1, 11)]
print(cubes_list)