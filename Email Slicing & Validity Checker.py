
# EMAIL SLICING & VALIDDITY CHECKING......
def part_1(): # GET INPUT AND ASSIGN PARTS IN TO  EACH VARIBLES

    global get_mail
    get_mail = input("Type Your Email : ")

    global set_1
    global set_2
    global set_3
    global set_4
    global set_5
    global set_6
    global set_7

    if len(get_mail) >= 15:
        set_1 = get_mail[0:3]
        set_2 = get_mail[-3:]
        set_3 = get_mail[3]
        set_4 = get_mail[-4]
        set_5 = get_mail[-10:-4]
        set_7 = get_mail[4:-4]

    else:
        set_1 = ""
        set_2 = ""
        set_3 = ""
        set_4 = ""
        set_5 = ""

def part_2(): # CHECK EACH PARTS VALIDDITY ONE BY ONE

    part_1()

    global val_d_1
    global val_d_2
    global val_d_3
    global val_d_4
    global val_d_5

    val_d_1 = False
    val_d_2 = False
    val_d_3 = False
    val_d_4 = False
    val_d_5 = False


    count = 0
    for i in set_7:
        if i == "@":
            count += 1

        else:
            continue


    if set_1.lower() == "www":
        val_d_1 = True

        if set_2.lower() == "com":
            val_d_2 = True

            if set_3.lower() == ".":
                val_d_3 = True

                if set_4.lower() == ".":
                    val_d_4 = True

                    if set_5.lower() == "@gmail" and count == 1 :
                        val_d_5 = True

def part_3(): # DISPLAY EACH PARTS & VALIDDITY

    part_2()

    if val_d_1 and val_d_2 and val_d_3 and val_d_4 and val_d_5 == True:
        print("-------Information About Email Address-------")
        print("                                                ")
        print(f'          Protocol     :-------> {set_1}')
        print(f'          Account name :-------> {set_7}')
        print(f'          Domain Name  :-------> {set_2}')

    else:
        print(".\n.\n.")
        print("Ops Invalid Email Address !")

part_3() # CALLING TO THE FUNCTION.........