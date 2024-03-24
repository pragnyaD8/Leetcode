class Solution:
    def reverse(self, x: int) -> int:
            MAX_INT = 2 ** 31 - 1 # 2,147,483,647
            MIN_INT = -2 ** 31    #-2,147,483,648
            r=0
            while(x!=0):
                if r > MAX_INT / 10 or r < MIN_INT / 10:
                     return 0
                rem= x%10 if x>0 else x%-10
                r=r*10+rem
                x=math.trunc(x / 10) 
            return r          
                

        