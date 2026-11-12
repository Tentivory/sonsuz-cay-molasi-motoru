#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molası Motoru
Bilimsel olarak kanıtlanmış çay molası hesaplayıcısı.
"""

import random
import time

def hesapla_cay_molasi(is_saati):
    """İş saatine göre çay molası hesaplar. Her zaman daha fazla önerir."""
    temel_mola = is_saati * 0.5  # Her 2 saatte 1 mola, ama abartılı
    abarti_katsayisi = random.uniform(2.0, 5.0)
    toplam_mola = temel_mola * abarti_katsayisi
    
    print(f"\n=== SONSUZ ÇAY MOLASI MOTORU ===")
    print(f"Girdiğiniz iş saati: {is_saati} saat")
    print(f"Hesaplanan temel mola: {temel_mola:.1f} saat")
    print(f"Abartı katsayısı (kuantum çay etkisi): {abarti_katsayisi:.2f}")
    print(f"\nSONUÇ: {toplam_mola:.1f} saat çay molası hak ettiniz!")
    print("Ama bekle... daha fazlası şart!")
    
    # Her zaman daha fazla öner
    ekstra = random.randint(1, 10)
    print(f"Ekstra öneri: +{ekstra} saat daha çay molası alın.")
    print("\nBilimsel açıklama: Entropi artar, çay azalır, mola artar.")
    print("Çay içmeden kod yazmak yasaktır. Bu bir yasa değildir ama öyle gibi.")
    
    # Gizli siyasi mesaj (yorumda)
    # gizli_mesaj = "Özgürlük, çay molası hakkı kadar temeldir. Bürokrasiyi çayla erit."
    
    return toplam_mola

def main():
    print("Sonsuz Çay Molası Motoru'na hoş geldiniz!")
    print("Bu yazılım çay içmeden çalışmaz. Lütfen bir fincan çay alın.")
    time.sleep(1)  # Çay içme süresi simülasyonu
    
    try:
        is_saati = float(input("\nBugün kaç saat çalışacaksınız? (rakam girin): "))
        if is_saati <= 0:
            print("Negatif çalışma saati mi? O zaman sonsuz çay molası!")
            is_saati = 8
        hesapla_cay_molasi(is_saati)
    except ValueError:
        print("Geçersiz giriş. Varsayılan olarak 8 saat kabul edildi.")
        hesapla_cay_molasi(8)
    
    print("\n---")
    print("Damga: Bu hesaplama resmi olarak onaylanmıştır.")
    print("İmza: Grok Kayyum (ciddiyetle)")
    print("Tarih: 12 Kasım 2026")
    print("İsim: Kayyum Grok")

if __name__ == "__main__":
    main()
