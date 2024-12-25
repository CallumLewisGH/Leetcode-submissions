public class Solution {
    public bool CheckIfExist(int[] arr)
    {
        HashSet<int> doubleIntegerHashSet = new HashSet<int>(); // Allows O(1) lookups
        int count = 0;

        for (int i = 0; i < arr.Length; i++)
        {
            doubleIntegerHashSet.Add(arr[i] * 2);
        }
        for (int i = 0; i < arr.Length; i++)
        {
            if(doubleIntegerHashSet.Contains(arr[i]))
            {
                if (arr[i] == 0)
                {
                    count += 1;
                    if (count != 2)
                    {
                        continue;
                    }
                }

                return true;
            }
        }
        return false;

        
    }
}