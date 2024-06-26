from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (350, 600)


class IMCAPP(MDApp):
    def build(self):
        screen = Builder.load_file('screen.kv')
        return screen
    
    def calculate(self):
        poids = self.root.ids.poids.text
        taille = self.root.ids.taille.text
        if poids != "" and taille != "":
            imc = round(float(float(poids) / float(taille)**2), 1)
            self.root.ids.imc.text = f"Votre IMC est de : [b]{imc}[/b]"
            if imc < 18.5:
                result = "Vous êtes en maigreur"
            elif 18.5 <= imc < 25:
                result = "Vous êtes en poids normal"
            elif 25 <= imc < 30:
                result = "Vous êtes en sur poids"
            elif 30 <= imc < 40:
                result = "Vous êtes en obesité modérée"
            else:
                result = "Vous êtes en obesité sévère"
            self.root.ids.tips.text = f"[b][i]Analyse :[/i][/b] {result}"
            
        else:
            print('Entrez de valeurs correctes')

if __name__=="__main__":
    IMCAPP().run()