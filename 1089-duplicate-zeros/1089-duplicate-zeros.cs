public class Solution {
    public void DuplicateZeros(int[] arr) 
    {
        Queue<int> queue = new Queue<int>();
        for(int i = 0; i < arr.Length; i++)
        {
            queue.Enqueue(arr[i]);
            if (arr[i] == 0)
            {
                queue.Enqueue(arr[i]);
            }
            arr[i] = queue.Dequeue();
        }
    }
}