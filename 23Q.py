numbers = [12, 75, 150, 180, 145, 525, 50]
even_list = filter(lambda x: x%2 == 0, numbers)
print(sum(even_list))