class Session:
    def __init__(self, login):
        self.login = login
    
    def loging(self):
        return f"{self.login} logged in"
    
    def logout(self):
        return f"{self.login} logged out"
    
s = Session()
s.login("Ali")
s.logout()