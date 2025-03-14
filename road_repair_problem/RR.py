import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
#TODO: import icecream?

# Variables
road_size = [1, 2, 3, 4, 5, 6, 7]
fixing_speed = [1, 2, 3, 4, 5, 6, 7]
area_of_effect = [1, 2, 3, 4, 5, 6, 7]
travel_distance = [1, 2, 3, 4, 5,6, 7]
number_of_free_workers = [1, 2, 3, 4, 5, 6, 7] #TODO: make variables actually useful

# road_size = [1]
# fixing_speed = [1]
# area_of_effect = [1]
# travel_distance = [1]
# number_of_free_workers = [3] # for testing purposes


def random_choice(list_of_stuff):
    return random.choice(list_of_stuff)


# road class
class road:
    count = 0
    def __init__(self):
        self.name = chr(97 + road.count)
        self.size = random_choice(road_size)
        self.visited = 0
        road.count += 1
        
        self.chance_of_breakdown = 0.5
        
        if random.random()  < self.chance_of_breakdown:
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
        self.prev_pos = company_pos
        self.travel_distance = random_choice(travel_distance)

    def print_stats(self):
        print(f"worker: {self.name}")
        print(f"Fixing Speed: {self.fixing_speed}")
        print(f"Current position: {self.curr_pos}")
        print(f"travel distance: {self.travel_distance}")
        
        
    def fix_road(self):
        # check the nearby roads
        roads_to_fix = [(road, road.state, road.visited, self.curr_pos) for road in self.curr_pos.neighboring_roads]

        print(f"roads to fix: {roads_to_fix}")
        
        return roads_to_fix
        # print(f"nearby_roadsFix: {self.curr_pos.neighboring_roads[0].}")
        

    def move(self):
        if self.travel_distance == 0:
            print(f"staying at {self.curr_pos}")
            return self.curr_pos, self.curr_pos

        print(self.name)
        print(f"nearby_roads: {self.curr_pos.neighboring_roads}")
        
        roads_to_fix = self.fix_road()
        next_move = min(roads_to_fix, key=lambda x: x[0].visited) #TODO: i need to return the city with this
        
        available_hops = []
        
        for city in cities:
            if next_move[0] in city.neighboring_roads:
                available_hops.append(city)
        
        print(available_hops, "available_hops")
                
        city_hop = random_choice(available_hops)
        
        # Update positions and road state
        self.prev_pos = self.curr_pos
        self.curr_pos = city_hop
        next_move[0].state = 0
        next_move[0].visited += 1
        self.travel_distance -= 1
        
        print(f"going from {worker.prev_pos} to {worker.curr_pos}")
        print("")
        return worker.prev_pos, worker.curr_pos 
            
                         
# Company class
class company:
    def __init__(self, name):
        self.name = name
        self.area_of_effect = random_choice(area_of_effect) 
        self.number_of_free_workers = random_choice(number_of_free_workers)
        self.city_of_origin = random_choice(cities)
        
        self.num_workers = random_choice(number_of_free_workers)
        self.workers = [worker(chr(65 + i) + f": {name}", self.city_of_origin) for i in range(self.num_workers)]
        
        
        
        # if road is broken then fix else go to next city and find new roads to fix (breadth search first bsf)
  
    def print_stats(self):
        print(f"Company: {self.name}")
        print(f"Area of Effect: {self.area_of_effect}")
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
    companies = [company(chr(65 + i) + f"({i})") for i in range(num_companies)] 
    return companies

    
    


            
#TODO: next Visualize

# 1. Graph-Based Visualization (networkx_visual.py)
# Uses NetworkX and Matplotlib to visualize cities and roads as a graph


def visualize_graph(cities, roads):
    
    arr_of_cities = []
    
    G = nx.Graph()
    
    edge_color = ""
    
    for city in cities:
        G.add_node(city.name)
    # for road in roads:
    #     G.add_edge(road.city1.name, road.city2.name, color='red' if road.state == 1 else 'green')
    for city1 in cities:
        for city2 in cities:
            if city1 == city2:
                continue
            else:
                for road1 in city1.neighboring_roads:
                    for road2 in city2.neighboring_roads:
                        if road1 == road2:
                            arr_of_cities.append([city1, city2, road1, road2, edge_color])
    
    arr_of_cities = list(set(tuple(sorted(sublist, key=lambda x: x.name if hasattr(x, "name") else x)) for sublist in arr_of_cities))
    
    for couple in arr_of_cities:
        arr_of_cities[0] = "red" if couple[3].state == 1 or couple[4].state == 1 else 'green'
        G.add_edge(couple[1].name, couple[2].name, color=arr_of_cities[0])
                            
    
    colors = [G[u][v]['color'] for u, v in G.edges]
    
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    
    nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='lightblue', node_size=3000)
    
    # for u, v in G.edges():
    #     print(u, v)      
    
    # def update(frame):
    #     ax.clear()
        
    #     # Simulate road repairs over time
    #     while True:
    #         for comp in companies:
    #             for worker in comp.workers:
    #                 if worker.travel_distance != 0:
    #                     prev_pos, curr_pos = worker.move()
    #                     temp_arr = [[prev_pos, curr_pos]]
    #                     temp_arr = list(set(tuple(sorted(sublist, key=lambda x: x.name if hasattr(x, "name") else x)) for sublist in temp_arr))
                        
    #                     for road in G.edges():
    #                         if temp_arr in road:
    #                             G[u][v]['color'] = "green"
                        
    #                     # Update edge colors
    #                     colors = [G[u][v]['color'] for u, v in G.edges]

    #                     nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='lightblue', node_size=3000, ax=ax)
    #                     ax.set_title(f"Step {frame}")
    #                     sleep(1)


    # ani = animation.FuncAnimation(fig, update, frames=10, interval=1000, repeat=True)   
    # plt.show()  
    
    # take 2
    def update(frame):
        ax.clear()
        
        try:
            # Update road states and colors
            for comp in companies:
                for worker in comp.workers:
                    if worker.travel_distance > 0:  # Changed from != 0 to > 0
                        try:
                            prev_pos, curr_pos = worker.move()
                            if prev_pos is None or curr_pos is None:
                                continue
                            
                            # Update colors in the graph
                            for u, v in G.edges():
                                # Check if this edge connects prev_pos and curr_pos
                                if (u == prev_pos.name and v == curr_pos.name) or \
                                   (v == prev_pos.name and u == curr_pos.name):
                                    G[u][v]['color'] = 'green'
                        except Exception as e:
                            print(f"Error in worker move: {e}")
                            continue
                
            # Get updated colors
            colors = [G[u][v]['color'] for u, v in G.edges()]
            
            # Redraw the graph
            nx.draw(G, pos, with_labels=True, 
                   edge_color=colors, 
                   node_color='lightblue', 
                   node_size=3000, 
                   ax=ax)
                
            ax.set_title(f"Step {frame}")
            
        except Exception as e:
            print(f"Error in update function at step {frame}: {e}")
        
        return ax

    # Create animation with error handling
    try:
        ani = animation.FuncAnimation(fig, update, 
                                    frames=100, 
                                    interval=1000,
                                    repeat=False)
        plt.show()
    except Exception as e:
        print(f"Animation error: {e}")
    
###################

# import pygame

# def run_pygame_simulation():
#     pygame.init()
#     screen = pygame.display.set_mode((600, 600))
#     clock = pygame.time.Clock()
#     running = True
    
#     while running:
#         screen.fill((255, 255, 255))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         pygame.display.flip()
#         clock.tick(30)
#     pygame.quit()


# Testing
if __name__ == "__main__":
    # creating instances automatically
    min_num_roads, roads = setup_roads()
    cities = setup_cities()
    companies = setup_companies()
    
    print(f"\n\t total number of cities {len(cities)} roads {len(roads)} companies {len(companies)}")

        
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
            
    # companies[0].send_workers_out()
    

    visualize_graph(cities, roads)
    # run_pygame_simulation()
    
    # loop on all roads and if all roads are fixed print the data
    # TODO: Make it animated