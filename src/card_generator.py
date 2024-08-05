from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

def create_membership_card(name, qr_code_path, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Rk design
    c.setFillColor(colors.lightgrey)
    c.rect(0.5*inch, 1*inch, 3*inch, 2*inch, fill=1)
    
    # Rk Name
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 16)
    c.drawString(1*inch, 2.5*inch, f"Nom: {name}")
    
    # Rk qrCode
    c.drawImage(qr_code_path, 1*inch, 1.5*inch, width=1*inch, height=1*inch)
    
    # Sauvegarder le PDF
    c.save()
