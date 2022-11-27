#Q.4

from collections import Counter
class String_Count:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = 0
        right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

#Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
My_String_Count=String_Count()
My_String_Count.lengthOfLongestSubstring('abcdefabbdcdssa')
