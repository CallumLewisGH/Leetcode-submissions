public class Solution {
    public int FindNumbers(int[] nums) 
    {
        int evenDigitCount = 0;

        foreach (int num in nums)
        {
            int digitCount = num.ToString().Length;
            
            if (digitCount % 2 == 0)
            {
                evenDigitCount += 1;
            }
        }
        return evenDigitCount;
    }
}