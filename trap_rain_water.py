height=[0,2,0,3,1,0,1,3,2,1]
#output=9

#using two pointers:
def trap_water(height):
    left=0;right=len(height)-1
    water=0
    max_left=0;max_right=0
    while left<right:
        if height[left]<=height[right]:
            if height[left]>=max_left:
                max_left=height[left]    
            else:
                water+=max_left-height[left] 
            left+=1       
        else:
            if height[right]<=height[left]:
                if height[right]>=max_right:
                    max_right=height[right]
                else:
                    water+=max_right-height[right]
                right-=1    
    return water                
print(trap_water(height))        
