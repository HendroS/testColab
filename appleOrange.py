# lebar rumah (s, t)
# lokasi pohon apple, orange (a, b)
# jumlah apple, orange (m, n)
# jarak apple jatuh dari point a ((-) ke kiri, (+) ke kanan)
# jarak orange jatuh dari point b ((-) ke kiri, (+) ke kanan)

# s, t = [7 11]
# a, b = [5 15]
# m, n = [3 2]
# d.m = [-2 2 1] 
# d.n = [5 -6]

# 1. menentukan lebar rumah (s, t)
# 2. menetukan posisi pohon apple, dan jarak apple jatuh
    # (a + d.m)
# 3. jika hasil "step 2" >=s dan <=t
# 4. hasil m+1
# 5. ulangi untuk mencari jumlah orange

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     lebar_rumah = range(s, t+1)
#     apple = 0
#     orange = 0
#     for i in apples:
#         lokasi_apple = a + i
#         if lokasi_apple in lebar_rumah:
#             apple+=1
#     for i in oranges:
#         lokasi_orange = b + i
#         if lokasi_orange in lebar_rumah:
#             orange+=1
#     print(apple)
#     print(orange)
    
def Apples_Oranges(s, t, a, b, apples, oranges):
    # lebar_rumah = range(s, t+1)
    apple = 0
    orange = 0
    for i in apples:
        lokasi_apple = a + i
        if lokasi_apple >=s and lokasi_apple <=t:
            apple+=1
    for i in oranges: 
        lokasi_orange = b + i
        if lokasi_orange >=s and lokasi_orange <=t:
            orange+=1
    return {'apple': apple, 'orange': orange}
    
    
Apples_Oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])