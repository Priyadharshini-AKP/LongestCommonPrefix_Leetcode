class Solution(object):
    def longestCommonPrefix(self, strs):
      str_list=[]
      while all(strs):
        x=strs[0][0]
        true_list = [s.startswith(x) for s in strs]
        if all(true_list):
          str_list.append(x)
          strs=[string[1:] for string in strs]
        else:
          break
      return "".join(str_list)   
        
