try:
    my_list = [1,2,3]
    print(my_list[1]) #This index does not exist
    
except IndexError :
    print("Index out of range !")
    
else :
    print("element found successfully!")
    
finally :
    print("program finished")