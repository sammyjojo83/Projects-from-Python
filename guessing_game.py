
# Name:             Samantha Merton

# Section:          Engineering 102 556
# Assignment:   guessing game (lab 10 individual)
# Date:              10 November 2022



#####ORIGINAL######

#creating function to get lucky number
def get_lucky():
    flag = True # setting boolean to check for validity of lucky
    lucky = input('What is your guess?\n')
    while flag: #setting up loop to continue guessing until is false and lucky = int
        try:
            lucky = int(lucky)
            flag = False #update flag if lucky = int
        except:
            lucky=input("Bad input! Try again:\n") #tr-except statement
    return lucky # RETURN VALID INPUT
    

    
#setting up game function   
def game():
    num = 26
    print("Guess the secret number! Hint: it's an integer between 1 and 100...\n") #printing intial statment
    random = get_lucky()  #running function to get user input number
    i = 1#setting variable counter for guesses
    #seeting conditional statements 
    if random == num:
        print("You guessed it! It took you", i ,"guesses.\n")
        #each have nested loop to get new number
    while random != num:
        if random > num:
            print("Too high!\n")
            i += 1
            random = get_lucky()
            if random == num:
               print("You guessed it! It took you", i ,"guesses.\n") 
        if random < num:
            print("Too low!\n")
            i += 1
            random = get_lucky()
            if random == num:
                print("You guessed it! It took you", i ,"guesses.\n")
    return("") #setting empty return statement to eliminate None from printing
                
game()