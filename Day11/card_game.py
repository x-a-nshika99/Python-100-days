# 🔑 How this works:
# Deck setup → Numbers 2–10, face cards as 10, Ace as 11.
# Score calculation → If you bust with an Ace, it changes to 1.
# Gameplay loop → You choose to draw or stop.
# Dealer rules → Dealer must draw until reaching 17 or more.
# Result comparison → Win, lose, or draw.




# 👉 Try running this code in your Python editor. 
# It’s interactive — you’ll type y or n to decide whether to draw another card



import random

# Step 1: Create the deck (simplified)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  
# 10 appears 4 times (10, Jack, Queen, King), Ace = 11

# Step 2: Function to calculate score
def calculate_score(hand):
    score = sum(hand)
    # If score > 21 and there's an Ace (11), change Ace to 1
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

# Step 3: Deal initial cards
def deal_card():
    return random.choice(cards)

def play_blackjack():
    user_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        # Check if user already won or lost
        if user_score == 21 or dealer_score == 21 or user_score > 21:
            game_over = True
        else:
            # Ask user if they want another card
            user_choice = input("Type 'y' to get another card, 'n' to pass: ")
            if user_choice == "y":
                user_hand.append(deal_card())
            else:
                game_over = True

    # Dealer must draw until score >= 17
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

    # Step 4: Compare results
    if user_score > 21:
        print("You went over 21. You lose 😢")
    elif dealer_score > 21:
        print("Dealer went over 21. You win 🎉")
    elif user_score > dealer_score:
        print("You win 🎉")
    elif user_score < dealer_score:
        print("You lose 😢")
    else:
        print("It's a draw 🤝")

# Run the game
play_blackjack()
