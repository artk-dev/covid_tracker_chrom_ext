def solution(aircraftEmissions, flightItineraries, origin, destination):
    found_origin = False
    found_dest = False
    distance = None
    aircraftType = None

    #Let's start by scanning the origins and destinations in the itenararies
    for item in flightItineraries:
        dash_counter = 0
        
        #Loop through each letter in each itinerary and separate origin and destination
        scanned_word = ''

        for i in range(len(item)):
            if item[i] == '-':
                if dash_counter<1:
                    dash_counter+=1
                #If the first word is origin clear scanned word and continue else break this loop
                    if scanned_word == origin:
                        scanned_word = ''
                        found_origin = True
                    else:
                        scanned_word = ''
                        break
                #if the second word is destination clear scanned word and continue else break this loop
                elif dash_counter<2:
                    if scanned_word == destination:
                        scanned_word = ''
                        found_dest = True
                    else:
                        scanned_word = ''
                        break
                elif dash_counter<3:
                    distance = scanned_word
                    scanned_word = ''
                scanned_word = ''
            else:    
                scanned_word+=item[i]
                aircraftType = scanned_word
        
    if found_origin==True and found_dest==True:
        return find_emission(aircraftEmissions, aircraftType, distance)
    else:
        return 0
  
  #Funcion to calculate total emission on a route
def find_emission(aircraftEmissions, aircraftType, distance):
    emission_rate = None

    #Loop through each emission_set
    for item in aircraftEmissions:
        dash_counter = 0
        scanned_word = ''
        #Loop thru each letter in emission_set
        for i in range(len(item)):
            if item[i]=='-':
                if scanned_word != aircraftType:
                    break
                scanned_word = ''
        scanned_word+=item[i]
        emission_rate = scanned_word

    return emission_rate*distance
    	