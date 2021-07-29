from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        window=deque()
        cur_max = float('-inf')
        
        for i,x in enumerate(nums):
            while window and nums[window[-1]] < x:
                window.pop()
            window.append(i)
            
            if window[0] == i - k:
                window.popleft()
            if i >= k - 1:
                output.append(nums[window[0]])
        return output