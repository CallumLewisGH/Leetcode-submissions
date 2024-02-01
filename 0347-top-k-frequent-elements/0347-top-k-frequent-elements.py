class Solution(object):
    def topKFrequent(self, nums, k):
        numCount = {}
        reList = []
        for i in nums:
            if i in numCount:
                numCount[i] += 1
            else:
                numCount[i] = 1
        
                   
        temp1 = numCount.keys()
        temp2 = numCount.values()

        for i in range(k):
 

            reList.append(temp1[temp2.index(max(temp2))])
            
            temp1.remove(temp1[temp2.index(max(temp2))])
            temp2.remove(max(temp2))
            
        return reList