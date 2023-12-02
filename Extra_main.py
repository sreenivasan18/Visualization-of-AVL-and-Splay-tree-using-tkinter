def AVL_animate_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/avl animate code.txt","r")
    print(file.read())
                                    
    print("\n\nPress Enter To Continue")
                                
    input()
    
def AVL_insertion_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/avl in code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def AVL_deletion_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/avl del code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def AVL_extra_functions_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/avl add fun code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def Splay_animate_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/splay animate code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def Splay_insertion_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/splay in code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def Splay_splaying_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/splay splay code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def Splay_deletion_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/splay del code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def Splay_extra_functions_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/splay add fun code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
    
def Full_program_code():
    
    file = open("C:/Users/PAVAN/OneDrive/Desktop/Piccu/Package/full program code.txt","r")
    print(file.read())
                                        
    print("\n\nPress Enter To Continue")
                                
    input()
       
if __name__ == "__main__":
    
    import time
    import sys

    def print_letter_by_letter_1(sentence):
        for letter in sentence:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.10) 
            
    def print_letter_by_letter_2(sentence):
        for letter in sentence:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)
    
    sentences = [
        "NOTE : PRESS ENTER KEY THROUGHOUT THE PROCESS TO CONTINUE THE PROGRAM",
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nADVANCE DATA STRUCTURES PACKAGE",
        "\nTopic : Application Of AVL and SPLAY Tree Data Structures\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
        "\n\t\t\t\t\t\t\t\tTitle : ENCHANTED TREES",
        "\n\t\t\t\t\t\t\tThe Visual Symphony Of AVL And SPLAY Magic\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
        "\nProject By -",
        "\n\t\t  Pavanraj ( 22PT23 )",
        "\n\t\t  V Sreenivasan ( 22PT36 )"
    ]

    for sentence in sentences:
        print_letter_by_letter_1(sentence)
     
    input()
    choice = 0
    ch1 = 0
    ch2 = 0
    ch3 = 0
    ch4 = 0
    ch41 = 0
    ch42 = 0
    ch43 = 0
    temp = 0
    
    while(choice != 5):
        
        sentences = [
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "\nMENU"
            "\nPress 1 For Visualization Of Trees Via Animation"
            "\nPress 2 For Visualization Of Trees Via Explanation Through Console Text"
            "\nPress 3 For Performing Additional Functionalities Of Trees"
            "\nPress 4 For Exporting The Codes Of The Above Functions"
            "\nPress 5 To exit the interface"
        ]
        
        for sentence in sentences:
            print_letter_by_letter_2(sentence)
        
        choice=int(input("\nyour choice : "))
        
        if(choice == 1):
            
            while(ch1 != 3):
                
                sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\nYou Have Choosen Visualization Of Trees Via Animation"
                    "\n\n\nSUB MENU - VISUALIZATION VIA ANIMATION"
                    "\nPress 1 For Visualization Of AVL Tree"
                    "\nPress 2 For Visualization Of Splay Tree"
                    "\nPress 3 To Exit From The Sub-menu"
                ]
                
                for sentence in sentences:
                    print_letter_by_letter_2(sentence)
                
                ch1=int(input("\nyour choice : "))
                
                if(ch1 == 1):
                    print("\n\nWelcome to Visualization Of AVL Tree Via Animation")
                    print("Exit The Tkinter App/Web To Continue")
                    print("Press enter to continue")
                    input()
                    AVL_animate()
                    print("\n\nThank You , You Have Exited From The AVL Tree Visualization Via Animation")
                                    
                    print("\n\nPress Enter To Continue")
                    
                elif(ch1 == 2):
                    print("\n\nWelcome to Visualization Of Splay Tree Via Animation")
                    print("Exit The Tkinter App/Web To Continue")
                    print("Press enter to continue")
                    input()
                    Splay_animate()
                    print("\n\nThank You , You Have Exited From The Splay Tree Visualization Via Animation")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                elif(ch1 == 3):
                    print("\n\nThank you !! , You Have Exited From The Sub-Menu (Visualization Of Trees Via Animation)")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                else:
                    print("\n\nInvalid Choice !! Please Try Again")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                input()
                    
                    
        elif(choice == 2):
            
            while(ch2 != 6):
                
                sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\nYou Have Choosen Visualization Of Trees Via Explanation Through Console Text"
                    "\n\n\nSUB MENU - VISUALIZATION VIA EXPLANATION THROUGH CONSOLE TEXT"
                    "\nPress 1 For Visualization Of AVL Tree Insertion"
                    "\nPress 2 For Visualization Of AVL Tree Deletion"
                    "\nPress 3 For Visualization Of Splay Tree Insertion"
                    "\nPress 4 For Visualization Of Splay Tree Splaying A Node"
                    "\nPress 5 For Visualization Of Splay Tree Deletion"
                    "\nPress 6 To Exit From The Sub-menu"
                ]
                
                for sentence in sentences:
                    print_letter_by_letter_2(sentence)
                
                ch2=int(input("\nyour choice : "))
                
                if(ch2 == 1):
                    print("\n\nWelcome to Visualization Of AVL Tree Insertion")
                    print("Press enter to continue")
                    input()
                    AVL_insertion()
                    print("\n\nThank You , You Have Exited From The AVL Tree Insertion Visualization Via Explanation Through Console Text")
                                                        
                    print("\n\nPress Enter To Continue")

                elif(ch2 == 2):
                    print("\n\nWelcome to Visualization Of AVL Tree Deletion")
                    print("Press enter to continue")
                    input()
                    AVL_deletion()
                    print("\n\nThank You , You Have Exited From The AVL Tree Deletion Visualization Via Explanation Through Console Text")
                                                        
                    print("\n\nPress Enter To Continue")

                elif(ch2 == 3):
                    print("\n\nWelcome to Visualization Of Splay Tree Insertion")
                    print("Press enter to continue")
                    input()
                    Splay_insertion()
                    print("\n\nThank You , You Have Exited From The Splay Tree Insertion Visualization Via Explanation Through Console Text")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                elif(ch2 == 4):
                    print("\n\nWelcome to Visualization Of Splay Tree Splaying A Node")
                    print("Press enter to continue")
                    input()
                    Splay_splaying()
                    print("\n\nThank You , You Have Exited From The Splay Tree Splaying A Node Visualization Via Explanation Through Console Text")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                elif(ch2 == 5):
                    print("\n\nWelcome to Visualization Of Splay Tree Deletion")
                    print("Press enter to continue")
                    input()
                    Splay_deletion()
                    print("\n\nThank You , You Have Exited From The Splay Tree Deletion Visualization Via Explanation Through Console Text")
                                                        
                    print("\n\nPress Enter To Continue")
                        
                elif(ch2 == 6):
                    print("\n\nThank you !! , You Have Exited From The Sub-Menu (Visualization Of Trees Via Explanation Through Console Text)")
                                                        
                    print("\n\nPress Enter To Continue")
                  
                else:
                    print("\n\nInvalid Choice !! Please Try Again")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                input()
                    
            
        elif(choice == 3):
            
            while(ch3 != 3):
                        
                sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nMENU - PERFORMING ADDITIONAL FUNCTIONALITIES ON THE TREES"
                    "\nPress 1 For Additional Functions Relating AVL-Tree"
                    "\nPress 2 For Additional Functions Relating Splay-Tree"
                    "\nPress 3 To Exit From The menu"
                    ]
                        
                for sentence in sentences:
                    print_letter_by_letter_2(sentence)
                                                
                ch3=int(input("\nyour choice : "))
                        
                if(ch3 == 1):
                    print("\n\nWelcome to Additional Functions Relating AVL-Tree")
                    print("Press enter to continue")
                    input()
                    AVL_extra_functions()
                    print("\n\nThank You , You Have Exited From Additional Functions Relating AVL-Tree") 
                                                        
                    print("\n\nPress Enter To Continue")
                            
                if(ch3 == 2):
                    print("\n\nWelcome to Additional Functions Relating Splay-Tree")
                    print("Press enter to continue")
                    input()
                    Splay_extra_functions()
                    print("\n\nThank You , You Have Exited From Additional Relating Splay-Tree")  
                                                        
                    print("\n\nPress Enter To Continue")
                            
                if(ch3 == 3):
                    print("\n\nThank you !! , You Have Exited From The Menu PERFORMING ADDITIONAL FUNCTIONALITIES ON THE TREES")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                input()
  
            
        elif(choice == 4):
            
            while(ch4 != 5):
                
                sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\nYou Have Choosen Exporting The Codes Of The Above Functions"
                    "\n\n\nSUB MENU - EXPORTING THE CODE FOR THE ABOVE FUNCTION"
                    "\nPress 1 For Displaying Code For Animation"
                    "\nPress 2 For Displaying Code For Explanation"
                    "\nPress 3 For Displaying Code For Other Functionalities"
                    "\nPress 4 For Displaying Code For The Whole Program"
                    "\nPress 5 To Exit From The Sub-menu"
                ]
                
                for sentence in sentences:
                    print_letter_by_letter_2(sentence)
                    
                ch4=int(input("\nyour choice : "))
                
                if(ch4 == 1):
                    
                    print("Welcome to Displaying of the Code For Animation")
                    
                    while(ch41 != 3):
                        
                        sentences = [
                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                            "\n\n\nSUB MENU - CODES FOR ANIMATION"
                            "\nPress 1 For Visualization Of AVL Tree Codes"
                            "\nPress 2 For Visualization Of Splay Tree Codes"
                            "\nPress 3 To Exit From The Sub-menu"
                        ]
                        
                        for sentence in sentences:
                            print_letter_by_letter_2(sentence)
                        
                        ch41=int(input("\nyour choice : "))
                        
                        if(ch41 == 1):
                            print("\n\nWelcome to Displaying Of Codes Of Visualization Of AVL Tree Via Animation")
                            print("Press enter to continue")
                            input()
                            AVL_animate_code()
                            print("\n\nThank You , You Have Exited From Displaying Of Codes Of Visualization Of AVL Tree Via Animation")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        elif(ch41 == 2):
                            print("\n\nWelcome to Displaying Of Codes Of Visualization Of Splay Tree Via Animation")
                            print("Press enter to continue")
                            input()
                            Splay_animate_code()
                            print("\n\nThank You , You Have Exited From Displaying Of Codes Of Visualization Of Splay Tree Via Animation")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        elif(ch41 == 3):
                            print("\n\nThank you !! , You Have Exited From The Sub-Menu (Codes For Animation)")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        else:
                            print("\n\nInvalid Choice !! Please Try Again")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        input()
                    
                    print("\n\nThank You , You Have Exited From Displaying of the Code For Animation")
                                                        
                    print("\n\nPress Enter To Continue")
                    input()
                    

                elif(ch4 == 2):
                    
                    print("\n\nWelcome to Displaying of the Code For Explanation")
                    
                    while(ch42 != 6):
                        
                        sentences = [
                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                            "\n\n\nSUB MENU - CODES FOR EXPLANATION"
                            "\nPress 1 For Displaying Codes Of Visualization Of AVL Tree Insertion VIA Console"
                            "\nPress 2 For Displaying Codes OF Visualization Of AVL Tree Deletion VIA Console"
                            "\nPress 3 For Displaying Codes Of Visualization Of Splay Tree Insertion VIA Console"
                            "\nPress 4 For Displaying Codes Of Visualization Of Splay Tree Splaying A Node VIA Console"
                            "\nPress 5 For Displaying Codes Of Visualization Of Splay Tree Deletion VIA Console"
                            "\nPress 6 To Exit From The Sub-menu"
                        ]
                        
                        for sentence in sentences:
                            print_letter_by_letter_2(sentence)
                                                
                        ch42=int(input("\nyour choice : "))
                        
                        if(ch42 == 1):
                            print("\n\nWelcome to Displaying Codes Of Visualization Of AVL Tree Insertion VIA Console")
                            print("Press enter to continue")
                            input()
                            AVL_insertion_code()
                            print("\n\nThank You , You Have Exited From Displaying Codes Of Visualization Of AVL Tree Insertion VIA Console")
                                                                
                            print("\n\nPress Enter To Continue")

                        elif(ch42 == 2):
                            print("\n\nWelcome to  Displaying Codes OF Visualization Of AVL Tree Deletion VIA Console")
                            print("Press enter to continue")
                            input()
                            AVL_deletion_code()
                            print("\n\nThank You , You Have Exited From  Displaying Codes OF Visualization Of AVL Tree Deletion VIA Console")
                                                                
                            print("\n\nPress Enter To Continue")

                        elif(ch42 == 3):
                            print("\n\nWelcome to Displaying Codes Of Visualization Of Splay Tree Insertion VIA Console")
                            print("Press enter to continue")
                            input()
                            Splay_insertion_code()
                            print("\n\nThank You , You Have Exited From Displaying Codes Of Visualization Of Splay Tree Insertion VIA Console")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        elif(ch42 == 4):
                            print("\n\nWelcome to Displaying Codes Of Visualization Of Splay Tree Splaying A Node VIA Console")
                            print("Press enter to continue")
                            input()
                            Splay_splaying_code()
                            print("\n\nThank You , You Have Exited From Displaying Codes Of Visualization Of Splay Tree Splaying A Node VIA Console")
                                                                
                            print("\n\nPress Enter To Continue")

                        elif(ch42 == 5):
                            print("\n\nWelcome to Displaying Codes Of Visualization Of Splay Tree Deletion VIA Console")
                            print("Press enter to continue")
                            input()
                            Splay_deletion_code()
                            print("\n\nThank You , You Have Exited From Displaying Codes Of Visualization Of Splay Deletion VIA Console")
                                                                
                            print("\n\nPress Enter To Continue")

                        elif(ch42 == 6):
                            print("\n\nThank you !! , You Have Exited From The Sub-Menu (Codes For Explanation)")
                                                                
                            print("\n\nPress Enter To Continue")
                          
                        else:
                            print("\n\nInvalid Choice !! Please Try Again")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        input()
                    
                    print("\n\nThank You , You Have Exited From Displaying of the Code For Explanation")
                                                        
                    print("\n\nPress Enter To Continue")
                    input()
                    

                elif(ch4 == 3):
                    
                    print("\n\nWelcome to Displaying of the Code For Other Functionalities")
                    
                    while(ch43 != 3):
                        
                        sentences = [
                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                            "\n\n\nSUB MENU - CODES FOR OTHER FUNCTIONALITIES"
                            "\nPress 1 For Displaying Codes Of All Functions Relating AVL-Tree"
                            "\nPress 2 For Displaying Codes OF All Functions Relating Splay-Tree"
                            "\nPress 3 To Exit From The Sub-menu"
                        ]
                        
                        for sentence in sentences:
                            print_letter_by_letter_2(sentence)
                                                
                        ch43=int(input("\nyour choice : "))
                        
                        if(ch43 == 1):
                            print("\n\nWelcome to Displaying of All Functions Relating AVL-Tree")
                            print("Press enter to continue")
                            input()
                            AVL_extra_functions_code()
                            print("\n\nThank You , You Have Exited From Displaying of All Functions Relating AVL-Tree") 
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        if(ch43 == 2):
                            print("\n\nWelcome to Displaying of All Functions Relating Splay-Tree")
                            print("Press enter to continue")
                            input()
                            Splay_extra_functions_code()
                            print("\n\nThank You , You Have Exited From Displaying of All Functions Relating Splay-Tree")
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        if(ch43 == 3):
                            print("\n\nThank you !! , You Have Exited From The Sub-Menu (CODES FOR OTHER FUNCTIONALITIES)")  
                                                                
                            print("\n\nPress Enter To Continue")
                            
                        input()
                                
                        
                    print("\n\nThank You , You Have Exited From Displaying of the Code For Other Functionalities")
                                                        
                    print("\n\nPress Enter To Continue")
                    input()
                    
                elif(ch4==4):
                    print("\n\nWelcome to Displaying of the Code For Whole Program")
                    print("Press enter to continue")
                    input()
                    Full_program_code()
                    print("\n\nThank You , You Have Exited From Displaying of the Code For Whole Program")
                                                        
                    print("\n\nPress Enter To Continue")
                    input()
    
                elif(ch4 == 5):
                    print("\n\nThank you !! , You Have Exited From The Sub-Menu (Exporting The Codes Of The Above Functions)")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                    input()
                    
                  
                else:
                    print("\n\nInvalid Choice !! Please Try Again")
                                                        
                    print("\n\nPress Enter To Continue")
                    
                    input()
            
            
        elif(choice == 5):
            print("You Have Exited From The Interface , Thank You !!")
                                                
            print("\n\nPress Enter To Continue")
            
        
        else:
            print("invalid Input!! please select again")
                                                
            print("\n\nPress Enter To Continue")
            
        input()
