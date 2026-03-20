class Solution:
	def minJumps(self,arr):
	    n = len(arr)
	    
	    if n == 1:
	        return 0
	        
        if arr[0] == 0:
            return -1
	            
        jumps = 0
        currentEnd = 0
        farthest = 0
	        
        for i in range(n - 1):
            farthest = max(farthest, i + arr[i])
	            
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
	                
                if currentEnd <=i:
                    return -1
	                    
                if currentEnd >= n - 1:
                    return jumps
                
        return -1
	    
