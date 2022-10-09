def hello() :
    print("hello")

def pack(one,two,three) :
    return [one,two,three]

def eat_lunch(lunch) :
    if len(lunch) == 0 :
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch)) :
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")


hello() 
print(pack('one','two','three'))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(['chips'])
eat_lunch(['leftovers', 'apple', 'cheesecake'])

                
