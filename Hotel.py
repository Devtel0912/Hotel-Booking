print("Welcome to The Hotel!")
print("Welcome to The home!")
print("Welcome to The home dev!")
nights = int(input("Number of Nights: "))
people = int(input("Number of People: "))

print("Room Types: \n(1)-Two Queen Beds\n(2)-One King Bed\n(3)-Queen Suite\n(4)-King Suit")
type = int(input("Select Type:"))

brunch = int(input("How many Brunches? "))
dinner = int(input("How many Dinners? "))
picnic = input("Picnic?")
snorkel = input("Snorkel?")
hike = input("Hike?")
boatdinner = input("Boatdinner?")


question = input("What Excites You?")

Age = int(input("How Old are u?")

def room_cost(type, nights):
    if type == 1:
        return 375 * nights
    elif type == 2:
        return 350 * nights
    elif type == 3:
        return 525 * nights
    elif type == 4:
        return 475 * nights
    
    
    
    
    
    
    
    
def meal_cost(brunch, dinner):
    sub = (brunch * 25) + (dinner * 75)
    grat = sub * 0.15
    return sub + grat
    
    
    
    
    
    
    

def excursion_cost(people, picnic, snorkel, hike, boatdinner):
    t = 0
    if picnic == 'y':
        t += 50
    if snorkel == 'y':
        t += 25 * people
    if hike == 'y':
        t += 17 * people
    if boatdinner == 'y':
        t += 200
    return t
         
    
         
         
         
         
rc = room_cost(type, nights)
mc = meal_cost(brunch, dinner)
ec = excursion_cost(people, picnic, snorkel, hike, boatdinner)
Total_Cost = rc + mc + ec
