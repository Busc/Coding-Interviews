# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        for i,data in enumerate(sequence):
            if data >= root:
                break
        if i != len(sequence)-1 and min(sequence[i:]) < root:
            return False
        leftSeq = sequence[:i]
        rightSeq = sequence[i:len(sequence)-1]
        self.VerifySquenceOfBST(leftSeq)
        self.VerifySquenceOfBST(rightSeq)
        return True
