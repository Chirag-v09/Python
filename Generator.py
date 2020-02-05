
def topten():

    return 5

value = topten()
print(value)

def Generator():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

value = Generator()
print(value) # object of generator
print(value.__next__())
print(value.__next__())
for i in value:
    print(i)

print("Square of first 10 no.:-")
def ten_no_sq():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n = n + 1

value = ten_no_sq()
for i in value:
    print(i)

for value in Generator():
    print(value)
