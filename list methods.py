numbers = [5,2,1,7,4]
numbers.append(10)
print(numbers)

numbers = [5,2,1,7,4]
numbers.insert(0,1)
print(numbers)

numbers = [2,2,4,2,2,3,4,6,]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)