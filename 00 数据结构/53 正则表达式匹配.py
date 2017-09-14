# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 模式的第2个字符是*
        if len(pattern) > 1 and pattern[1] == '*':
            # 第1个字符是匹配的
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 模式后移2位（认为*为0）/ 字符串后移1位且模式后移2位（认为*为1）/字符串后移一位且模式不动（认为*大于1）
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        # 模式的第2个字符不是*或者模式长度为1
        if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
            # 第1个字符匹配，各后移1位
            return self.match(s[1:], pattern[1:])
        return False
