public class Solution {
    public bool CanConstruct(string ransomNote, string magazine)
    {
        var magazineChars = new List<char>(magazine);

        foreach (char c in ransomNote)
        {
            if (magazineChars.Contains(c))
            {
                magazineChars.Remove(c);
            }
            else
            {
                return false;
            }
        }

        return true;
    }

}