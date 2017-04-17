import sqlite3
import os
def DB_Olustur(): #İstenilen İsme Göre Veritabanını Oluşturur Yada Önceden Oluşturulmuş Veri Tabanına Bağlanır

    Db_Adi = input("Seçeneklere Ulaşmak İçin Önce; \nOluşturmak İstediğiniz Yada Önceden Oluşturduğunuz \n Veritabanına Bağlanmak İçin Adını Giriniz: \n") + '.db'  #Veritabanı adı girişi
    conn = sqlite3.connect(str(Db_Adi))  # ilk bağlantı veritabanı oluşturma yada önceden oluşturulmuş veritabanına bağlanan connect komutu
    cuser=conn.cursor() #bağlatı değişkeni oluşturduğumuz kod

    secenekler = "1-Veri Tabanını Sil\n 2-Tablo İşlemleri \n 3-Tablo Listele \n 4-Veri Gir-Güncelle-Sil \n 5-Exit"
    print(secenekler) #Seçenekleri Ekrana Yazdırır

    def tabo_listele(): #Tablo Adlarını Listelediğimiz ve Adlarına Göre İçeriklerini Listelediğimiz Fonksiyon
        komut = "SELECT name FROM sqlite_master WHERE type='table'" #Tablo adlarını çekmek için göndereceğimiz SQL komuru
        cuser.execute(komut) #Burada komutu çalıştırıyoruz
        print("Veri Tabanındaki Tablolar")
        for row in cuser: #Tabloları döndürür ve içerisindeki print komutu ile yazdırır
            print(row)
        cuser.close()
        Listelenecek_Tablo=input("Listelemek İstediğiniz Tablonun Adını Giriniz:\n")  #Listelemek istediğimiz tablonun adını buradan gireriz
        komut_query="Select * From"+" "+Listelenecek_Tablo #Listeleme Komutu
        cuser2=conn.cursor()
        cuser2.execute(komut_query) #bağlantımız ile komutu çalıştırırız
        for row in cuser2: #Tablonun her satırını döndürür ve yazdırır.
            print(row)
        cuser2.close() #bağlantıyı kapatırız
        DB_Olustur() #başa döndürür

    def tablo_islemleri(): #Tablo işlemlerinin gerçekleştirildiği Fonksiyon
        print("1-Tablo Oluştur \n 2-Tablo Adı Değiştir \n 3-Tabloya Alan Ekle \n 4-Tablo Sil \n 5-Ana Menüye Dön") #Seçenekleri Listeler
        Secim2 = input("Yukarıdaki Seçeneklerden Birini Seçiniz") #Seçimi Tutar

        if Secim2 == '1': #Tablo oluşturma sorgumuz
            Tablo_adi = input("Oluşturmak İstediğiniz Tablo Adını Giriniz \n") #Yeni Tablo adını girdiğimiz değişken
            Alan_Adi = input("Önce Alan Adı Daha Sonra Veri Tipini Giriniz Gireceğiniz Her Alanı Virgül İle Ayırınız \n Örnek:AlanAdi Text, AlanAdi2 int \n") #Alan adlarını ve veri tiplerini girdiğimiz alan
            tb_adi = 'Create table IF NOT EXISTS' + ' ' + Tablo_adi + ' ' + '(' + Alan_Adi + ')'  #Tablo oluşturan SQL sorguusu
            conn.execute(str(tb_adi)) #Sorguyu çalıştırdığımız kod
            conn.commit() #veritabanı üzerinden işlem yapmamızı sağlayan kod
            conn.close() #bağlantıyı kapatır
            tablo_islemleri()#Başa dönmemizi sağlar

        if Secim2=='2': #Tablo adını değiştirme işlemini seçme sorgumuz
            Tablo_eskiAd = input("Adını Değiştirmek İstediğiniz Tablo Adını Giriniz \n") #Adını değiştirmek istediğimiz tablonun adını tutan değişken
            Tablo_yeniAd=input("Yeni Tablo Adını Giriniz\n") #Yeni adı tutan değişken
            Tablo_guncelle = 'Alter table' + ' ' + Tablo_eskiAd + ' '+'Rename TO'+' '+Tablo_yeniAd #tablo adını değiştiren SQL sorgusu
            conn.execute(str(Tablo_guncelle)) #Sorguyu çalıştırdığımız kod
            conn.commit() #DB üzerinden işlem yapmamızı sağlayan kod
            conn.close() #Bağlantı Kapatma
            tablo_islemleri()#Başa dönmemizi sağlar

        if Secim2=='3': #Alan ekleme işlemini başlatan sorgu
            Tablo_adi3 = input("Alan Eklemek İstediğiniz Tablo Adını Giriniz \n") #Eklemen istediğimiz alanın adını tutan değişken
            Alan_Adi2 = input(
                    "Oluşturmak İstediğiniz Alan Adını ve Veri Tipini Giriniz \n Örnek:AlanAdi Text, AlanAdi2 int \n") #Alan adını ve Veri tipini tutan değişken
            Alan_Ekle = 'Alter table' + ' ' + Tablo_adi3 + ' ' + 'ADD Column' +' '+ Alan_Adi2 #Alan adı eklemek için gerekli sorguyu tutan değişken
            conn.execute(str(Alan_Ekle)) #Sorguyu çalıştıran kod
            conn.commit() #DB üzerinden işlem yapmamızı sağlayan kod
            conn.close() #Bağlantıyı kapatır
            tablo_islemleri()#Başa dönmemizi sağlar

        if Secim2=='4':#Silme işlemini başlatmak için gerekli sorgu
            Silinecek_Tablo = input("Silmek İstediğiniz Tablo Adını Giriniz \n")#Silinecek Tablo adını tutar
            Tablo_Sil = 'Drop table'+ ' ' + Silinecek_Tablo#Silmek için gerekli SQL sorgusunu tutan değişken
            conn.execute(str(Tablo_Sil)) #Sorguyu çalıştıran kod
            conn.commit()#DB üzerinde işlem yapmamızı sağlayan kod
            conn.close()#Bağlantıyı kapatır
            tablo_islemleri()#Başa dönmemizi sağlar

        if Secim2=='5':#Ana Menüye Dönmemizi sağlayan sorgu
            DB_Olustur()#Ana Menüye Döner

        tablo_islemleri()


    def veri_islemleri(): #Veri Girişi, Güncelleme ve Silme işlemlerini Gerçekleştirdiğimiz Fonksiyon
        veri_secenekler=input(" 1-Veri Girişi\n 2-Veri Güncelle\n 3-Veri Sil \n 4-Ana Menüye Dön\n İşlem Yapmak İstediğiniz Seçeneği Seçiniz.\n") #Seçenekleri Listeleyen ve Seçeneği Tutan Değişken

        if veri_secenekler=='1':#Veri Girişini Seçeneğini Başlatmak için gerekli sorgu
            Veri_Girilecek_Tablo = input("Ekleme yapmak istediğiniz Tabloyu Seçiniz") #Veri Girilecek Tablo adını tutar
            print(Veri_Girilecek_Tablo+" İsimli Tablo İçerisindeki Alanlar ve Veri Tipleri") #Veri Girilecek tabloyu gösterir
            query_list="PRAGMA table_info('"+Veri_Girilecek_Tablo+"')" #Veri girilecek tablonun alanlarını ve değişken tipilerini listeler
            cuser.execute(query_list)#Komutu çalıştırır
            for row in cuser:#Tablo alanlarını ve veri tiplerini listeler
                print(row)

            Veri_Girilecek_Alan=input("Veri Girilecek Alanları Virgülle Ayırarak Giriniz")#Veri Girişi yapılacak alanları tutar
            Veri_icerik=input("Girmek İstediğiniz Verileri Metinsel İfadeler İçin ' ' İçerisinde Sayısal İfadeler İçin Direk Giriş Yaparak Virgüller ile Ayırılmış Şekilde Giriniz:\n") #Veri içeriklerini tutar
            query_insert = ("INSERT INTO" + " " + Veri_Girilecek_Tablo+"("+Veri_Girilecek_Alan+") "+"Values("+Veri_icerik+")")#Veri girişini gerçekleştiren Sql komutu
            conn.execute(query_insert)#Komutu çalıştırır
            conn.commit()#Veritabanı üzerinden değişiklik yapmamızı sağlar
            conn.close()#Bağlantıyı kapatır

        if veri_secenekler=='2':#Güncelleme Seçeneğini Başlatmak için gerekli sorgu
            Veri_Guncellenecek_Tablo = input("Güncelleme yapmak istediğiniz Tabloyu Seçiniz\n")#Güncelleme yapılacak tablonun adını tutan değişken
            print(Veri_Guncellenecek_Tablo + " İsimli Tablo İçerisindeki Alanlar ve Veri Tipleri")#Güncelleme yapılacak tabloyu gösterir
            query_list = "PRAGMA table_info('" + Veri_Guncellenecek_Tablo + "')"#Alanlarını ve veri tiplerini listeleyecek sql komutu
            cuser.execute(query_list)#komutu çalıştırır
            for row in cuser:#Alanları ve veri tiplerini listeler
                print(row)
            Veri_Guncellenecek_Alan=input("Her Güncelleme İşlemi Sadece Bir Alan İçin Çalışır\n Güncelleme Yapmak İstediğiniz Alanı Giriniz:\n") #Veri güncellenecek Alanı tutar
            Veri_Guncellenecek_Yeni_Deger=input("Güncellemek İstediğiniz Alanın Yeni Değerini Giriniz: Sayısal için Örnek(15) Metinsel için Örnek('Metin')\n")#Yeni Değeri Tutar
            Veri_Sorgu=input("Hedef Veri İçin Sorgu Alanı Ardından Sorgu Operatörünüzü ve Şartınızı Giriniz: Örnek(Ad='Oğuzhan')\n")#Hedef veri veya verilerin sorgusu
            query_guncelle="Update"+" "+Veri_Guncellenecek_Tablo+" "+"SET" +" "+Veri_Guncellenecek_Alan+"="+Veri_Guncellenecek_Yeni_Deger+" "+"where"+" "+Veri_Sorgu #İşlemi gerçekleştirecek SQL komut
            conn.execute(query_guncelle)#komutu çalıştırır
            conn.commit()#DB üzerinde değişiklik yapmamızı sağlar
            conn.close()# Bağlantıyı Kapatır

        if veri_secenekler=='3':#Silme Seçeneğini Başlatmak İçin Gerekli Sorgu
            Veri_Silinecek_Tablo = input("Veri Silmek istediğiniz Tabloyu Seçiniz")#Veri Silinecek Tabloyu tutar
            print(Veri_Silinecek_Tablo + " İsimli Tablo İçerisindeki Alanlar ve Veri Tipleri")#Veri Silinecek tabloyu gösterir
            query_list = "PRAGMA table_info('" + Veri_Silinecek_Tablo + "')"#Alanlarını ve veri tiplerini gösterir
            cuser.execute(query_list)#komutu çalıştırır
            for row in cuser:#Listelemeyi yapar
                print(row)
            Veri_Sil_Sorgu = input(
                "Hedef Veri İçin Sorgu Alanı Ardından Sorgu Operatörünüzü ve Şartınızı Giriniz: Örnek(Ad='Oğuzhan')\n")#Silinecek hedef veri için gerekli sorguyu tutar
            query_sil = "Delete From" + " " + Veri_Silinecek_Tablo +" "+ "where" + " " + Veri_Sil_Sorgu#Silme işlemini gerçekleştiren komut
            conn.execute(query_sil)#komutu çalıştırır
            conn.commit()#Veritabanında değişiklik yapmamızı sağlar
            conn.close()#bağlantıyı kapatır

        if veri_secenekler=='4':#Başa dönmemizi sağlayacak seçenek
            DB_Olustur()#başa dönmemizi sağlayan fonksiyon


    Secim = input("Yukarıdaki Seçeneklerden Birini Seçiniz:\n")#İlk Menü için seçeneğimizi tutar
    if Secim == '1':#Veri Tabanı silme seçeneğini başlatacak sorgu
        conn.close()#bağlantıyı kapatır
        silinecek=input("Silinecek Veritabanı")+".db"#Veritabanı adını tutar
        os.remove(silinecek)#Veritabanı dosyasını siler

    if Secim=='2':#Tablo işlemleri seçeneğini çalıştıracak sorgu
        tablo_islemleri()

    if Secim=='3':#Tablo listeleme işlemleriini çalıştıracak sorgu
        tabo_listele()

    if Secim=='4':#Veri işlemleri seçeneğini çalıştıracak sorgu
        veri_islemleri()
    if Secim=='5':#Çıkış seçeneğinin sorgusu
        StopIteration()#programı durdurur

DB_Olustur()