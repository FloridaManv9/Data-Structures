# The following "read" function reads values from a file named "inputHW1.txt" and returns the values in an array.
binStepCounter = 0
binStepIndexCounter = 0
linStepCounter = 0
linStepIndexCounter = 0


def linear_search(linKey, linList):
    global linStepCounter
    global linStepIndexCounter
    step = 0
    for x in linList:
        step = step + 1
        if linKey == x:
            break
    print("Linear Steps = ", step)
    linStepIndexCounter = linStepIndexCounter + 1
    linStepCounter = linStepCounter + step


def binary_search(binKey, binList):
    global binStepCounter
    global binStepIndexCounter
    mid = len(binList) // 2
    low = 0
    high = (len(binList) - 1)
    step = 0
    while high >= low:
        step += 1
        mid = (high + low) // 2
        if binList[mid] < binKey:
            low = mid + 1
        elif binList[mid] > binKey:
            high = mid - 1
        else:

            print("Binary Steps = ", step)
            binStepCounter = (binStepCounter + step)
            binStepIndexCounter = binStepIndexCounter + 1
            return

    print("Binary Steps = ", step)
    binStepCounter = binStepCounter + step
    binStepIndexCounter = binStepIndexCounter + 1


def main():
    file = open("sortedLinearInput.txt", "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]

    file2 = open("sortedBinaryInput.txt", "r")
    lines = file2.readlines()
    linesNew2 = [int(x) for x in lines]

    file3 = open("keyLinear.txt", "r")
    linelinearkey = file3.readline()
    values3 = []
    for value in linelinearkey.split(' '):
        values3.append(int(value))

    file4 = open("keyBinary.txt", "r")
    linebinarykey = file4.readline()
    values4 = []
    for value in linebinarykey.split(' '):
        values4.append(int(value))

    for x in range(len(values3)):
        linear_search(values3[x], linesNew)

    for x in range(len(values4)):
        binary_search(values4[x], linesNew2)

    print("Avg Counter for Binary = ", binStepCounter / binStepIndexCounter)
    print("Avg Counter for Binary = ", linStepCounter / linStepIndexCounter)


main()
