class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        '''
        intialize a list recording the amount of candy of each children
        '''
        candy = [1] * len(ratings)
    
        '''
        from left to right, if rating of current children is greater than the left one
        #let current children have one more than children on the left
        '''
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        '''
        from right to left, do the same thing
        except for that if current children already has one more candy than 
        the children to the right, let the children keep it
        '''
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i],candy[i+1]+1)
            
        return sum(candy)
    
        '''
        Space: O(n)     Time: O(n)
        '''
