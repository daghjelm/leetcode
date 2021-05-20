class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      l = 0
      c = 0
      strings  = [""]
      index_dict = {}

      print(s)

      for i in range(len(s))

      for i, char in enumerate(s):  
        if char in strings[c]:
          str_l = len(strings[c])
          if str_l > l:
            l = str_l
          c += 1
          char_index = index_dict[char]
          missed_str = s[char_index + 1:i + 1]
          strings.append(missed_str)
          index_dict[char] = i
        else:
          strings[c] += char
          index_dict[char] = i

      print(strings)

      if len(strings[c]) > l:
        l = len(strings[c])
      
      return l

#sol = Solution()
#str1 = "abcabcbb"
#str2 = " "
#str3 = "dvdf"
#print(sol.lengthOfLongestSubstring(str1))
#print(sol.lengthOfLongestSubstring(str2))
#print(sol.lengthOfLongestSubstring(str3))

        
          
