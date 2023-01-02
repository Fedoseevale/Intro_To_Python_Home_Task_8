import view
phone_book = []


def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def change_contact(id: int, contact: list):
    global phone_book
    phone_book.pop(id - 1)
    phone_book.insert((id-1), contact)

def find_contact(symbol: str):
    global phone_book
    for i in range(0, len(phone_book)):
        if (symbol in phone_book[i][0]) or (symbol in phone_book[i][1]) or (symbol in phone_book[i][2]):
            id = i+1
            return id
        # else:
        #     view.fail_find_contact()