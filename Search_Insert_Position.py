from typing import List
def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            count = 0
            for i in nums:
                if i > target:
                    return nums.index(i)
                if count == len(nums) -1 and i <target :
                    return len(nums)
                if len(nums) == 1:
                    if i < target:
                        return 1
                    else:
                        return 0
                count +=1
print(searchInsert(self='',nums=[1,3], target = 2))
