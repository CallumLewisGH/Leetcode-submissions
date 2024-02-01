class Solution(object):
    def groupAnagrams(self, strs):
        hashMap = {}
        for i in strs:
            list1 = list(i)
            list1.sort()
            list1 = ''.join(list1)
            
            if list1 in hashMap.keys():
                hashMap[list1].append(i)
                
            else:
                hashMap[list1] = [i]
        return hashMap.values()