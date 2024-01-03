import pickle
from matplotlib import pyplot as plt
import numpy as np
import os


def start_the_program() -> None:
    list_the_pkl_files()


# İstenilen .pkl dosyası yüklenir
def list_the_pkl_files() -> None:
    try:
        print(f"_" * 60)  # FOR GOOD SEEN
        saved_files_list = os.listdir(os.getcwd())  # Dizinde ki dosyaları al
        last_saved_file = sorted(saved_files_list)[-1]  # Kaydedilen .pkl son elemanı
        for file in saved_files_list:
            if file.endswith('.pkl'):  # .pkl olanları seç
                print(f"\nSaved Prime list {file}: {os.stat(file).st_size / (1024 ** 2)} MB")  # Boyut Kontrolü
                print(f"_" * 60)  # Sadece görsellik için
    except Exception as ex:
        print(f"{ex}")

    remove_character_in_file_name(last_saved_file)


# Kaydedilen .pkl dosyasının son sayısını belirler
def remove_character_in_file_name(last_saved_file) -> None:
    # Kaç tane .pkl dosyasının kayıtlı olduğu sayısıdır.
    last_digit_ = ''.join(filter(str.isdigit, last_saved_file))
    if last_digit_:
        last_digit_ = int(last_digit_)
    else:
        last_digit_ = 0

    chose_the_pkl_file(last_digit_)


# İncelenecek .pkl dosyasını seçilir
def chose_the_pkl_file(last_digit_) -> None:
    print(f"""
    Enter the number value at the end of the name of whichever of the files with the .pkl
    extension registered above you want to examine, e.g: saved_prime_list0.pkl -> Enter: 0
    
    The largest number registered: saved_prime_list{last_digit_}.pkl
    """)

    while True:
        try:
            chosen_number = int(input("Enter: "))
            if chosen_number > last_digit_ or chosen_number < 0:
                raise print("Enter a valid number!")
        except Exception as ex:
            print(f"{ex}")
        file_name_to_review = f"saved_prime_list{chosen_number}.pkl"
        break
    confirmation_()
    load_the_chosen_pkl_file(file_name_to_review)


def load_the_chosen_pkl_file(file_name_to_review) -> None:
    try:
        with open(f'{file_name_to_review}', 'rb') as pkl_list:
            examined_file = pickle.load(pkl_list)
    except Exception as ex:
        print(ex)
    numerate_the_array(examined_file)


def numerate_the_array(examined_file) -> None:
    numerated_examined_file = list(enumerate(examined_file, 1))
    information_about_the_file(examined_file, numerated_examined_file)


def information_about_the_file(examined_file: list, numerated_examined_file: list) -> None:
    len_of_list = len(numerated_examined_file)
    print(f" This file contains {len_of_list} prime numbers")
    print(f"\nThe prime number at the top of the list: {numerated_examined_file[0]}")
    print(f"The prime number in the middle of the list: {len_of_list / 2}")
    print(f"The prime number at the end of the list: {numerated_examined_file[-1]}")
    confirmation_()
    convert_array_to_integer(examined_file)


def convert_array_to_integer(examined_file) -> None:
    examined_file = [int(prime) for prime in examined_file]
    chose_visual_(examined_file)


def chose_visual_(examined_file) -> None:
    any_problem_ = True
    print("""
    1-) Approximate quantity graph of PRIME NUMBERS less than N
    2-) Density graph of PRIME NUMBERS less than N
    3-) Visual distribution of PRIME NUMBERS less than N
    4-) Double difference graph of PRIME NUMBERS less than N
    0-) Quit
    """)

    while any_problem_:
        try:
            value_ = int(input("Chose: "))
            if value_ < 0 or value_ > 4 or type(value_) is not int:
                raise print("Enter a valid number!")
            elif value_ == 1:
                visualizing_prime_number_count_matplotlib()
            elif value_ == 2:
                visualizing_prime_number_density_matplotlib()
            elif value_ == 3:
                visualizing_prime_number_matplotlib(examined_file)
            elif value_ == 4:
                visualizing_double_difference_prime_number_matplotlib(examined_file)
            elif value_ == 0:
                any_problem_ = False
                break
        except Exception as ex:
            print(f"{ex}")
    kill_the_program(any_problem_)


def confirmation_() -> None:
    print(f"{"_":>50}")
    print(f"{"Do you want to continue ? Y/N":>30}")
    print(f"{"_":>50}")
    while True:
        try:
            user_key_ = input(f"{"Enter:"}")
            user_key_ = user_key_.upper()  # Büyük Harfe çevir.

            if user_key_ == 'Y' or user_key_ == ' Y':
                return None
            elif user_key_ == 'N' or user_key_ == ' N':
                any_problem_ = True
                kill_the_program(any_problem_)
                break
            else:
                raise print("Y means yes I want to continue and N means you guess :)")
        except Exception as ex:
            print(f"{ex}")


def kill_the_program(any_problem_) -> None:
    if any_problem_:
        print('Puff :(')
    else:
        print('Boom :)')


def visualizing_prime_number_count_matplotlib():
    temp_array = np.linspace(2, 10 ** 5)  # Verilen aralıklarda sayılar oluşturulur
    plt.style.use('ggplot')  # Tema belirlenir

    plt.plot(temp_array, temp_array / np.log(temp_array), label='p_Count', color='red', linewidth=2.5)
    plt.ylim(-1000, 10000)  # Y ekseninin sınırları belirlenir

    # X ve Y eksenlerini belirginleştirme
    plt.axhline(0, color='black', linewidth=2.5)
    plt.axvline(0, color='black', linewidth=2.5)

    plt.xlabel('X-Axis')  # X ekseni etiketi
    plt.ylabel('Y-Axis')  # Y ekseni etiketi
    plt.title('Approximate number of primes less than X')  # Grafik başlığı
    plt.legend()  # Labelleri etkinleştirmek için gerekli
    plt.show()  # Programın ekranda kalmasını sağlar


def visualizing_prime_number_density_matplotlib():
    temp_array = np.linspace(2, 10 ** 5, 10 ** 3)  # Verilen aralıklarda sayılar oluşturulur
    plt.style.use('ggplot')  # Tema belirlenir

    plt.plot(temp_array, 100 / np.log(temp_array), label='% p_Density', color='purple', linewidth=2.5)
    plt.ylim(-10, 100)  # Y ekseninin sınırları belirlenir

    # X ve Y eksenlerini belirginleştirme
    plt.axhline(0, color='black', linewidth=2.5)
    plt.axvline(0, color='black', linewidth=2.5)

    plt.xlabel('X-Axis')  # X ekseni etiketi
    plt.ylabel('Y-Axis')  # Y ekseni etiketi
    plt.title('Approximate density of primes less than X')  # Grafik başlığı
    plt.legend()  # Labelleri etkinleştirmek için gerekli
    plt.show()  # Programın ekranda kalmasını sağlar


def visualizing_prime_number_matplotlib(examined_file):
    # Asal sayıların sıra değerleri tutulur
    y_list = list(range(len(examined_file)))

    # Tema belirlenir
    plt.style.use('ggplot')

    # plt.plot(examined_file, examined_file/np.log(examined_file), label='IDK', color='blue', linewidth=2.5)
    plt.plot(examined_file, y_list, marker='o', linestyle='--', label='Primes', color='purple', linewidth=2.5)

    # Asal sayıları marker üstüne yazdırmak
    for y, x in zip(y_list, examined_file):
        plt.annotate(f'{x}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center',
                     bbox=dict(boxstyle='round,pad=0.1', edgecolor='black', facecolor='white'))

    plt.xlim(-10, 100)  # X ekseninin sınırları belirlenir
    plt.ylim(-10, 100)  # Y ekseninin sınırları belirlenir

    # X ve Y eksenlerini belirginleştirme
    plt.axhline(0, color='black', linewidth=2.5)
    plt.axvline(0, color='black', linewidth=2.5)

    plt.xlabel('X-Axis(Primes)')  # X ekseni etiketi
    plt.ylabel('Y-Axis(Order of prime numbers)')  # Y ekseni etiketi
    plt.title('Distribution of prime numbers')  # Grafik başlığı
    plt.legend()  # Labelleri etkinleştirmek için gerekli
    plt.show()  # Programın ekranda kalmasını sağlar


def visualizing_double_difference_prime_number_matplotlib(examined_file):
    # İkili fark hesaplama
    double_dif_prime_list: list = []
    double_dif_list: list = []
    y_list = list(range(len(examined_file) - 1))

    for index in y_list:
        double_dif_prime_list.append((examined_file[index], examined_file[index + 1]))
        temp_diff = examined_file[index + 1] - examined_file[index]
        double_dif_list.append(temp_diff)

    plt.style.use('ggplot')  # Tema belirlenir

    plt.plot(double_dif_prime_list, double_dif_list, marker='o', linestyle='--', label='DoubleDifference',
             color='purple', linewidth=2)

    # Asal sayıları marker üstüne yazdırmak
    for y, x in double_dif_prime_list:
        plt.annotate(f'{x, y}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center',
                     bbox=dict(boxstyle='round,pad=0.1', edgecolor='black', facecolor='white'))

    # X ve Y eksenlerini belirginleştirme
    plt.axhline(0, color='black', linewidth=2.5)
    plt.axvline(0, color='black', linewidth=2.5)

    plt.xlabel('X-Axis(Primes)')  # X ekseni etiketi
    plt.ylabel('Y-Axis(Order of prime numbers)')  # Y ekseni etiketi
    plt.title('Distribution of prime numbers')  # Grafik başlığı
    plt.legend()  # Labelleri etkinleştirmek için gerekli
    plt.show()  # Programın ekranda kalmasını sağlar


start_the_program()
