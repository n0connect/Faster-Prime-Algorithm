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
        load_prime_list(selected_number)
    except ValueError as er:
        raise print(f"{er}")

    return None


def look_in_terminal(output_list: list) -> None:
    counter: int = 0
    for item in output_list:
        counter = counter + 1
        print(item, end="\n" if counter % 10 == 1 else ",")

    return print("\nDone_Success_w_in_terminal")


def process_bar(number,user_numbers):
    temp_time: int = 100 * ((number + 2) / user_numbers)
    sys.stdout.write(f"\rProgress: [{'=' * int(temp_time*0.5)}] {temp_time:.2f}%")
    sys.stdout.flush()


def prime_control(user_numbers, default_prime_list: list):

    for number in range(default_prime_list[-1], user_numbers, 2):
        for prime_item in default_prime_list:
            if number % prime_item == 0:
                process_bar(number, user_numbers)
                break
        else:
            default_prime_list.append(number)

    default_prime_list.insert(0, 2)
    save_prime_list(default_prime_list)
    look_in_terminal(default_prime_list)
    
    return None


def save_prime_list(save_list: list):
    with open('saved_prime_list.pkl', 'wb') as temp_list:
        pickle.dump(save_list, temp_list)

    return None


def load_prime_list(user_number) -> list or None:
    try:
        current_directory = os.getcwd()

        file_name = 'saved_prime_list.pkl'
        file_path = os.path.join(current_directory, file_name)
    except Exception as ex:
        raise print(f"{ex}")

    if os.path.exists(file_path):
        print(f"{file_name} file exists.")

        with open('saved_prime_list.pkl', 'rb') as saved_file:
            loaded_list = pickle.load(saved_file)
            print(f"{file_name} last number in list: {loaded_list[-1]}\nPreparing...")
            time.sleep(5)
            prime_control(user_number, loaded_list)

    else:
        print(f"{file_name} file does not exist, program is closing...")
        sys.exit(1)


take_user_number()
