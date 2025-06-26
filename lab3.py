
# Lab 3 

# Task 1: Working with Strings 
food = 'chicken alfredo pasta'
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last) 
food_list = food.split()
print(food_list) 
joined_food = ' '.join(food_list)
print(joined_food)

# Task 2: Working with Lists 
number_list = [57, 38290, 3892, -22, 1] 
number_list.append(3)
print(number_list)
number_list.insert(3, -100001)
print(number_list) 
number_list.pop()
print(number_list)
number_list.remove(38290)
print(number_list)
print(number_list[:3])
print(number_list[-3:]) 

# Task 3: Working with Dictionaries 
books = {'Tommy Orange' : 'There There' , 'George Orwell' : 
         'Animal Farm', 'F. Scott Fitzgerald' : 'The Great Gatsby' , 
         'Rick Riorden' : 'Percy Jackson' , 
         'William Shakespear' : 'Romeo And Juliet'} 
print(books.keys()) 
print(books.values())
print(books.get('George Orwell'))
books.pop('F. Scott Fitzgerald')
print(books) 
del books['Tommy Orange']
print(books) 