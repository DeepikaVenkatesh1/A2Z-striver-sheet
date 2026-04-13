class Solution:
    def moveZeroes(self,arr:list)->list:
        j=0

        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr
sol=Solution()
print(sol.moveZeroes([0,1,2,30,9,7,0,2,3,5]))