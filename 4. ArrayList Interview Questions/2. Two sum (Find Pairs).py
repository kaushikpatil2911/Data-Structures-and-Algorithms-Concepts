def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(nums[i],nums[j])

nums = [1,2,4,6,3,2,0]
findPairs(nums,9)


#Leetcode Problem 1 solution

def twoSum(self, nums, target):
    seen = {}
    for i, num in enumerate(nums):
        exist = target - num
        if exist in seen:
            return [seen[exist],i]
        seen[num] = i