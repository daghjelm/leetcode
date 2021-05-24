#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
class Solution:
  
  def romanToInt(self, s: str) -> int:
    res = 0

    symbol_dict = {
      'I' : 1,
      'V' : 5,
      'X' : 10,
      'L' : 50,
      'C' : 100,
      'D' : 500,
      'M' : 1000
    }

    current = 1

    for i in reversed(range(0, len(s))):
      val = symbol_dict[s[i]]
      if val < current:
        res -= val
      else:
        res += val
      current = val

    return res

sol = Solution()
print(sol.romanToInt("XXVI"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("VX"))

    
      

    
