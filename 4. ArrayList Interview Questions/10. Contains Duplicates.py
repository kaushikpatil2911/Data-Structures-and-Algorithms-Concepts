def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            print(True)
        seen.add(num)

nums = [1,2,3,4,1]
contains_duplicate(nums)    