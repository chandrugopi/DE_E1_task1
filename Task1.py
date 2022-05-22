import re
print("*********Welcome*********")


re_user = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$' 

def login():
    username = input("Username : ")
    password = input("Password : ")
    for line in open("register.txt","r").readlines():
        name = line.split() 
        if username == name[0] :
            #print("Correct username!")
            if password == name[1]:
                print(username+" : logged in successfully....!!!!!!!!")
            else:
                print("Incorrect Password. Please try again/forgot password")
                log_pwd()
            return  
    print("Invalid Username. Try with correct username or please register, If you have not registered already")
    website() 
    return 

def register(username,password):
        
    for line in open("register.txt","r").readlines(): 
        login_info = line.split() 
        if username == login_info[0]:
            print("You have already register with email :"+username+".")
            print("Redirecting to login page")
            login()
            return  
    with open('register.txt' , 'at') as f:
        f.write (username+" "+password+"\n")
        f.close()
        print(username+" : User registered successfully....!!!")
        print("Now you can login")
        print("\n*********Login page***********")
        login()
    return 

def val_user():
    username = input("Username : ")
    password = input("Password : ")      
    if(re.fullmatch(re_user, username)):
        #print("Valid Username")
        pwd(username,password)
    else:
        print("Invalid Username. Username should be your email id") 
        val_user()
        
def pwd(username,password):
      
    val = True
      
    if (len(password) < 5 or len(password) > 16) :
        print('Password length should be 6 to 15 characters')
        val_user()
        val = False
          
    elif not re.search("[1-9]",password):
        print("""Password should have at least one number,\n 
one special character,one upper case and one lower case""")
        val_user()
        val = False
          
    elif not re.search("[A-Z]",password):
        print("""Password should have at least one number,\n 
one special character,one upper case and one lower case""")
        val_user()
        val = False
          
    elif not re.search("[a-z]",password):
        print("""Password should have at least one number,\n 
one special character,one upper case and one lower case""")
        val_user()
        val = False
                
    elif not re.search("[~!@#$%^&*()_-]",password):
        print("""Password should have at least one number,\n 
one special character,one upper case and one lower case""")
        val_user()
        val = False
    elif (password.replace(" ", "") != password):
        print('Password should have any empty space')
        val_user()
        val = False
    else:
        #print("vaild password")
        register(username,password)

def forgot_password():
    username = input("Username : ")
    for line in open("register.txt","r").readlines():
        name = line.split()
        if username == name[0]:
            print("Password for "+username+" : " +name[1])
            print("Continue with login")
            login()
            return
    print("Invalid username. Try again")
    forgot_password()
    return
        
def website():  
    webpage = input("register/login : ")
    if (webpage.lower() == "register"):
  
        val_user()
        
    elif(webpage.lower() == "login"):
        print("Login Page")
        login() 
    else:
        print("Please provide valid input \"register\" or \"login\"")
        website()
        
def log_pwd():  
    ln_fp = input("login/forgot_password : ")
    if (ln_fp.lower() == "forgot_password"):
        
        forgot_password()
        
        
    elif(ln_fp.lower() == "login"):
        print("Login Page")
        login()  
    else:
        print("Please provide valid input \"login\" or \"forgot_password\"")
        log_pwd()

website()   
