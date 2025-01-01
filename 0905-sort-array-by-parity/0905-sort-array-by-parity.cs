public class Solution {
    public int[] SortArrayByParity(int[] nums) 
    {
        int temp;

        for (int p1 = 0, p2 = 0; p2 < nums.Length && p1 < nums.Length;)
        {
            if(nums.Length == 1) return nums;

            if (nums[p1] % 2 == 0) 
            {
                p1++;
                continue;
            }

            if (nums[p2] % 2 == 0)
            {
                temp = nums[p1];
                nums[p1] = nums[p2];
                nums[p2] = temp;
                continue;
            }

            p2++;
        }
        return nums;
        
    }
}