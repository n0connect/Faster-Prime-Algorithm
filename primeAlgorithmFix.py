import pickle
import os
import sys
import time

new_created_file_name_ = ''


def take_user_number() -> None:
    print("""
    This program has been developed with a new algorithm to find prime numbers faster,
    the basic principle of this algorithm is to use the prime numbers that exist up to
    a certain range to determine the status of other numbers.

    """)
    try:
        selected_number: int = int(input("Enter a number (number>=2000): "))
        load_prime_list(selected_number)
    except ValueError as er:
        print(f"{er}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as ex:
        print(f"{ex}")


def information_about_last_saved_file(loaded_list: list) -> None:
    len_of_list = len(loaded_list)
    print(f"The prime number at the top of the list: {loaded_list[0]}")
    print(f"The prime number in the middle of the list: {loaded_list[int(len_of_list / 2)]}")
    print(f"The prime number at the end of the list: {loaded_list[-1]}")
    print(f"the list contains {len_of_list} prime numbers")
    time.sleep(5)


def look_in_terminal(output_list: list) -> None:
    counter: int = 0
    for item in output_list:
        counter = counter + 1
        print(item, end="\n" if counter % 10 == 1 else ",")
    print("\nDone_Success_look_in_terminal")


def process_bar(number, user_numbers):
    temp_time: int = 100 * ((number + 2) / user_numbers)
    sys.stdout.write(f"\rProgress: [{'=' * int(temp_time * 0.5)}] {temp_time:.2f}%")
    sys.stdout.flush()


def prime_control(user_numbers, default_prime_list: list):
    for number in range(default_prime_list[-1], user_numbers, 2):
        for prime_item in default_prime_list:
            if number % prime_item == 0:
                process_bar(number, user_numbers)
                break
        else:
            default_prime_list.append(number)
            save_prime_list(default_prime_list)
    default_prime_list.insert(0, 2)
    look_in_terminal(default_prime_list)


def save_prime_list(save_list: list):
    global new_created_file_name_

    try:
        with open(f'{not_secure_file_name}', 'wb') as temp_list:
            pickle.dump(save_list, temp_list)
    except Exception as ex:
        print(f"{ex}")


def load_prime_list(user_number) -> list or None:
    global new_created_file_name_

    print(f"{not_secure_file_name}file exists.")
    with open(f'{not_secure_file_name}', 'rb') as saved_file:
        loaded_list = pickle.load(saved_file)
        print(f"{not_secure_file_name}\n\nPreparing...")
        information_about_last_saved_file(loaded_list)
        time.sleep(5)
        prime_control(user_number, loaded_list)


def file_size_control():
    global new_created_file_name_

    try:
        saved_files_list = os.listdir(os.getcwd())
        last_saved_file = sorted(saved_files_list)[-1]
        for file in saved_files_list:
            if file.endswith('.pkl'):
                print(f"Saved Prime list {file}: {os.stat(file).st_size}\n")

        if 2048 <= os.stat(last_saved_file).st_size / (1024 ** 2):
            print(f"{last_saved_file} size is max.")
            last_digit_ = remove_character_in_file_name(last_saved_file)
            not_secure_file_name = f'saved_prime_list{last_digit_ + 1}.pkl'
        else:
            not_secure_file_name = f'{last_saved_file}'
    except FileNotFoundError as fe:
        print(f"{fe}")
    except Exception as ex:
        raise print(f"{ex}")


def remove_character_in_file_name(last_saved_file) -> int:
    digits = ''.join(filter(str.isdigit, last_saved_file))
    return int(digits)


def rename_the_current_saved_file():
    pass


file_size_control()
take_user_number()
