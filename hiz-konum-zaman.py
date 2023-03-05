import time

yol_liste = [600, 1000, 1400, 1800, 2200, 2600, 3000, 3400, 3800, 4200, 4600, 5000, 5400, 5800, 6200, 6600, 7000, 7400, 7800, 7805, 7810, 7815, 7820, 7825, 7830, 7835, 7840, 7845, 7850, 7855, 7860, 7865, 7870, 7875, 7880, 7885, 7890, 7895, 7900, 7905, 7910, 7915, 7920, 7925, 7930, 7935, 7940, 7945, 7950, 7955, 7960, 7965, 7970, 7975, 7980, 7985, 7990, 7995, 8200, 8600, 9000, 9400, 9800, 10200, 10600, 11000, 11400, 11800, 12200, 12600, 13000, 13005, 13010, 13015, 13020, 13025, 13030, 13035, 13040, 13045, 13050, 13055, 13060, 13065, 13070, 13075, 13080, 13085, 13090, 13095, 13400, 13800, 14200, 14600, 15000, 15400, 15800, 16200, 16600, 17000, 17400]

def zamanlayici(reflektorVeri):
    control = reflektorVeri
    t0 = 0
    t1 = 0
    t0 = time.time()
    while True:
        time.sleep(10)
        # if reflektorVeri > control:
        t1 = time.time()
            # control = reflektorVeri
        return int(t1-t0)
        break
    
for reklektor in range(0,5):
    zaman = zamanlayici(reflektorVeri=reklektor)
    if reklektor == 0:
        konum = yol_liste[reklektor]
    else:
        konum = yol_liste[reklektor] - yol_liste[reklektor-1]
    hiz = konum/zaman
    print(f"Zaman: {str(zaman)}, Konum: {konum}, Hiz: {hiz}")