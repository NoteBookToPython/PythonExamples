#Defination of the generators to produce even numbers
def all_even():
    n=0
    while True:
        yield n
        n+=2


my_gen = all_even()


#Generate the first 5 even numbers

for i in range(5):
    print(next(my_gen))