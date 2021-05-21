class Solution:
    def reverse(self, x: int) -> int:

      sign = [1, -1][x < 0]
      x *= sign

      y = 0

      int_max = 2147483647
      int_min = -2147483648

      while x:
        y *= 10
        y += x % 10
        x //= 10

      y *= sign

      if y < 0 and y < int_min or y > 0 and y > int_max:
        return 0
      else:
        return y
      


      
          
