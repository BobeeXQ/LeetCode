class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
		#if there is 2 or less points, return its length
        if len(points) <= 2:
            return len(points)
        
        lines = {}
    
        def intersection(p1, p2):
            #the line is vertical, thus slope is infinite
            if p2[0] == p1[0]:
                return (p1[0], 0, math.inf )
				
			#otherwise, find intersection point and slope and return
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            y = p1[1] - p1[0] * slope
            return (0, y, slope)
        
		#now iterate through every two points combination
        for i in range(len(points)):
            for j in range(i+1,len(points)):
				
				#find the info of the line connecting these two points
                info = intersection(points[i],points[j])
				
				#if there is a key in hashmap matching the info, add these two points to it if hasn't already
                if info in lines.keys():
                    if points[i] not in lines[info]:
                        lines[info].append(points[i])
                    if points[j] not in lines[info]:
                        lines[info].append(points[j])
					
				#otherwise, create a new key containing these two points
                else:
                    lines[info] = [points[i], points[j]]
        
		#find the length of the longest line and return it
        length = 0
        for a in lines.values():
            if len(a) > length:
                length = len(a)
                
        return length
