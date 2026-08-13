import FreeCAD as App

# Aktives Dokument holen
doc = App.activeDocument()
if not doc:
    doc = App.newDocument("Tastatur_Projekt")

# ==============================================================================
# 1. TRANSAKTION STARTEN (Setzt den Strg+Z Ankerpunkt)
# ==============================================================================
# Der Name erscheint später im Bearbeiten -> Rückgängig-Menü
doc.openTransaction("Tastatur Layout Generieren")

try:
    # 2. SPREADSHEET ANLEGEN ODER HOLEN
    sheet_name = "Tastatur_Layout"
    sheet = doc.getObject(sheet_name)
    if not sheet:
        sheet = doc.addObject("Spreadsheet::Sheet", sheet_name)

    # Performance-Booster: Live-Recompute während des Schreibens ausschalten
    sheet.Recompute = False

    # ==========================================================================
    # 3. ZELLEN, ALIASE & FORMELN BEFÜLLEN
    # ==========================================================================
    
    # KOPFZEILEN
    sheet.set("A1", "Parameter")
    sheet.set("B1", "Wert")
    sheet.set("C1", "Einheit")

    # GRUNDPARAMETER (Parameter-Aliase)
    sheet.set("A2", "Key Pitch X")
    sheet.set("B2", "19.05")
    sheet.setAlias("B2", "Key_Pitch_X")

    sheet.set("A3", "Key Width")
    sheet.set("B3", "18.00")
    sheet.setAlias("B3", "Key_Width")

    # BEISPIEL SCHLEIFE: Tastenpositionen mit dynamischen Formeln
    sheet.set("A5", "Taste ID")
    sheet.set("B5", "X-Position (mm)")

    for i in range(1, 11):  # Erzeugt beispielhaft 10 Tasten
        row = 5 + i
        key_id = f"Key_{i:02d}"
        
        # Spalte A: Name der Taste
        sheet.set(f"A{row}", key_id)

        # Spalte B: Dynamische Formel eintragen
        if i == 1:
            sheet.set(f"B{row}", "0.0")
        else:
            prev_row = row - 1
            # Schreibt eine echte FreeCAD-Formel in die Zelle!
            sheet.set(f"B{row}", f"=B{prev_row} + Key_Pitch_X")

        # Alias für die Positionszelle vergeben (z.B. Key_01_X, Key_02_X)
        sheet.setAlias(f"B{row}", f"{key_id}_X")

    # ==========================================================================
    # 4. ABSCHLUSS & RECOMPUTE
    # ==========================================================================
    sheet.Recompute = True
    doc.recompute()

    # TRANSAKTION ERFOLGREICH SCHLIESSEN
    doc.commitTransaction()
    print("✅ Spreadsheet 'Tastatur_Layout' wurde erfolgreich erzeugt.")
    print("ℹ️ Du kannst diese Aktion jetzt komplett mit Strg + Z rückgängig machen.")

except Exception as e:
    # Falls im Code ein Fehler auftritt: Alle bisherigen Änderungen verwerfen
    doc.abortTransaction()
    print(f"❌ Fehler aufgetreten. Transaktion abgebrochen: {e}")