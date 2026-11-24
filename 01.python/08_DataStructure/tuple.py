#number tuple
my_tuple = (20,10,30,40)

#string tuple
string_tuple = ("razik", "khan")

#all data types 
mixed_data = ("razik", 23,43,[4.4,3.1])

for item in mixed_data:
    print(item)

#using Constructor
t = tuple((1,2,[32,3.3]))
#del t
single_element = (5,)
print(type(single_element))


print(my_tuple, string_tuple, mixed_data, t)

student = ("razik", 26, "Graduate in Bechalor of computer application")
name, age , degree  = student
print(degree)

list_of_tuple = (1,2,3,3,3.3,3,3,4,5,6)
print(list_of_tuple.count(3))