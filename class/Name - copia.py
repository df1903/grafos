"""————————————————
   name class
———————————————————"""
class Name:

    # builder
    def __init__(self, var1, var2, var3, var4, var5):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.var5 = var5

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | Var1
    def getVar1(self):
        return self.var1

    def setVar1(self,var1):
        self.var1 = var1

    # Set - Get | var2
    def getVar2(self):
        return self.var2

    def setVar2(self,var2):
        self.var2 = var2

    # Set - Get | var3
    def getVar3(self):
        return self.var3

    def setVar3(self,var3):
        self.var3 = var3

    # Set - Get | var4
    def getVar4(self):
        return self.var4

    def setVar4(self,var4):
        self.var4 = var4

    # Set - Get | var5
    def getVar5(self):
        return self.var5

    def setVar5(self,var5):
        self.var5 = var5

    """————————————————————————————————————————————METHODS———————————————————————————————————————————————————————"""

    # to string
    def toString(self):
        s = '▌▓▒░    | dato ' + str(self.var1()) + \
            ' | var2: ' + str(self.var2) + \
            ' | var3: ' + str(self.var3) + \
            ' | var4: ' + str(self.var4) + \
            ' | var5: ' + str(self.var5)
        return s





