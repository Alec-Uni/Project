#This is where the user selects what type of venue
import keyboard

#Get location
latitude = 40.73359624
longitude = -74.00313914


#User Input Selection
    #Bar/Restaurant
    #Museums/Galleries
    #Music Venues

while True:
    if keyboard.read_key() == "1":
        print("Searching for Bars and Restaurants... \n \n")

        #Call function to use DT for Bars and Restaurants
        #print("We've found the following venues" \n + List of first 10 results)
    elif keyboard.read_key() == "2":
        print("Searching for Museums and Galleries... \n \n")
        
        #Call function to use DT for Museums and Galleries
        #print("We've found the following venues" \n + List of first 10 results)
    elif keyboard.read_key() == "3":
        print("Searching for Music Venues... \n \n")

        #Call function to use DT for Music Venues
        #print("We've found the following venues" \n + List of first 10 results)
    break


#Add Ranking? More check ins make it rank higher