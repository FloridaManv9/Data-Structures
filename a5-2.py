from node import Node

def mergeSort(head):
    if (head.next == None):
        return head

    mid = findMidpoint(head)
    head2 = mid.next
    mid.next = None

    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)

    finalHead = merge(newHead1, newHead2)
    return finalHead



def merge(headleft, headright):
    sorted = Node(-1)
    probe = sorted

    while (headleft != None and headright != None):
        if (headleft.data < headright.data):
            probe.next = headleft
            headleft = headleft.next
        else:
            probe.next = headright
            headright = headright.next
        probe = probe.next

    while (headleft != None):
        probe.next = headleft
        headleft = headleft.next
        probe = probe.next

    while (headright != None):
        probe.next = headright
        headright = headright.next
        probe = probe.next

    return sorted.next



def findMidpoint(head):
    slow = head
    fast = head.next
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


file = open("hw5-2.txt", "r")
lines = file.readline().split()
linesNew = [int(x) for x in lines]

head = Node(linesNew[0])
probe = head



for i in range(len(linesNew)-1):
        probe.next = Node(linesNew[i + 1])
        probe = probe.next

head = mergeSort(head)
printList(head)
