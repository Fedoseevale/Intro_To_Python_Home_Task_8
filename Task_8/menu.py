import view
import phone_book as pb
import data_base as db



def main_menu(choice: int):
    match choice:
        case 1:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2:
            db.load_data_base()
            view.load_success()
        case 3:
            db.save_data_base()
            view.save_success()
        case 4:
            contact = view.input_new_contact()
            pb.add_contact(contact)
        case 5:
            id = view.input_id_change_contact()
            contact = view.input_body_change_contact()
            pb.change_contact(id, contact)
        case 6:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
        case 7:
            find_symbol = view.input_find_contact()
            phone_book = pb.get_phone_book()
            if pb.find_contact(find_symbol):
                id = pb.find_contact(find_symbol)
                contact = phone_book[id-1]
                view.success_find_contact(contact)
            else:
                view.fail_find_contact()
        case 0:
            return True

def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break