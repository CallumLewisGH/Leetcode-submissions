public class Solution {
    public int MajorityElement(int[] nums) 
    {
        Dictionary<int, int> numberCount = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++)
        {
            if (numberCount.ContainsKey(nums[i]))
            {
                numberCount[nums[i]]++;
                continue;
            }
            numberCount.Add(nums[i], 1);
        }
        return numberCount.Aggregate((x, y) => x.Value > y.Value ? x : y).Key;
    }
}