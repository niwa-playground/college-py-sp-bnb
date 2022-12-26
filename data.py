denah = {
    "pintu": {
        "kebutuhan_rumah_tangga": 9,
        "alat_mandi": 10,
        "makanan": 12,
        "makanan_beku": 3,
        "minuman": 20
    },
    "kasir": {
        "kebutuhan_rumah_tangga": 7,
        "alat_mandi": 8,
        "makanan": 9,
        "makanan_beku": 5,
        "minuman": 18
    },
    "kebutuhan_rumah_tangga": {
        "pintu": 9,
        "kasir": 7,
        "alat_mandi": 3,
        "makanan": 10,
        "makanan_beku": 15,
        "minuman": 6
    },
    "alat_mandi": {
        "pintu": 10,
        "kasir": 8,
        "kebutuhan_rumah_tangga": 3,
        "makanan": 3,
        "makanan_beku": 12,
        "minuman": 3
    },
    "makanan": {
        "pintu": 12,
        "kasir": 9,
        "kebutuhan_rumah_tangga": 10,
        "alat_mandi": 3,
        "makanan_beku": 9,
        "minuman": 3
    },
    "makanan_beku": {
        "pintu": 3,
        "kasir": 5,
        "kebutuhan_rumah_tangga": 15,
        "makanan": 9,
        "alat_mandi": 12,
        "minuman": 18
    },
    "minuman": {
        "pintu": 20,
        "kasir": 18,
        "kebutuhan_rumah_tangga": 6,
        "makanan": 3,
        "makanan_beku": 18,
        "alat_mandi": 3
    },
}

kebutuhan_rt = ["Deterjen", "Cairan pengharum pakaian",
                "Cairan pembersih lantai"]
alat_mandi = ["Sabun", "Shampo", "Pasta Gigi", "Sikat gigi"]
makanan = ["Snack", "mie instan", "dairy product", "roti", "buah-buahan"]
makanan_beku = ["ice cream", "nugget", "sosis"]
minuman = ["Minuman berenergi", "Kopi"]
all_etalase = {"kebutuhan_rumah_tangga": [x.lower() for x in kebutuhan_rt],
               "alat_mandi": [x.lower() for x in alat_mandi],
               "makanan": [x.lower() for x in makanan],
               "makanan_beku": [x.lower() for x in makanan_beku],
               "minuman": [x.lower() for x in minuman]
               }
