#Problem 1: List 
#This function is complete, use as a reference only if you have completed the solution or are stuck. 

def reverse_order(lst):
    return lst[::-1]

#Test Problem 1: List  

lst = [1, 2, 3, 4, 5]
result = reverse_order(lst)
assert result == [5, 4, 3, 2, 1]



#Problem 2: Collections.dequeue
#This function is complete, use as a reference only if you have completed the solution or are stuck. 

from  collections import deque

def check_if_palindrome(s):
    words = deque(s)
    while len(words) > 1:
        if words.popleft() != words.pop():
            return False
    return True



#Test Problem 2: Collections.dequeue

word1 = 'kayak'
word2 = 'airplane'
assert check_if_palindrome(word1) == True
assert check_if_palindrome(word2) == False 




#Problem 3: Queue Module 
#This function is complete, use as a reference only if you have completed the solution or are stuck.  

from queue import Queue

class PracticeQueue:
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, element):
        self.queue.put(element)

    def dequeue(self):
        self.queue.get()
    
    def search_empty(self):
        return self.queue.empty()
    
    def size(self):
        return self.queue.qsize()




#Test Problem 3: Queue Module

p = PracticeQueue()
assert p.search_empty() == True
assert p.size() == 0
p.enqueue(1)
p.enqueue(2)
assert p.search_empty() == False 
assert p.size() == 2
assert p.dequeue() == 1
assert p.dequeue() == 2
assert p.search_empty() == True 
assert p.size() == 0