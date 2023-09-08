# 1. diketahui jumlah waktu kedatangan (n), dan batas minimum murid hadir (k)
# 2. jika jumlah murid yang hadir tepat waktu (<= 0) lebih sedikit dari k maka return YES (kelas dibatalkan)
# 3. jika jumlah murid yang datang tepat waktu (<= 0) sama atau lebih dari k return NO (kelas berlangsung)


def angry_Professor(k, a):
    late = 0
    on_time = 0
    
    for i in a:
        if i <= 0 :
            on_time += 1
        else :
            late += 1
    
    if on_time >= k:
        return 'NO'
    elif on_time < k:
        return 'YES'
    
# print (angryProfessor(3, [-1, -3, 4, 2]))
# print (angryProfessor(2, [0, -1, 2, 1]))


            
