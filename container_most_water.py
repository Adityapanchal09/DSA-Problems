height=[1,7,2,5,4,7,3,6]
#output=36

#formula=min(height[l],height[r])*(r-l)

#using two pointers:
def most_water(height):
    l=0
    r=len(height)-1

    for _ in range(len(height)):
        container=min(height[l],height[r])*(r-l)
        if min==height[l]:
            l+=1
        else:
            r-=1

        return container
            
    
print(most_water(height))    