DATA = ['Ankara', 'Turkey', 'Tokyo', 'Japan', 'Lisbon', 'Portugal']
CITY = []
COUNTRY = []
for i in range(0, len(DATA), 2):
    CITY.append(DATA[i])
    COUNTRY.append(DATA[i + 1])

print(CITY, COUNTRY)