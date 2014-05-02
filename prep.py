# random list manipulation things
def listManip():
    stuff = [1, "a", "b", 2, 3, "c"]
    stuff[:] = [i for i in stuff if not type(i) == int]
    print(stuff)

    stuff = ["1", "2", "A", "B"]
    stuff[:] = [i for i in stuff if not i.isdigit()]
    print(stuff)

    stuff = [1, 2, 3, 4, 5, 6]
    stuff[:] = [i for i in stuff[::-1] if not i%2]
    print(stuff)

# get combinations of items in a list
def combinations():
    ret = []
    stuff = ["a", "b", "c", "d"]
    for i in range(2**len(stuff)):
        idx = bin(i)[2:]
        while(len(idx) < len(stuff)):
            idx = "0" + idx
        interm = []
        for j in range(len(idx)):
            if idx[j] != "0":
                interm.append(stuff[j])
        ret.append(interm)
    print(ret)

# binary search tree
class Node:
    def __init__(self, value, parent):
        self.val = value
        self.parent = parent
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, val):
        inserted = False
        cur = self.root
        while(not inserted):
            if(val < cur.val):
                if(cur.left == None):
                    cur.left = Node(val, cur)
                    inserted = True
                else:
                    cur = cur.left
            else:
                if(cur.right == None):
                    cur.right = Node(val, cur)
                    inserted = True
                else:
                    cur = cur.right

# get the right neighbor of a node
# arthur got asked this question at tripadvisor
# can also be easily modified to do level-order traversal of a binary tree
def rightneighbor(root, q, node):
    if root.val == "Guard":
        if q:
            q.append(root)
            root = q.pop(0)
        else:
            print()
            return

    if root.left:
        q.append(root.left)
    if root.right:
        q.append(root.right)
    # print(root.val, end=' ')
    # code for finding a neighbor
    if root.val == node:
        if q:
            next = q.pop(0)
            if next.val != "Guard":
                return next.val
            else: return -1
        else: return -1

    return rightneighbor(q.pop(0), q, node)

# tree things I guess
def treeshit():
    node1 = Node(12, None)
    node2 = Node(8, node1)
    node1.left = node2
    tree = BST(node1)
    tree.insert(11)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    q = []
    q.append(Node("Guard", None))
    neighbor = (rightneighbor(node1, q, 1))
    print(neighbor)

# sum of BST nodes
def sumBST(root):
    if not root:
        return 0
    else:
        return root.val + sumBST(root.left) + sumBST(root.right)

# order traversals
def preorder(node):
    print(node.val)
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

def inorder(node):
    if node.left != None:
        inorder(node.left)
    print(node.val)
    if node.right != None:
        inorder(node.right)

def postorder(node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.val)

# subtract strings... intersect is the same index
def minusintersect():
    a = "aabbcc"
    b = "ccbbaa"
    ret = [i[0] for i in zip(a,b) if i[0] != i[1]]

    str_ret = ""
    for i in ret:
        str_ret += i

    print(str_ret)

# binary search in an array
def binsearch_array(number, array, start, end):
    idx = (start+end)/2
    if start == end:
        return -1
    if number == array[idx]:
        return idx
    elif number < array[idx]:
        return binsearch_array(number, array, start, idx)
    elif number > array[idx]:
        return binsearch_array(number, array, idx, end)

def arraysearchshit():
    array = [0, 1, 2, 3, 4, 5, 6]
    print(binsearch_array(5, array, 0, len(array)))

# with python methods
def stringintersect():
    a = "abcde"
    b = "whatever"
    c = set(a) & set(b)
    d = set(a) - c
    print(d)

# linkedlist
class lNode():
    def __init__(self, value):
        self.next = None
        self.value = value

# reverses linkedlist iteratively
def revlinkedlist_iter():
    node1 = lNode(1)
    node2 = lNode(2)
    node1.next = node2
    node3 = lNode(3)
    node2.next = node3

    head = node1
    prev = None
    while(1):
        next = head.next
        head.next = prev
        prev = head
        if next == None:
            print("Done")
            break
        head = next

    cur = node3
    while(cur != None):
        print(cur.value)
        cur = cur.next

def revll():
    node1 = lNode(1)
    node2 = lNode(2)
    node1.next = node2
    node3 = lNode(3)
    node2.next = node3
    head = revll_recur(node1)
    while head:
        print(head.value)
        head = head.next

#reverse it recursively
def revll_recur(cur):
    if cur.next == None or cur == None:
        return cur
    r = revll_recur(cur.next)
    cur.next.next = cur
    cur.next = None
    return r

# merge 2 sorted arrays
def merge_sorted(a, b):
    ai = 0
    bi = 0
    c = []
    while(a or b):
        if not a:
            for i in b:
                c.append(i)
            return c
        if not b:
            for i in a:
                c.append(i)
            return c

        elif a[0] == b[0]:
            c.append(a[0])
            a = a[1:]
            b = b[1:]
        elif a[0] < b[0]:
            c.append(a[0])
            a = a[1:]
        else:
            c.append(b[0])
            b = b[1:]
    return c

def merge():
    a = [1, 2, 4, 5, 6, 7]
    b = [3, 8, 9, 10]
    print(merge_sorted(a, b))
    print (a)
    print (b)

"""
LRU cache in java:
public class Cache extends LinkedHashMap {
    private final int cap

    public Cache(int cap) {
        super(cap + 1, 1.1, true);
        this.cap = cap;
    }

    protected boolean removeEldestEntry(Entry eldest) {
        return size() > capacity;
    }
}


"""

# Given a binary tree described by the class:

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right

        self.value = value


#do BFS
def BFS(root, q, path):
    #add the children of the current node to the queue
    q.append(root.left)
    q.append(root.right)
    #update the path dictionary
    path[root.right] = root
    path[root.left] = root
    #pop next item in the queue, and continue
    next = q.pop(0)
    BFS(next, q, path)

#find the lowest common ancestor for a, b and root
def findlowest(a, b, root):
    #empty dict
    path = {}
    #dictionary : {node: parent}
    path[root] = None
    #queue for BFS
    q = [] # collection.deque()
    q.append(root)
    # O(n)
    BFS(root, q, path)
    path1 = []
    path2 = []
    #build path from a to the root
    while a:
        path1.append(path[a])
        a = path[a]
    
    #build path from b
    while b:
        path2.append(path[b])
        b = path[b]
    
    #go through path 1, first common node should be lowest ancestor
    #O(logn * logn)
    for i in path1:
        if i in path2:
            return i

# Write a function that finds the lowest common ancestor of two nodes, given the two nodes and the root of the tree.
#       o
#      / \
#     o   o <- c
#        / \
#       a   o
#          / \
#             b

# a = {}
# a["b"] = "c"
# print(a)

# picture a keypad with A: 1, 2, 3 etc (phone), make all the words with 3 digits
def keypad(a, b, c):
    pad = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6]]
    if a > len(pad) or b > len(pad) or c > len(pad):
        print("Out of bounds")
        return None
    for i in pad[a]:
        for j in pad[b]:
            for k in pad[c]:
                print(str(i) + j + str(k))

thing = {}
thing[1] = 2

# check if a string is a palindrome
def string_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num)//2):
        if str_num[i] != str_num[:-i]:
            return False
    return True