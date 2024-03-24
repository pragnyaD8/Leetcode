class Solution:
    def convert(self, s: str, numRows: int) -> str:
       sb=["" for k in range(numRows)]
       i=0
       length=len(s)
       while i<length:
           for j in range(numRows):
            if i<length:
               sb[j]=sb[j]+s[i]
               i=i+1
           for j in range(numRows-2,0,-1):
               if i <length:
                   sb[j]=sb[j]+s[i]
                   i=i+1
       sb= "".join(sb)
       return sb

    
       


            