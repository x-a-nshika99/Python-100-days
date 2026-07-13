 

# play = input("do you want to give your name ? type 'y' for yes and 'n' for no ").lower()


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bender = 0
    max(bidding_dictionary)


    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bender :
            highest_bender = bid_amount 
            winner = bidder
            max(bids , key = bids.get)


    print("the winner is {winner} with a bid of ${highest_bidder}")

  



# todo 1 ask for user for input 
name = input("what is your name? :")
price = int(input("what is you bid? : $"))

bids ={}
# todo 2 save data into dict 

bids[name] = price

# todo 3 whether if new bids need to be added 
should_continue = input("are there any other bidders? type 'yes' or " \
"no .\n")

continue_bidding= True 
while continue_bidding:
    name = input("what is your name? :")
    price = int(input("what is you bid? : $"))
    bids[name] = price
    should_continue = input("are there any other bidders? type 'yes' or 'no' .\n".lower())
    if should_continue == "no" :
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes" :
        price("\n" * 20)



    


winner=print( max(bids , key = bids.get))



 
    

