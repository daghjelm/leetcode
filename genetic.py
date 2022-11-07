class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not end in bank:
            return -1
        viable = [False] * len(bank)
        if self.string_diff(start, end) == 1:
            return 1
        
        current = start for i in range(len(bank)):
            if self.string_diff(end, bank[i]) == 1:
                viable[i] = True
             
    def helper(self, current, end, bank):
        viable = [False] * len(bank)
        for i in range(len(bank)):
            if self.string_diff(end, bank[i]) == 1:
                viable[i] = True
             
        
    def string_diff(self, s1, s2):
        diff = 0
        for i in range(8):
            if s1[i] != s1[i]:
                diff += 1
        return diff
        
 #       start = "AAAAACCC", end = "AACCCCCC", 
 #       bank = ["AAAACCCC",
 #               "AAACCCCC",
 #               "AACCCCCC"]
 #               "AACCCCCC", 

