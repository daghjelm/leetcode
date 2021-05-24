class Solution:
  def isValid(self, s: str) -> bool:
    
    if len(s) == 1:
      return False

    matching = {
      '(' : ')',
      '{' : '}',
      '[' : ']'
    }

    arr = []

    for c in s:
      if matching.get(c):
        arr.append(c)
      else:
        if len(arr) == 0 or not c == matching[arr.pop()]:
          return False

    if len(arr) > 0:
      return False

    return True

sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
      



