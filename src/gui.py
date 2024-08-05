import tkinter as tk
from tkinter import messagebox
from qr_code_generator import generate_qr_code
from card_generator import create_membership_card
import os

class MembershipCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RK_Solution - Gestion des Cartes d'Apprenants")

        # Nom
        self.name_label = tk.Label(root, text="Nom de l'apprenant:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # URL QR Code
        self.qr_data_label = tk.Label(root, text="Données pour QR Code:")
        self.qr_data_label.pack()
        self.qr_data_entry = tk.Entry(root)
        self.qr_data_entry.pack()

        # Bouton pour générer la carte
        self.generate_button = tk.Button(root, text="Générer la carte", command=self.generate_card)
        self.generate_button.pack()

    def generate_card(self):
        name = self.name_entry.get()
        qr_data = self.qr_data_entry.get()
        if not name or not qr_data:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        # Créer un dossier pour les codes QR s'il n'existe pas
        qr_code_dir = "assets/qr_codes"
        os.makedirs(qr_code_dir, exist_ok=True)
        
        # Générer le code QR
        qr_code_path = os.path.join(qr_code_dir, f"{name}_qr.png")
        generate_qr_code(qr_data, qr_code_path)
        
        # Créer la carte d'apprenant
        card_output_path = f"assets/member_card_{name}.pdf"
        create_membership_card(name, qr_code_path, card_output_path)
        
        messagebox.showinfo("Succès", f"Carte d'apprenant générée : {card_output_path}")

def main():
    root = tk.Tk()
    app = MembershipCardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
