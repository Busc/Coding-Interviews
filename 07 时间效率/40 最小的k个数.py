class Solution(object):
    def __init__(self, random_list):
        self.random_list = random_list
        
    def partitionPoint(self, begin_ind, end_ind):
        # 作为递归结束的条件，也可按照merge_sort中的写法
        if begin_ind >= end_ind:
            return
        # 选择最后的元素作为主元
        pivot = self.random_list[end_ind]
        # i指向需排序数组首元素之前
        i = begin_ind - 1
        # j初始时指向首元素,随后一直移动到主元前面的元素位置
        for j in range(begin_ind, end_ind):
            if self.random_list[j] < pivot:  # 发现小元素
                i += 1   # i向后移动一个位置
                self.random_list[i], self.random_list[j] = self.random_list[j], self.random_list[i]  # 小元素换位
        # 主元被交换,位于两部分之间,位置索引为i+1
        self.random_list[end_ind], self.random_list[i+1] = self.random_list[i+1], self.random_list[end_ind]
        return i+1

     def topK(self, K):
         begin_ind, end_ind = 0, len(self.random_list)-1
         pointInd = partitionPoint(begin_ind, end_ind)
         while pointInd != K-1:
             if pointInd > K-1:
                 end_ind = pointInd - 1
             else:
                 begin_ind = pointInd +1
             pointInd = self.partitionPoint(begin_ind, end_ind)
         return self.random_list[:K-1]
