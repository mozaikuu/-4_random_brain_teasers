import random
#TODO: import icecream?

# Variables
road_size = [1, 2, 3, 4, 5, 6, 7]
fixing_speed = [1, 2, 3, 4, 5, 6, 7]
area_of_effect = [1, 2, 3, 4, 5, 6, 7]
distance_from_road = [1, 2, 3, 4, 5,6, 7]
number_of_free_workers = [1, 2, 3, 4, 5, 6, 7] #TODO: make variables actually useful


def random_choice(list_of_stuff):
    return random.choice(list_of_stuff)


# road class
class road:
    count = 0
    def __init__(self):
        self.name = chr(97 + road.count)
        self.size = random_choice(road_size)
        road.count += 1
    
    def print_stats(self):
        print(f"road name: {self.name}")
        print(f"Road size: {self.size}")
        


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
        self.fixing_speed = random_choice(fixing_speed)
        self.area_of_effect = random_choice(area_of_effect)
        self.distance_from_road = random_choice(distance_from_road) #TODO: FIX
        self.number_of_free_workers = random_choice(number_of_free_workers)
        self.city_of_origin = random_choice(cities)
  
    def print_stats(self):
        print(f"Company: {self.name}")
        print(f"Fixing Speed: {self.fixing_speed}")
        print(f"Area of Effect: {self.area_of_effect}")
        print(f"Distance from Road: {self.distance_from_road}") #TODO: FIX
        print(f"Number of Free Workers: {self.number_of_free_workers}")
        print(f"City of origin: {self.city_of_origin.name}")
        print("-" * 30)


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