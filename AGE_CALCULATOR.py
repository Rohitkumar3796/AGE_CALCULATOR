# AGE CALCULATOR
import datetime
todays_date=datetime.date.today()
def Age_2090(): #Function define
    BirthYear=input("enter the age or birth date") #take input of your birth year
    #here i use if condition because if if want to know my age only
    if len(BirthYear)==2:
        if int(BirthYear)<125:
            its_age=True
            print(BirthYear,its_age)
    #here i use else block for year
    elif int(BirthYear)>1900 and int(BirthYear)<todays_date.year:
        its_age=True
        now_age=2021-int(BirthYear)
        print('your age is ',now_age)
    else:
        print("you entered wrong age")
        print("Try again")
Age_2090()