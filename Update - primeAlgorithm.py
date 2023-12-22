import math
import pickle
import os
import sys
import time

# GLOBAL VARIABLES
new_created_file_name_ = ''
last_digit_ = 0
temp_user_number_: int
another_list_has_been_loaded_: bool = False
current_num_: int = 1999    # saved_prime_list0.pkl dosyasının son elemanı isterseniz değiştirebilirsiniz
last_num_in_next_list_: int
temporary_prime_list: list = []
number_of_current_loaded_list_: int
set_zero_num_of_loaded_list_: bool = False


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

    global new_created_file_name_
    global last_digit_

    try:
        print(f"_" * 50)  # Güzel bir görünüm için
        saved_files_list = os.listdir(os.getcwd())
        last_saved_file = sorted(saved_files_list)[-1]
        for file in saved_files_list:
            if file.endswith('.pkl'):
                print(f"Saved Prime list {file}: {os.stat(file).st_size / (1024 ** 2)} MB\n")
                print(f"_" * 50)

        if 1 <= os.stat(last_saved_file).st_size:
            print(f"{last_saved_file:>30} size is max.")
            last_digit_ = remove_character_in_file_name(last_saved_file)
            new_created_file_name_ = f'saved_prime_list{last_digit_ + 1}.pkl'
            create_new_pkl_file_()
        else:
            last_digit_ = remove_character_in_file_name(last_saved_file)
            new_created_file_name_ = f'{last_saved_file}'
    except FileNotFoundError as fe:
        print(f"{fe}")
    except Exception as ex:
        raise print(f"{ex}")


def remove_character_in_file_name(last_saved_file) -> int:
    # Algoritma için gerekli adım

    digits = ''.join(filter(str.isdigit, last_saved_file))
    if digits:
        digits = int(digits)
    else:
        digits = 0
    return digits


def create_new_pkl_file_() -> None:
    # 1MB aşan dosya varsa onun üzerinden algoritmayı sürdürür

    global last_digit_

    try:
        with open(f'saved_prime_list{last_digit_ + 1}.pkl', 'wb') as new_pkl_:
            new_pkl_.close()
    except Exception as ex:
        print(f"saved_prime_list{last_digit_ + 1}.pkl is not created: {ex}")


def take_user_number() -> None:
    global temp_user_number_

    print("""
    This program has been developed with a new algorithm to find prime numbers faster,
    the basic principle of this algorithm is to use the prime numbers that exist up to
    a certain range to determine the status of other numbers.

    """)
    try:
        temp_user_number_ = int(input("Enter a ODD number (number>=2000): "))
        load_prime_list()
    except ValueError as er:
        print(f"{er}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as ex:
        print(f"{ex}")


def information_about_loaded_list_file(loaded_list: list) -> None:
    # Test aşamasında kullanığım fonksiyon

    len_of_list = len(loaded_list)
    print(f"The prime number at the top of the list: {loaded_list[0]}")
    print(f"The prime number in the middle of the list: {loaded_list[int(len_of_list / 2)]}")
    print(f"The prime number at the end of the list: {loaded_list[-1]}")
    print(f"the list contains {len_of_list} prime numbers")
    time.sleep(2)


def load_prime_list() -> list or str:
    # Algoritmanın !BEL KEMIĞI! geliştirmeye devam edeceğim.

    global last_digit_
    global another_list_has_been_loaded_
    global number_of_current_loaded_list_
    global set_zero_num_of_loaded_list_
    global temp_user_number_
    end_of_the_program_: bool = True

    while end_of_the_program_:
        for temp_num in range(0, last_digit_ + 2):

            number_of_current_loaded_list_ = temp_num

            try:
                with open(f'saved_prime_list{temp_num}.pkl', 'rb') as saved_file:
                    loaded_list = pickle.load(saved_file)
                    if prime_control(temp_user_number_, loaded_list):
                        another_list_has_been_loaded_ = True
                        continue
                    elif set_zero_num_of_loaded_list_:
                        temp_num = 0
                        another_list_has_been_loaded_ = False
                        set_zero_num_of_loaded_list_ = False
                        break
                    else:
                        end_of_the_program_ = False
                        break

            except Exception as ex:
                print(f"saved_prime_list{temp_num}.pkl file is not broken: {ex}")

        return print(":) boom")


def prime_control(user_numbers, loaded_list: list) -> str or bool:
    # Asallık kontrolünü yapar, Algoritmanın !BEL KEMIĞI! geliştirmeye devam edeceğim.

    global another_list_has_been_loaded_
    global current_num_
    global last_num_in_next_list_
    global temporary_prime_list
    global number_of_current_loaded_list_
    global set_zero_num_of_loaded_list_

    for number in range(current_num_, temp_user_number_ + 2, 2):

        if another_list_has_been_loaded_ or set_zero_num_of_loaded_list_:
            number = current_num_

        for prime_item in loaded_list:
            # ASAL DEĞİL
            if number % prime_item == 0:
                if another_list_has_been_loaded_:
                    current_num_ = number + 2
                    set_zero_num_of_loaded_list_ = True
                    return False
                break

            elif number in loaded_list:
                break

            # ASALDIR
            elif prime_item > math.sqrt(number + 10):
                process_bar(number, user_numbers)
                temporary_prime_list.append(number)

                if another_list_has_been_loaded_:
                    current_num_ = number + 2
                    set_zero_num_of_loaded_list_ = True
                    return False

                break

            # BAŞKA BİR LİSTE YÜKLE
            elif prime_item == loaded_list[-1]:
                current_num_ = number
                return True

    print("\n")
    save_prime_list()
    return ":)"


def process_bar(number, user_numbers) -> None:
    # Stabil bir ProcessBar sağlar.

    global number_of_current_loaded_list_

    temp_time: int = 100 * ((number + 2) / user_numbers)
    sys.stdout.write(f"\rProgress: [{'#' * int(temp_time * 0.5)}] {temp_time:.2f}% Calculated number: {number}")
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


def done_job_and_give_all_list_in_last_list(output_list: list) -> None:
    # Test aşamasında kullanığım fonksiyon

    counter: int = 0
    for item in output_list:
        counter = counter + 1
        print(item, end="\n" if counter % 10 == 1 else ",")
    print("\nDone_Success_done_job_and_give_all_list_in_last_list")


file_size_control()
take_user_number()
