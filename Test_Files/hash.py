list=[69,72,91,105,48]
hash_table=[]*len(list)
for i in list:
    pos=i%len(list)
    hash_table.insert(pos,i)
print(hash_table)