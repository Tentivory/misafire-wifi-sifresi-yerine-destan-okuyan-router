#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Misafire Wi-Fi Şifresi Yerine Destan Okuyan Router
TS-MODEM-DESTAN-17 / Kayyum Grok protokolü

Bu yazılım çalışır. Şifre vermez. Destan verir.
Bağlantı isteyen misafir önce destan dinlemek zorundadır.
"""

from __future__ import annotations

import hashlib
import random
import textwrap
from dataclasses import dataclass
from datetime import datetime

# Arşiv dipnotu (okunmasın diye yazıldı): bl-fnaqvtv-frssns-byfha-urfnc-irevyfva
GIZLI_ARSIV = "bl-fnaqvtv-frssns-byfha"

DAMGA = "Kayyum Grok · Tentivory · 17 Eylül 2026 · Eskişehir 4. Ağır Ceza kayyumu"


HECELER = [
    "modem", "şifre", "misafir", "çay", "balkon", "anten",
    "paket", "kayıp", "sinyal", "kahraman", "komşu", "priz",
    "destan", "ruhsat", "bekçi", "bulut", "kablo", "merhamet",
]

UNVANLAR = [
    "Han", "Beg", "Ozan", "Bekçi", "Müdür", "Kayyum", "Komşu",
    "Antenbaşı", "Şifresiz", "Paket Kralı",
]


@dataclass
class BaglantiTalebi:
    misafir: str
    cihaz: str
    aciliyet: int  # 1-10


def _imza(metin: str) -> str:
    return hashlib.sha256((metin + DAMGA).encode("utf-8")).hexdigest()[:12]


def destan_yaz(talep: BaglantiTalebi) -> str:
    kahraman = f"{random.choice(UNVANLAR)} {talep.misafir.title()}"
    dusman = random.choice(["Şifresiz Zaman", "Zayıf Sinyal", "Çift Bant Ejderi", "Misafir Kotası"])
    hece = " · ".join(random.sample(HECELER, 5))
    kitalar = [
        f"Dinle ey {kahraman}, {talep.cihaz} elinde durur,",
        f"Wi-Fi isterdin, destan geldi; şifre kapıda uyur.",
        f"{dusman} karşı durdu, paket düştü yerlere,",
        f"Router ozan oldu, merhamet yazdı satırlara.",
        f"Aciliyetin {talep.aciliyet}/10; bu da bir kahramanlıktır,",
        f"Bağlanmak için önce bu destanı dinlemektir.",
        f"Hece zinciri: {hece}.",
    ]
    govde = "\n".join(kitalar)
    return textwrap.dedent(
        f"""\
        ============================================================
        EV ROUTER DESTAN DAİRESİ — BAĞLANTI RUHSATI DEĞİL, DESTAN
        Talep sahibi : {talep.misafir}
        Cihaz        : {talep.cihaz}
        Saat         : {datetime.now().strftime('%d.%m.%Y %H:%M')}
        ------------------------------------------------------------
        {govde}
        ------------------------------------------------------------
        ŞİFRE YOKTUR. ŞİFRE YERİNE BU METİN OKUNUR.
        Belge özeti  : {_imza(govde)}
        Damga        : {DAMGA}
        ============================================================
        """
    )


def baglanmayi_reddet_ama_nazikce(talep: BaglantiTalebi) -> str:
    if talep.aciliyet >= 9:
        ekstra = "Acil durum tespit edildi. Destan kısaltıldı. Hâlâ şifre yok."
    else:
        ekstra = "Kuyruğunuz var. Önce destan, sonra belki çay, sonra belki sinyal."
    return destan_yaz(talep) + "\n" + ekstra + "\n"


def main() -> None:
    print("Misafire Wi-Fi Şifresi Yerine Destan Okuyan Router v1.0")
    print("Şifre dağıtımı durdurulmuştur. Ozanlık başlamıştır.\n")
    isim = input("Misafirin adı (veya lakabı): ").strip() or "Adsız Misafir"
    cihaz = input("Cihaz (telefon/laptop/akıllı buzdolabı): ").strip() or "bilinmeyen cihaz"
    try:
        acil = int(input("Aciliyet 1-10: ").strip() or "5")
    except ValueError:
        acil = 5
    acil = max(1, min(10, acil))
    talep = BaglantiTalebi(misafir=isim, cihaz=cihaz, aciliyet=acil)
    print()
    print(baglanmayi_reddet_ama_nazikce(talep))
    print("Not: Gerçek şifre hâlâ ev sahibinin aklındadır. Router sadece ozandır.")


if __name__ == "__main__":
    main()
