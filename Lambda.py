answer = lambda x: x*7
print(answer(3)) # 21


def mul(num):
    return lambda x: x*num

answer = mul(10) # here code is like -> answer = lambda x: x*10
print(answer(9)) # 90


''' filter(object, iterable) '''
# object is lambda and iterable is our list
# Result is True or False and then it wil use as to find our filter_list
a = [1, 2, 3, 4, 5]
filter_list = list(filter(lambda num: num%2 == 0 , a))
print(filter_list)


''' map(object, iterable1, iterable2, ..., iterablen) '''
# object is lambda and iterable's is our list or dictionary
# Result is True or False
b = [6, 7, 8, 9, 10]
c = ['abc', 'def', 'ghi', 'jkl', 'mno']
map_list = list(map(lambda num: num%2 == 0, a))
print(map_list) # Here gives True or False
map_list_2 = list(map(lambda num: num%2, a))
print(map_list_2) # Here gives result drawm by lambda fn
map_list_3 = list(map(lambda x ,y: x + y, a, b))
print(map_list_3) # Gives the sum of corresponding elements
map_list_4 = list(map(list, c))
print(map_list_4) # Makes the list of letters of each word in list
