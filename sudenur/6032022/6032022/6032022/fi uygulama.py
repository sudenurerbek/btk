"""
kullanıcı yılsonu ortlaması girsin.Ortalama 85 üstü ise takdir,
70 üstü teşekkür,bunların dışında ise hiçbir belge alamadınız
"""
ortalamanız=int(input("Yılsonu ortalamanız:"))
if ortalama>=85:
    print("Taktir belgesi aldınız")
elif ortalama>=70:
    print("Teşekkür belgesi aldınız")
else:
    print("Hiçbir belge alamadınız")




