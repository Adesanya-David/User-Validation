import random
import string

def user_details():
    FirstName = str(input("Please Enter your First name : ")) 
    LastName = str(input ("\nPlease Enter your last name : " ))
    Email = str(input ("\nPlease Enter your email address : " ))
    
    user = [FirstName, LastName, Email]
    return user

def pass_details(user):
    letters = string.ascii_letters
    random_pass = ''.join(random.choice(letters) for i in range(5))
    
    password = str(user[0][0:2] + user[1][-2:] + random_pass)
    return password
  
status = True 
container = []

while status:
        user = user_details()
        password = pass_details(user)
        print ( "\nYour password is " + str(password))
    
        pass_ver = input(str("Are you satisfied with the password: y/n? "))
    
        password_loop = True

        while password_loop:

            if (pass_ver == "y"):
                user.append(password)
                container.append(user)
                
                password_loop = False
    
            else:
                 newPassword = input(str("Please enter your Desired password: " ))
        
                 pass_check = True

                 while pass_check:
          
                        if (len(newPassword) >= 7): 
                            user.append(newPassword)
                            container.append(user)
                
                            pass_check = False 
                            password_loop = False
            
                        else:
                            print("Sorry, your password must not be less than 7 characters.")
                            newPassword = input(str("Please re-enter your password: "))
     
        add_user = input(str("\n Do you want to add a new user: Yes or No? "))

        if (add_user == "No"):
    
             status = False
             for item in container:
                    print('[{}]'.format(', '.join(map('{}'.format, container))))
    
        else: 
         status = True