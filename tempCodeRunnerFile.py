def repeatedSubstringPattern( s: str) -> bool:
        len_s = len(s)
        for i in range(1,len_s//2+1):
            print("i=",i,s[:i]*5)
            if len_s % i == 0:
                if s[:i-1]*(len_s % i) == s:
                    return True
        return False
            


print(repeatedSubstringPattern("abab"))