from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
import base64
from hashlib import sha256

# --- LOGIQUE DE SÉCURITÉ (Intrinsèquement liée au projet) ---
def decrypt_report(encrypted_string, pin):
    try:
        if not encrypted_string.startswith("CCC_LOCKED_"):
            return "Format Invalide"
        encoded = encrypted_string.replace("CCC_LOCKED_", "")
        return base64.b64decode(encoded).decode()
    except:
        return "Erreur de déchiffrement"

# --- INTERFACE VISUELLE (KV) ---
KV = """
ScreenManager:
    LoginScreen:
    EmployeeScreen:
    PatronScreen:

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        Label:
            text: 'CASH CONTROL CLOUD'
            font_size: '24sp'
            bold: True
        Button:
            text: 'ACCÈS EMPLOYÉ (SAISIE)'
            on_press: root.manager.current = 'employee'
        Button:
            text: 'ACCÈS PATRON (BILAN)'
            on_press: root.manager.current = 'patron'

<EmployeeScreen>:
    name: 'employee'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: 'MODE SAISIE (BRIDE)'
        TextInput:
            id: sales
            hint_text: 'Total Recettes (FCFA)'
        TextInput:
            id: expenses
            hint_text: 'Dépenses du jour'
        Button:
            text: 'GÉNÉRER LE CODE SÉCURISÉ'
            on_press: root.generate_report()
        Button:
            text: 'RETOUR'
            on_press: root.manager.current = 'login'

<PatronScreen>:
    name: 'patron'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: 'TABLEAU DE BORD PATRON'
        TextInput:
            id: pin_code
            hint_text: 'Entrez votre code PIN'
            password: True
        TextInput:
            id: encrypted_input
            hint_text: 'Collez le code reçu ici'
        Button:
            text: 'VOIR LE BÉNÉFICE NET'
            on_press: root.show_profit()
        Label:
            id: result_label
            text: 'Bilan : -- FCFA'
        Button:
            text: 'RETOUR'
            on_press: root.manager.current = 'login'
"""

class LoginScreen(Screen): pass

class EmployeeScreen(Screen):
    def generate_report(self):
        # Simulation du chiffrement pour l'envoi
        data = f"{self.ids.sales.text}|{self.ids.expenses.text}"
        encoded = base64.b64encode(data.encode()).decode()
        self.ids.sales.text = f"CCC_LOCKED_{encoded}" # Affiche le code à envoyer

class PatronScreen(Screen):
    def show_profit(self):
        # Ici on applique la règle du PDF : Recettes - (Dépenses + Charges Fixes)
        raw_data = decrypt_report(self.ids.encrypted_input.text, self.ids.pin_code.text)
        if "|" in raw_data:
            recettes, depenses = map(float, raw_data.split("|"))
            # Simulation charges fixes (Loyer/Eau) définies dans le PDF
            charges_fixes = 5000 # Exemple par jour
            profit = recettes - (depenses + charges_fixes)
            self.ids.result_label.text = f"Bénéfice Net : {profit} FCFA"

class CashControlApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    CashControlApp().run()
