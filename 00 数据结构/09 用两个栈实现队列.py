class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        '''
        appendTail
        '''
        # note: self.
        self.stack1.append(node)

    def pop(self):
        '''
        deleteHead
        '''
        if not self.stack2:
            # stack2=[]
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
