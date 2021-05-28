class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:

    tracker = 0
    for n in nums[1:]:
      if n != nums[tracker]:
        tracker += 1
        nums[tracker] = n
    
    return tracker + 1
    

      

            
        
