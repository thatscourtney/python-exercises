import random
name = "Gladys"
question = "Should I invest in leather pants?"
answer = ""

random_number = random.randint(1,10)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
  
elif random_number == 2:
  answer = "It is decidely so"

elif random_number == 3:
  answer = "Without a doubt"

elif random_number == 4:
  answer = "Reply hazy, try again"

elif random_number == 5:
  answer = "Ask again later"

elif random_number == 6:
  answer = "Better not tell you now"

elif random_number == 7:
  answer = "My sources say no"

elif random_number == 8:
  answer = "Outlook not so good"

elif random_number == 9:
  answer = "Very doubtful"

elif random_number == 10:
  answer = "Girl, I have no idea. Take agency over your life and stop bothering me with your human weakness."

else: 
  print ("Error")

print(name, "asks: ", question)
print("Magic 8-Ball's answer: ", answer)
