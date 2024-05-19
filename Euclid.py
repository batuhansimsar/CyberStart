import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 1), (3, 3), (7, 8)]
xlist = []
ylist = []

# xlist ve ylist'i oluşturma
for point in points:
    xlist.append(point[0])
    ylist.append(point[1])

# 2. Mesafelerin Hesaplanması
def distance(a, b, c, d):
    return math.sqrt((c - a) ** 2 + (d - b) ** 2)

# Her bir noktanın x ve y koordinatlarını kullanarak mesafeleri hesapla ve yazdır
for _, (x, y) in enumerate(zip(xlist, ylist)):
    for i, (xx, yy) in enumerate(zip(xlist, ylist)):
        if i != _:
            dist = distance(x, y, xx, yy)
            print(f"Nokta {_} ile Nokta {i} arasındaki mesafe: {dist}")


        
