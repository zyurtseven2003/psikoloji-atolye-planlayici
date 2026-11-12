# Psikoloji Atölyesi Katılımcı ve Etkinlik Planlayıcısı
# Bu program gerçek katılımcıların kişisel bilgilerini toplamaz.


def pozitif_sayi_al(soru):
    """Kullanıcıdan sıfırdan büyük bir tam sayı alır."""
    while True:
        cevap = input(soru).strip()
        try:
            sayi = int(cevap)
            if sayi > 0:
                return sayi
            else:
                print("Uyarı: Lütfen sıfırdan büyük bir sayı girin.")
        except ValueError:
            print("Uyarı: Lütfen geçerli bir tam sayı girin.")


def konu_al():
    """Boş olmayan bir atölye konusu alır."""
    while True:
        konu = input("Atölye konusu: ").strip()
        if konu:
            return konu
        else:
            print("Uyarı: Atölye konusu boş olamaz.")


def plan_olustur(konu, katilimci, kapasite, sure):
    """Katılımcıları kapasiteyi aşmadan gruplara dağıtır."""
    grup_sayisi = (katilimci + kapasite - 1) // kapasite
    gruplar = []
    kalan = katilimci
    for _ in range(grup_sayisi):
        kisi = min(kapasite, kalan)
        gruplar.append(kisi)
        kalan -= kisi
    if grup_sayisi == 1:
        durum = "Tek grup yeterli."
    else:
        durum = "Birden fazla grup gerekiyor."
    return {"konu": konu, "katilimci": katilimci,
            "kapasite": kapasite, "sure": sure,
            "gruplar": gruplar, "durum": durum}


def rapor_metni(planlar):
    """Atölye planlarını okunabilir metne dönüştürür."""
    satirlar = ["PSİKOLOJİ ATÖLYESİ PLANLAMA RAPORU", "=" * 38]
    for sira, plan in enumerate(planlar, 1):
        satirlar.extend([
            f"\nAtölye {sira}: {plan['konu']}",
            f"Katılımcı sayısı: {plan['katilimci']}",
            f"Grup kapasitesi: {plan['kapasite']}",
            f"Etkinlik süresi: {plan['sure']} dakika (grup başına)",
            f"Gerekli grup sayısı: {len(plan['gruplar'])}",
            f"Gruplardaki kişi sayıları: {', '.join(map(str, plan['gruplar']))}",
            f"Durum: {plan['durum']}",
        ])
    return "\n".join(satirlar) + "\n"


def dosyaya_kaydet(metin, dosya_adi="atolye_plani.txt"):
    """Raporu UTF-8 kodlamasıyla TXT dosyasına kaydeder."""
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write(metin)


def main():
    planlar = []  # Liste, oluşturulan bütün atölye planlarını saklar.
    print("=== Psikoloji Atölyesi Planlayıcısı ===")
    while True:  # Kullanıcı isterse yeni bir atölye ekleyebilir.
        konu = konu_al()
        katilimci = pozitif_sayi_al("Katılımcı sayısı: ")
        kapasite = pozitif_sayi_al("Bir grubun kapasitesi: ")
        sure = pozitif_sayi_al("Etkinlik süresi (dakika): ")
        planlar.append(plan_olustur(konu, katilimci, kapasite, sure))
        print("\n" + rapor_metni(planlar))
        while True:
            cevap = input("Başka bir atölye eklensin mi? (E/H): ").strip().lower()
            if cevap in ("e", "h"):
                break
            else:
                print("Uyarı: Lütfen E veya H girin.")
        if cevap == "h":
            break
    metin = rapor_metni(planlar)
    try:
        dosyaya_kaydet(metin)
        print("Rapor 'atolye_plani.txt' dosyasına kaydedildi.")
    except OSError as hata:
        print(f"Dosya kaydedilemedi: {hata}")


if __name__ == "__main__":
    main()
