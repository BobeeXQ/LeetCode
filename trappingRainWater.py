class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''
        h is the height of the highest bar of the map
        if it is 0, return 0
        '''
        h = max(height)
        if not h:
            return 0
        
        '''
        l is the index of leftmost non-zero bar
        r is the index of rightmost non-zero bar
        h1 is the index of the leftmost highest bar
        h2 is the index of the righ most highest bar
        if l equals to r, means there is only one bar that holds 0 water, return 0
        '''
        l = next((i for i, x in enumerate(height) if x), None)
        r = len(height) - 1 - next((i for i, x in enumerate(height[::-1]) if x), None)
        h1 = next((i for i, x in enumerate(height) if x == h), None)
        h2 = len(height) - 1 - next((i for i, x in enumerate(height[::-1]) if x == h), None)
        if l == r:
            return 0
        
        '''
        find the final result using outer_area - inner_area which is amount of water trapped
        outer_area: from the left side and right side of the map, consider the entire outer_area 
                    as two opposing ascending stairs plus the central rectangular area of the highest bar
        inner_area: simply the sum of the input list
        '''
        outer_area = 0
        inner_area = sum(height)
        curr = height[l]
        for i in range(l,h1):
            if height[i] > curr:
                curr = height[i]
            outer_area += curr
        outer_area += h * (h2 - h1 + 1)
        curr = height[r]
        for i in range(r,h2,-1):
            if height[i] > curr:
                curr = height[i]
            outer_area += curr
            
        return outer_area - inner_area
