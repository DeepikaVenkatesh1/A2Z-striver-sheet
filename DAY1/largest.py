class Solution:
    def largest(self,n:list)->int:
        max=0
        for i in range(1,len(n)):
            if n[i]>max:
                max=n[i]
        return max
sol=Solution()
print(sol.largest([1,2,3,4,5,6,7,8,9]))
print(sol.largest([10,20,30,40,50,9960,70,80,99990]))