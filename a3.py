def readm1():
    file = open("hw2-m1.txt", "r")
    lines = file.readlines()
    a = []
    for line in lines:
        b = []
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)
    return a


def readm2():
    file = open("hw2-m2.txt", "r")
    lines = file.readlines()
    a = []
    for line in lines:
        b = []
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)
    return a


def main():
    a = []
    b = []
    a = readm1()
    b = readm2()

    tuplewhole = []
    TargetMatrix = []
    x = int

    if len(a) != len(b):
        print("Error: Size of Matrices are different")
        exit()


    for x in range(5):
        tuplenum = []
        for j in range(5):


            mat1val = a[x][j]
            mat2val = b[x][j]
            mat3val = (mat1val + mat2val)
            tuplenum.insert(j, mat3val)
        tuplewhole.append(tuplenum)




    print("The result is:")
    for x in range(5):
        for j in range(5):

            print(tuplewhole[x][j], end=" ")
        print("")

main()
