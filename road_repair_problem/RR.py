import random
#TODO: import icecream?

# Variables
# road_size = [1, 2, 3, 4, 5, 6, 7]
# fixing_speed = [1, 2, 3, 4, 5, 6, 7]
# area_of_effect = [1, 2, 3, 4, 5, 6, 7]
# distance_from_road = [1, 2, 3, 4, 5,6, 7]
# number_of_free_workers = [1, 2, 3, 4, 5, 6, 7] #TODO: make variables actually useful

road_size = [1]
fixing_speed = [1]
area_of_effect = [1]
distance_from_road = [1]
number_of_free_workers = [1] #TODO: make variables actually useful


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
        print(f"Road Size: {self.size}")
        print(f"Road State: {self.state}")
        


# city class
class city:
    def __init__(self, name):
        self.name = name
        self.number_of_roads = 1 + random_choice(range(min_num_roads))
        self.neighboring_roads = []
        self.number_of_roads_copy = self.number_of_roads
        self.roads_copy = [r.name for r in roads]
        
        while self.number_of_roads_copy > 0:
            choice = random_choice(self.roads_copy)
            self.neighboring_roads.append(choice)
            self.roads_copy.remove(choice)
            self.number_of_roads_copy -= 1
        
    
    
    def print_stats(self):
        print(f"City: {self.name}")
        print(f"number_of_roads: {self.number_of_roads}")
        print(f"neighboring_roads: {self.neighboring_roads}")
        
        

# Company class
class company:
    def __init__(self, name):
        self.name = name
        self.area_of_effect = random_choice(area_of_effect)
        self.distance_from_road = random_choice(distance_from_road) #TODO: FIX
        self.number_of_free_workers = random_choice(number_of_free_workers)
        self.city_of_origin = random_choice(cities)
        
        self.workers = setup_worker(self.name)
        
        
        # if road is broken then fix else go to next city and find new roads to fix (breadth search first bsf)
    def check_roads():
        pass
  
    def print_stats(self):
        print(f"Company: {self.name}")
        print(f"Area of Effect: {self.area_of_effect}")
        print(f"Distance from Road: {self.distance_from_road}") #TODO: FIX
        print(f"Number of Free Workers: {self.number_of_free_workers}")
        print(f"City of origin: {self.city_of_origin.name}")
        print(f"workers: {[worker.name for worker in self.workers]}")
        print("-" * 30)
        
class worker:
    def __init__(self, name):
        self.name = name
        self.fixing_speed = random_choice(fixing_speed)
        # self.curr_pos = #TODO: add the position of the company origin then move it with the move() function

    def print_stats(self):
        print(f"worker: {self.name}")
        print(f"Fixing Speed: {self.fixing_speed}")
        
    def move(self):
        pass
    
    def fix_road(self):
        pass
        
        
# Game setup
def setup_roads():
    min_num_roads = int(input('input the minimum number of roads: '))
    roads = [road() for _ in range(min_num_roads)] #TODO: maybe roads should have only 2 endpoints?
    return min_num_roads, roads

def setup_cities():
    num_cities = int(input('input the number of cities: '))
    cities = [city(chr(65 + i)) for i in range(num_cities)]  
    return cities

def setup_companies():
    num_companies = int(input('input the number of companies: '))
    companies = [company(chr(65 + i) + f"({i})") for i in range(num_companies)]  #TODO: add same company different branch later
    return companies

def setup_worker(name):
    num_workers = random_choice(number_of_free_workers)
    workers = [worker(chr(65 + i) + f": {name}") for i in range(num_workers)] 
    return workers
    
    

# Testing
if __name__ == "__main__":
    # creating instances automatically
    min_num_roads, roads = setup_roads()
    cities = setup_cities()
    companies = setup_companies()
    
    print(f"\n\t total number of cities {len(cities)} roads {len(roads)} companies {len(companies)}")

    #TODO: inherit .print_stats? actually no cuz they all print different stuff? idk yet

    print("\nRoads:")
    for r in roads:
        r.print_stats()
        
    print("\nCities:")
    for c in cities:
        c.print_stats()
        
    print("\nCompanies:")
    for comp in companies:
        comp.print_stats()
        
    print("\nWorkers:")
    for comp in companies:
        for worker in comp.workers:
            worker.print_stats()
            
#TODO: next add worker functionality