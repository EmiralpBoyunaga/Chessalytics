# Hazırlayanlar: Ömer Faruk Ünal, Emiralp Boyunaga, Emre Kıyak, Yiğit Bal
# https://www.kaggle.com/datasets/arashnic/chess-opening-dataset?resource=download - Kaggle'dan alinan veri seti

import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tabulate import tabulate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# VERI SETI HAKKINDA LABEL BILGILERI
# ------------------------------
# opening_name -> acilis adi
# side -> beyaz veya siyah
# num_games -> oynanan oyun sayisi
# last_played_date -> son oynanma tarihi
# perf_rating -> performans ratingi
# avg_player -> ortalama oyuncu ratingi
# perc_player_win -> oyuncu kazanma sansi
# perc_player_draw -> oyuncu beraberlik sansi
# perc_opponent_win -> rakip kazanma sansi

# HAMLE BILGILERI VE ACILIS KODU YERINE ACILIS ADINI KULLANDIGIMIZ ICIN ALTTAKI BILGILERI CIKARTIYORUZ
# ------------------------------ 
# ECO -> acilis kodu
# moves_list -> hamle listesi
# move1w -> beyazin 1. hamlesi
# move1b -> siyahin 1. hamlesi
# move2w -> beyazin 2. hamlesi
# move2b -> siyahin 2. hamlesi
# move3w -> beyazin 3. hamlesi
# move3b -> siyahin 3. hamlesi
# move4w -> beyazin 4. hamlesi
# move4b -> siyahin 4. hamlesi
# ------------------------------

# perc_wihite_win -> beyazin kazanma sansi
# perc_black_win -> siyahin kazanma sansi
# white_odds -> beyazin kazanma orani -----SADECE BU SUTUNDAKI ORANLARI KULLANMADIGIMIZ ICIN CIKARTIYORUZ-----
# white_wins -> beyazin kazanma sayisi
# black_wins -> siyahin kazanma sayisi
# ------------------------------

# CSV dosyasını okuma
DataFrame_CSV = pd.read_csv(r'C:\Users\Emiralp\Desktop\Chessalytics\high_elo_opening.csv') 

# Gereksiz sütunları silme
drop_columns = ['moves_list', 'move1w', 'move1b', 'move2w', 'move2b', 'move3w', 'move3b', 'move4w', 'move4b', 'ECO', 'white_odds']
DataFrame_CSV_Clean = DataFrame_CSV.drop(drop_columns, axis='columns') 

# Machine learning Regression Line 
MachineLearning_DataFrame = DataFrame_CSV[['perc_white_win' , 'perc_black_win']]
x = MachineLearning_DataFrame['perc_black_win']
y = MachineLearning_DataFrame['perc_white_win']
type(x)
type(y)
Percentage_Mean_White = MachineLearning_DataFrame['perc_white_win'].mean()
Percentage_Mean_Black = MachineLearning_DataFrame['perc_black_win'].mean()

# DataFrame'in index sayısını al
index_count = len(DataFrame_CSV_Clean)

# Platforma göre ekranı temizle
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # MacOS/Linux
    os.system('clear')

print("Veri seti üzerinde yapilacak islemi seçiniz: \n")
print("1 - En cok oynanan acilislar")
print("2 - En cok kazanan acilislar")
print("3 - Beyaz veya siyahin en cok kazandigi acilislar")
print("4 - En dusuk veya yüksek elo puanli kazanan acilislar")
print("5 - Bir acilisin tarafa göre kazanma, kaybetme ve beraberlik yüzdeleri")
print("6 - Beyaz ve Siyah'in regression line ile win rateleri")
print("7 - Programdan cikis yap")

guard = 0
while guard == 0:
    input_secim = int(input("Seciminizi yapiniz: "))

    if input_secim == 1:
        input_head = int(input("Kac adet acilis gormek istersiniz: "))

        acilis_oyun_sayilari = DataFrame_CSV_Clean.groupby('opening_name')['num_games'].sum().sort_values(ascending=False)

        en_populer_acilislar = acilis_oyun_sayilari.head(input_head)

        plt.grid(axis='y')
        plt.figure(figsize=(12, 8))
        en_populer_acilislar.plot(kind='bar', color='skyblue')
        plt.xlabel('Acilis adi')
        plt.ylabel('Oynanan oyun sayisi')
        plt.title('En popüler acilişlarin oynandigi oyun sayisi')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        exit()

    elif input_secim == 2:
        input_head = int(input("Kac adet acilis gormek istersiniz: "))

        acilis_kazanma_sayilari_beyaz = DataFrame_CSV_Clean.groupby('opening_name')['white_wins'].mean().sort_values(ascending=False)
        acilis_kazanma_sayilari_siyah = DataFrame_CSV_Clean.groupby('opening_name')['black_wins'].mean().sort_values(ascending=False)

        en_cok_kazanan_acilislar = acilis_kazanma_sayilari_beyaz + acilis_kazanma_sayilari_siyah
        en_cok_kazanan_acilislar = en_cok_kazanan_acilislar.sort_values(ascending=False).head(input_head)

        plt.figure(figsize=(12, 8))
        en_cok_kazanan_acilislar.plot(kind='bar', color='green')
        plt.grid(axis='y')
        plt.xlabel('Acilis adi')
        plt.ylabel('Kazanilan oyun sayisi')
        plt.title('En cok kazanan açilislar')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        exit()

    elif input_secim == 3:
        input_secim_3 = int(input("Beyaz icin 1, Siyah icin 2 giriniz: "))

        if input_secim_3 == 1:
            input_head = int(input("Kac adet acilis gormek istersiniz: "))

            acilis_kazanma_sayilari_beyaz = DataFrame_CSV_Clean.groupby('opening_name')['white_wins'].mean().sort_values(ascending=False)

            en_cok_kazanan_acilislar_beyaz = acilis_kazanma_sayilari_beyaz.head(input_head)

            hist = en_cok_kazanan_acilislar_beyaz.plot(kind='bar', color='blue')
            plt.grid(axis='y')
            plt.xlabel('Acilis adi')
            plt.ylabel('Kazanilan oyun sayisi')
            plt.title('Beyaz icin en çok kazanan acilislar')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            exit()

        elif input_secim_3 == 2:
            input_head = int(input("Kac adet acilis gormek istersiniz: "))

            acilis_kazanma_sayilari_siyah = DataFrame_CSV_Clean.groupby('opening_name')['black_wins'].mean().sort_values(ascending=False)

            en_cok_kazanan_acilislar_siyah = acilis_kazanma_sayilari_siyah.head(input_head)

            hist = en_cok_kazanan_acilislar_siyah.plot(kind='bar', color='black')
            plt.grid(axis='y')
            plt.xlabel('Acilis adi')
            plt.ylabel('Kazanilan oyun sayisi')
            plt.title('Siyah icin en çok kazanan acilislar')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            exit()

        else:
            print("Hatali secim yaptiniz. Lutfen tekrar deneyiniz.")        

    elif input_secim == 4:
        input_secim_4 = int(input("En dusuk eloda oynanan acilislar icin 1, En yuksek icin ise 2 giriniz: "))

        if input_secim_4 == 1:
            input_head = int(input("Kac adet acilis gormek istersiniz: "))
            acilis_kazanma_sayilari = DataFrame_CSV_Clean.groupby('opening_name')['perf_rating'].mean().sort_values(ascending=True).head(input_head)

            hist = acilis_kazanma_sayilari.plot(kind='bar', color='peru')
            plt.grid(axis='y')
            plt.xlabel('Acilis adi')
            plt.ylabel('Performans ratingi')
            plt.title('En dusuk performans ratingli oynanan acilislar')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            exit()

        elif input_secim_4 == 2:
            input_head = int(input("Kac adet acilis gormek istersiniz: "))
            acilis_kazanma_sayilari = DataFrame_CSV_Clean.groupby('opening_name')['perf_rating'].mean().sort_values(ascending=False).head(input_head)

            hist = acilis_kazanma_sayilari.plot(kind='bar', color='gold')
            plt.grid(axis='y')
            plt.xlabel('Acilis adi')
            plt.ylabel('Performans ratingi')
            plt.title('En yuksek performans ratingli oynanan acilislar')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            exit()

        else:
            print("Hatali secim yaptiniz. Lutfen tekrar deneyiniz.")

    elif input_secim == 5:
        # Burada data'nın daha güzel yazılması için tabulate kullanmaya karar verdim.
        unique_openings = DataFrame_CSV_Clean['opening_name'].unique()

        # Tablo formatı için veriyi hazırla
        table_data = [[idx, acilis] for idx, acilis in enumerate(unique_openings)]
        table_data_preview = [[idx, acilis] for idx, acilis in enumerate(unique_openings[:10])]

        # Tabulate ile tablo oluştur ve yazdır
        print(tabulate(table_data_preview, headers=["Index", "Opening Name"], tablefmt="grid"))
        with open("D:\Workspace\PythonProjects\Chessalytics\output.txt", "w", encoding="utf-8") as f:
            f.write(tabulate(table_data, headers='keys', tablefmt='grid'))
            print("                   .                   ")
            print("                   .                   ")
            print("                   .                   ")
            print("(Acilislerin geri kalani için lutfen output.txt dosyasina bakin)")
            print("")

        # Kodun yanlış girdide devamlılığı için while döngüsü.
        guard = 0
        while guard == 0:
            int_acilis = int(input("Sectiginiz acilisin numarasini giriniz: "))
            if int_acilis >= 0 and int_acilis < index_count:
                acilis = DataFrame_CSV_Clean['opening_name'].unique()[int_acilis]
                taraf = DataFrame_CSV_Clean['side'][int_acilis]

                plt.pie([DataFrame_CSV_Clean[DataFrame_CSV_Clean['opening_name'] == acilis]['perc_player_win'].mean(),
                    DataFrame_CSV_Clean[DataFrame_CSV_Clean['opening_name'] == acilis]['pec_opponent_win'].mean(),
                    DataFrame_CSV_Clean[DataFrame_CSV_Clean['opening_name'] == acilis]['perc_draw'].mean()],
                    labels=['Kazanma', 'Kaybetme', 'Beraberlik'],
                    autopct='%1.1f%%',
                    startangle=90,
                    colors=['green', 'red', 'lightgrey'])
                plt.axis('equal')
                plt.title(f'{acilis} acilisinda {taraf} tarafin oyun sonucunun yuzdeleri')
                plt.show()

                # Döngüden çıkış yap
                guard = 1

            else:
                print("Hatali seçim yaptiniz. Lutfen tekrar deneyiniz.")
    
    elif input_secim == 6:
        # Lineer Regression nesnesi
        lr = LinearRegression()
        x = x.values.reshape(-1, 1)
        y = y.values.reshape(-1, 1)

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=100)
        type(x_train)
        lr.fit(x_train, y_train)

        y_pred = lr.predict(x_test)
        x_test_mean = x_test.mean()

        y_pred_mean = y_pred.mean()

        # Gerçek Data -> Grand Truth
        fig, ax = plt.subplots(figsize=(12,8))
        ax.scatter(x_test, y_test, label='Grand Truth', color='black')

        # Tahmin -> Prediction
        ax.scatter(x_test, y_pred, label='Prediction', color='red')

        plt.title('Percentage White Wins - Percentage Black Wins - PREDICTION')
        plt.xlabel('Percentage Black Wins')
        plt.ylabel('Percentage White Wins')
        plt.legend(loc='upper left')
        plt.show()

        print(f"Siyah'in Kazanma Oranlari Ortalamasi: {Percentage_Mean_Black:.2f}")
        print(f"Beyaz'in Kazanma Oranlari Ortalamasi: {Percentage_Mean_White:.2f}")
        print(f"Siyah'in Kazanma Oraninin Ortalama Tahmini: {x_test_mean:.2f}")
        print(f"Beyaz'in Kazanma Oraninin Ortalama Tahmini: {y_pred_mean:.2f}")

        exit()

    elif input_secim == 7:
        exit()

    else:
        print("Hatali seçim yaptiniz. Lutfen tekrar deneyiniz.")