public class Solution {
    public int ThirdMax(int[] nums)
    {
        int[] distinctMaximums = new int[3];
        int count = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if(distinctMaximums.Contains(nums[i]) && nums[i] != 0) continue;
            if(nums[i] > distinctMaximums[0] || distinctMaximums[0] == 0 )
            {
                count++;
                distinctMaximums[2] = distinctMaximums[1];
                distinctMaximums[1] = distinctMaximums[0];
                distinctMaximums[0] = nums[i];
            }
            else if(nums[i] > distinctMaximums[1] || distinctMaximums[1] == 0 )
            {
                count++;
                distinctMaximums[2] = distinctMaximums[1];
                distinctMaximums[1] = nums[i];
            }
            else if(nums[i] > distinctMaximums[2] || distinctMaximums[2] == 0 )
            {
                count++;
                distinctMaximums[2] = nums[i];
            }
        }
        if (count >= 3) return distinctMaximums[2];
        return distinctMaximums[0];
    }
}