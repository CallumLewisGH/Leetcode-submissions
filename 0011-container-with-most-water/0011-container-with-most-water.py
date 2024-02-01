class Solution(object):
    def maxArea(self, height):
        returnArea = 0
        lp = 0
        rp = len(height) - 1
        while rp > lp:
            if height[lp] > height[rp]:
                length = height[rp]
                width = rp - lp
                area = width * length
                rp -= 1

            else:
                length = height[lp]
                width = rp - lp
                area = width * length
                lp += 1


            if area > returnArea:
                returnArea = area
            
        return returnArea