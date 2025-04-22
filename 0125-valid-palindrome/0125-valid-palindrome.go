func strip(s []byte) []byte {
    n := 0
    for _, b := range s {
        if ('a' <= b && b <= 'z') ||
            ('0' <= b && b <= '9'){
            s[n] = b
            n++
        }
    }
    return s[:n]
}

func isPalindrome(s string) bool {
    var str = strip([]byte(strings.ToLower(s)))
	lp, rp := 0, len(str) - 1
	for lp < rp {
		if str[lp] != str[rp] {
            return false
		}
        lp++
        rp--
	}
	return true
    
}