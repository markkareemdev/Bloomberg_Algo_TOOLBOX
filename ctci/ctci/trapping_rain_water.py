class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        globalMax = height[0]
        globalMaxIndex = 0
        
        rainWater = 0
        
        for i in range(1, len(height)):
            if height[i] > globalMax:
                globalMax = height[i]
                globalMaxIndex = i
                
        leftMax = 0
        for i in range(globalMaxIndex):
            if height[i] >= leftMax:
                leftMax = height[i]
            else:
                rainWater += leftMax - height[i]
            
        rightMax = 0
        for i in range(len(height)-1, globalMaxIndex, -1):
            if height[i] >= rightMax:
                rightMax = height[i]
            else:
                rainWater += rightMax - height[i]
                
        return rainWater