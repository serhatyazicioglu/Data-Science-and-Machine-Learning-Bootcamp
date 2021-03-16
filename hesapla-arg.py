# -*- coding: UTF-8 -*-

"""
Yazdığımız her uygulama grafik arayüzüne sahip olmaz.
Bazı uygulamalar komut satırına daha uygundur ve bu uygulamalar bazı parametrelere ihtiyaç duyar.

Argparse: Terminal üzerinden yazdığımız kodlara input'lar vermemizi sağlar.

Aşağıdaki argparse fonksiyonunu terminal üzerinden çalıştırmak için örnek kullanım şu şekildedir:

python <fonk.ismi.py> --sayi1 <1.değer> --sayi2 <2.değer> --islem <işlem türü>
python hesapla-arg.py --sayi1 5 --sayi2 10 --islem carp
"""

import argparse  # kütüphane yüklenmesi. (mevcut değilse pip install argparse)

# get args
ap = argparse.ArgumentParser()  # argparse nesnesini yapılandırma
ap.add_argument("--sayi1", required=True, help="sayi1 giriniz! (--sayi1)")  # required: bu argümanın gerekli olduğunu belirtir.
ap.add_argument("--sayi2", required=True, help="sayi2 giriniz! (--sayi2)")  # help: kullanıcıya bilgilendirme yapar.
ap.add_argument("--islem", required=True, help="İslem turu giriniz! (--islem=topla|cikar|carp|bol)")  # kullanıcıdan yapacağı işlem bilgisini alıyoruz.
# terminal üzerinden örnek kullanım: python hesapla-arg.py --sayi1 5 --sayi2 10 --islem carp
args = vars(ap.parse_args()) # alınan tüm inputları args içerisinde topladık. sayi1 inputunu çağırmak için args["sayi1"] kullanılır.

try:
    # set args to vars
    sayi1 = float(args["sayi1"])  # sayi1 olarak girilen değeri float tipine dönüştürür ve sayi1 olarak kaydeder.
    sayi2 = int(args["sayi2"])  # sayi2 olarak girilen değeri integer tipine dönüştürür ve sayi2 olarak kaydeder.
    islem = args["islem"]  # kullanıcıdan alınan islem inputunu islem olarak kaydettik.

    print(islem + " isleminin sonucu:")  # asagidaki islemlere göre yapilan islemi ve islem sonucunu baskilar.

    if islem == "topla":  # kullanıcıdan alınan input değeri topla ise ekrana toplamı baskılar.
        print(sayi1 + sayi2)
    elif islem == "cikar":  # kullanıcıdan alınan input değeri cikar ise ekrana farkı baskılar.
        print(sayi1 - sayi2)
    elif islem == "carp":  # kullanıcıdan alınan input değeri çarpma ise ekrana çarpımı baskılar.
        print(sayi1 * sayi2)
    elif islem == "bol":  # kullanıcıdan alınan input değeri bölme ise ekrana bölümü baskılar.
        print(sayi1 / sayi2)
    else:
        print("Tanımlanmamıs islem turu girdiniz!")  # kullanıcı farklı bir değer girerse hata mesajı çıkarır.

except Exception as e:
    print("Hata var! ==> " + str(e))
