#   files concept 
# creating a class called programer and having the information of programes 

class Programers:
    company = "MircoSoft"
    def profile(self,name,age,lang):
        self.name = name
        self.age = age
        self.lang = lang
        print(f'''
                The Programer Name is : {self.name},
                The Programer Age is: {self.age},
                The Programer Language is : {self.lang}
        ''')

atiq = Programers()
atiq.profile("Atiq",19,"python") #  Progarmer.profile(atiq)

