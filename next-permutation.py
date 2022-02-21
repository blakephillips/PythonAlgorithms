from typing import List

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return
        swapIndex = None

        for i in range(len(nums) - 2, -1, -1):

            prevNum = nums[i + 1]
            currNum = nums[i]

            if prevNum > nums[i]:
                # The next number that is bigger, but by the smallest amount

                for j in range(i, len(nums)):
                    if nums[j] > nums[i]:
                        # Bigger number found, check if it is closer to the target then the previous bigger number
                        if swapIndex == None or (nums[j] < nums[swapIndex]):
                            swapIndex = j

                if swapIndex != None:
                    nums[i] = nums[swapIndex]
                    nums[swapIndex] = currNum

                    nums[i + 1:] = sorted(nums[i + 1:])
                    break

        if not swapIndex: nums = nums.sort()


if __name__ == '__main__':

    nums = [2,3,1]
    solution = Solution()
    solution.nextPermutation(nums)
    print(nums)