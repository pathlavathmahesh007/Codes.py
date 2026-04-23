class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: count good elements
        good = sum(1 for x in arr if x <= k)
        
        # Step 2: count bad elements in first window
        bad = sum(1 for x in arr[:good] if x > k)
        
        ans = bad
        
        # Step 3: slide the window
        i, j = 0, good
        
        while j < n:
            # remove left element
            if arr[i] > k:
                bad -= 1
            
            # add right element
            if arr[j] > k:
                bad += 1
            
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans
