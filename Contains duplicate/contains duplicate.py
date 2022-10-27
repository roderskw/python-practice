def containsDuplicate(self, nums: list[int]) -> bool:
    if(len(set(nums)) == len(nums)):
        return False
    return True
# set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements