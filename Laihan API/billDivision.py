# n adalah jumlah menu dlm bill, k index yang tidak dikonsuumsi (n, k) (4, 1)
# harga item dalam bill [3, 10, 2, 9]
# jumlah pembayaran brian (b) (7)

# 1. Jumlahkan semua nilai dalam bill
# 2. Total bill dikurangi item yang tidak dikonsumsi k[index]
# 3. hasil selisih bill bagi 2 = a
# 4. jika b sama dengan a print "bon apetit"
# 5. jika tidak print b-a

def bonAppetit(bill, k, b):
    total_bill = 0
    # index_k = k[1]
    
    for i in bill:
        total_bill += i
    correct_bill = total_bill - bill[k]
    
    if correct_bill /2 == b:
        print ('Bon Apetit')
    else :
        print (int(abs(b - (correct_bill/2))))
    
bonAppetit ([3, 10, 2, 9], 1, 12)
        
    
    # print (total_bill)
    # print (correct_bill)


