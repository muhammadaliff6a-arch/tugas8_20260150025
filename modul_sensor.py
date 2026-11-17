

# Konstanta bertipe Tuple
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)  # (Suhu Max dalam C, Kelembaban Min dalam %)


def hitung_tren(data_slice):
    """
    Menerima list (hasil slicing) berisi tuple (suhu, kelembaban).
    Mengembalikan rata-rata suhu dan rata-rata kelembaban.
    """
    total_suhu = 0.0
    total_lembab = 0.0

    for suhu, lembab in data_slice:
        total_suhu += suhu
        total_lembab += lembab

    jumlah = len(data_slice)
    rata_suhu = total_suhu / jumlah
    rata_lembab = total_lembab / jumlah

    return rata_suhu, rata_lembab


def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """
    Mengevaluasi status pompa irigasi berdasarkan ambang kritis.
    tuple_kritis = (suhu_max, lembab_min)
    """
    suhu_max, lembab_min = tuple_kritis

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    return "NORMAL: Pompa Mati."