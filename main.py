# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Data types type hints
    name:str="adrian"
    age:int=20
    pi:float=3.4
    boolean:bool=True #False
    cars=["ford","chevrolet","nissan"]
    cars2=cars[0]
    listVariable=["1","2",3]
    mapVariable:dict={"name":"adrian"}
    setVariable:set={"adrian","rogelio"}
    tupleVariable:tuple=("java",name)

    #type hinting the return value
    def sum_numbers(x:int,y:int) ->int:
        return x+y
    print(sum_numbers(10, 15))

    #casting int(), float(), str()

    x=int("10")
    y=float(2)
    z=str(y)

    #condition if

    a:int=25
    b:int=30

    if a>b:
        print(a)
    elif a==b:
        print("both")
    else:
        print(b)

    #short if

    if a>b: print(a+b)

    print("A") if a>b else print("B")


    # nested if
    if a>b:
        print("above ten")

        if a>5:
            print("nested if")
        else:
            print("but not above 5")


    #AND OR NOT

    c=5
    d=15

    if a>b and c<b:
        print("true")
    else:
        print("false")

    if a>b or c<b:
        print("true")
    else:
        print("false")

    if not a>b:
        print("a is not greater than b")

    #pass statement only if you dont want to implement the logic yet

    if a>b:
        pass

    #While Loop

    i=0

    while i<6:
        print(i)
        i+=1

    #break and continue statement
    i=0
    while i<6:
        print(i)
        if i==3:
            break
        else:
            continue
        i+=1

    #else statement with while we use it as once when the condition is not longer true

    i=0

    while i<6:
        print(i)
        i+=1
    else:
        print("finish")

    #For Loop

    fruits:list=["apple","banana","peaches"]

    for fruit in fruits:
        print(fruit)

    for x in "banana":
        print(x)

    #break statement

    for fruit in fruits:
        print(fruit)
        if fruit=="banana":
            break
        else:
            continue

    # else in for loop

    for fruit in fruits:
        print(fruit)
    else:
        print("Fruits were printed successfuly")

    #nested loops

    colors:list=["red","blue","yellow"]

    for color in colors:
        for fruit in fruits:
            print(color,fruit)


    #the range() function

    for x in range(15):
        print(x)

    for x in range(2,10):
        print(x)
    # pass statement

    for i in range(10):
        pass


    #Functions in python a function is defined using the def keyword

    def my_function():
        print("helo my function")

    my_function()

    def my_function(name2):
        print(name2)

    my_function("adrian")

    def my_function(name,lastname):
        print(name)
        print(lastname)
    my_function("Rogelio","Chacon")

    #Arbitrary arguments *args

    def my_function(*kids):
        print("The youngest child is"+kids[2])

    my_function("email","tobias","luis")

    #Arbitrary keyword arguments
    def my_function(**kid):
        print("His last name is"+ kid["name"])


    #default parameter value

    def my_function(country="usa"):
        print(country)


    my_function()

    #Return values

    def my_function_number():
        return 52

    print(my_function_number())

    def hinting_return_value()->int:
        return 40

    #pass statement
    def my_function():
        pass


    #Lambda function  lambda arguments : expression

    x = lambda a : a+10

    y = lambda a,b : a+b


    print(x(5))
    print(y(10,20))


    def lambda_function(n):
        return lambda a : a*n

    saveFunction = lambda_function(10)

    print(saveFunction(15))

    #Data Structured

    #Array
    cars3 = ["ford","nissan","honda"]
    #access the element of an array
    cars[0]="toyota"
    #the length of array

    i=0
    while i<len(cars3):
        print(cars[i])
        i+=1
    #looping array elements

    for element in cars3:
        print(element)

    #Adding elements to the array
    cars.append("kia")
    #removing elements to the array
    cars.pop(1) # delete the second element of the array
    cars.remove("honda") #only remove the first ocurrence

    #arrays methods
    # append() clear() copy() count() extend() index() insert() pop() remove() reverse() sort()


    #List

    names:list=["adrian","rogelio","chacon"]

    #Adding more elements

    names.append(["alberto"])

    names.extend(["pedro","juan"])

    names.insert(1,"uriel")

    #Deleting elements

    del names[5] #we delete the element in the position 5

    manes.remove("pedro")

    name4=names.pop(4)

    names.clear() #remove all the elements

    #Accessing the elements

    for element in names:
        print(element)

    print(names)

    print(names[3])

    print(names[0:2]) # prints 0 1 exclude 2

    print(names[::-1]) #access elements in reverse mode


    #other functions
    # len() index() count() sorted() sort()

    #Dictionary key-values like map in java

    my_dict={}

    my_dict={1:"adrian",2:"rogelio"}

    print(my_dict)

    #changin and adding key values pairs
    new_dict={'first':'python','second':'java','thrid':'c++'}

    new_dict['second']='c++' #changin the element
    new_dict['fourd']='Golang' # adding a new element key-value pair

    #Deleting key value pair

    a=new_dict.pop('second')
    b=new_dict.popitem('thrid') # pop the key value pair
    my_dict.clear() #delete all elements

    #Accessing elements
    print(new_dict['first']) # accessing to the element using the key
    print(new_dict.get('second'))

    #Other functions
    # new_dict.keys() new_dict.values() new_dict.items() new_dict.get('key')


    #Tuple
    #Tuples are the same as list with the exception that once the data is already entered into the tuple it can be changed no matter what

    my_tuple=(1,2,3)

    #accessing to the elements
    for element in my_tuple:
        print(element)

    print(my_tuple)
    print(my_tuple[0])
    print(my_tuple[:])
    print(my_tuple[1][2])

    #Adding more elements
    my_tuple = my_tuple + (4,5,6)


    #Set
    #sets are a collection of unordered elements that are unique. so we cannot repeat the information

    my_set={1,2,3,4,5,6,7,8,9}

    #adding more elements
    my_set.add(10)

    #Operations in set

    my_set2={11,12,13,14}

    print(my_set.union(my_set2))
    print(my_set.intersection(my_set2))
    print(my_set.difference(my_set2))
    print(my_set.symmetric_difference(my_set2))


    #Error handling with Try/except

    try:
        my_set2={1,2,3
    except:
        print("error")
    else:
        print("it is going to execute at the end")

    #nested try except
    try:
        f=open("demo.txt")

        try:
            f.write("lorum lesum")
        except:
            print("error")
        finally:
            print("finally")
    except:
        print("error")

    #creating exception variable

    try:

    except Exception as ex:
        print(ex)


    try:

    except (Exception,BlockingIOError) as ex:
        print(ex)


    #Raise an Exception

    if i<0:
        raise Exception("Throwing and exception")
    else:
        raise TypeError("Only integer are allowed")

    try:
        raise Error("custom error")
    except Error as ex:
        prrint(ex)


    #Oriented Object Programming

    class Person():

        def __init__(self,name,lastname):
            self.name=name
            self.lastname=lastname

        def get_name(self):
            return self.name

        def get_lastname(self):
            return self.lastname

    person = Person("adrian","Orozco")


    #constructor  def __init__(self):
    #self must be the first and if you want to access to the attributes of the contructor in another method you must add self to the method

    #Accessing to the Attributes
    print(person.name)

    print(person.get_lastname())

    #Private Attributes

    class Animal:

        def __init__(self,name,lastname):
            self._name=name
            self._lastname=lastname
        #Private methods
        def _printName(self):
            print(self._name)

    #Inheritance

    class Car():

        def __int__(self,make,model,year):
            self.make=make
            self.model=model
            self.year=year

        def get_descriptive_name(self):
            long_name=str(self.year)+' '+self.make+' '+self.model

    class ElectricCar(Car):
        def __init__(self,make,model,year):
            super().__init__(make,model,year)
            #own attributes
            self.battery_size=70

        # Overriding methods
        def get_descriptive_name(self):
            print("overriding methods")

    my_tesla=ElectricCar("tesla","model s",2006)




