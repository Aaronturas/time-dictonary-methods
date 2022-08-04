import time

# Create a list with 100000 items using the range() method
mylist = list(range(100000))

# Create a dictionary with 100000 items using the range() method
mydict = {}
for i in range(100000):
     mydict[i] = i

# Access the element at key 10000
print("\n Access the element at key 10000")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
mydict[10000]

end = time.time()
print(end-start)

# Add a new key-value pair to the dictionary
print("\n Add a new key-value pair to the dictionary")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
mydict[10000] = 7

end = time.time()
print(end-start)


# Increment the value at key 10 by 1
print("\n Increment the value at key 10 by 1")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
mydict[10] += 1

end = time.time()
print(end-start)

# Delete key 10000
print("\n Delete key 10000")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
del mydict[10000] 

end = time.time()
print(end-start)

# Check if the key 10 is in the dictionary
print("\n Check if the key 10 is in the dictionary")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
10 in mydict

end = time.time()
print(end-start)

# Check if the key -10 is in the dictionary
print("\n Check if the key -10 is in the dictionary")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
-10 in mydict
end = time.time()
print(end-start)

# Pop the first item off of the list
print("\n Pop the first item off of the list")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
mydict.pop(0)

end = time.time()
print(end-start)

# Pop the last item off of the list
print("\n Pop the last item off of the list")
start = time.time()
# TODO: ADD FUNCTION CALL BELOW
mydict.pop(100000-1)

end = time.time()
print(end-start)
