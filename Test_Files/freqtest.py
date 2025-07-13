# def count_values_frequency(dictt):
#     frequency = {}
#     for value in dictt.values():
#         if value in frequency:
#             frequency[value] += 1
#         else:
#             frequency[value] = 1
#     return frequency

# dictt = {
#     'V': 10,
#     'VI': 10,
#     'VII': 40,
#     'VIII': 20,
#     'IX': 70,
#     'X': 80,
#     'XI': 40,
#     'XII': 20
# }

# print(count_values_frequency(dictt))
# list1=[]
# struct={}
# for i in range(0,10):
#     char=input("Enter test: ")
#     list1.append(char)
# print(list1)
# list1.sort()
# print(list1)
# for a in list1:
#     for freq in a:
#         struct[freq]=
# print(struct)
from collections import defaultdict

list1 = []
word_freq = defaultdict(int)

for i in range(0, 10):
    text = input("Enter text: ")
    list1.append(text)

# Split each text into words and count frequency
for text in list1:
    words = text.split()
    for word in words:
        word_freq[word] += 1

print("Word frequencies:", dict(word_freq))