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
	var leftHalf []byte
	var rightHalf []byte
	lp, rp := 0, len(str) - 1
	for lp < rp {
		if str[lp] == str[rp] {
			rightHalf = append(rightHalf, str[rp])
			leftHalf = append(leftHalf, str[lp])
		}
        lp++
        rp--
	}

	if len(str)%2 != 0 && len(str) != 1 {
		rightHalf = append(rightHalf, str[(len(str)/2)+1])
	}else if len(str) == 1 {
        rightHalf = append(rightHalf, str[(len(str)/2)])
    }

	var palindrome string = string(rightHalf) + string(leftHalf)

	if len(palindrome) != len(str) {
		return false
	}

	return true
    
}