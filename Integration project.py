# Joshua Paul - Integration Project
# Basketball trivia
# Questions taken out from https://www.usefultrivia.com/sports_trivia/basketball_trivia_index.html
name = input("What is your name? ")
age = int(input("What is your age? "))
#defining a function
#len() counts the charcaters of the name input
def participant():
    if len(name) < int(age):
        print("you are old enough to play")
    else:
        print("I'm not so sure how well you are going to do but lets start the game!")
#calls the function
participant()
print("Welcome to basketball trivia", age, "year old", name + "!")
print("This is going to be a NBA multiple choice game, after the question pops up")
print("and the 4 different answers show you will be asked to pick one")
print("A correct answer will award you 2 points")
#use of for, in and range functions
print("Before we start lets show some positive messages\n")
positiveness = ['good', 'relaxed','great', 'amazing', 'smart']
for x in range(len(positiveness)):
    print("I'm", positiveness[x])
print("\ndisclaimer: write down just the letter next to the answer, unless told otherwise")
print("Lets start with a practice round: ")
#practice question for user
#\n sets the print on the next line (skips a line)
wrong = "You are wrong"
right = "Correct"
print("\nWhat year is it?")
print("a. 2020\nb. 2019\nc. 3000\nd. 1840") 
practice_question = input("Answer: ")
#test if the input is the correct answer or not 
if  practice_question != "a":
    print(wrong)
else:
    print(right)
print("\nNow that we know how to work this, lest play the trivia game!")
print("It is 10 questions,\nGood Luck!\n")
#Trivia game starts
#start the game with a countdown
countdown = 11
while countdown>0:
    countdown -= 1
    print(countdown)
#The points awarded with short cut operator
score = 0
score += 2
#Question 1
print("\nWhat NBA player scored 100 points on March 2, 1962?")
print("a. Kareem Abdul-Jabbar\nb. Elgin Baylor\nc. Wilt Chamberlain\nd. Bill Russell") 
first_question = input("Answer: ")
if  first_question != "c":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 2
print("\nHow many games did Wilt Chamberlain foul out of during his 14 year NBA career?")
#addition
print("a. " + str(10+1))
#subtraction
print("b. " + str(2-2))
#Multiplication
print("c. " + str(47*2))
#Exponent
print("d. "+ str(5**2))
second_question = input("Answer: ")
if  second_question != "b":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 3
print("\nWho was the first teenager in NBA history to score 20+ points in 10 consecutive games?")
print("a. Zion Williamson\nb. Lebron James\nc. Luka Doncic\nd. Kobe Bryant") 
third_question = input("Answer: ")
if  third_question != "a":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 4
print("\nWhat are the Dallas Mavericks named after?")
print("a. Broadway Show\nb. Short Story\nc. TV Show\nd. Novel") 
fourth_question = input("Answer: ")
if  fourth_question != "c":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 5
print("\nWhich player holds the NBA record for most assists in a single game?")
print("a. John Stockton\nb. Scott Skiles\nc. Rajon Rondo\nd. Jason Kidd") 
fith_question = input("Answer: ")
if  fith_question != "b":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 6
print("\nWho was the first NBA player to shatter a backboard?")
print("a. Shaquille O'Neal\nb. Darryl Dawkins\nc. Gus Johnson\nd. Chuck Connors") 
sixth_question = input("Answer: ")
if  sixth_question != "d":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 7
print("\nWho was the first player in NBA history to make 400 three-pointers in a season?")
print("a. James Harden\nb. Dennis Scott\nc. Ray Allen\nd. Stephen Curry") 
seventh_question = input("Answer: ")
if  seventh_question != "d":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 8
print("\nWhat NBA player has won the most league MVPs?")
print("a. Kareem Abdul-Jabbar\nb. Lebron James\nc. Stephen Curry\nd. Michael Jordan") 
eigth_question = input("Answer: ")
if  eigth_question != "a":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 9
print("\nWho invented the game of basketball?")
print("a. Frank Mahan\nb. Abner Doubleday\nc. Walter Camp\nd. James Naismith") 
ninth_question = input("Answer: ")
if  ninth_question != "d":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 10
print("\nWhich NBA team plays at Madison Square Garden?")
print("a. Miami Heat\nb. Brooklyn Nets\nc. New York Knicks\nd. Golden State Warriors") 
tenth_question = input("Answer: ")
if  tenth_question != "d":
    print(wrong)
else:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 11
print("\nWhat player have made 200 3-pointers in 7 consecutive seasons?")
print("a. Klay Thompson\nb. Stephen Curry\nc. Ray Allen\nd. Reggie Miller")
eleventh_question = input("Answer: ")
if eleventh_question == "a":
    print(right)
    if right == "Correct":
        print(score, "Points")
elif eleventh_question == "b":
    print(right)
    if right == "Correct":
        print(score, "Points")
else:
    print(wrong + ", there was a 50% chance to get it right, both Klay and Stephen have accomplished this stat")
#Question 12
print("\nWhat has been the highest scroing game in NBA history by a single team?")
print("a. 200\nb. 190\nc. 186\nd. 196")
print("Write down the score of the game")
twelve_question = int(input("Answer: "))
if twelve_question > 186:
    print(wrong)
elif twelve_question == 186:
    print(right)
    if right == "Correct":
        print(score, "Points")
#Question 13
print("\nWhich team has retired Charles Barkley jersey number?")
print("a. 76ers\nb. Phoenix Suns\nc. Houston Rockets\nd. other")
thirteen_question = input("Answer: ")
#using OR either one is correct
if thirteen_question == "a" or "b":
    print(right + ", he has his jersey retired with the 76ers and the Phoenix Suns")
    if right == "Correct":
            print(score, "Points")
else:
    print(wrong)
#Question 14
print("\nLet's test some of your basketball knowledge")
print("\nWhat is the highest points awarded after one play?\nAnswer the following questions\n")
#Parameter def with the use of and
def get_bigger(number_one, number_two, number_three, number_four):
    if number_one and number_two and number_three < number_four:
        bigger = number_four
    elif number_one and number_two and number_four < number_three:
        bigger = number_three
    elif number_one and number_three and number_four < number_two:
        bigger = number_two
    else:
        bigger = number_one
    return bigger
def main():
    one_point = int(input("How many points are awarded after a technical foul? "))
    two_point = int(input("How many points is a layup? "))
    three_point = int(input("How many points is a show behind the arc? "))
    four_point = int(input("How many points is a three pointer plus the foul? "))  
    bigger_num = get_bigger(one_point, two_point, three_point, four_point)
    print(bigger_num, "points is the highest points awarded in one play")
#Call to main       
main()
#Ends Program
print("END OF THE GAME")
quit()




