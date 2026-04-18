import pandas as pd
import numpy as np

sales_tab = pd.DataFrame({
    "ID": [101, 102, 103, 101, 105, 106, 107, np.nan, 109, 110, 111, 112, 113, 114, 115, 
           116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130],
    "Data": ["2024-04-01", "02.04.2024", "2024/04/03", "2024-04-01", "brak", "2024-04-06", 
             "2024-04-07", "2024-04-08", "2024-04-09", "10-04-2024", "2024-04-11", "wczoraj", 
             "2024-04-13", "2024-04-14", "2024-04-15", "16.04.2024", "2024/04/17", "18-04-2024",
             "2024-04-19", "brak", "21.04.2024", "2024-04-22", "23/04/2024", "24.04.2024",
             "25-04-2024", "brak", "27.04.2024", "28/04/2024", "2024-04-29", "30.04.2024"],
    "Produkt": ["Monitor", "Myszka ", "Klawiatura", "Monitor", "Laptop", " Monitor", 
                "Podkladka", "Glosniki", "Myszka", "Klawiatura", None, "Sluchawki", 
                "Monitor", "Laptop", "Myszka", "Kabel HDMI", " Monitor", "Myszka ", 
                "Klawiatura", "Laptop", "Podkladka", "Glosniki", "Monitor", "Laptop", 
                "Kabel HDMI", "Myszka", "Monitor", "Klawiatura", "Monitor", "Laptop"],
    "Cena": ["1200", " 50.00 PLN", None, "1200", "3500", "1250", "25.50", "150", "-10", 
             "120.00", "450", "300", "1200", "3500", "50", "40 PLN", "1250", " 55.00 PLN",
             "130", "3500", "25", "160", "1200", "3400", "45", "50", "-1200", "125", "1150", "3500"],
    "Ilosc": ["2", "1", "5", "2", "brak", "1", "10", "2", "3", "0", "1", "2", "brak", "1", "2",
              "5", "1", "2", "4", "1", "10", "2", "3", "1", "5", "brak", "1", "3", "2", "1"],
    "Kraj": ["Polska", "Polka", "PL", "Polska", "Niemcy", "nIEMCY", "Polska", "polska", 
             "Poland", "Polska", "Francja", "France", "Polska", "Polska", "Polska",
             "Polska", "Niemcy", "Polka", "Polska", "nIEMCY", "Polska", "Polska", "Polska",
             "Niemcy", "Polska", "Polska", "PL", "Francja", "Polska", "Niemcy"]
})

df = sales_tab
df.loc[0,"ID"] = 100
df["ID"] = df["ID"].interpolate()
df["Data"] = pd.to_datetime(df["Data"],dayfirst = True, errors = "coerce",format="mixed")
df = df.sort_values(by="Data", ascending = True)

df["Produkt"] = df["Produkt"].str.strip()

df["Cena"] = df["Cena"].str.replace(" PLN", "")
df["Cena"] = pd.to_numeric(df["Cena"])
df["Cena"] = abs(df["Cena"])

df["Ilosc"] = pd.to_numeric(df["Ilosc"], errors = "coerce")

df["Kraj"] = df["Kraj"].replace({"Poland": "Polska",
                                  "polska": "Polska",
                                  "Polka": "Polska",
                                  "PL" : "Polska",
                                 "nIEMCY" : "Niemcy",
                                 "France" : "Francja"})
df = df.dropna(subset = "Data")
df["ID"] = df["ID"].astype(int)
df["Cena"] = df["Cena"].fillna(0)
df["Ilosc"] = df["Ilosc"].fillna(0)
df["Ilosc"] = df["Ilosc"].astype(int)

df["Przychod"] = df["Cena"] * df["Ilosc"]

print(df.to_string())
print(df.dtypes)

df.to_csv("clean_sales.csv", index=False)


