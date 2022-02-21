from typing import List

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Step 1: Loop thru ever num in array
        # Step 2: Lookup amnt of times appeared in array 
        # Step 3: += 1, or return the num is bigger > n / 2

        #Time Complexity O(n)
        #Space Complexity O(n)
        
        numDictionary = {}
        if len(nums) == 1: return nums[0]
        for num in nums:
            if num in numDictionary:
                numDictionary[num] += 1
                
                if (numDictionary[num] > (len(nums) / 2)): return num
            else:
                numDictionary[num] = 1

    def majorityElementBoyMoore(self, nums: List[int]) -> int:
        
        #Boyer Moore Voting Algorithm
        #Better then dictionary method because it uses constant space O(1)
    
        candidate = None
        count = 0
        
        for n in nums:
            if n == candidate:
                count += 1
            
            elif n != candidate:
                count -= 1
                if count < 1: 
                    count = 1
                    candidate = n
                
            
        return candidate
            
if __name__ == '__main__':

    nums = [1,2,2,2,3]
    solution = Solution()
    num = solution.majorityElement(nums)
    print(num)