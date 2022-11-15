class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.l1 = len(v1)
        self.l2 = len(v2)
        
    def next(self) -> int:
		#iterator has iterated through the entire list of v2 and now only iterates through v1
        if self.i + 1 > 2 * self.l2:
            curr = self.v1[self.i-self.l2]
			
		#iterator has iterated through the entire list of v1 and now only iterates through v2
        elif self.i + 1 > 2 * self.l1:
            curr = self.v2[self.i-self.l1]
			
		#iterator hasn't iterate through any entire list and now on a location in v1
        elif self.i % 2 == 0:
            curr = self.v1[self.i//2]
			
		#iterator hasn't iterate through any entire list and now on a location in v2
        else:
            curr = self.v2[self.i//2]
			
        self.i += 1
        return curr

    def hasNext(self) -> bool:
        return False if self.i + 1 > self.l1 + self.l2 else True
