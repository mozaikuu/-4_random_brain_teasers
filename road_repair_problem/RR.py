import random
#TODO: import icecream?

# Variables
road_size = [1, 2, 3, 4, 5, 6, 7]
fixing_speed = [1, 2, 3, 4, 5, 6, 7]
area_of_effect = [1, 2, 3, 4, 5, 6, 7]
distance_from_road = [1, 2, 3, 4, 5,6, 7]
number_of_free_workers = [1, 2, 3, 4, 5, 6, 7] #TODO: make variables actually useful

# road_size = [1]
# fixing_speed = [1]
# area_of_effect = [1]
# distance_from_road = [1]
# number_of_free_workers = [3] # for testing purposes


def random_choice(list_of_stuff):
    return random.choice(list_of_stuff)


# road class
class road:
    count = 0
    def __init__(self):
        self.name = chr(97 + road.count)
        self.size = random_choice(road_size)
        road.count += 1
        
        self.chance_of_breakdown = 0.5
        
        if random.random() * 100 < self.chance_of_breakdown:
            self.state = 0
        else:
            self.state = 1
    
    def print_stats(self):
        print(f"road Name: {self.name}")
        print(f"road Size: {self.size}")
        print(f"road State: {self.state}")
    
    def __str__(self):
        return self.name  # Returns the city name when printed

    def __repr__(self):
        return f"road({self.name})"  # For debugging
        


# city class
class city:
    def __init__(self, name):
        self.name = name
        self.number_of_roads = 1 + random_choice(range(min_num_roads))
        self.neighboring_roads = roads.copy() #TODO: maybe roads should have only 2 endpoints? naaaaaaaaaaaaaaaaaah
        self.number_of_roads_to_remove = random.randint(0,len(self.neighboring_roads) - 1)
        
        while self.number_of_roads_to_remove > 0:
            self.neighboring_roads.remove(random_choice(self.neighboring_roads))
            self.number_of_roads_to_remove -= 1

            
    
    
    def print_stats(self):
        print(f"City: {self.name}")
        print(f"number_of_roads: {self.number_of_roads}")
        print(f"neighboring_roads: {self.neighboring_roads}")
    
    def __str__(self):
        return self.name  # Returns the city name when printed

    def __repr__(self):
        return f"City({self.name})"  # For debugging
        
        
        

class worker:
    def __init__(self, name, company_pos):
        self.name = name
        self.fixing_speed = random_choice(fixing_speed)
        self.curr_pos = company_pos

    def print_stats(self):
        print(f"worker: {self.name}")
        print(f"Fixing Speed: {self.fixing_speed}")
        print(f"Current position: {self.curr_pos}")
        
    def fix_road(self):
        pass
        # check the nearby roads
        # print(f"roads to fix: {self.curr_pos.neighboring_roads}")
        # print(f"nearby_roadsFix: {self.curr_pos.neighboring_roads[0].}")

        
    def move(self):
        
        # check the nearby roads
        print(f"nearby_roads: {self.curr_pos.neighboring_roads}")
        
        self.fix_road()
        
        available_cities = []
        
        for city in cities:
            for road in self.curr_pos.neighboring_roads:
                if road in city.neighboring_roads and self.curr_pos != city:
                    available_cities.append(city)
        available_cities = list(set(available_cities))  
        print(f"available cities to go to are: {available_cities}")
        
        
                
    
    
        

# Company class
class company:
    def __init__(self, name):
        self.name = name
        self.area_of_effect = random_choice(area_of_effect)
        self.distance_from_road = random_choice(distance_from_road) #TODO: FIX
        self.number_of_free_workers = random_choice(number_of_free_workers)
        self.city_of_origin = random_choice(cities)
        
        self.num_workers = random_choice(number_of_free_workers)
        self.workers = [worker(chr(65 + i) + f": {name}", self.city_of_origin) for i in range(self.num_workers)]
        
        
        
        # if road is broken then fix else go to next city and find new roads to fix (breadth search first bsf)
    def send_workers_out(self):
        # self.workers[0].move()
        for worker in self.workers:
            worker.move()
  
    def print_stats(self):
        print(f"Company: {self.name}")
        print(f"Area of Effect: {self.area_of_effect}")
        print(f"Distance from Road: {self.distance_from_road}") #TODO: FIX
        print(f"Number of Free Workers: {self.number_of_free_workers}")
        print(f"City of origin: {self.city_of_origin}")
        print(f"workers: {[worker.name for worker in self.workers]}")
        print("-" * 30)
        
        
        
        
# Game setup
def setup_roads():
    min_num_roads = int(input('input the minimum number of roads: '))
    roads = [road() for _ in range(min_num_roads)]
    return min_num_roads, roads

def setup_cities():
    num_cities = int(input('input the number of cities: '))
    cities = [city(chr(65 + i)) for i in range(num_cities)]  
    return cities

def setup_companies():
    num_companies = int(input('input the number of companies: '))
    # num_companies = int(input('input the number range of workers: '))
    companies = [company(chr(65 + i) + f"({i})") for i in range(num_companies)]  #TODO: add same company different branch later
    return companies

    
    

# Testing
if __name__ == "__main__":
    # creating instances automatically
    min_num_roads, roads = setup_roads()
    cities = setup_cities()
    companies = setup_companies()
    
    print(f"\n\t total number of cities {len(cities)} roads {len(roads)} companies {len(companies)}")

    #TODO: inherit .print_stats? actually no cuz they all print different stuff? idk yet
        
    print("\nCities:")
    for c in cities:
        c.print_stats()
    
    print("\nCity Roads:")
    for c in cities:
        print(c.neighboring_roads)
        
    print("\nCompanies:")
    for comp in companies:
        comp.print_stats()
        
    print("\nWorkers:")
    for comp in companies:
        for worker in comp.workers:
            worker.print_stats()
            
    companies[0].send_workers_out()
    
    # loop on all roads and if all roads are fixed print the data
            
#TODO: next add worker functionality