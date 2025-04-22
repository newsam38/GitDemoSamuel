def add(x, y):
    return x + y


print(add(3, 5))

addition = lambda x, y: x + y

print(addition(2,3))


numbers = [1, 2, 3, 4, 5]
squeared_number = map(lambda x : x*2, numbers)
print(list(squeared_number))


even_number = filter(lambda x: x % 2 == 0,numbers )
print(list(even_number))

number_list = [3, 7,1,9,4]
print(f"lista original {number_list}")
print(f"lista ordenada {sorted(number_list)}")
print(f"lista invertida {number_list[::-1]}")
