def user(name, age):
    print(f"Hey my name is {name} and im {age} old ! ")
user(f"razik",25)
user(f"yusuf", 2.5)

#Example-2

def fatch_sales():
    print(f"this is sales data !")

def filter_valid_order():
    print(f"This is a filter order data")
def summarize_data():
    print(f"This is Summarized Data ")    

def generateData():
    fatch_sales()
    filter_valid_order()
    summarize_data()
generateData()



# writes the Fibonacci series to an arbitrary boundary
def fibonacci(n):
    a , b = 0,1
    while a < n:
        print(a, end=" ")
        a,b = b, a+b

fibonacci(100)           