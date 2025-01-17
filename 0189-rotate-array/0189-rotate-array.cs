public class Solution {
    public void Rotate(int[] nums, int k) 
    {
        for(int i = k; nums[0] != nums[i]; i += k)
        {
            int temp = nums[0];
            nums[0] = nums[i];
            nums[i] = temp;
            Console.WriteLine(i);
            Console.WriteLine(string.Join(", ", nums));
            if(i >= nums.Length) i = i % nums.Length;
        }
        if(nums.Length % 2 == 0 && k % 2 == 0)
        {
            for(int i = k + 1; nums[1] != nums[i % nums.Length]; i += k)
            {
                if(i >= nums.Length) i = i % nums.Length;
                int temp = nums[1];
                nums[1] = nums[i];
                nums[i] = temp;
                Console.WriteLine(i);
                Console.WriteLine(string.Join(", ", nums));
                
            }
        }
    }
}