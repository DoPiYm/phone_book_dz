import txt
import viev
import model

def search_func(msg: str):
    word =viev.input_info(msg)
    result =model.search(word)
    viev.show_contacts(result,txt.search_contact_error(word))
    return result

def  start():
    while True:
       choice=viev.main_menu()
       match choice:
           case'1':
               model.open_file()
               viev.print_message(txt.open_successful)
           case '2':
               model.save_file()
               viev.print_message(txt.open_successful)
           case'3':
               viev.show_contacts(model.phone_book, txt.empty_phone_book_error)
           case'4':
               contact=viev.input_new_contact(txt.input_new_contact)
               model.new_contact(contact)
               viev.print_message(txt.contact_successful_result(contact[0],0))
           case'5':
               search_func(txt.input_search_word)
           case'6':
               if search_func(txt.input_search_word):
                   u_id = viev.input_info(txt.input_edit_id)
                   new_contact=viev.input_new_contact(txt.input_edit_contact)
                   name = model.edit(int(u_id), new_contact)
                   viev.print_message(txt.contact_successful_result(name, 1))
           case'7':
               if search_func(txt.input_delete_word):
                   u_id = viev.input_info(txt.input_delete_id)
                   confirm_name = model.phone_book.get(int(u_id))[0]
                   if viev.input_info(txt.confirm_delete_contact(confirm_name)).lower()=='y':
                       name = model.delete(int(u_id))
                       viev.print_message(txt.contact_successful_result(name,2))
           case'8':
               if model.original_book!= model.phone_book:
                   if viev. input_info(txt.confirm_changes).lower()=='y':
                       model.save_file()
               viev.print_message(txt.good_bay)
               break