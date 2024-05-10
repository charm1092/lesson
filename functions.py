# numbers_1 = [9, 8, 7, 6, 5]
# numbers_2 = [4, 3, 2, 1, 0]


# def find_average(numbers):
#     average = sum(numbers) // len(numbers)
#     return average

# average_1 = find_average(numbers_1)
# average_2 = find_average(numbers_2)
# print(average_1, average_2)


# def count_vowels(string):
#     VOWELS = 'aeuioyAEUIOY'
#     count = 0
#     for char in string:
#         if char in VOWELS:
#             count += 1

#     return count


# print(count_vowels('aeuioy'))
# print(count_vowels('My name is Roma. I am 17.'))


# def formate_date(*, day: int, month: str) -> str:
#     return f'The day is {day} of {month}'


# print(formate_date(day=5, month="May"))


# def custom_greeting(*, name: str, greeting: str = 'Hello') -> str:
#     return f'{greeting}, {name}' + ':)'


# print(custom_greeting(name='Roma', greeting='Good evening'))
# print(custom_greeting(name='Roma'))