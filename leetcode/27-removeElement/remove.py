class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                nums[i-count] = nums[i]
        return len(nums) - count
