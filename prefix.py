from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:

    if len(strs) == 0:
      return ""

    common = strs[0]

    if len(common) == 0:
      return ""

    for s in strs[1:]:
      if len(s) == 0 or s[0] != common[0]:
        return ""

      i = 0

      n = len(s) if len(s) < len(common) else len(common)

      while i < n and s[i] == common[i]:
        i += 1
      
      common = s[:i]

    return common

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))

