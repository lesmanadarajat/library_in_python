import pandas as pd

biodata_scientists = {"Nama" : ["Albert Einstein", "Isaac Newton", "Neils Bohr",
                        "Marie Curie", "Richard Feynman"],
                        "Lahir" : ["14-03-1879", "4-01-1643", "7-10-1885", "7-11-1867", "11-05-1918"],
                        "Wafat" : ["18-04-1955", "31-03-1727", "18-11-1962", "4-07-1934", "15-02-1988"],
                
                        "Umur" : [76, 84, 77, 66, 69],
                
                        "Penemuan" : ["Teori Relativitas Khusus & Umum", "Hukum Gravitasi Universal",
                              "Model Atom", "unsur polonium & radium", "Elektrodinamika kuantum"],
                
                   "Penghargaan" : ["Nobel Fisika (1921)", "Ga Ada", "Nobel fisika (1922)", "Nobel Fisika (1903) & Nobel Kimia (1911)",
                                    "Nobel Fisika (1965)"],
}
                
# buat variabel biodata yg isinya biodata_scientists
biodata = pd.DataFrame(biodata_scientists)

# nyimpen ke excel
name_to = "Biografi_Scientist.xlsx"
biodata.to_excel(name_to, index=False)

print(f"file excel {name_to} telah di buat")