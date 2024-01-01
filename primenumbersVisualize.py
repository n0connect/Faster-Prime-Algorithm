from matplotlib import pyplot as plt
import numpy as np

# np.linspace(başla,bitiş,kaçtane) -> istenilen aralıkta değerler üretir
x = np.linspace(-np.pi, np.pi, 50)  # Eksi pi den artı pi ye kadar 50 tane sayı üret

# x dizisini sinüs fonksiyonu ile görselleştirir. Etiket olarak Label
plt.plot(x, np.sin(x), label='Sinüs', color='black', linewidth='2')

# linestyle ile çizgi şekli belirlenebilir: -,--,-.-vb , alpha= 0.2 ile şeffaflık ayarlanır
# plt.plot.([4,3,7]) için , marker='o' , markersize=int

plt.plot(x, np.cos(x), label='Cosines', linestyle='--', color='purple', linewidth='1.5')

# dark_background, fast, Solarize_Light2, seaborn-talk, seaborn-ticks, seaborn-whitegrid, ggplot
plt.style.use('dark_background')

# plt.xlim(-100,2000) plt.ylim(-100,2000) belirlenen değerler için grafiği limitler
# Grafiği otomatik olarak sıkı gösterir
plt.axis('tight')

# X,Y eksenlerine ve projeye isim veriyoruz
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

"""
Olasılık dağılımları

np.random.seed(12345)
prob_ = np.random.normal(loc=0, scale=1, size=100000)
plt.hist(prob_, _P=True)
"""

plt.title('Study Project')
plt.legend()  # Labelleri etkinleştirmek için gerekli
plt.show()  # Programın ekranda kalmasını sağlar
