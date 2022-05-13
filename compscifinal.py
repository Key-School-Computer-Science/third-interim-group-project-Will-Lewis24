  
#game introduction
print("Welcome to Quest! My name is Clyde. I will be your guide on your quest. This is the beginning of your long and treacherous journey. You will face much adversity along the way, so you must choose a weapon to protect yourself.")
#requests name from user
name = input("Do tell me traveler, what is your name?")
#prints name
print("Now " + name + "," + "choose wisely.")

# requires user to choose a weapon
response = input('Select a weapon: sword, mace, or bow and arrow.')

#indicates outcomes/ set variables
outcome1 = "You have received excalibur."
outcome2 = "You have received a bow and arrow."
outcome3 = "You have received a mace."

# if statements & outcomes
if response == 'sword':
    print(outcome1)

if response == 'bow and arrow':
    print(outcome2)

if response == 'mace':
    print(outcome3)

#narration
print("Now that you have your first weapon, I will tell you about the journey ahead of you. You must trek up Grendel Mountain. Along the way, you will face many beasts and challenges. This is why you will need to keep your weapon close by at all times. You never know when evil will strike. Look, Over there! Someone is approaching us.") 

#requires user to make a choice
response2 = input('What do you choose: Attack or Approach with caution.')

#set more outcome variables
outcome4 = "Clyde- Oh no! That was a traveling Warlock. I heard he carries many potions and ailments. I guess you will have to continue on journey without his aid. Tough luck."
outcome5 = "Warlock Samson- Hello young adventurer, my name is Warlock Samson. I’m on my way to a Cytlleville to sell potions to adventurers. Since you are the first adventurer I have accounted for, I will give you one for free. Use it wisely young adventurer. I’ll be on my way."
reward = "Clyde- You have received a health potion."

# if statements & outcomes
if response2 == 'Attack':
    print(outcome4)

if response2 == 'Approach with caution':
    print(outcome5)
    
if response2 == 'Approach with caution':
    print(reward)

print("Now " + name +", in order to complete your quest and find the treasure, you'll have to make it to the top of this mountain")
print("Atop this mountain lies the terrible Troll, who guards the treasure that you seek with his life.")
print("In order to get to the troll, you must first cross the dreaded Thorendal River.# -*- coding: latin-1 -*-")
print("*as you approach the river, you see an old boat perched against an oak tree.*")
#this section is setting up my section of the story using basic print statements 
river_response = input("There are three possible ways to cross the river: 1: I will grant you with extra strength to swim across the river 2: Stay and camp on this side of the river. Maybe tomorrow there will be another way to cross. 3: use the old row boat to row across the river.")
#this provides the user to inout a number that will determine how their journey will go. 

if river_response == '1':
    print('*Clyde grants you with extra stregnth* You begin to swim across the river, then your stregnth starts to wear out. The shore is slowly getting closer, but you can barely move your arms. Just before you pass out, your feet touch sand. Congratulations! You made it across the Thorendal River.')
    #these if statements allow the user to decide their own adventure 
    print("*You struggle ashore and crawl onto the ground. You have little to no strength left. If you're going to survive, you'll need food quicly*")
    swim_response = input("How will you get food on this side of the River? 1: go hunting in the woods and hope you find some berries or wild animals. 2: Try eating some of the wild vegetation right on the shore. 3: Who needs food? Kepp going into the woods")
    if swim_response == '1':
        print('*You go searching for food in the woods, but suddenly, a wolf appears out of the shadows and strikes! You have no strength to run away. The wolf eats you.')
        print("I'm sorry, " + name + " your Quest is over.")
        
    if swim_response == '2':
        print("You try to eat some of the wild vegetation on the shore. It tastes pretty good, so you eat more. But soon, your stomach begins to hurt. Something isn't right. You begin to throw up uncontrollably. All the nutrients you gained from the vegetaion is drained from you. You can no longer stand. You pass out, giving into defeat.")
        print("I'm sorry, " + name + " your Quest is over.")
        
    if swim_response == '3':
        print("You begin to travel deeper into the woods without eating. You feel alright, but you know you can't do this forever. You start to stumble, and you collapse in the middle of the path.")
        print("I'm sorry, " + name + " your Quest is over.")
        
if river_response == '2': 
    print('*You decide to set up camp on the shore. The night is cold, but you survive. You wake up, and see that the river has frozen over. You pack up camp and walk across the river!*')
    #these repsonses will each set up their own reality in the story. the reality will be dictated by the users input
    print("On the other side of the river, your body temperature is dropping dramatically. You have to do something to keep warm.")
    ice_response = input("What will you do? 1: build a fire with the supplies on the shore. 2: try running around in circles really fast in hopes to get your blood pumping.")
    if ice_response == '1':
        print("You gather sticks to build your fire and you start to warm up. You make it through the night. In the morning you see in the distance a bridge.")
        print('You continue on your journey.')
        #Start of trial 3
        #while loop starting with first riddle
         #sets variables
        print("Clyde- It appears a troll blocks the bridge.")
        rid1 = True
        rid2 = True
        rid3 = True
        print("Troll- To have safe passage across the bridge, you must answer riddles that come in three.")
        while rid1 == True:
            riddle1 = input("Troll- Here is the first riddle: What, is the answer to this question.")
            ans1 = ' what'or' What'#first riddle answer
            rid2 = True#So nested 1 while loop will run
            rid3 = True#So nested 2 while loop will run
            if riddle1 == ans1:
                print('Troll- Good you have answered the first riddle of three.')
                while rid2 == True:#nested while loop 1
                    riddle2 = input("Troll- What dissapears as soon as you say its name?")
                    ans2 = 'silence' or 'Silence'#2nd riddle answer
                    if riddle2 == ans2:
                        print('Troll- Yet, again traveler you are correct.')
                        while rid3 == True:#nested while loop 2
                            riddle3 = input('Troll- Here is your final riddle: I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?')
                            ans3 = 'map' or 'Map'#3rd riddle answer
                            if riddle3 == ans3:
                                print('Troll- You have answered all of my riddles you may cross the bridge and complete your journey.')
                                print('Clyde- Congratulations you have found the Ancient Kings crown. You are now the crowned King of Grendel Mountain.')
                                rid1 = False#so the loop wont run again
                                rid2 = False#so nested loop wont run again
                                break#makes sure the code will not keep running after everything is done
                            else:
                                print('You must restart the riddles.')
                                rid1 = True#restarts loop
                                rid2 = False#allows for full restart
                                rid3 = False#allows for full restart
                    else:#relates to nested 1 
                        rid2 = False#now it wont run again
                        rid1 = True#restarts loop
                        print('Troll- You must restart the riddles.')
            else:
                print('Troll- You must restart the riddles')
    
    if ice_response == '2':
        print("I'm sorry but why did you choose this option, it's clearly the wrong choice. A dragon comes and eats you becuase you're beign so silly.")
        print("Tough Luck, " + name + " your Quest is over.")
        

if river_response == '3':
    print('*You take the rowboat and put it in the water. It is very rusty, and the paddles are short, but you manage to row all the way accross the river!*')
    print("You notice something off about the shore. It's hard to walk on almost as if... it's Quicksand! You're sinking fast, What will you do?")
    boat_response = input("1: try to climb out with you bare hands and feet. 2: Stay perfectly still, and pray the Clyde saves you.")
    if boat_response == '1':
        print("You struggle to get out, but you sink deeper and deeper into the sand. The sunlight vanishes above your head and you sink below the surface.")
        print("I'm sorry " + name + " your Quest is over.")
    if boat_response == '2':
        print("Sadly, Cylde is unable to help you. He's not a mean guy, but he was distracted by a butterfly and didn't hear your cries for help.")
        print("My bad, " + name + " your Quest is over.")
        

    

 