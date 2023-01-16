def read():
    file = open("HanoiTower.txt", "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew





def main():


    A = read()
    L = len(A)
    A.reverse()

    B = []
    C = []
    A.insert(0, 11)
    B.insert(0, 22)
    C.insert(0, 33)

    def event(N, First, Second, Third):
        if N > 0:
            event(N - 1, First, Third, Second)
            diskBeingMoved = First[-1]
            towerFrom = First[0]
            if towerFrom == 11:
                towerFrom = 'A'
            elif towerFrom == 22:
                towerFrom = 'B'
            else:
                towerFrom = 'C'
            towerTo = Second[0]
            if towerTo == 11:
                towerTo = 'A'
            elif towerFrom == 22:
                towerTo = 'B'
            else:
                towerTo = 'C'
            Second.append(First.pop())


            print(f"Disk {diskBeingMoved} moved from {towerFrom} to {towerTo}")
            event(N - 1, Third, Second, First)

    event(L, A, C, B)


main()
