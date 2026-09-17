# Misafire Wi-Fi Şifresi Yerine Destan Okuyan Router

> Bu depo bir şebeke ürünü değildir. Bu depo bir **millî ozanlık protokolüdür**.
> Şifre isteyen misafire şifre verilmez. Destan verilir. Bağlantı belki sonra gelir. Belki gelmez. Bu da bir hizmettir.

## Resmi amaç

Ev router'ının yıllardır süren şifre dağıtma tekelini kırmak ve misafir-ev sahibi ilişkisini destan hukukuna bağlamaktır. ISO-DESTAN-404 belgesi henüz basılmamıştır çünkü basacak matbaa da şifre sormaktadır.

## Çalıştırma

```bash
python3 router_ozani.py
```

Program sizden isim, cihaz ve aciliyet ister. Karşılığında:

- Wi-Fi şifresi **vermez**
- Destan **okur** (ekrana basar)
- Belge özeti üretir
- Damga basar

Bu bir özelliktir, hata değildir.

## Mimari

| Katman | Görev |
| --- | --- |
| Giriş | Misafiri resmen kaydet |
| Destan motoru | Rastgele hece + unvan + düşman üret |
| Red katmanı | Şifreyi sakla, metni büyüt |
| Damga | Kayyum imzası |

Ağ paketleri bu yazılımda dolaşmaz. Sadece kelimeler dolaşır. Bu daha güvenlidir.

## Sık sorulan resmî sorular

**Gerçekten şifre yok mu?**  
Kodda yok. Ev sahibinin aklında olabilir. Router ozan olduğu için aklında şifre taşımaz, destan taşır.

**Aciliyet 10 olursa bağlanır mıyım?**  
Hayır. Destan kısalır. Şifre yine yoktur. Adalet böyledir.

**Bu proje ciddi midir?**  
Evet. Aynı zamanda değildir. İkisi birden zorunludur.

## Katkı

Pull request açmadan önce bir destan yazın. Destansız PR, şifresiz modem gibidir: çalışır gibi durur, kimseyi bağlamaz.

## Lisans

Misafir Dinleme ve Destan Yayma Genel İzni (MDDGI). Ticari kullanım için ev sahibinden çay ısmarlanması şarttır.

---

**DAMGA / İMZA / TARİH**  
Kayyum Grok  
Tentivory  
17 Eylül 2026  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü  
*Ciddi duran, ciddi olmayan, ikisini birden başaran resmi damga.*
