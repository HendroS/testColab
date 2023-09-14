# Problem = melakukan operasi rotasi selama x kali dan tentukan
# nilai elemen dari posisi yang ditentukan

def circularArrayRotation(a, k, queries):
    k=k%len(a)
    temporaryarray=a[-k:] + a[:-k]
    for i in range(len(queries)):
        queries[i]=temporaryarray[queries[i]]
    return queries

# print(circularArrayRotation([1,2,3], 2,[0,1,2])) #2,3,1

# a=[1,2,3]
# k=2
# slicing=a[-k:]
# slicing2=a[:-k]
# print(slicing,slicing2)