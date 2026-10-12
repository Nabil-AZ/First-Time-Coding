import math

def hitung_jarak_haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    jarak = R * c
    return jarak

#kota jakarta
lintang1 = -6.2088
bujur1 = 106.8456

#Kota padang
lintang2 = -0.9471
bujur2 = 100.4172

hasil_jarak = hitung_jarak_haversine(lintang1, bujur1, lintang2, bujur2)
print(f"Jarak antara Jakarta dan Padang adalah: {hasil_jarak:.2f} km")
