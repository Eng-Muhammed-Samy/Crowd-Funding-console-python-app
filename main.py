import authentication.inputs_validations as validation
import authentication.registration as register
import authentication.login as login
import user_functionality.user_functions as user_fun

reg = register.Registeration()
validate = validation.Validation
user_f = user_fun.UserFunctionality()
log = login.Login()

while True:
    print("Welcome To Crowd-Funding System\n1- Create New User\n2- Login\n3- exit")
    input_user = input()
    # register new user ***************************************************************
    if input_user == '1':
        while True:
            f_name = input("Enter First Name: ")
            if validate.validate_f_name(f_name):
                l_name = input("Enter Last Name: ")
                if validate.validate_l_name(l_name):
                    email = input("Enter Email: ")
                    if validate.validate_email(email):
                        password = input("Enter Password: ")
                        confirm_password = input("Enter password again: ")
                        if validate.validate_password(password, confirm_password):
                            reg.create_new_user(f_name, l_name, email, password)
                            break

    # login registered user ***************************************************************
    elif input_user == '2':
        email_input = input("Enter Email: ")
        password_input = input("Enter Password: ")
        if log.login(email_input, password_input):
            while True:
                print('1- Create New Project\n2- View All Projects\n3- Edit Project\n4- Delete Project\n5- Search\n6 '
                      '- exit')
                input_user2 = input();
                if input_user2 == '1':
                    while True:
                        title = input("Enter Project Title: ")
                        detailes = input("Enter Project Detailes: ")
                        target = input("Enter Project Target: ")
                        start_date = input("Enter Project Start Date: ")
                        end_date = input("Enter Project End Date: ")
                        user_f.create_project(email_input, title, detailes, target, start_date, end_date)
                        if input("to create new user please select Y : ") == 'n':
                            break

                elif input_user2 == '2':
                    user_f.view_all_projects(email_input)
                elif input_user2 == '3':
                    project_title = input("Enter project name : ")
                    user_f.edit_project(email_input, project_title)
                elif input_user2 == '4':
                    project_title = input("Enter project name : ")
                    agree = user_f.delete_project(email_input, project_title)
                    if agree:
                        print("project deleted")
                    else:
                        print('enter valid title')
                elif input_user2 == '5':
                    start_date = input("Enter Start Data : ")
                    end_date = input("Enter End Data : ")
                    user_f.search_obout_project(email_input, start_date, end_date)
                else:
                    break


    else:
        break
