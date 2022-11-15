class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        '''
        Adding all the words from wordDict to hm binding to their first letter
        '''
        hm = {}
        for word in wordDict:
            if word[0] in hm.keys():
                hm[word[0]].append(word)
            else:
                hm[word[0]] = [word]
        
        res = []
        
        '''
        currList is a list of words that could potentially combine to construct a sentence and be stored in res. 
        i in the index of s that we are currently working on.
        '''
        def dfs(currList, i):
			#if there are words that has first letter equal to the next letter in s
            if s[i] in hm.keys():
				#iterate through every words of that key in map
                for w in hm[s[i]]:
					#if the word is part of s
                    if w == s[i:i+len(w)]:
						#option 1: we could accept this word and add it to the list
                        currList.append(w)
						#if adding this word reaches the end of s, a sentence is found, we add it to result
                        if i + len(w) == len(s):
                            res.append(' '.join(currList))
						#else we continue searching
                        else:
                            dfs(currList, i+len(w))
						#option 2: we reject this word and continue searching without it
                        currList.pop()
                            
        dfs([],0)
        return res
