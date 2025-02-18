'''
Homework7
Name: Jonathan Sedgwick
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

'''
A class that models a queue and is able
to output different informatin about the
queue
'''
class Queue:
    # Initializes the q variable
    # to be the inputted lsit
    def __init__(self,lst=[]): 
        self.q = list(lst)

    # Outputs a representation of the 
    # list as a string
    def __repr__(self):
        return (f"Queue({self.q})")

    # Adds the inputted item to the
    # end of the queue
    def enqueue(self,item): 
        self.q.append(item)

    # Removes the item from the front
    # of the queue and returns it
    def dequeue(self): 
        return self.q.pop(0)

    # Returns the item at the index inputted
    def __getitem__(self,index):
        return self.q[index]

    # Returns the lenth of the queue
    def __len__(self): 
        return len(self.q)

    # Checks if the other object is a Queue
    # object and if it is equals to the self Queue
    def __eq__(self,other):
        if (isinstance(other, Queue)):
            if self.q == other.q:
                return True
            else:
                return False
        else:
            return False
        
    # Adds two Queues together and returns it
    # as a new Queue
    def __add__(self,other):
        newlist = self.q + other.q
        return Queue(newlist)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))

