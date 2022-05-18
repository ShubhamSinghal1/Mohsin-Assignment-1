
""" 3)Count no of odd and even  """ 
data = (1,2,3,4,5,6,7,8,9)
no_of_odd = 0
no_of_even = 0
for i in data:
    if i%2 == 0:
        no_of_even += 1
    else:
        no_of_odd +=1
print("Count of even number = " ,no_of_even)
print( "Count of odd number = " , no_of_odd)
