#strings have indices , and can be negative
#slicing strings

#compound datatypes
#lists, dictionaries, tuples, sets

# Lists are bookended by square brackets []
# Dictionaries are bookended by {} and they have key value pairs.
# Tuples are bookended by parentheses () and they are immutable.
# Sets are bookended by {} and they are immutable and disallow duplication of values

#concatenate lists

my_list = [1,2,3,4]

print(my_list + [5,6,7])

students = [
    {
        'name': 'Jagdeep Singh',
        'class': 'Python Stack'
    },
    {
        'name': 'Nathan Bludworth',
        'class': 'MERN stack'
    },
]
for student in students:      #much more readable and useful
    print(student['name'])

    for i in range(len(students)):
        print(students[i]['name'])

# tuples are like lists except that they're immutable

my_tuple = (1,2,3,4,5,6,7)
print(my_tuple)
my_tuple[0] = 0  ### will not work, it's like a const variable

my_list_of_nums = [1,2,2,4,4,5,6,7,7,7,7,7,7]
my_list_of_nums = set(my_list_of_nums)
print((my_list_of_nums))
my_list_of_nums = list(my_list_of_nums)
print(my_list_of_nums)

my_list_of_nums = tuple(my_list_of_nums)  ## tuplifies it
print(my_list_of_nums)

my_set = {3,6,1,8,9}   ## this is how you assign a set


#if statements
x= int(input("please enter an integer:"))
please enter an integer: 42
if x < 0:
    x=0
    print('negative changed to zero')
elif x==0:
    print('zero')
elif x==1:
    print('single')
else:
    print('more')

    # for statements

    
