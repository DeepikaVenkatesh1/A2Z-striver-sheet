class Solution:
    def rotateArray(self,arr:list)->list:
        temp=arr[0]

        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=temp
        return arr
sol=Solution()
print(sol.rotateArray([1,2,3,4]))