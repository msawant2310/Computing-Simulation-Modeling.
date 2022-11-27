#Q.8
class anagram:
    def ana(self,s,t):
        if set(s)==set(t) and len(s)==len(t):
            return True
        else:
            return False
        
anagram().ana("Avinash","ivshanA")
