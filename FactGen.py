#method to generate factorial

def prod(a,b):
    # returns the product
    output =a*b
    return output
def fact_gen():
    i=1
    n=1
    while True:
        output= prod(n,i)
        yield output
        i+=1
        n=output
        #TODO: update i and n
        # i is the successive INteger and n is the previous product

#Test Block
my_gen = fact_gen()
num=5
for i in range(num):
    print(next(my_gen))
