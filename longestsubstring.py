'''
Level: Medium
Frequency: High
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

TODO: Retake this test with second and third approaches
'''


class Solution:
    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        # Time Complexity: O(n^3)
        # Space Complexity:O(n)
        ans = 0
        
        
        N = len(s)
        for i in range(N):
            repeated_word = False
            sub = s[i]
            j = i
            current_size = 1
            while not repeated_word and j + 1 < N:
                j += 1
                if s[j] not in sub:
                    sub += s[j]
                    current_size += 1
                else:
                    repeated_word = True
                
            
            ans = max(ans, current_size)
        return ans


    def lengthOfLongestSubstringSlidingWindowSet(self, s: str) -> int:
        # Time Complexity: O(n) -> actually O(2n)
        # Space Complexity: O(n)        
        N = len(s)
        set_chars = set()
        ans = 0
        i = 0
        j = 0 
        while (i < N and j < N):
            # Try to extend window -> [i, j)
            if s[j] not in set_chars:
                set_chars.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                # Remove only first letter, we do not need to start all over
                set_chars.remove(s[i])
                i += 1
        return ans

    def lengthOfLongestSubstringSlidingWindowHash(self, s: str) -> int:
        # Time Complexity: O(n) -> actually O(2n)
        # Space Complexity: O(n) 
        N = len(s)
        d = {}
        ans = 0
        i = 0
        j = 0
        for j in range(N):
            # Try to extend window -> [i, j)
            if s[j] in d.keys():
                # Start by the next position for i d[s[j]] + 1
                i = max(i, d[s[j]] + 1
            ans = max(ans, j - i + 1)
            d[s[j]] = j
            
        return ans