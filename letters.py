sentence = "This is python class"
length = len(sentence)
list1 = []
list2 = []
for i in range(length):
    a = sentence[i]
    if a not in list1:
        num = 0
        list1.append(a)
        for j in range(length):
            if(a == sentence[j]):
                num = num + 1
        list2.append(num)
for i in range(len(list1)):
    print(list1[i], list2[i], sep = " : ")
