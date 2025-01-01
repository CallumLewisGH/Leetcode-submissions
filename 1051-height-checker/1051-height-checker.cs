public class Solution {
    public int HeightChecker(int[] heights) 
    {
        int count = 0; 
        int[] nonSortedHeights = heights.ToArray();
        Array.Sort(heights);

        for(int i = 0; i < heights.Length;i++)
        {
            if (nonSortedHeights[i] != heights[i]) count++;
        }

        return count;
    }
}