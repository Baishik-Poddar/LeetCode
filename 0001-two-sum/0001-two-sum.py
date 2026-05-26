class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict ={}
        difference=0
        for i in range(0,len(nums)):
            difference= target - nums[i]
            if difference in my_dict:
                return( my_dict[difference],i)
            my_dict[nums[i]]=i
        return[]
