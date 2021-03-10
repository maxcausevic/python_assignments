function is_palindrome(str){
    temp = ""
    for (i=str.length-1; i>=0; i--){
        if (str[i] != str[str.length-1-i]){
            return false;
        } 
    
    return true;
}
console.log(is_palindrome("racecar"))