class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] not in nums[:i]:
                nums[index]=nums[i]
                index=index+1
        return index