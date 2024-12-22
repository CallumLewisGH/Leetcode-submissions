public class Solution {
    public int RemoveElement(int[] nums, int val) 
    {
        int lp = 0;
        int rp = nums.Length - 1;
        for (; lp <= rp;)
        {
            if (nums[lp] == val)
            {
                if (nums[rp] != val)
                {
                    nums[lp] = nums[rp];
                    lp += 1;
                }
                rp -= 1;
            }
            else
            {
                lp += 1;
            }
        }
        return rp + 1;
    }
}