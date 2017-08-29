class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')

    def replaceSpaceGeneral(self, s):
        oldLen = len(s)
        spaceNum = s.count(' ')
        if spaceNum > 0:
            newLen = oldLen + 2 * spaceNum
            oldInd = oldLen - 1
            newInd = newLen - 1
            s = s + 2 * spaceNum * ' '
            s = list(s)
            while spaceNum>0:
                if s[oldInd] == ' ':
                    s[newInd] = '0'
                    s[newInd-1] = '2'
                    s[newInd-2] = '%'
                    newInd -= 3
                    oldInd -= 1
                    spaceNum -= 1
                else:
                    s[newInd] = s[oldInd]
                    newInd -= 1
                    oldInd -= 1
            s = ''.join(s)
        return s

    def replaceSpaceTop(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)