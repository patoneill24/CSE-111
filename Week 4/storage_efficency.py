#helps us calculate the value of Pi
import math

def main():
    #Provides values of radiuses,heights, and names
    #calculates the surface area, volume, and storage efficency based on those values in the lists
    #prints the item name and storage efficency for all 12 items
    radiuses = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
    heights = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
    names = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    costs = [0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42]
    best_storage_efficency = 0
    best_cost_efficency = 0
    for i in range(len(radiuses)):
        name = names[i]
        radius = radiuses[i]
        height = heights[i]
        cost = costs[i]
        storage_efficency = compute_storage_efficency(radius,height)
        cost_efficency = compute_cost_efficency(radius,height,cost)
        if cost_efficency > best_cost_efficency:
            best_cost_efficency = cost_efficency
            best_cost_name = names[i]
        if storage_efficency > best_storage_efficency:
            best_storage_efficency = storage_efficency
            best_storage_name = names[i]
        print(f'{name} {storage_efficency:,.2f}    {cost_efficency:,.2f}')
    print()
    print(f'Best Storage Efficency: {best_storage_name}: {best_storage_efficency:,.2f}')
    print(f'Best Cost Efficency: {best_cost_name}: {best_cost_efficency:,.2f}')
        


def compute_storage_efficency(radius,height):
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    storage_efficency = volume / surface_area
    return storage_efficency

def compute_cost_efficency(radius,height,cost):
    volume = compute_volume(radius,height)
    cost_efficency = volume / cost
    return cost_efficency

def compute_volume(radius,height):
    #utilizes the math library
    #calculates the volume based on the parameters named, "radius" and "height"
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius,height):
    #calcualtes surface area based on the same parameters as the "compute_volume" function
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

#calls the main function
main()