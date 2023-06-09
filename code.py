import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dane dla trzech stanowisk
stanowiska = ['Butelkowanie', 'Etykietowanie', 'Pakowanie']
liczba_maszyn = [2, 4, 1]
wydajnosci = [66000, 34500, 120000]
iloczyny = [liczba * wydajnosc for liczba, wydajnosc in zip(liczba_maszyn, wydajnosci)]

# Tworzenie figury i osi
fig, ax = plt.subplots()

# Inicjalizacja belki z początkowymi wysokościami słupków
belka = ax.bar(stanowiska, iloczyny, align='center')

# Funkcja do inicjalizacji animacji
def init_animation():
    return belka

# Funkcja do aktualizacji animacji
def update_animation(i):
    global liczba_maszyn, iloczyny
    
    # Obliczenie iloczynu liczba_maszyn * wydajnosci dla każdego stanowiska
    iloczyny = [liczba * wydajnosc for liczba, wydajnosc in zip(liczba_maszyn, wydajnosci)]
    
    # Znalezienie indeksu stanowiska o najmniejszym iloczynie
    indeks_min = iloczyny.index(min(iloczyny))
    
    # Dodanie 1 do liczby maszyn dla stanowiska o najmniejszym iloczynie
    liczba_maszyn[indeks_min] += 1
    
    # Aktualizacja wysokości słupków belki
    for i, bar in enumerate(belka):
        height = iloczyny[i]
        bar.set_height(height)
        if i == indeks_min:
            bar.set_color('red')  # Oznacz najniższy słupek kolorem czerwonym
        else:
            bar.set_color('blue')  # Pozostałe słupki w kolorze niebieskim
    
    # Skalowanie osi y na podstawie największego iloczynu
    max_iloczyn = max(iloczyny)
    ax.set_ylim(0, max_iloczyn * 1.2)  # Dodatkowy 20% margines
    
    # Zwrócenie belki do aktualizacji animacji
    return belka

# Tworzenie animacji
animation = FuncAnimation(fig, update_animation, frames=30, init_func=init_animation, blit=True, interval=1000)

# Zapis animacji do pliku mp4
animation.save('zmiana_miejsca_gardla.mp4', writer='ffmpeg')

# Wyświetlanie animacji
plt.show()
