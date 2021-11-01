from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return nums

print(removeElement(self='',nums =[3,2,2,3],val= 3))