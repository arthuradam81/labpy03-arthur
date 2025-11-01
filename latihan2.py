modal = 100000000

total = 0

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0
    elif bulan <= 4:
        laba = 0.01 * modal
    elif bulan <= 7:
        laba = 0.05 * modal
    else:
        laba = 0.03 * modal
    
    total += laba
    print(f"laba bulan ke-{bulan} sebesar: {laba}")

print(f"Total laba adalah: {total}")
