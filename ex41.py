#!/usr/bin/python
from sys import exit
from random import randint

def death():
	quips = ["you died. you kinda suck at this.", 
		"Nice job, you died ...jackass.", 
		"such a luser.", 
		"I have a small puppy that's better at this."]
	print quips[randint(0,len(quips)-1)]
	exit(1)

def central_corridor():
	print "the gothons of planet percal #25 have invaded your ship and destroyed"
	print "your entire crew, you are the last surviving member and your last"
	print "mission is to get neutron destruct bomb from the weapons armory,"
	print "put it in the bridge, and blow the ship up after getting into an"
	print "escape pod."
	print "\n"
	print "you're running down the central corridor to the weapons armory when"
	print "a gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. he's blocking the door to the"
	print "armory and about to pull a weapon to blast you."

	action = raw_input("> ")
	
	if action == "shoot!":
		print "quick on the draw you yank out your blaster and fire it at the gothon."
		print "his clown costume is flowing and moving around his body, which throws"
		print "off your aim, your laser hits his costume but misses him entirely. this"
		print "completely ruins his brand new costume his mother bought him, which"
		print "makes him sly into an insane rage and blast you repeatedly in the face until"
		print "you are dead. then he eates you."
		return 'death'

	elif action == "dodge!":
		print "like a world class boxer you dodge, weave, slip and slide right"
		print "as the gothon's blaster cranks a laser past your head."
		print "in the middle of your artful dodge your foot slips and you"
		print "bang your head on the metal wall and pass out."
		print "you wake up shortly after only to die as the gothon stomps on"
		print "your head and eats you."
		return 'death'

	elif action == "tell a joke":
		print "lucky for you they made you learn gothon insults in the academy."
		print "you tell the one gothon joke you know:"
		print "lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
		print "the gothon stops, tries not to laugh, then busts out laughing and can't move."
		print "While he's laughing you run up and shoot him square in the head"
		print "putting him down, then jump through the weapon armory door."
		return 'laser_weapon_armory'
	else:
		print "DOES NOT COMPUTE!"
		return 'central_corridor'

def laser_weapon_armory():
	print "you do a dive roll into the weapon armory, crouch and scan the room"
	print "for more gothons that might be hiding. it's dead quiet, too quiet."
	print "you stand up and run to the far side of the room and find the"
	print "neutron bomb in its container. there's a keypad lock on the box"
	print "and you need the code to get the bomb out. if you get the code"
	print "wrong 10 times then the lock closes forever and you can't"
	print "get the bomb. the code is 3 digits."
	
	code ="%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
	guess = raw_input("[keypad]> ")
	guesses = 0
	while guess != code and guesses < 10:
		print "bzzzzeddd!"
		guesses += 1
		guess = raw_input("[keypad]> ")
	
	if guess == code:
		print "the container clicks open and the seal breaks, letting gas out."
		print "you grab the nuetron bomb and run as fast as you can to the"
		print "bridge where you must place it in the right spot."
		return 'the_bridge'

	else:
		print "the lock buzzes"
		print "melting sound"
		print "you decide to sit there"
		print "ship from their ship and you die."
		return 'death'

def the_bridge():
	print "you burst onto the bridge"
	print "under your arm"
	print "take control of the ship"
	print "clown costume than the last"
	print "weapons out yet"
	print "arm and don't want to set it off."
	
	action = raw_input("> ")
	if action == "throw the bomb":
		print "throw the bomb at the group of gothons"
		print "and make a leap for the door."
		print "gothon shoots you"
		print "as you die you see another gothon"
		print "the bomb"
		print "it goes off"
		return 'death'
	elif action =="slowly place the bomb":
		print "you point your blaster at the bomb"
		print "and the gothons put their hands up and start to sweat"
		print "you inch"
		print "place the bomb on the floor"
		print "you jump back"
		print "and blast the lock"
		print "now that the bomb is placed"
		print "get off"
		return 'escape_pod'
	else:
		print "does not compute!"
		return "the bridge"
def escape_pod():
	print "rush"
	print "escape"
	print "clear of"
	print "interference"
	print "pick one to take"
	print "have no time to look"
	print "do you take?"
	
	good_pod = randint(1,5)
	guess = raw_input("[pod #]> ")
	if int(guess) != good_pod:
		print "jump into pod %s" % guess
		print "the pod escape"
		print "implodes"
		print "into jam jelly."
		return 'death'
	else:
		print "jump into pod %s" % guess
		print "slides"
		print "planet below"
		print "back and see"
		print "bright star"
		print "time. you won!"
		exit(0)
ROOMS = {
	'death': death,
	'central_corridor': central_corridor,
	'laser_weapon_armory': laser_weapon_armory,
	'the_bridge': the_bridge,
	'escape_pod': escape_pod
}


def runner(map, start):
	next = start
	
	while True:
		room = map[next]
		print "\n-----------"
		next = room()
runner(ROOMS, 'central_corridor')
