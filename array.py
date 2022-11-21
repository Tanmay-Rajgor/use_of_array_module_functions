from array import * #star means we are importing everything from array module.

#1. created an array and traversed through an array.
my_array = array('i', [1,2,3,4,5])
my_second_array = array('i', [8,9,10])
my_third_list = [11,12,13]


# traverse through array
for i in my_array:
    print(i)

#2. access individual elements through indexes. 
print("The elements in the index 4 of the array is: ", my_array[4])

#3. append any value to the array using append() method. 
my_array.append(6)
print(my_array)

#4. insert value in an array using insert() method. 
my_array.insert(6, 7)
print(my_array)

#5. extend python array using extend() method. 
my_array.extend(my_second_array)
print(my_array)

#6. add items from list into array using fromlist() method. 
my_array.fromlist(my_third_list)
print(my_array)