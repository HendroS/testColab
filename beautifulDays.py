def beautiful_Days(i, j, k):
    beautiful = 0
   
    for i in range(i , j+1):
        reversed_day = int(str(i)[::-1])
        check = abs((i - reversed_day))
        
        if check % k == 0:
            beautiful += 1
        else:
            beautiful += 0
    return beautiful
           
  

# print(beautifulDays(10, 15, 5))
# print(beautifulDays(20, 23, 6))