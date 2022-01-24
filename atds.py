#!/usr/bin/env python3 

"""
atds.py
This file holds classes implementing the
abstract data types covered in the Advanced
Topics class. 
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-02-25'


class Stack(object):
    """Implements a stack ADT with push, pop, peek, size, and
    isEmpty methods.
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return True if self.stack==[] else False
    
    def __repr__(self):
        return f'Stack{str(self.stack)}'

class Queue(object):
    """Implements a queue ADT with enqueue, dequeue, peek, size,
    and isEmpty methods.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return True if self.queue==[] else False
    
    def __repr__(self):
        return f'Queue{str(self.queue)}'

class Deque(object):
    """Implements a deque ADT with addFront, addRear,
    removeFront, removeRear, size, and isEmpty methods.
    """
    def __init__(self):
        self.deque = []
    
    def addFront(self, item):
        self.deque.insert(0, item)
    
    def addRear(self, item):
        self.deque.append(item)
        
    def removeFront(self):
        return self.deque.pop(0)

    def removeRear(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def isEmpty(self):
        return True if self.deque==[] else False

    def __repr__(self):
        return f'Deque{str(self.deque)}'

class Node(object):
    """This class is a Node that can be used in linked lists.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, new):
        self.data = new
    
    def setNext(self, new):
        self.next = new
    
    def __repr__(self):
        return f'Node[data={str(self.data)}, next={str(self.next)}]'

class UnorderedList(object):
    """Maintains an unordered list via a linked series of Nodes.
    """
    def __init__(self):
       self.head = None
    
    def add(self, new_data):
        """Creates a new node at the beginning of the list.
        """
        tempNode = Node(new_data)
        tempNode.setNext(self.head)
        self.head = tempNode

    def append(self, new_data):
        """Creates a new node at the end of the list.
        """
        newNode = Node(new_data)
        current = self.head
        while current!=None:
            if current.getNext()==None:
                current.setNext(newNode)
                return
            current = current.getNext()
        self.head = newNode

    def index(self, item):
        """Returns the index of the first instance of the item.
        """
        ind = 0
        current = self.head
        while current!=None:
            if current.getData()==item:
                return ind
            ind+=1
            current = current.getNext()
    
    def insert(self, pos, item):
        """Inserts item at pos index in the list.
        """
        if pos==0:
            self.add(item)
            return
        newNode = Node(item)
        ind = 0
        current = self.head
        while current.getNext()!=None:
            if ind==pos-1:
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                return
            ind+=1
            current = current.getNext()

    def length(self):
        """Traverses the entire length of the UnorderedList to identify
        how many vlaues (nodes) there are in the list.
        """
        node_count = 0
        current = self.head
        while current!=None:
            node_count+=1
            current = current.getNext()
        return node_count

    def isEmpty(self):
        return True if self.head==None else False

    def search(self, data):
        """Traverses the UnorderedList to find the specified data.
        Returns True if the data is found, else False.
        """
        current = self.head
        found = False
        while current!=None and not found:
            if current.getData()==data:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, data):
        """Find's the data's Node while keeping track of the previous Node,
        then sets the previous Node's next to the data's Node's next.
        """
        actually_done = False
        while not actually_done:
            current = self.head
            prev = None
            done = False
            while current!=None and not done:
                if current.getData()==data:
                    try:
                        prev.setNext(current.getNext())
                        done = True
                    except:
                        self.head = current.getNext()
                        done = True
                else:
                    prev = current
                    current = current.getNext()
            if not self.search(data):
                actually_done = True

    def pop(self, pos=-1):
        ind = 0
        current = self.head
        prev = None
        while current!=None:
            if ind==pos:
                try:
                    prev.setNext(current.getNext())
                    return current.getData()
                except:
                    self.head = current.getNext()
                    return current.getData()
            else:
                ind+=1
                prev = current
                current = current.getNext()
        self.remove(prev.getData())
        return prev.getData()

    def __repr__(self):
        result = 'UnorderedList['
        nextNode = self.head
        while nextNode!=None:
            result+=str(nextNode.getData())+','
            nextNode = nextNode.getNext()
        if result[-1:]==',':
            result = result[:-1]
        result+=']'
        return result
    
class UnorderedListStack(object):
    """Creates a stack ADT using the UnorderedList made above.
    """
    def __init__(self):
        self.stack = UnorderedList()

    def push(self, item):
        self.stack.add(item)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack.head
    
    def size(self):
        return self.stack.size()

    def isEmpty(self):
        return True if self.stack.isEmpty() else False

    def __repr__(self):
        return f'UnorderedListStack[{self.stack}]'
    
class HashTable(object):
    """Describes a hash table that will store key-value pairs.
    One way to do this would be to create a single array of dictionary-style
    objects. Another strategy--simultaneously simpler and more cumbersome--
    is to maintain a pair of parallel arrays. One array--keys--keeps track
    of the keys, while a second array--data--stores the value associated with
    each key.
    
    At the beginning, the parallel arrays for a hash table of size 7 look like 
    this:
    
        keys = [ None, None, None, None, None, None, None ]
    
        data =  [ None, None, None, None, None, None, None ]
        
    Calling the .put(key, value) method will update the keys and data in 
    those arrays:
    
        .put(8, "Adam")
        
    Updated hash table (based on slot 8 % 7 = 1)
     
        keys = [ None,    8  , None, None, None, None, None ]
    
        data =  [ None, "Adam", None, None, None, None, None ]
    
    """
    def __init__(self, size):
        self.size = size
        self.keys = [None]*size
        self.values = [None]*size
    
    def hashfunction(self, key):
        """Calculates the hash index"""
        return key%self.size

    def put(self, key, value):
        index = self.hashfunction(key)
        while self.keys[index] is not None and self.keys[index]!=key and index<len(self.keys):
            index+=1
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            self.values[index] = value

    def get(self, key):
        """Returns the value associated with the key, or None if the value doesn't exist
        in the hash table.
        """
        index = self.hashfunction(key)
        while self.keys[index] is not None and index<len(self.keys):
            if self.keys[index]==key:
                return self.values[index]
            index+=1

    def __repr__(self):
        return f'Keys: {str(self.keys)} \n Values: {str(self.values)}'

class BinaryTree(object):
    """Creates a binary tree using a variation of the Node object.
    """
    def __init__(self, value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def getRootVal(self):
        return self.value

    def setRootVal(self, new_val):
        self.value = new_val

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def insertLeft(self, new_left_child):
        new_tree = BinaryTree(new_left_child)
        new_tree.leftChild = self.leftChild
        self.leftChild = new_tree

    def insertRight(self, new_right_child):
        new_tree = BinaryTree(new_right_child)
        new_tree.rightChild = self.rightChild
        self.rightChild = new_tree 

    def __repr__(self):
        return f'BinaryTree[value={str(self.value)},leftChild={str(self.leftChild)},rightChild={str(self.rightChild)}]'

class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary
        "connections" where we'll store other vertices to which this vertex is connected.
        """
        self.id = key
        self.connections = {}
        self.color = 'white'
        self.dist = 0
        self.pred = None
        self.disc = 0
        self.fin = 0

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def addNeighbor(self, neighborVertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the dictionary, 
        to which this vertex is connected by an edge. If a weight is not indicated, 
        default weight is 0.
        """
        self.connections[neighborVertex] = weight

    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 
        'list comprehension' here!
        """
        return f'{str(self.id)}, color={self.color}, distance={self.dist}, predecessor={self.pred}'\
            f', discovery time={self.disc}, finish time={self.fin}\n'\
                f'connectedTo: {str([x.getID() for x in self.connections])}'

    def getConnections(self):
        """Returns the keys of the vertices we're connected to
        """
        return self.connections.keys()

    def getID(self):
        """Returns the id ("key") for this vertex
        """
        return self.id

    def getWeight(self, neighborVertex):
        """Returns the weight of an edge connecting this vertex with another.
        """
        return self.connections[neighborVertex]

class Graph(object):
    """Describes the Graph class, which is primarily a dictionary  
    mapping vertex names to Vertex objects, along with a few methods 
    that can be used to manipulate them.
    """
    def __init__(self):
        """Initializes an empty dictionary of Vertex objects
        """
        self.vertices = {}

    def addVertex(self, key):
        """Creates a new "key-value" dictionary entry with the string "key"
        key as the dictionary key, and the Vertex object itself as the value. 
        Returns the new vertex as a result.
        """
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def getVertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and 
        returns the Vertex if found. Otherwise, returns None.
        """
        if key in self.vertices.keys():
            return self.vertices[key]
        return None

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in" 
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in myGraph" will be True, otherwise False.
        """
        return key in self.vertices.keys()

    def addEdge(self, fromVertex, toVertex, weight=0):
        """Adds an edge connecting two vertices (specified by key parameters)
        by modifying those vertex objects. Note that the weight can be 
        specified as well, but if one isn't specified, the value of weight 
        will be the default value of 0.
        """
        if fromVertex not in self.vertices.keys():
            self.addVertex(fromVertex)
        
        if toVertex not in self.vertices.keys():
            self.addVertex(toVertex)

        self.vertices[fromVertex].addNeighbor(self.vertices[toVertex], weight)

    def getVertices(self):
        """Returns a list of the Vertex keys"""
        return [key for key in self.vertices.keys()]

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vert in graph:  # Python understands this now!
            print(v)
        """
        return iter(self.vertices.values())
        
class BinaryHeap():
    """The BinaryHeap class implements the Binary Heap Abstract 
    Data Type as a list of values, where the index p of a parent
    can be calculated from the index c of a child as c // 2.
    """
    def __init__(self):
        self.heapList = [0]  # not used. Here just to make parent-
                             # child calculations work nicely.
        # Note that current size of heap = len(self.heapList) - 1

    def insert(self,value):
        """Inserts a value into the heap by:
        a. adding it to the end of the list, and then
        b. "percolating" it up to an appropriate position
        """
        self.heapList.append(value)
        i = len(self.heapList)-1
        while value<=self.heapList[i//2]:
            self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2]
            i = i//2
    '''
    def percolateUp(self, i):
        """Beginning at i, check to see if parent above is greater than
        value at i. If so, percolate i upwards to parent's position.
        """
        pass 
    '''

    def delMin(self):
        """This is a bit trickier. It's easy to return the minimum item,
        the first item on the list, but how do we readjust the heap then?
        """
        if not self.isEmpty():
            result = self.heapList[1]
            self.heapList[1] = self.heapList[self.size()]
            self.heapList.pop()
            self.percolateDown(1)
            return result
            
    def percolateDown(self,i):
        """Moves the item at i down to a correct level in the heap. To
        work correctly, needs to identify the minimum child for parent i.
        """
        while i*2<=self.size():
            if i*2+1>self.size() or self.heapList[i*2]<self.heapList[i*2+1]:
                smaller_i = i*2
            else:
                smaller_i = i*2+1
            if self.heapList[i]>self.heapList[smaller_i]:
                self.heapList[i], self.heapList[smaller_i] = self.heapList[smaller_i], self.heapList[i]
            i = smaller_i

    def findMin(self):
        """Returns the minimum item in the heap, without removing it.
        """
        return self.heapList[1]

    def isEmpty(self):
        return len(self.heapList) - 1 == 0

    def size(self):
        return len(self.heapList) - 1

    def buildHeap(self, list_of_keys):
        """Returns a new heap based on a pre-existing list of key 
        values."""
        i = len(list_of_keys)//2
        self.heapList = [0]+list_of_keys[:]
        while i>0:
            self.percolateDown(i)
            i-=1

    def __repr__(self):
        return "BinaryHeap" + str([self.heapList[i] for i in range(1, self.size()+1)])

class DFSGraph(Graph):
    """Used to create a depth first forest. Inherits from the
    Graph class, but also adds a `time` variable used to track
    distances along the graph, as well as the two methods below.
    """

    def __init__(self):
        super().__init__()
        self.time = 0       # allows us to keep track of times when vertices
                            # are "discovered"

    def dfs(self):
        """Keeps track of time (ie. depth) across calls to dfsvisit
        for *all* nodes, not just a single node: we want to make sure
        that all nodes are considered, and that no vertices are left
        out of the forest.
        """
        for aVertex in self:            # iterate over all vertices
            aVertex.setColor('white')   # initial value of unexamined vertex
            aVertex.setPred(-1)         # no predecessor for first vertex
        for aVertex in self:            # now start working our way through
            if aVertex.getColor() == 'white':   # a depth-first exploration
                self.dfsvisit(aVertex)          # of the vertices

    def dfsvisit(self, startVertex):
        """Effectively uses a stack (by calling itself recursively) to
        explore down through the depth of the graph.
        """
        startVertex.setColor('gray')        # Gray color indicates that this
                                            # vertex is the one being explored
        self.time += 1                      # Increment the timer
        startVertex.setDiscovery(self.time) # Record the current time for this 
                                            # vertex's discovery
        for nextVertex in startVertex.getConnections(): # check all connections
            if nextVertex.getColor() == 'white':        # if we've touched this
                nextVertex.setPred(startVertex)         # reset pred to our start
                self.dfsvisit(nextVertex)               # continue depth search
        startVertex.setColor('black')       # After exploring all the way down
        self.time += 1                      # Last increment
        startVertex.setFinish(self.time)    # Stop "timing"

def main():
    pass
    

if __name__ == "__main__":
    main()