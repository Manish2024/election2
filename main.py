no1 = input("Enter first nomineter's name :")
no2 = input("Enter second nomineter's name :")
vote1 =0
vote2 =0
total_vote = int(input("total numbers of voters :"))
m = int(total_vote)
voter_ID = []
while total_vote >0 :
    voter_ID.append(total_vote)
    total_vote = total_vote -1
x =0
while True :
    if len(voter_ID) >0 :
        voterid = int(input("Enter your voter id :"))
        if voterid in voter_ID:
            print("You are applicable for voting..")
            print("please wait....")
            voter_ID.remove(voterid)
            vote = int(input("Enter your nomineter code : "))
            x =x +1
            if vote == 1:
                vote1 = vote1 + 1
                print("Thanking you for voting :", no1)
            elif vote == 2:
                vote2 = vote2 + 1
                print("Thanking you for voting :", no2)
            else:
                print("Please Enter the code only show in the list at top")
        else:
            print("You are not applicable for voting ")
            print("Check your voter ID or you have already voted.")
    else :
        break
print("Result is here :")
if vote1 > vote2 :
    print("congratulation wineer is ", no1)
    print(no1,"won by ",int(vote1) - int(vote2),"votes")
elif vote1 == vote2 :
    print("their are same votes for nomineters ")
elif vote1 < vote2 :
    print("congratulation wineer is ", no2)
    print(no2, "won by ", int(vote2) - int(vote1), "votes")
print("total vote gived :", x)
print("thanks for voting ..")
print("best of luck for new prdhan.")