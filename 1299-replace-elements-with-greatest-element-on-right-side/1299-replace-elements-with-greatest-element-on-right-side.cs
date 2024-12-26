public class Solution {
    public int[] ReplaceElements(int[] arr) 
    {
        int i = arr.Length - 1;
        int greatest = arr[i];
        int temp;
        while(i >= 0)
        {
            temp = greatest;

            if (arr[i] > greatest)
            {
                greatest = arr[i];
            }

            arr[i] = temp;

            i -= 1;
        }
        arr[arr.Length - 1] = -1;
        return arr;
        
    }
}