import pandas as pd
import os


# CONFIG
nume_fisier_txt = 'output.txt'
nume_fisier_excel = 'input.xlsx'


def sterge_fisier(nume_fisier):
    try:
        os.remove(nume_fisier)
        print(f"Fisierul {nume_fisier} a fost sters cu succes.")
    except Exception as e:
        print(f"Eroare la stergerea fisierului: {e}")


def citeste_fisier_xlsx(nume_fisier):
    try:
        df = pd.read_excel(nume_fisier)
        return df
    except Exception as e:
        print(f"Eroare la citirea fisierului: {e}")
        return None


def scrie_fisier_txt(nume_fisier, date):
    try:
        with open(nume_fisier, 'w', encoding='utf-8') as f:
            # Scrie primul rand fix
            f.write("205,12,2024,#0#,#NUMEADMINISTRATOR#,#PRENUMEADMINISTRATOR#,#ADMINISTRATOR#,11223344,#NUME SOCIETATE SRL#,#JUDET  LOCALITATE  STR TESTSTRADA  NR 1 AP 1\n")
            # Scrie restul randurilor din date si verifica daca sunt Rezidenti sau Nerezidenti
            for _, row in date.iterrows():
                # Rezidenti
                if row['Rezident'] == 'Rezident':
                    linie = f"{row['Tip Venituri']},#{row['Nume si prenume beneficiar']}#,1,##,{row['CNP']},##,2,,,{row['Baza impozabila']},{row['Impozit']},##\n"
                    f.write(linie)
                # Nerezidenti
                else:
                    linie = f"{row['Tip Venituri']},#{row['Nume si prenume beneficiar']}#,2,##,{row['CNP']},##,2,,,{row['Baza impozabila']},{row['Impozit']},##\n"
                    f.write(linie)
        print(f"Fisierul {nume_fisier} a fost creat cu succes.")
    except Exception as e:
        print(f"Eroare la scrierea fisierului: {e}")


if __name__ == "__main__":
    print("...start...")

    # Sterge Fisier TXT vechi
    sterge_fisier(nume_fisier_txt)

    # Citeste Fisier Excel
    date = citeste_fisier_xlsx(nume_fisier_excel)
    if date is not None:
        print(date.head())

    # Scrie Fisier TXT nou
    if date is not None:
        scrie_fisier_txt(nume_fisier_txt, date)

    print("...end...")
