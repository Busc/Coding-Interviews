class Solution:
    def InversePairs(self, data):
        count = 0
        backup = data.copy()
        backup.sort()
        for i in range(len(backup)):
            count += data.index(backup[i])
            data.remove(backup[i])
        return count


    def InversePairs(self, data):
        global count
        count=0
        def A(array):
            global count
            if len(array)<=1:
                return array
            k=int(len(array)/2)
            left=A(array[:k])
            right=A(array[k:])
            l=0
            r=0
            result=[]
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    result.append(left[l])
                    l+=1
                else:
                    result.append(right[r])
                    r+=1
                    count+=len(left)-l
            result+=left[l:]
            result+=right[r:]
            return result
        A(data)
        return count%1000000007
