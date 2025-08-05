lines = [
    "Toi hoc o Aptech.",
    "Troi  nong dien!",
    "Aptech cung cap cac khoa hoc CNTT.",
    "Yeu lai tu dau Python.",
    "Aptech co 2 cs o HN.",
    "Mai chua thay mua dau.",
    "Me aptech.",
    "Roll lech char.",
    " Dg lam bai tap  o Aptech.",
    "Di ngu thoi!"
]

with open("data.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "aptech" in line.lower():
            print(line.strip())

