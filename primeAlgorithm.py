import pickle
import os
import sys
import time


def take_user_number() -> None:
    print("""
    This program has been developed with a new algorithm to find prime numbers faster,
    the basic principle of this algorithm is to use the prime numbers that exist up to
    a certain range to determine the status of other numbers.

    """)
    try:
        selected_number: int = int(input("Enter a number (number>=2000): "))
        check_last_saved_file(selected_number)
    except ValueError as er:
        raise print(f"{er}")
    except Exception as ex:
        raise print(f"{ex}")

    return None


def information_about_last_saved_file(loaded_list: list) -> None:
    len_of_list = len(loaded_list)
    print(f"The prime number at the top of the list: {loaded_list[0]}")
    print(f"The prime number in the middle of the list: {loaded_list[int(len_of_list/2)]}")
    print(f"The prime number at the end of the list: {loaded_list[-1]}")
    print(f"the list contains {len_of_list} prime numbers")


def look_in_terminal(output_list: list) -> None:
    counter: int = 0
    for item in output_list:
        counter = counter + 1
        print(item, end="\n" if counter % 10 == 1 else ",")

    return print("\nDone_Success_look_in_terminal")


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

    return None


def save_prime_list(save_list: list):
    try:
        with open('saved_prime_list.pkl', 'wb') as temp_list:
            pickle.dump(save_list, temp_list)
    except Exception as ex:
        raise print(f"{ex}")

    return None


def load_prime_list(user_number, file_name) -> list or None:
    print(f"{file_name} file exists.")

    with open('saved_prime_list.pkl', 'rb') as saved_file:
        loaded_list = pickle.load(saved_file)
        print(f"{file_name}\n\nPreparing...")
        information_about_last_saved_file(loaded_list)
        time.sleep(3)
        prime_control(user_number, loaded_list)


def check_last_saved_file(user_number) -> object or None:
    try:
        current_directory = os.getcwd()

        file_name = 'saved_prime_list.pkl'
        file_path = os.path.join(current_directory, file_name)
    except Exception as ex:
        raise print(f"{ex}")

    if not os.path.exists(file_path):
        raise FileNotFoundError

    load_prime_list(user_number, file_name)


take_user_number()
