import sys
initial_confirmation=input("Hi there, do you want to know some things about me? You will need to answer Yes or No.")
if initial_confirmation=="Yes":
    name=input("Great! First of all, my name is Antonio and I am 15 years old. How about you, what is your name?")
    print("Nice to meet you, "+name )
elif initial_confirmation=="No":
    print("Oh... OK. It is fine. Bye :(")
    sys.exit()
country=input("Next question, where are you from?")
print("Wow! "+country+" is a beautiful country. I almost forgot, I am from Spain")
animal=input("Final question, my favorite one: What animal do you like the most? I love cats.")
print("Good choice! "+animal+ " are the best.")
print("It is time to say goodbay. Thank you so much for giving me a try, you are the best. Consider leaving a comment :)")
sys.exit()



