Contact = {}

def showFunction():
    print (Contact.items())  # dict_items etai print hocche
    print ("name \t contact" )
    for key in Contact:
        print("{} \t  {}".format(key,Contact.get(key)))

while True:
    choice = int( input("1. Add New Contact \n"
                   "2. Search The Contact \n"
                   "3. Display The Contact \n"
                   "4. Edit The Contact \n"
                   "5. Delete The Contact \n"
                   "6. Exit \n"
                   "Please Write The Number Between 1-6:  "
                   ) )   
    if choice == 1 :
        name = input ("Add Your Contact Name: ")
        phone = input ("Add Your Phone Number: ")
        Contact[name] = phone


    elif choice == 2 :
        ContactName = input ("Search The Contact: ")   
        if ContactName in Contact:
            print(ContactName, "Contact Number is ", Contact[ContactName])
        else:
            print(" No Contact Number Found")    



    elif choice == 3 :
        if not Contact:
            print ("Contact Book is Empty")
        else:
            showFunction() 

    elif choice == 4 :
        EditContact = input("Edit your Contact: ")     
        if EditContact in Contact :
            phone = input ("Change Your Number: ")
            Contact[EditContact] = phone
            print(" Contact Update Successfully ")
            showFunction() 
        else:
            print ("Name is not Found")


    elif choice == 5 :
        del_Contact = input ("Which Contact do you want to delete?: ")
        if del_Contact in Contact :
            DeleteConfirmed = input ("Do you want to delete this contact y/n :")
            if DeleteConfirmed == "y" or DeleteConfirmed == "Y":
                Contact.pop(del_Contact)
                showFunction() 
                print(" Contact Delete Successfully ")
            else:
                print ("The name is not Found in the contact ")

    else:
        break            
