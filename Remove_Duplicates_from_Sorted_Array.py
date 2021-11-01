from collections import OrderedDict
from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    nums = list(OrderedDict.fromkeys(nums))
    return 5

print(removeDuplicates(self='',nums= [0,0,1,1,1,2,2,3,3,4]))