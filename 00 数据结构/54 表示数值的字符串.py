# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        length = len(s)
        i = 0
        # 符号位
        if s[0] == '+' or s[0] == '-':
            i += 1
        # 只有符号位
        if length == 1 and i == 1:
            return False
        numeric = True
        # 扫描0到9的整数数位部分
        i = self.scanDigits(s, i)
        # 整数后面还有内容
        if i < length:
            # 浮点数
            if s[i] == '.':
                i += 1
                # 扫描0到9的小数数位部分
                i = self.scanDigits(s, i)
                # 科学计数法
                if i < length and (s[i] == 'e' or s[i] == 'E'):
                    # 匹配结尾部分
                    numeric, i = self.isExp(s, i+1)
            elif s[i] == 'e' or s[i] == 'E':
                    # 匹配结尾部分
                    numeric, i = self.isExp(s, i+1)
            # 其余不符合标准字符
            else:
                numeric, i = False, i+1
        # 整数后面还有内容且内容正确 and 不管有无内容最后都要检查到字符串末尾
        return numeric and i == length
    def scanDigits(self, s, i):
        '''
        s:整个原始字符串
        i:要检查的部分的开始索引
        return 非数字部分的开始索引
        '''
        if i >= len(s):
            return i
        while i < len(s) and s[i] >= '0' and s[i] <='9':
            i += 1
        return i

    def isExp(self, s, i):
        '''
        匹配科学计数法表示的数值的结尾部分
        s:整个原始字符串
        i:要检查的部分的开始索引
        return 下一部分的开始索引
        '''
        # e/E是结尾
        if i >= len(s):
            return False, -1
        # 符号位
        if s[i] == '+' or s[i] == '-':
            i += 1
        # 符号位是结尾
        if i >= len(s):
            return False, -1
        # 扫描0到9的整数数位部分
        i = self.scanDigits(s, i)
        # e/E后面的部分不允许出现小数
        if i == len(s):
            return True, i
        else:
            return False, -1



