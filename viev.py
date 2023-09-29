import txt

def main_menu():
    print(txt.main_menu[0])
    for i in range(len(txt.main_menu)):
        if i:
            print(f'{i:>3}. {txt.main_menu[i]}')
    while True:
        choice = input(txt.input_main_menu)
        if choice. isdigit() and 0<int(choice)<len(txt.main_menu):
            return choice
        print(txt.input_main_menu_error)

def print_message(msg: str):
    print('\n'+ '='* len(msg))
    print(msg)
    print('='* len(msg)+'\n')

def show_contacts(book: dict, msg:str):
    if book:
        max_size=[len(max(field, key=len)) for field in zip(*list(book.values()))]
        print('\n' + '='*(sum(max_size)+10))
        for u_id, contact in book.items():
            contact_str = ' '.join([f'{contact[i]:<{max_size[i]}}' for i in range(len(contact))])
            print(f'{u_id:>3} {contact_str}')
        print('=' *(sum(max_size)+10)+'\n')
    else:
        print_message(msg)

def input_new_contact(msg:list) ->list[str, str, str]:
    contact=[]
    for field in msg:
        contact.append(input(field))
    return contact
def input_info(msg: str):
    return input(msg)