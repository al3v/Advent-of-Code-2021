listLength = int(input("Enter number of elements : "))

init_crab_positions = []
for i in range(0, listLength):
    elements = int(input('Enter crab positions : '))
    init_crab_positions.append(elements) 


candidate_locations = []
for i in range (min(init_crab_positions), max(init_crab_positions)+1): # Now candidate_locations has possible positions to align
    candidate_locations.append(i)

fuel_list = []
for i in range (0, len(candidate_locations)):
    for j in range (0, len(init_crab_positions)):
        fuel = abs(init_crab_positions[j] - candidate_locations[i])
        #print('position', init_crab_positions[j], 'to', candidate_locations[i], 'fuel is: ', fuel)
        fuel_list.append(fuel)


split_size = len(init_crab_positions)
fuel_splited = [fuel_list[x:x+split_size] for x in range(0, len(fuel_list), split_size)]

AllFuels = []
for i in range (0, len(fuel_splited)):
    total = sum(fuel_splited[i])
    AllFuels.append(total)
    print('the total cost of fuel for position:', candidate_locations[i], 'is:' , total)


pos = AllFuels.index(min(AllFuels)) #position of min(AllFuels)
print('The least fuel possible is:', min(AllFuels), 'that is provided by the position', pos)


