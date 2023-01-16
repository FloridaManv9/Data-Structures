

def read():
    file = open("TestInputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))

    return values


ArrayValues = read()
DecFlag = False
IncFlag = False
k = ArrayValues[0]
IncFlagArray = []


if ArrayValues[1] > ArrayValues[0]:
    PastIncrease = True
if ArrayValues[1] < ArrayValues[0]:
    PastIncrease = False

print("Trend Change Points: ", end='')
x: int
for x in ArrayValues[1:8]:

    if x > k:
        Increase = True
    if x < k:
        Increase = False


    if Increase != PastIncrease:
        print(k,x, end=' ')
    k = x
    PastIncrease = Increase

