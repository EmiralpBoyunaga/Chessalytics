#  Chessalytics

Yüksek ELO'lu oyunlardaki satranç açılışlarını analiz eden, terminal tabanlı bir veri bilimi projesi. Açılışların popülerliğini, kazanma oranlarını ve performans ratinglerini grafiklerle görselleştirir; ayrıca beyaz ve siyahın kazanma yüzdeleri arasındaki ilişkiyi doğrusal regresyonla modeller.

##  Veri Seti

Projede Kaggle'daki [Chess Opening Dataset](https://www.kaggle.com/datasets/arashnic/chess-opening-dataset) kullanılmıştır (`high_elo_opening.csv`).

- **1884 satır**, **24 sütun**
- Analizde kullanılan başlıca sütunlar:

| Sütun | Açıklama |
|---|---|
| `opening_name` | Açılış adı |
| `side` | Taraf (beyaz / siyah) |
| `num_games` | Oynanan oyun sayısı |
| `perf_rating` | Performans ratingi |
| `avg_player` | Ortalama oyuncu ratingi |
| `perc_player_win` | Oyuncunun kazanma yüzdesi |
| `perc_draw` | Beraberlik yüzdesi |
| `pec_opponent_win` | Rakibin kazanma yüzdesi |
| `perc_white_win` / `perc_black_win` | Beyazın / siyahın kazanma yüzdesi |
| `white_wins` / `black_wins` | Beyazın / siyahın kazanma sayısı |

Hamle bilgileri (`moves_list`, `move1w` … `move4b`), açılış kodu (`ECO`) ve `white_odds` sütunları analizde kullanılmadığı için veri temizleme aşamasında çıkarılır.

##  Özellikler

Program çalıştırıldığında bir menü açılır:

1. **En çok oynanan açılışlar** – Toplam oyun sayısına göre bar grafik
2. **En çok kazanan açılışlar** – Beyaz + siyah ortalama galibiyetlerine göre sıralama
3. **Beyaz veya siyahın en çok kazandığı açılışlar** – Tarafa özel bar grafik
4. **En düşük / en yüksek performans ratingli açılışlar**
5. **Bir açılışın sonuç dağılımı** – Seçilen açılış için kazanma / kaybetme / beraberlik pasta grafiği (tüm açılış listesi `output.txt` dosyasına yazılır)
6. **Regresyon analizi** – Siyahın kazanma yüzdesinden beyazın kazanma yüzdesini tahmin eden doğrusal regresyon modeli (%70 eğitim / %30 test), gerçek değerler ve tahminlerin dağılım grafiği
7. **Çıkış**

##  Kurulum

```bash
git clone https://github.com/<kullanici-adi>/Chessalytics.git
cd Chessalytics
pip install -r requirements.txt
```

Veri setini Kaggle'dan indirip `high_elo_opening.csv` dosyasını proje klasörüne koyun.

> **Not:** Kod içindeki dosya yolları (`C:\Users\...\high_elo_opening.csv` ve `D:\Workspace\...\output.txt`) kendi bilgisayarınıza göre güncellenmelidir.

##  Kullanım

```bash
python VeriBilimiProjesi.py
```

Menüden bir seçenek numarası girin ve istenirse gösterilecek açılış sayısını belirtin.

##  Kullanılan Teknolojiler

- **pandas** – Veri okuma ve işleme
- **matplotlib** & **seaborn** – Görselleştirme
- **scikit-learn** – Doğrusal regresyon ve train/test ayrımı
- **tabulate** – Terminalde tablo çıktısı

##  Proje Yapısı

```
Chessalytics/
├── VeriBilimiProjesi.py   # Ana program
├── high_elo_opening.csv   # Veri seti
├── output.txt             # Açılış listesi (5. seçenekte oluşturulur)
├── requirements.txt
└── README.md
```

##  Hazırlayanlar

- Ömer Faruk Ünal
- Emiralp Boyunaga
- Emre Kıyak
- Yiğit Bal
