# Complete Python Program to Detect the Starting Node of a Cycle in Linked List

# Definition for singly-linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):

        slow = head
        fast = head

        # Step 1: Detect whether cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If both pointers meet, cycle exists
            if slow == fast:
                break
        else:
            # No cycle found
            return None

        # Step 2: Find starting node of cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


# Function to create linked list
def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    nodes = [head]

    for value in arr[1:]:
        newNode = ListNode(value)
        current.next = newNode
        current = newNode
        nodes.append(newNode)

    return head, nodes


# Function to create cycle in linked list
def createCycle(head, nodes, pos):
    if pos != -1:
        tail = nodes[-1]
        tail.next = nodes[pos]


# ---------------- MAIN PROGRAM ----------------

# Example 1
arr = [3, 2, 0, -4]
pos = 1

head, nodes = createLinkedList(arr)
createCycle(head, nodes, pos)

solution = Solution()
cycleNode = solution.detectCycle(head)

if cycleNode:
    print("Cycle starts at node with value:", cycleNode.val)
else:
    print("No cycle")


# Example 2
arr2 = [1, 2]
pos2 = 0

head2, nodes2 = createLinkedList(arr2)
createCycle(head2, nodes2, pos2)

cycleNode2 = solution.detectCycle(head2)

if cycleNode2:
    print("Cycle starts at node with value:", cycleNode2.val)
else:
    print("No cycle")


# Example 3
arr3 = [1]
pos3 = -1

head3, nodes3 = createLinkedList(arr3)
createCycle(head3, nodes3, pos3)

cycleNode3 = solution.detectCycle(head3)

if cycleNode3:
    print("Cycle starts at node with value:", cycleNode3.val)
else:
    print("No cycle")