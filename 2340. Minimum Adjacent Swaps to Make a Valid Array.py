# find index of first maximum from the right
# find index of first minimum from the left
# smaller index will need smaller index number of swaps to move to left.
# larger number will need n - larger index - 1 number of swaps to move to right
# if smaller index is to the right of larger index, subtract 1 from the result
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_num = max(nums)
        largest_idx = len(nums) -1
        n = len(nums) 
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == max_num:
                largest_idx = i
                break
        min_num = min(nums)
        smallest_idx = 0
        for i in range(len(nums)):
            if nums[i] == min_num:
                smallest_idx = i
                break
        if smallest_idx > largest_idx:
            return smallest_idx + n - largest_idx - 2
        else:
            return smallest_idx + n - largest_idx - 1
