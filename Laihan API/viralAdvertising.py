# 1. diketahui jumlah shares di hari pertama, dan like nya setengah dr jumlah share
# 2. di hari kedua jumlah shares adalah, 3 kali liked hari pertama.
# 3. cari total liked di hari n

def viral_Advertising(n):
    shares = 5
    total_likes = 0
    likes = 0 #2
    
    for i in range(n) :
        likes = shares // 2
        total_likes += likes
        shares = likes *3
       
        
    return total_likes
# print(viralAdvertising(4))




# 0   5   2   2
# 1   6   3   5
# 2   9   4   9
# 3   12  6   15
# 4   18  9   24


        

    
    


        