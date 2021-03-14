
Member_detail = {}
Regimen_for_All_Member = {}


class Member:
    @classmethod
    def Add_Member(cls):
        Person = {}
        Name = input("Enter Member Name -")
        Age = input("Enter Member Age -")
        Gender = input("Enter Member Gender -")
        Mobile_no = input("Enter Member Mobile_no. -")
        Email = input("Enter Member Email -")
        BMI = input("Enter Member BMI(Body Mass Index)-")
        Month = input("Enter Membership Duration"
                      " Month 1,3,6 and 12 -")
        Person["Name"] = Name
        Person["Age"] = Age
        Person["Gender"] = Gender
        Person["Mobile_no"] = Mobile_no
        Person["Email"] = Email
        Person["BMI"] = BMI
        Person["Duration of Membership Month"] = Month
        Member_detail[Mobile_no] = Person
        Regimen_for_All_Member[Mobile_no] = Member.Regimens(BMI)

    @classmethod
    def Details(cls, number):
        if number in Member_detail:
            user = Member_detail[number]
            print("Name                         - ", user["Name"])
            print("Age                          - ", user["Age"])
            print("Gender                       - ", user["Gender"])
            print("Mobile_no                    - ", user["Mobile_no"])
            print("Email                        _ ", user["Email"])
            print("BMI                          - ", user["BMI"])
            print("Duration of Membership month - ", user["Duration of Membership Month"])

    @classmethod
    def DeleteMember(cls, x):
        del Member_detail[x]

    @classmethod
    def Regimens(cls, BMI):
        if int(BMI) < 18.5:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Rest",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Rest", "Sun": "Rest"}
        elif int(BMI) < 25:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio/Abs",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Legs", "Sun": "Rest"}
        elif int(BMI) < 30:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Abs/Cardio",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Legs", "Sun": "Cardio"}
        else:
            regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio",
                                "Thu": "Back", "Fri": "Triceps", "Sat": "Cardio", "Sun": "Cardio"}
        return regimens_details


while True:
    x = input("Press 1 for SUPER-USER \nPress 2 for Member \n--")
    choose_option = 100
    if x == "1":
        print("  WELCOME SUPER-USER  ")
        while choose_option != "0":
            choose_option = input("Press 1 for create Member \nPress 2 for view Member "
                                  "\nPress 3 for Delete Member \nPress 4 for Update Member "
                                  "\nPress 5 for Create Regimen \nPress 6 for View Regimen "
                                  "\nPress 7 for Delete Regimen \nPress 8 for Update Regimen \n"
                                  "Press 0 for Exit from super-user Group\n--")
            if choose_option == "1":
                Member.Add_Member()
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "2":
                mobile_number = input("Enter Member Mobile no-\n--")
                if mobile_number in Member_detail:
                    Member.Details(mobile_number)
                else:
                    print("Not Found Details  !!!")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "3":
                Enter_no_to_delete = input("Enter Mobile Number to Delete Member Details-\n--")
                if Enter_no_to_delete in Member_detail:
                    Member.DeleteMember(Enter_no_to_delete)
                    del Regimen_for_All_Member[Enter_no_to_delete]
                    print("Member details was deleted...")
                else:
                    print("Mobile Not Present in Database...")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "4":
                process = input("0 for update details \n1 for Extend Member \n2 for Delete Member-\n--")
                number = input("Enter Member Mobile Number -\n--")
                if process == "0":
                    input1 = input("What you want to update- Name, Age, Gender, Email, BMI, Month [case sensitive]\n"
                                   "**mobile number would not to changed***\n--")
                    Member_detail[number][input1] = input("Enter changes-\n--")
                elif process == "1":
                    Member.Add_Member()

                elif process == "2":
                    if number in Member_detail:
                        conform = input(" yes for delete-\n--")
                        if conform == "yes":
                            Member.DeleteMember(number)
                            print("Details of Member was DELETED ...")
                        else:
                            print("Member Details not be DELETED !!!")
                    else:
                        print("Invalid Mobile Number Enter by You")
                else:
                    print("YOU CHOOSE INVALID OPTION !!!")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "5":
                dict_day = {}
                Enter_number = input("Enter Mobile Number of Member -\n--")
                list_of_day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                if Enter_number in Regimen_for_All_Member:
                    for i in list_of_day:
                        for j in range(1, 2):
                            dict_day[i] = input(f"{i} Regimen - ")
                else:
                    print("This number don't have Membership!!!")
                Regimen_for_All_Member[Enter_number] = dict_day
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "6":
                Input = input("Enter Member Mobile Number-\n--")
                if Input in Regimen_for_All_Member:
                    for key in Regimen_for_All_Member[Input]:
                        print(key, "-", Regimen_for_All_Member[Input][key])
                else:
                    print("Regimen not found for this member")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "7":
                Input2 = input("Enter Member Mobile Number -\n--")
                if Input2 in Regimen_for_All_Member:
                    del Regimen_for_All_Member[Input2]
                    print("Regimen is DELETED for this Member")
                else:
                    print("Regimen is Not present in Database")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "8":
                Input3 = input("Enter Member Mobile Number-\n--")
                if Input3 in Regimen_for_All_Member:
                    Input4 = int(input("Enter Total Number of day you want to change Regimen -\n--"))
                    for i in range(1, (Input4 + 1)):
                        q = input("Enter day as like Sun, Mon, Tue, Wed, Thu, Fri, Sat - \n--")
                        r = input(f"Enter Regimen for {q} day -\n")
                        Regimen_for_All_Member[Input3][q] = r
                else:
                    print("Regimen not found (you delete it or not have Membership)")
                for_pass = input("Press 'Enter' for next - ")

            else:
                if choose_option != "0":
                    print("Invalid Input!!!")
                else:
                    print("Exit!!!")
            print()

    elif x == "2":
        print("  WELCOME MEMBER  ")
        number = input("Enter your Mobile Number -\n--")
        while choose_option != "0":
            choose_option = input("Press 1 for My Regimen \nPress 2 for My Profile "
                                  "\nPress 0 for Exit from Member Group!!! \n--")
            if choose_option == "1":
                if number in Regimen_for_All_Member:
                    for key in Regimen_for_All_Member[number]:
                        print(key, "-", Regimen_for_All_Member[number][key])
                else:
                    print("Regimen Not Found For You")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "2":
                if number in Member_detail:
                    Member.Details(number)
                else:
                    print("Member Details Not Found.")
                for_pass = input("Press 'Enter' for next - ")

            elif choose_option == "0":
                print("Exit!!!")
            else:
                print("Invalid Input Enter By You")
            print()
    else:
        print("Invalid Input!!")