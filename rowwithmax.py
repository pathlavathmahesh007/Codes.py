class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        i, j = 0, m - 1
        max_row = -1
        
        while i < n and j >= 0:
            if arr[i][j] == 1:
                max_row = i
                j -= 1  # move left
            else:
                i += 1  # move down
        
        return max_row
