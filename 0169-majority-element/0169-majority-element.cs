public class Solution {
    public int MajorityElement(int[] nums) 
    {
        int num = nums[0];
        int count = 0;
        Console.WriteLine(string.Join(", ", nums));
        for( int i = 0; i < nums.Length; i++)
        {
            if(count == 0)
            {
                num = nums[i];
                count = 1;
            }
            else if(num == nums[i])
            {
                count += 1;
            }
            else
            {
                count -= 1;
            }
            Console.WriteLine($"Count = {count}|Num = {num}| pointer = {i}");
        }

        return num;
    }
}