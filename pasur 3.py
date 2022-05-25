import random
import sys
model=["SPADE","DIAMOND","CLUB","HEART"]
it=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
def card(who):
    global model
    global it
    global all_
    global cor
    global me
    global computer
    global shuff
    global fica
    if len(all_)==0:
        for ap in model:
            for ap2 in it:
                all_.append([ap,ap2])
        for ap3 in me:
            nu=-1
            for ap4 in all_:
                nu+=1
                if ap3==ap4:
                    del all_[nu]
                    break
        for ap5 in computer:
            nu=-1
            for ap6 in all_:
                nu+=1
                if ap5==ap6:
                    del all_[nu]
                    break
        nu=-1
        for ap7 in all_:
            nu+=1
            if ap7==maca:
                del all_[nu]
                break
        shuff+=1
    try:
        ra=random.choice(all_)
        who.append(ra)
        for item in all_:
            if item!=ra:
                cor.append(item)
        all_=cor
        cor=[]
    except:
        fica="yes"
def pr(order="no"):
    print("_________________________________________")
    print(f"move:{rounds}")
    print(f"shuffle number: {shuff}")
    if pi!=0:
        print(f"pick number: {pi}")
    print("")
    print("")
    print(f"computer's cards left:  ( {len(computer)} )")
    print(f"your's cards left:  ( {len(me)} )")
    print("")
    print("")
    print("your cards:")
    for item in me:
        print("         "+"<"+item[0]+"   "+ item[1]+">")
    print("")
    print("")
    print("       ___________________")
    print("")
    print(f"<{maca[0]}   {maca[1]}> is on top from {fr}")
    if order!="no":                                 
        print(f"order is {order}")               
    print("_________________________________________")
st=0
print("hi","welcome to my program","this program is a card game like uno but it has some diffrences","hope you enjoy it","you have to write with caps lock",sep="\n" )
while True:
    A="no"
    fica="no"
    pi=0
    fr="shuffle"
    po="no"
    rounds=0
    maca=None
    shuff=0
    all_=[]
    cor=[]
    me=[]
    computer=[]
    seven=0
    nocar=0 
    pas=0
    if st==0:    
        print("suits : SPADE , DIAMOND , CLUB , HEART")
        print("types : A , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , J , Q , K")
        level=input("continue=1 exit=2  :")
    if level=="continue" or level=="CONTINUE" or level=="1": 
        tu_as=input("start => computer or you(me):")
        while True:
            if tu_as=="computer" or tu_as=="COMPUTER":
                turn="computer's"
                break
            elif tu_as=="you" or tu_as=="YOU" or tu_as=="me" or tu_as=="ME":
                turn="your"
                break
            elif tu_as=="exit" or tu_as=="2":
                sys.exit()
            else:
                tu_as=input("computer or you(me):")
        st=0    
        for ap in model:
            for ap2 in it:
                all_.append([ap,ap2])
        ra=random.choice(all_)
        while ra[1]=="7" or ra[1]=="J":
            ra=random.choice(all_)
        maca=ra
        for item in all_:
            if item!=ra:
                cor.append(item)
        all_=cor
        cor=[] 
        card(me)    
        card(me) 
        card(me) 
        card(me) 
        card(me) 
        card(computer) 
        card(computer) 
        card(computer) 
        card(computer) 
        card(computer) 
        rounds+=1
        pr()
        while True:
            A="no"
            pas=0
            canum=-1
            po="no"
            if fica=="yes":
                if len(computer)>len(me):
                    print("computer's cards:")
                    for itemmm in computer:
                        print("         "+"<"+itemmm[0]+"   "+ itemmm[1]+">")
                    print("you won")
                elif len(me)>len(computer):
                    print("computer's cards:")
                    for itemmm2 in computer:
                        print("         "+"<"+itemmm2[0]+"   "+ itemmm2[1]+">")
                    print("computer won")
                else:
                    print("computer's cards:")
                    for itemmm3 in computer:
                        print("         "+"<"+itemmm3[0]+"   "+ itemmm3[1]+">")
                    print("draw")
                break
            if len(me)==0:
                if maca[1]!="A":
                    for itemm in computer:
                        canum+=1
                        if itemm[1]=="7" and (itemm[0]==maca[0] or itemm[1]==maca[1]):
                            break
                    if itemm[1]=="7" and (itemm[0]==maca[0] or itemm[1]==maca[1]):
                        seven+=2
                        maca=itemm
                        del computer[canum]
                        rounds+=1
                        turn="your"
                        pi=0
                        fr="computer"
                        pr()
                    else:       
                        print("computer's cards:")
                        for itemm2 in computer:
                            print("         "+"<"+itemm2[0]+"   "+ itemm2[1]+">")
                        print("you won")
                        break
                canum=-1
            elif len(computer)==0:
                if maca[1]!="A":
                    print("computer is out of card")
                    print("you have to put a card that have 7 number in it")
                    print("if you dont have any card that possible to put it surrender")
                    ask_m=input("which card do you want to choose:")
                    print("_________________________________________")
                    while True:
                        canum=-1
                        for itemm3 in me:
                            canum+=1
                            if (itemm3[0]+"   "+itemm3[1]==ask_m or itemm3[0]+" "+itemm3[1]==ask_m) and itemm3[1]=="7" and (itemm3[0]==maca[0] or itemm3[1]==maca[1]):
                                break
                        if (itemm3[0]+"   "+itemm3[1]==ask_m or itemm3[0]+" "+itemm3[1]==ask_m) and itemm3[1]=="7" and (itemm3[0]==maca[0] or itemm3[1]==maca[1]):
                            turn="computer's"
                            fr="you"
                            for itemm4 in range(1,seven+3):
                                card(computer)
                            print(f"computer have {seven+2} more cards")
                            seven=0
                            maca=itemm3
                            del me[canum]
                            rounds+=1
                            fr="you"
                            pr()     
                            break 
                        elif ask_m=="surrender" or ask_m=="SURRENDER":
                            break
                        elif ask_m=="exit" or ask_m=="EXIT" or ask_m=="2":
                            sys.exit()
                        else:
                            ask_m=input("pls choose a card from your cards:")
                    if ask_m=="surrender" or ask_m=="SURRENDER":
                        print("computer won")
                        break
                canum=-1
            if turn=="your":
                if seven==0:
                    nocar=0
                    for item3 in me:
                        if item3[0]==maca[0] or item3[1]==maca[1] or item3[1]=="J":
                            None
                        else:
                            nocar+=1
                    if nocar==len(me):
                        card(me)
                        pas=1
                        print("you dont have any card that can put it on the top card")
                        rounds+=1
                        pr()
                ask_m=input("which card do you want to choose:")
                while True:
                    canum=-1
                    for item4 in me:
                        canum+=1
                        if (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="7" and (item4[0]==maca[0] or item4[1]==maca[1]):
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="J":
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="A" and (item4[0]==maca[0] or item4[1]==maca[1]):
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and (item4[0]==maca[0] or item4[1]==maca[1]):
                            break
                    if seven==0:
                        if (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="7" and (item4[0]==maca[0] or item4[1]==maca[1]):
                            seven+=2
                            maca=item4
                            del me[canum]
                            rounds+=1
                            fr="you"
                            pr()                                    
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="J":
                            rounds+=1
                            maca=item4
                            del me[canum]
                            order=input("choose your order:")
                            while True:
                                if order=="SPADE":
                                    fr="you"
                                    pr("SPADE")
                                    maca=["SPADE","=>order"]
                                    break
                                elif order=="DIAMOND":
                                    fr="you"
                                    pr("DIAMOND")
                                    maca=["DIAMOND","=>order"]
                                    break
                                elif order=="CLUB":
                                    fr="you"
                                    pr("CLUB")
                                    maca=["CLUB","=>order"]
                                    break
                                elif order=="HEART":
                                    fr="you"
                                    pr("HEART")
                                    maca=["HEART","=>order"]
                                    break
                                else:
                                    order=input("choose your order:")
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="A" and (item4[0]==maca[0] or item4[1]==maca[1]):
                            maca=item4
                            del me[canum]
                            rounds+=1
                            fr="you"
                            A="yes"
                            pr()
                            print("A is on top you have 1 more move")
                            print("_________________________________________")
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and (item4[0]==maca[0] or item4[1]==maca[1]):
                            maca=item4
                            del me[canum]
                            rounds+=1
                            fr="you"
                            pr()
                            break
                        elif ask_m=="exit" or ask_m=="EXIT" or ask_m=="2":
                            sys.exit()
                        elif (ask_m=="pick" or ask_m=="PICK") and pi<3:
                            pi+=1
                            card(me)
                            print("you have 1 more card")
                            rounds+=1
                            po="yes"
                            pr()
                            break
                        elif (ask_m=="pas" or ask_m=="PAS") and (pas==1 or pi!=0):
                            print("you pased")
                            break
                        else:
                            ask_m=input("pls choose a card from your cards:")
                    elif seven!=0:
                        if (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="7":
                            seven+=2
                            maca=item4
                            del me[canum]
                            rounds+=1
                            fr="you"
                            pr()
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and item4[1]=="J":
                            rounds+=1
                            for item5 in range(1,seven+1):
                                card(me)
                            print(f"you have {seven} more cards")
                            maca=item4
                            del me[canum]
                            order=input("choose your order:")
                            while True:
                                if order=="SPADE":
                                    fr="you"
                                    pr("SPADE")
                                    maca=["SPADE","=>order"]
                                    break
                                elif order=="DIAMOND":
                                    fr="you"
                                    pr("DIAMOND")
                                    maca=["DIAMOND","=>order"]
                                    break
                                elif order=="CLUB":
                                    fr="you"
                                    pr("CLUB")
                                    maca=["CLUB","=>order"]
                                    break
                                elif order=="HEART":
                                    fr="you"
                                    pr("HEART")
                                    maca=["HEART","=>order"]
                                    break
                                else:
                                    order=input("choose your order:")
                            seven=0
                            break
                        elif (item4[0]+"   "+item4[1]==ask_m or item4[0]+" "+item4[1]==ask_m) and (item4[0]==maca[0] or item4[1]==maca[1]):
                            for item5 in range(1,seven+1):
                                card(me)
                            print(f"you have {seven} more cards")
                            seven=0
                            maca=item4
                            del me[canum]
                            rounds+=1
                            fr="you"
                            pr()
                            break
                        elif ask_m=="exit" or ask_m=="EXIT" or ask_m=="2":
                            sys.exit()
                        elif ask_m=="pick" or ask_m=="PICK":
                            for item5 in range(1,seven+1):
                                card(me)
                            print(f"you have {seven} more cards")
                            seven=0
                            rounds+=1
                            po="yes"
                            pr()
                            break
                        else:
                            ask_m=input("pls choose a card from your cards:")
                if maca[1]!=7 and po=="no" and A!="yes":                          
                    turn="computer's"
                nocar=0
            elif turn=="computer's":
                if seven==0:
                    nocar=0
                    for item3 in computer:
                        if item3[0]==maca[0] or item3[1]==maca[1] or item3[1]=="J":
                            None
                        else:
                            nocar+=1
                    if nocar==len(computer):
                        card(computer)
                        print("computer doesnt have any card that can put it on the top card")
                        rounds+=1
                        pi=0
                        pr()
                    nocar=0
                    for item7 in computer:
                        if item7[0]==maca[0] or item7[1]==maca[1] or item7[1]=="J":
                            None
                        else:
                            nocar+=1
                    if nocar==len(computer):
                        print("computer pased")
                        pas=1 
                if pas==0:
                    ask_c=random.choice(computer)
                    while True:
                        if seven!=0:
                            for item5 in computer:
                                canum+=1
                                if item5[1]=="7":
                                    break
                            if item5[1]=="7":
                                seven+=2
                                maca=item5
                                del computer[canum]
                                rounds+=1
                                fr="computer"
                                pr()
                                break
                            else:
                                for item5 in range(1,seven+1):
                                    card(computer)
                                print(f"computer have {seven} more cards")
                                seven=0
                                rounds+=1
                                po="yes"
                                pr()
                                break
                        elif seven==0:
                            if ask_c[1]=="7" and (ask_c[0]==maca[0] or ask_c[1]==maca[1]):
                                seven+=2
                                maca=ask_c
                                for item5 in computer:
                                    canum+=1
                                    if ask_c==item5:
                                        del computer[canum]
                                rounds+=1
                                fr="computer"
                                pr()
                                break
                            elif ask_c[1]=="J":
                                rounds+=1
                                maca=ask_c
                                for item5 in computer:
                                    canum+=1
                                    if ask_c==item5:
                                        del computer[canum]
                                spade=0
                                diamond=0
                                club=0
                                heart=0
                                for item6 in computer:
                                    if item6[0]=="SPADE":
                                        spade+=1
                                    elif item6[0]=="DIAMOND":
                                        diamond+=1
                                    elif item6[0]=="CLUB":
                                        club+=1
                                    elif item6[0]=="HEART":
                                        heart+=1
                                if spade>=diamond  and spade>=heart and spade>=club:
                                    fr="computer"
                                    pr("SPADE")
                                    maca=["SPADE","=>order"]
                                elif diamond>=spade  and diamond>=heart and diamond>=club:
                                    fr="computer"
                                    pr("DIAMOND")
                                    maca=["DIAMOND","=>order"]
                                elif heart>=diamond  and heart>=spade and heart>=club:
                                    fr="computer"
                                    pr("HEART")
                                    maca=["HEART","=>order"]
                                elif club>=diamond  and club>=heart and club>=spade:
                                    fr="computer"
                                    pr("CLUB")
                                    maca=["CLUB","=>order"]
                                else:
                                    luck=random.choice("CLUB","SPADE","DIAMOND","HEART")
                                    fr="computer"
                                    pr(luck)
                                    maca=[luck,"=>order"]
                                spade=0
                                diamond=0
                                club=0
                                heart=0
                                break
                            elif ask_c[1]=="A" and (ask_c[0]==maca[0] or ask_c[1]==maca[1]):
                                maca=ask_c
                                for item5 in computer:
                                    canum+=1
                                    if ask_c==item5:
                                        del computer[canum]
                                rounds+=1
                                fr="computer"
                                A="yes"
                                pr()
                                print("A is on top computer has 1 more move")
                                print("_________________________________________")
                                break
                            elif ask_c[0]==maca[0] or ask_c[1]==maca[1]:
                                maca=ask_c
                                for item5 in computer:
                                    canum+=1
                                    if ask_c==item5:
                                        del computer[canum]
                                rounds+=1
                                fr="computer"
                                pr()
                                break
                            else:
                                canum=-1
                                ask_c=random.choice(computer)  
                if maca[1]!=7 and po=="no" and A!="yes":                          
                    turn="your" 
                nocar=0                      
                pi=0    
    elif level=="exit" or level=="EXIT" or level=="2":
        sys.exit()
    else:
        level=input("pls choose one of the items:")
        st=1