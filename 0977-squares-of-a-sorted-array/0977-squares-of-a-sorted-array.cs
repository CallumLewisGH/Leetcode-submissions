public class Solution {
   public int[] SortedSquares(int[] nums)
{
    int pointer1 = 0; 
    int pointer2 = nums.Length - 1;
    int[] result = new int[nums.Length]; 
    int insertPos = nums.Length - 1; 

    while (pointer1 <= pointer2)
    {
        int leftSquare = nums[pointer1] * nums[pointer1];
        int rightSquare = nums[pointer2] * nums[pointer2];

        if (leftSquare > rightSquare)
        {
            result[insertPos] = leftSquare;
            pointer1 += 1;
        }
        else
        {
            result[insertPos] = rightSquare;
            pointer2 -= 1;
        }

        insertPos -= 1;
    }

    return result;
}

}