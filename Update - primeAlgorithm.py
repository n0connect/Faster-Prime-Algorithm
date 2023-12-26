import math
import pickle
import os
import sys
import time

# GLOBAL VARIABLES
new_created_file_name_ = ''  # Program ilk çalıştığında son kaydedilen .pkl boyutuna göre belirlenir.
user_end_number_: int  # Kullanıdan alınan bitiş değerini bellekte tutar.
last_digit_ = 0  # Son kaydedilen .pkl dosyasının sayı değerini bellekte tutar.
temp_num_: int = 0  # Yüklenilen .pkl dosyasının sayı değerini bellekte tutar.
start_number_: int = 1999  # saved_prime_list0.pkl dosyasının son elemanı isterseniz değiştirebilirsiniz.
another_list_has_been_set_: bool = False  # Başka bir .pkl dosyası kontrol için gerektiğinde TRUE alır.
set_zero_num_of_loaded_list_: bool = False  # 0.pkl dosyasını loaded liste eşitler.
end_of_the_program: bool = True  # Program hesaplama işlemlerini sorunsuz tamamlarsa TRUE alır.
temporary_prime_list: list = []  # Tespit edilen asal sayıları kaydetmek için geçici listede tutar.
loaded_list: list = []  # Kontrol için yüklenen .pkl dosyası bu listede tutulur.

# UPDATE VARIABLES
average_prime_number_quantity: float  # Yaklaşık asal sayı miktarı
density_of_primes_less_than_end_number: float  # Yoğunluk miktarı
kill_counts_of_a_prime_numbers: list = [(3, 0)]  # İlk sayı asal diğeri kill sayısıdır.
the_all_divisibility_probability_of_prime_numbers: list = [(3, 5.7), (5, 6.7)]  # Asal sayının bölebilme olasılığı

"""

1MB -> 3 MILYONA KADAR OLAN ASAL SAYILARI TUTABILIYOR

üzerinde çalıştığım şey dosya boyutu 1MB aşınca yeni dosya
üretmesi ve asal kontrolünü "ona göre yapması"

Algoritmanın %100 ve kodların %98'i kendime aittir. Ufak sorunlar olabilir
fakat stabilite ve gelişmeler üzerinde çalışacağım.

Program gayet hızlı çalışıyor, olasılık dağılımı üzerinde çalışmalarıma
başlayacağım.

"""


def file_size_control() -> None:
    # Program ilk çalıştığında kaydedilen .pkl dosyalarını kontrol eder
    global new_created_file_name_  # Oluşturulan yeni dosya ismidir eğer >?1MB Aksi halde son dosya ismini alır
    global last_digit_

    try:
        print(f"_" * 60)  # FOR GOOD SEEN
        saved_files_list = os.listdir(os.getcwd())
        last_saved_file = sorted(saved_files_list)[-1]
        for file in saved_files_list:
            if file.endswith('.pkl'):
                print(f"\nSaved Prime list {file}: {os.stat(file).st_size / (1024 ** 2)} MB")
                print(f"_" * 60)

        if 1 <= os.stat(last_saved_file).st_size / (1024 ** 2):
            print(f"\n{last_saved_file:>30} size is max.")
            print(f"_" * 60)
            last_digit_ = remove_character_in_file_name(last_saved_file)
            new_created_file_name_ = f'saved_prime_list{last_digit_ + 1}.pkl'
            create_new_pkl_file_()
        else:
            last_digit_ = remove_character_in_file_name(last_saved_file)
            new_created_file_name_ = f'{last_saved_file}'
    except Exception as ex:
        raise print(f"{ex}")


def remove_character_in_file_name(last_saved_file) -> int:
    # Kaç tane .pkl dosyasının kayıtlı olduğu sayısıdır.
    digits = ''.join(filter(str.isdigit, last_saved_file))
    if digits:
        digits = int(digits)
    else:
        digits = 0
    return digits


def create_new_pkl_file_() -> None:
    # 1MB aşan dosya varsa bu fonksiyon üzerinden algoritmayı sürdürür
    global last_digit_

    try:
        with open(f'saved_prime_list{last_digit_ + 1}.pkl', 'wb') as new_pkl_:
            new_pkl_.close()
    except Exception as ex:
        print(f"saved_prime_list{last_digit_ + 1}.pkl is not created: {ex}")


def take_user_number() -> None:
    global user_end_number_  # Kullanıcıdan alınan hesaplanacak son sayıdır
    global start_number_  # Başlangıç sayıdır doğru belirlenmelidir aksi halde soruna yol açar

    print("""
    This program has been developed with a new algorithm to find prime numbers faster,
    the basic principle of this algorithm is to use the prime numbers that exist up to
    a certain range to determine the status of other numbers.
    
    If you have used the program before ignore the default values, you also need to start
    by giving the starting number and the final number a number larger than the last number
    in the list you calculated.
    
    """)
    try:
        start_number_ = int(input("Enter a ODD positive start number(default: number>=3): "))
        user_end_number_ = int(input("Enter a ODD last number (default: number>=2001): "))
        if start_number_ <= 0 or user_end_number_ <= 0:
            raise ValueError
        if start_number_ % 2 == 0 or user_end_number_ % 2 == 0:
            raise print("Please Enter two ODD number.")
    except ValueError as er:
        print(f"{er}")
    except Exception as ex:
        print(f"{ex}")


def approx_calculation_of_probability() -> None:
    # Yaklaşık Asal Miktarı ve Yoğunluğu
    global average_prime_number_quantity
    global density_of_primes_less_than_end_number

    average_prime_number_quantity = user_end_number_ / math.log(user_end_number_)
    density_of_primes_less_than_end_number = 100*average_prime_number_quantity/user_end_number_

    print(f"Average prime number count until {user_end_number_}: {average_prime_number_quantity}")
    print(f"Density of prime less than {user_end_number_}: %{density_of_primes_less_than_end_number}")
    time.sleep(3)


def load_with_this_value_prime_list():
    global last_digit_  # Kaydedilen son .pkl dosyasının numarasını bellekte tutar
    global another_list_has_been_set_  # Başka bir liste yüklenmişse True Alır Default:False
    global set_zero_num_of_loaded_list_  # 0. listteyi yükler Default:False
    global loaded_list  # Yüklenecek .pkl dosyasını bellekte tutar
    global temp_num_  # Liste değerini bellekte tutar

    for temp_num in range(0, last_digit_ + 2, 1):

        if set_zero_num_of_loaded_list_:
            set_zero_num_of_loaded_list_ = False
        if another_list_has_been_set_:
            another_list_has_been_set_ = False
            temp_num = temp_num_
        try:
            with open(f'saved_prime_list{temp_num}.pkl', 'rb') as saved_file:
                loaded_list = pickle.load(saved_file)
                return ":)"
        except Exception as ex:
            print(f"saved_prime_list{temp_num}.pkl file is not broken: {ex}")
            print("Please Delete Broken and Empty Files. And Restart The Program")


def prime_control() -> str or bool:
    global another_list_has_been_set_
    global temporary_prime_list
    global loaded_list
    global start_number_

    for number in range(start_number_, user_end_number_ + 2, 2):
        for prime_item in loaded_list:
            # NOT PRİME
            if number % prime_item == 0:
                # OLASILIK HESABI İÇİN
                for kills in loaded_list:
                    if number % kills == 0:
                        probability_of_primes(kills)
                # OLASILIK HESABI İÇİN
                if another_list_has_been_set_:
                    freshness_for_prime_control(False)
                break
            # IS PRIME
            elif number in loaded_list:
                break
            # IS PRIME
            elif prime_item > math.sqrt(number + 10):
                process_bar(number)
                temporary_prime_list.append(number)
                if another_list_has_been_set_:
                    freshness_for_prime_control(False)
                break
            # LOAD ANOTHER LIST
            elif prime_item == loaded_list[-1]:
                freshness_for_prime_control(True)
    print("\n")
    return ":)"


def freshness_for_prime_control(condition: bool):
    global set_zero_num_of_loaded_list_
    global another_list_has_been_set_
    global temp_num_

    if not condition:
        # LOAD 0. PKL LIST
        temp_num_ = 0
        set_zero_num_of_loaded_list_ = True
    if condition:
        # LOAD ANOTHER LIST
        temp_num_ += 1
        another_list_has_been_set_ = True

    load_with_this_value_prime_list()


def probability_of_primes(fav_prime) -> None:
    # Hangi asal sayının kaç tane sayıyı elediğini kaydeder
    not_in_list: bool = False
    index_count: int = -1

    # Listenin içinde varmı kontrolü eğer yoksa True alır.
    if not any(fav_prime == prime for prime, _ in kill_counts_of_a_prime_numbers):
        not_in_list = True  # Listede değil
    for prime, kill_count in kill_counts_of_a_prime_numbers:
        index_count += 1
        if not_in_list:
            kill_counts_of_a_prime_numbers.append((fav_prime, 1))  # Listeye ekle
            break  # Döngüyü Bitir
        elif prime == fav_prime:
            updated_tuple = (kill_counts_of_a_prime_numbers[index_count][0],
                             kill_counts_of_a_prime_numbers[index_count][1] + 1)  # Değeri arttır
            kill_counts_of_a_prime_numbers[index_count] = updated_tuple
            break  # Döngüyü Bitir


def process_bar(number) -> None:
    # Stabil bir ProcessBar sağlar.
    global user_end_number_
    global temp_num_

    temp_time: int = 100 * ((number + 2) / user_end_number_)
    sys.stdout.write(f"\rProgress: [{'#' * int(temp_time * 0.5)}] {temp_time:.2f}%"
                     f" Calculated number: {number} Current Loaded list: saved_prime_list{temp_num_}.pkl")
    sys.stdout.flush()


def save_prime_list() -> None:
    # Yeni asal sayıları kaydeder.
    global new_created_file_name_
    global temporary_prime_list

    try:
        with open(f'{new_created_file_name_}', 'wb') as temp_list:
            pickle.dump(temporary_prime_list, temp_list)
    except Exception as ex:
        print(f"{ex}")


def save_probability_() -> None:
    global user_end_number_

    try:
        with open(f'dump_probability{user_end_number_}.pkl', 'wb') as prob_list:
            pickle.dump(kill_counts_of_a_prime_numbers, prob_list)
    except Exception as ex:
        print(f"{ex}")


def dump_terminal_all_file() -> None:
    # Son kaydedşlen listeyi "dosyayı" yükler
    global new_created_file_name_
    global last_digit_

    for temp_num in range(0, last_digit_ + 2, 1):
        try:
            with open(f'saved_prime_list{temp_num}.pkl', 'rb') as dump_in_terminal:
                dump_list = pickle.load(dump_in_terminal)
                len_of_list = len(dump_list)
                print(f"\nThe prime number at the top of the list: {dump_list[0]}")
                print(f"The prime number in the middle of the list: {dump_list[int(len_of_list / 2)]}")
                print(f"The prime number at the end of the list: {dump_list[-1]}")
                print(f"the list contains {len_of_list} prime numbers\nWait 2 sec.")
                time.sleep(2)
        except Exception as ex:
            print(f"saved_prime_list{temp_num}.pkl file is not broken: {ex}")
            print("Please Delete Broken and Empty Files. And Restart The Program")

    print("\nDone_Success_done_job_and_give_all_list_in_last_loaded_list")


def dump_probability_() -> None:
    total_count: int = 0

    for prime, count in kill_counts_of_a_prime_numbers:
        total_count += count

    for prime, count in kill_counts_of_a_prime_numbers:
        prob = count / total_count
        print(f"{prime} count is: {count} and probability: %{100 * prob:.2f}")


def kill_the_program() -> list or str:
    return print(":) boom")


file_size_control()
take_user_number()
approx_calculation_of_probability()
load_with_this_value_prime_list()
prime_control()
save_prime_list()
dump_terminal_all_file()
save_probability_()
dump_probability_()
kill_the_program()
