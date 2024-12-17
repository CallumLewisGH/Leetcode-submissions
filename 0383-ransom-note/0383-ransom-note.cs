public class Solution {
    public bool CanConstruct(string ransomNote, string magazine)
    {
        var magazineChars = new List<char>(magazine);

        for (int i = 0; i < ransomNote.Length; i++)//Faster than foreach
        {
            if (!magazineChars.Remove(ransomNote[i]))//Faster than .Contains()
            {
                return false;
            }
        }

        return true;
    }

}