def cari_koin_palsu(koin):
  """
  Menemukan koin palsu dengan timbangan dua panci.

  Args:
    koin: Daftar N koin.

  Returns:
    Indeks koin palsu.
  """
  if len(koin) == 1:
    return 0

  tengah = len(koin) // 3
  a = koin[:tengah]
  b = koin[tengah:2*tengah]
  c = koin[2*tengah:]

  if timbang(a, b) == 0:
    return cari_koin_palsu(c) + tengah * 2
  elif timbang(a, b) == -1:
    return cari_koin_palsu(a)
  else:
    return cari_koin_palsu(b) + tengah

def timbang(a, b):
  """
  Menimbang dua kelompok koin.

  Args:
    a: Daftar koin.
    b: Daftar koin.

  Returns:
    -1 jika a lebih ringan, 0 jika a dan b memiliki berat sama, 1 jika a lebih berat.
  """
  # Simulasi timbangan dua panci
  # ...

# Contoh penggunaan
koin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
koin[4] = 0.9 # Koin ke-5 (indeks 4) dibuat lebih ringan

indeks_koin_palsu = cari_koin_palsu(koin)
print(f"Koin palsu ditemukan pada indeks {indeks_koin_palsu}")