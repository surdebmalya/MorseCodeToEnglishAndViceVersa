##Making Morse Code Convertor
# .->1 bit
# _->3 bit
#left . , right ___
def MorseToEnglish(s):
    if s=='.':
        return 'E'
    elif s=='..':
        return 'I'
    elif s=='._':
        return 'A'
    elif s=='...':
        return 'S'
    elif s=='.._':
        return 'U'
    elif s=='....':
        return 'H'
    elif s=='..._':
        return 'V'
    elif s=='.._.':
        return 'F'
    elif s=='.....':
        return '5'
    elif s=='...._':
        return '4'
    elif s=='...__':
        return '3'
    elif s=='..___':
        return '2'
    elif s=='._.':
        return 'R'
    elif s=='.__':
        return 'W'
    elif s=='._..':
        return 'L'
    elif s=='.__.':
        return 'P'
    elif s=='.___':
        return 'J'
    elif s=='._._.':
        return '+'
    elif s=='.____':
        return '1'
    elif s=='_':
        return 'T'
    elif s=='_.':
        return 'N'
    elif s=='__':
        return 'M'
    elif s=='_..':
        return 'D'
    elif s=='_._':
        return 'K'
    elif s=='__.':
        return 'G'
    elif s=='___':
        return 'O'
    elif s=='_...':
        return 'B'
    elif s=='_.._':
        return 'X'
    elif s=='_._.':
        return 'C'
    elif s=='_.__':
        return 'Y'
    elif s=='__..':
        return 'Z'
    elif s=='__._':
        return 'Q'
    elif s=='_....':
        return '6'
    elif s=='_..._':
        return '='
    elif s=='_.._.':
        return '/'
    elif s=='__...':
        return '7'
    elif s=='___..':
        return '8'
    elif s=='____.':
        return '9'
    elif s=='_____':
        return '0'
    else:
        return 'Sorry'
def EnglishToMorse(s):
    if s=='E' or s=='e':
        return '.'
    elif s=='I' or s=='i':
        return '..'
    elif s=='A' or s=='a':
        return '._'
    elif s=='S' or s=='s':
        return '...'
    elif s=='U' or s=='u':
        return '.._'
    elif s=='H' or s=='h':
        return '....'
    elif s=='V' or s=='v':
        return '..._'
    elif s=='F' or s=='f':
        return '.._.'
    elif s=='5':
        return '.....'
    elif s=='4':
        return '...._'
    elif s=='3':
        return '...__'
    elif s=='2':
        return '..___'
    elif s=='R' or s=='r':
        return '._.'
    elif s=='W' or s=='w':
        return '.__'
    elif s=='L' or s=='l':
        return '._..'
    elif s=='P' or s=='p':
        return '.__.'
    elif s=='J' or s=='j':
        return '.___'
    elif s=='+':
        return '._._.'
    elif s=='1':
        return '.____'
    elif s=='T' or s=='t':
        return '_'
    elif s=='N' or s=='n':
        return '_.'
    elif s=='M' or s=='m':
        return '__'
    elif s=='D' or s=='d':
        return '_..'
    elif s=='K' or s=='k':
        return '_._'
    elif s=='G' or s=='g':
        return '__.'
    elif s=='O' or s=='o':
        return '___'
    elif s=='B' or s=='b':
        return '_...'
    elif s=='X' or s=='x':
        return '_.._'
    elif s=='C' or s=='c':
        return '_._.'
    elif s=='Y' or s=='y':
        return '_.__'
    elif s=='Z' or s=='z':
        return '__..'
    elif s=='Q' or s=='q':
        return '__._'
    elif s=='6':
        return '_....'
    elif s=='=':
        return '_..._'
    elif s=='/':
        return '_.._.'
    elif s=='7':
        return '__...'
    elif s=='8':
        return '___..'
    elif s=='9':
        return '____.'
    elif s=='0':
        return '_____'
    else:
        return 'Sorry'
#Main Loop
another='y'
while another=='y':
    print("\n Rules:")
    print(" =====")
    print(" Type 1 To Morse To English Conversion")
    print(" Type 2 To English To Morse Coversation")
    input_number=int(input("\n Enter Your Choice: "))
    while(input_number!=1 and input_number!=2):
        print(" Warning: You Type Other Than 1 Or 2")
        print(" Sorry!!! Please Enter Valid Input")
        print(" Type 1 To Morse To English Conversion")
        print(" Type 2 To English To Morse Coversation")
        input_number=int(input(" Enter Your Choice: "))
    if input_number==1:
        print("\n Input Pattern: ")
        print(" =============")
        print(" Type Two Adjacent Morse Codes With Space(s) Between Them")
        print(" Two Adjacent Letters Must Be Separated By <space>|<space>")
        input_string=input("\n Enter The String: ")
        final_input_string=input_string.split()
        output_string=''
        for i in range(len(final_input_string)):
            if final_input_string[i]=='|':
                output_string+=' '
            else:
                initial_output_string=MorseToEnglish(final_input_string[i])
                if initial_output_string!='Sorry':
                    output_string+=initial_output_string
                else:
                    print(" Warning: One Or More Than One Characters In Your String Have No Corresponding English Code!!!")
                    break
        print("\n Output: "+output_string)
    elif input_number==2:
        input_string=input("\n Enter The String: ")
        output_string=''
        for i in range(len(input_string)):
            if input_string[i]==' ':
                output_string+='   '
            else:    
                initial_output_string=EnglishToMorse(input_string[i])
                if initial_output_string!='Sorry':
                    output_string+=initial_output_string
                else:
                    print(" Warning: One Or More Than One Characters In Your String Have No Corresponding Morse Code!!!")
                    break
                output_string+=' | '
        print("\n Output Pattern: ")
        print(" ==============")
        print(" Each Character Of A Letter Is Separated By <space>|<space>")
        print(" Two Adjacent Letters Are Separated By Three Spaces, i.e. <space><space><space>")
        print("\n Output: "+output_string)
    print("\n Type y If You Want To Use It Again")
    print(" Type Any Other Key For Exit")
    another=input("\n Enter Your Choice: ")
print("\n Thanks For Using!!! See You Soon...")
