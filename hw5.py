data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
print(codes)
operators = dict(zip(designations, [{code} for code in set(codes)]))

del operators["Katel"]
del operators["Fonex"]


operators['Megacom'].update(['705', '704'])
operators['O!'].update(['551', '552'])
operators['Beeline'].update(['435', '405'])

for key, value in operators.items():
    print(f"{key} — {value}")