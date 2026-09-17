def isPalindrome(self, x: int) -> bool:
    x=input("x=?")
        s=str(x)
        if s==s[::-1]:
            return True      
        else :
            return False