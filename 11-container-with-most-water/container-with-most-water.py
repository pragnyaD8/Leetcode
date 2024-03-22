class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        area=[]
        for i in range(0,len(height)):
            if height[l]<height[h]:
                area.append((h-l)*min(height[l],height[h]))
                l=l+1
            else:
                area.append((h-l)*min(height[l],height[h]))
                h=h-1
        print(area)
        return max(area)
