from sortedcontainers import SortedDict

class Contacts:
    def __init__(self, name = None, email = None, phone_num = None):
        self.name = name
        self.email = email
        self.phone_num = phone_num

class ContactList:
    def __init__(self):
        self.id_dict = {}
        self.name_map = SortedDict()
        self.email_map = {}
        self.phone_map = {}

        self.global_id = 0
    
    def add_contact(self, name, phone_num, email):
        self.global_id += 1

        self.name_map[name] = self.global_id
        self.email_map[email] = self.global_id
        self.phone_map[phone_num] = self.global_id

        self.id_dict[self.global_id] = Contacts(name, email, phone_num)
    
    def get_by_name(self, name):
        return self.id_dict[self.name_map[name]]
    
    def get_by_email(self, email):
        return self.id_dict[self.email_map[email]]
    
    def get_by_phone(self, phone):
        return self.id_dict[self.phone_map[phone]]
    
    def get_by_id(self, id):
        return self.id_dict[id]
    
    def remove(self, id):
        contact = self.id_dict[id]

        del self.name_map[contact.name]
        del self.email_map[contact.email]
        del self.phone_map[contact.phone_num]

        del self.id_dict[id]
    
    def get_contacts_ordered_by_name(self):
        ordered_contact_lis = []

        for name in self.name_map:
            ordered_contact_lis.append(self.id_dict[self.name_map[name]])
        
        return ordered_contact_lis
    
    def __str__(self):
        ret_str = ""
        cont_list_ordered = self.get_contacts_ordered_by_name()

        for cont in cont_list_ordered:
            ret_str += "- " + "Name: " + str(cont.name) + " ; " + "Phone Number: " + str(cont.phone_num) + " ; " + "E-Mail: " + str(cont.email) + " -" + "\n"
        
        return ret_str

if __name__ == "__main__":
    contact_list = ContactList()

    contact_list.add_contact("Hanna Hönnudóttir", "1234567","hanna@hanna.is")
    contact_list.add_contact("Jón Jónsson", "2345678","jon@jon.is")
    contact_list.add_contact("Anna Önnudóttir", "3456789","anna@anna.is")
    contact_list.add_contact("Guðmundur Guðmundsson","4567890", "gummi@gummi.is")
    contact_list.add_contact("Bryndís Bryndísardóttir","0123456", "disa@disa.is")

    some_contact_1 = contact_list.get_by_name("Anna Önnudóttir")
    some_contact_2 = contact_list.get_by_phone("4567890")
    some_contact_3 = contact_list.get_by_email("hanna@hanna.is")

    ordered_contact_list = contact_list.get_contacts_ordered_by_name()
    for contact in ordered_contact_list:
        print(contact.name)
    
    print(contact_list)
            

    


