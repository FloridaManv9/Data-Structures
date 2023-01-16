# The following "read" function reads values from a file named "inputHW1.txt" and returns the values in an array.



def read():
    file = open("TestInputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))


    return values


ArrayValues = read()
max = ArrayValues[0]
min = ArrayValues[0]
x: int
for x in ArrayValues:
    k = x
    if k > max:
        max = k
    if k < min:
        min = k


print("Maximum element =", max)
print("Minimum element =", min)

