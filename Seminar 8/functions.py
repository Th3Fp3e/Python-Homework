def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('Seminar 8\\sem_8_practice\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())
        print()


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Enter the initials: ')
    phone_num = input('Enter the phone number: ')
    with open('Seminar 8\\sem_8_practice\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('Seminar 8\\sem_8_practice\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_info = input('Enter the value to search for: ')
    result = search(data, contact_info)
    print(result)


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return "No matches found"
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('---------------')
        print('\n'.join(result))
        new_info = input('Enter the clarificating information: ')
        return search(result, new_info)
    

def change_data() -> None:
    """Modifies or deletes data selected by search"""
    with open('Seminar 8\\sem_8_practice\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    to_edit = input('Enter tha data to search for: ')
    to_edit = search(data, to_edit)
    print()
    print(to_edit)
    mode = input("Delete or modify: Delete - 1, modify - 2")
    if mode == '1':
        data.remove(to_edit)
    elif mode == '2':
        data[data.index(to_edit)] = enter_contact()

    with open('Seminar 8\\sem_8_practice\\book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def enter_contact() -> None:
    surname = input('Enter the surname: ')
    first_name = input('Enter the first name: ')
    fathers_name = input("Enter the father's name (if available): ")
    phone_num = input('Enter the phone number: ')
    return f'{surname} {first_name} {fathers_name} | {phone_num}'