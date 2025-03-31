print("........... welcome to the college predictor.............. ")
name = input("enter your name : ") 

print (f" {name} kindly enter your gate score ")

gate_score = input("enter your gate score : ")

match gate_score:
    case '850':
        print(" welcome to the IIT DELHI/ IIT BOMBAY")
    case '800':
        print("welcome top 7 IIts")
    case '750':
        print("welcome to top nits and new iits")
    case '650' :
        print("welcome to mid range nits")
    case _ : 
        print("fuck off")


    

        


