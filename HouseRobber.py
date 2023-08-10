#TC: O(2^(n/2)) SC:O(n)
""" class Solution(object):
    def rob(self, nums):
        
        #:type nums: List[int]
        #:rtype: int
        
        self.nums = nums
        if len(nums)==1:
            return nums[0]
        return self.helper(0,0)


    def helper(self,index,profit):
        if index >= len(self.nums):
            return profit
        
        choose = self.helper(index+2,self.nums[index]+profit)
        nochoose = self.helper(index+1,profit)

        return max(choose,nochoose) """
#TC: O(n) SC:O(n)
""" class Solution(object):
    def rob(self, nums):
        
        #:type nums: List[int]
        #:rtype: int
        
        if len(nums)==1:
            return nums[0]

        dp = []

        
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))

        for i in range(2,len(nums)):
            dp.append(max(dp[i-1],nums[i]+dp[i-2]))
        return dp[-1] """

#TC: O(n) SC:O(1)
class Solution(object):
    def rob(self, nums):
        
        #:type nums: List[int]
        #:rtype: int
        
        if len(nums)==1:
            return nums[0]

        prevprev = nums[0]
        prev = max(prevprev,nums[1])
        

        for i in range(2,len(nums)):
            choose = nums[i]+prevprev
            nochoose = prev
            prevprev = prev
            prev = max(choose,nochoose)
        
        return prev