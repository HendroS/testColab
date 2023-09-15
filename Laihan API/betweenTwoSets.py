# 1. max arr a
# 2. min arr b
# 3. cari range antara max arr a dan min arr b hasil array baru = ab
# 4. bagi semua elemen dalam ab  dengan elemen a, hasil harus bilangan bulat
# 5. ulangi langkah 4 untuk dapat arr ab1
# 6. hasil adalah panjang array ab1


# na, mb (2, 3)
# a = (2, 4)
# ab = (4, 8, 12, 16)
# b = (16, 32, 96)
# ab1 = ab dibagi b
# hasil = jumlah elemen ab1

           
            
def getTotalX (a, b):
    ab = list(range(min(a), min(b)+1, min(a))) #[4, 16]4,6,8,
    # print(ab)
    ab1 = []
    hasil = []
    
    # check array kandidat ab dengan array a
    for i in ab: 
        status = True
        index = 0
        while status == True and index < len(a):
            if i % a[index] != 0:
                status = False
            index += 1
        if status == True:
            ab1.append(i)
    for j in ab1:
        status = True
        index = 0
        while status == True and index <len(b):
            if b [index] % j !=0:
                status = False
            index += 1
        if status == True:
            hasil.append(j)   
    return len(hasil)
            
        
print(getTotalX ([2, 4], [ 16, 32, 96]))