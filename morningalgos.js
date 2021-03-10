// Reverse String
// Create a function reverseString(str) that, given a string, will return a string of the same length but with characters reversed. Example: given "creature", return "erutaerc". Do not use the built-in reverse() function!

function reverseString(string){
    let a ="";
for (let i =string.length-1; i>=0; i--){
    a+= string[i];
}
return a
}
console.log(reverseString("mommy"));
//

def reverse_string(str):
    reversed = ''
    for i in range(len(str)-1, -1, -1):
    reverse+= string[i]
return reversed

print(reverse_string('welcome to python!'))


// Parens Valid
// Create a function that, given an input string, returns a boolean whether parentheses in that string are valid. Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n)0(t(0)k", return false.
//

function parensValid2(str){
    var countOpenParens = 0
    var countClosedParens = 0
    var read
    for(var i = 0; i<str.length; i++)
        read = str[i];
        if (read == '('){
            countOpenParens++
        }
        if (read == ')'){
            countClosedParens++
        }
    if(countOpenParens == countClosedParens){
        return true;
    }
    else
        return false;
}
//
function parensValid(str){
    const paranstack = [];

    for (const char of str) {
        if (char ==="(") {
            parenStack.push(char);
        }
        else if (char ===")") {
            if (parenStack.length ===0){
                return false;
            }else {
                parenStack.pop();
            }
        }
    }
}

def parens_valid(input_str):
    parens_stack = []
    for char in input_str:
        if char == '(':
            parens_stack.append(char)
        elif char ==')':
            if len(parens_stack)== 0:
                return false
            else: 
                parens_stack.pop()
    return len(parens_stack) ==0
print(parens_valid())

function is_palidrome(str){
    var temp = ""
    for(var i=str.length-1; i>=0;i--){
        temp += str[i]
    }
    if (temp == str){
        return true
    }
    else{
        return false
    }
}

console.log(is_palidrome("racecar"))
console.log(is_palidrome("snack"))
console.log(is_palidrome("nathan"))
console.log(is_palidrome("noon"))
console.log(is_palidrome("lol")) //returns true

// Make a function that is a palindrome
// Treat word as string  
// Figure out length of string
// Compare if first character and last character are same
// Stop at string.length/2
// If string.length/2 is even it's already a boolean, not a palindrome
    