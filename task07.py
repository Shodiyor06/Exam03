class StringTools:
    @staticmethod
    def is_palindrome(text):
        t = text[::-1]
        return t == text
    @classmethod
    def from_sentence(self, text):
        self.text = text
    
    def words(self):
        lst = []
        lst2 = []
        lst.append(self.text)
        for i in lst:
            lst2.append(i)
        print(lst2)
        

print(StringTools.is_palindrome("level"))
st = StringTools()
st.from_sentence("I love Python")
print(st.words())