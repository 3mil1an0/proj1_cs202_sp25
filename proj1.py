#complete your tasks in this file
import sys
import unittest
import math
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

@dataclass (frozen= True)
class GlobeRect ():
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass (frozen= True)
class Region ():

    rect: GlobeRect
    name: str
    terrain: str        # "ocean"  "mountains"  "forest"  "other"

@dataclass (frozen= True)
class RegionCondition ():

    region: Region
    year: int
    pop: int
    ghg_rate: float

nyc_region = Region(rect = GlobeRect(lo_lat= 40.5 ,hi_lat= 41.2,west_long= -74.3 ,east_long= -73.7 ), name= "NYC State", terrain = "other")
NYC = RegionCondition(nyc_region, year = 2026, pop = 8600000, ghg_rate = 58000000.0)

moscow_region = Region(rect = GlobeRect(lo_lat= 54.5  ,hi_lat= 56.9 ,west_long= 35.1,east_long= 40.2), name= "Moscow Oblast", terrain = "forest")
Moscow = RegionCondition(moscow_region, year = 2026, pop = 8700000, ghg_rate = 45000000.0)

tyrrhenian_region = Region(rect = GlobeRect(lo_lat = 37.5, hi_lat = 44.5, west_long = 9.5, east_long = 16.0), name = "Tyrrhenian Sea", terrain = "ocean")
Tyrrhenian_Sea = RegionCondition(tyrrhenian_region, year= 2026, pop = 0, ghg_rate = 500000.0)

slo_region = Region(rect = GlobeRect(lo_lat= 35.0, hi_lat= 35.7, west_long= -121.0, east_long= -120.2), name = "California Central Coast", terrain = "other")
SLO_County = RegionCondition(slo_region, year = 2026, pop= 282000, ghg_rate = 1200000.0 )


region_conditions = [NYC, Moscow, Tyrrhenian_Sea, SLO_County]

def emissions_per_capita(rc: RegionCondition) -> float:
    if rc.pop == 0:
        return 0.0
    else:
        return rc.ghg_rate/rc.pop

def area(gr:GlobeRect)-> float:
    lambda1_radians = math.radians(gr.west_long) 
    lambda2_radians = math.radians(gr.east_long)

    phi1_radians = math.radians(gr. lo_lat)
    phi2_radians = math.radians(gr.hi_lat)

    Surface_Area = 6378.1**2 * abs(lambda2_radians - lambda1_radians) * abs(math.sin(phi2_radians)-math.sin(phi1_radians))

    return Surface_Area

def emissions_per_square_km(rc: RegionCondition) -> float:
    km2 = area(rc.region.rect)
    if km2 == 0:
        return 0.0
    else:
        return rc.ghg_rate/km2

def densest(rc_list: list[RegionCondition]) -> str:
    if len(rc_list) == 1:
        return rc_list[0].region.name
    
    first_rc = rc_list[0]
    first_density = first_rc.pop / area(first_rc.region.rect)

    rest_name = densest(rc_list[1:])

    rest_rc = rc_list[1]
    if rest_rc.region.name != rest_name:
        rest_rc = rc_list[2]

    rest_density = rest_rc.pop / area(rest_rc.region.rect)

    if first_density >= rest_density:
        return first_rc.region.name
    else:
        return rest_name
    
def project_condition(rc: RegionCondition, years: int)-> RegionCondition:

    if years == 0:
        return rc
    
    if rc.region.terrain == "ocean":
        growth_rate = 0.0001
    elif rc.region.terrain == "mountains":
        growth_rate = 0.0005
    elif rc.region.terrain == "forest":
        growth_rate = -0.00001
    else: #other
        growth_rate = 0.0003

    new_pop = int(rc.pop * (1 + growth_rate))

    if rc.pop == 0:
        new_ghg_rate = rc.ghg_rate
    else:
        new_ghg_rate = rc.ghg_rate * (new_pop/rc.pop)

    new_rc = RegionCondition(
        region = rc.region,
        year = rc.year+1,
        pop = new_pop,
        ghg_rate= new_ghg_rate )
    
    return project_condition(new_rc, years - 1)






    
        
    





