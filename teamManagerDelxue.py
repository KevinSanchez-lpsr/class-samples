class Players(object):
    def __init__(self, name, age, goals):
    	self.name = name
    	self.age = age
        self.goals = goals
	self.jerseynumber = jerseynumber
	self.position = position
    
    def printStats(self):
      print("Name:" + self.name)
      print("Age:" + str(self.age))
      print("Goals:" + str(self.goals))
      print("Jersey Number:" + str(self.jerseynumber))
      print("Position:" + self.position)	

def saveTeam(list, filename):
	file = open(filename, "a")
	for player in list:
		file.write(player.name + " " + str(player.age) + " " + str(player.goals) + " " + str(player.jerseynumber) + " " + player.position + "/n")
	
	file.close()	
 
def loadTeam(filename):
	list = []
	flie = open(filename, "r")
	a = file.readline()
	while a:
		a.split()
		list.append(Player(player[0], player[1], player[2], player[3], player[4]))
		a = file.readline()
	file.close()
	return list


print("Welcome to  Team Manager Deluxe! Please select an option.")
print("Press (1) to make a new team.")
print("Press (2) to load an existing team")
choice = raw_input()

if choice == "2":
	print(" What's the file  name of your existing team? Enter with .tmd extention please.")
	filename = input()
	list = loadTeam(filename)

else:
	list = [] 

while choice != "0":
	print("Press (1) to add a player to the team.")
	print("Press (2) to see your players.")
	print("Press (3) to save players.")
print("Press (4) to quit your job.")

if choice == "1":
    print("You selected to add a player")
    print("Enter your player's name:")
    name = raw_input()
    print("Enter your player's age:")
    age = raw_input()
    print("Enter the amount of goals your player made:")
    goals = raw_input()
    print("Enter your player's jersey number:")
    jerseynumber = raw_input()
    print("Enter your player's position") 
    position = raw_input()
    myPlayers.append(Player(name, age, goals, jerseynumber, position))
    print("Your player has been made. Congrats!")
     
	print("Press (1) to add a player to the team.")
        print("Press (2) to see your players.")
        print("Press (3) to save players.")
        print("Press (4) to quit your job.")


  elif choice == "2":
      print("Here is your team and their stats.")
      for player in myPlayers:
        player.printStats()

  elif choice == "3
      print("Name your file/team:")
	filename = input()
	saveTeam(list, filename)  
  choice = raw_input()

