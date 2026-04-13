class Solution:
    def linearSearch(self,arr:list,target)->int:
        for i in range(len(arr)):
            if arr[i]==target:
                return i
        return -1
        
sol=Solution()
print(sol.linearSearch([1,2,3,4,5],3))
        
            