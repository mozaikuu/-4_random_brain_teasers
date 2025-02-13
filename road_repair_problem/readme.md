i was in the bus one day and was wondering who fixes all the roads and what i thought about was the gov and private companies.

since there are private companies i wondered how many were there and the optimal amount of them we need depending on the road "area and number of roads", "fixing speed", "area of effect", "distance from road", "number of free workers"

# Variables (made up)

"area and number of roads" = length, width and number of lanes that need fixing and how many roads need fixing in that block
"fixing speed" = efficiency of workers
"area of effect" = how much space does the company occupy
"number of free workers" = how many workers in the company
"distance from road" = distance from company to road and back

# Objective

-  [ ] find the optimal number of companies
-  [ ] visualize the problem
-  [ ] calculate amount of revenue lost due to idling
-  [ ] figure out the ideal amount of companies and workers based on previous variables
-  [ ] maybe simulate monopoly later idk

# Rules

-  [ ] Companies cant send out fixing workers unless they go back to company after finishing the job
-  [ ] amount of workers increases area of effect
-  [ ] workers must be idle
-  [ ] if job requires more than 8 hours calculate the trips taken accordingly
-  [ ] big roads can take more than one worker from the same company
-  [ ] roads degrade over random amounts of time
-  [ ] one seconds equals 1 month
-  [ ] broken roads increase travel time by 1.5x

# Loop

-  [ ] companies send workers
-  [ ] workers travel
-  [ ] workers fix
-  [ ] workers go back to company
-  [ ] repeat
