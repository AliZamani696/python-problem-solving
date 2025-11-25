
def palindrome(InStr):
        start ,end = 0,len(InStr)-1
        while start < end:
                while not InStr[start].isalnum():
                        start += 1
                while not InStr[end].isalnum():
                        end -= 1
                if InStr[start] != InStr[end]:
                        return False
                start +=1
                end -= 1
        return True
print( palindrome("ama"))
