public class Solution {
    public int RemoveElement(int[] nums, int val) 
    {
        int count = 0;
        for (int lp = 0, rp = nums.Length - 1; lp <= rp;)
        {
            if (nums[lp] == val)
            {
                if (nums[rp] == val)
                {
                    count += 1;
                    rp -= 1;
                }
                else
                {
                    nums[lp] = nums[rp];
                    count += 1;
                    lp += 1;
                    rp -= 1;
                }
            }
            else
            {
                lp += 1;
            }
        }
        return (nums.Length) - count;
    }
}