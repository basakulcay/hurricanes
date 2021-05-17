# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#2
def convert_damages_data(damages):
  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)
print(convert_damages_data(damages))

# Create and view the hurricanes dictionary
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  hurricanes = {}
  num_hurricanes = len(names)

  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],"Areas Affected": areas_affected[i], "Damage": updated_damages[i],"Deaths": deaths[i]}
  return hurricanes

hurricane_dict = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print("......")
#print(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def create_year_dict(hurricane_dictionary):
  h_by_year={}
  for year in years:
    hurricanes = []
    for hurricane in hurricane_dict.values():
      if hurricane['Year'] == year:
        hurricanes.append(hurricane)
      h_by_year[year] = hurricanes
  return h_by_year

create_year_dict(hurricane_dict)
#print(create_year_dict(hurricane_dict))
# Counting Damaged Areas

def count_areas (affected_areas):
  affected_area_count = {}
  for area in affected_areas:
    for location in area:
      if affected_area_count.get(location) is None:
        affected_area_count[location] = 1
      else:
        affected_area_count[location] += 1
  return affected_area_count

areas_affected_count = count_areas(areas_affected)
print (areas_affected_count)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def max_affected(areas_affected_count):
  listed=[]
  list_keys=list(areas_affected_count.keys())
  print("---")
  for i in areas_affected_count.values():
    listed.append(i)
  maximum=max(listed)
  max_index=list_keys[listed.index(maximum)]
  print(max_index+" has got hit by hurricanes by "+str(maximum)+" times.")
  
max_affected(areas_affected_count)
# 6
def greatest_deaths (hurricane_dictionary):
  hurricane_name = ""
  total_deaths = 0
  for hurricane in hurricane_dictionary.values():
    if hurricane.get("Deaths") > total_deaths:
      hurricane_name = hurricane.get("Name")
      total_deaths = hurricane.get("Deaths")
  return hurricane_name, total_deaths

hurricane, deaths = greatest_deaths(hurricane_dict)

greatest_deaths (hurricane_dict)
print("The greatest number of deaths is:{deaths} from hurricane {hurricane}".format(deaths = deaths, hurricane = hurricane))

def categorize_by_mortality (hurricane_dictionary):
  hurricane_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[]}
  
  for hurricane in hurricane_dictionary.values():
    deaths = hurricane.get("Deaths")
    if deaths >= 0 and deaths < 100:
      hurricane_by_mortality[0].append(hurricane.get("Name"))
    elif deaths >=100 and deaths < 500:
      hurricane_by_mortality[1].append(hurricane.get("Name"))
    elif deaths >=500 and deaths < 1000:
      hurricane_by_mortality[2].append(hurricane.get("Name"))
    elif deaths >=1000 and deaths < 10000:
      hurricane_by_mortality[3].append(hurricane.get("Name"))
    else:
      hurricane_by_mortality[4].append(hurricane.get("Name"))
  
  return hurricane_by_mortality

hurricane = categorize_by_mortality (hurricane_dict)

print("***")
for category, name_list in hurricane.items():
  print("Category {category}: {hurricanes}".format(category = category, hurricanes = name_list))

# 9
def greatest_damages (hurricane_dictionary):
  hurricane_name = ""
  max_damage = 0
  for hurricane in hurricane_dictionary.values():
    if type(hurricane.get("Damage"))!=str:
      if hurricane.get("Damage") > max_damage:
        hurricane_name = hurricane.get("Name")
        max_damage = hurricane.get("Damage")
  return hurricane_name, max_damage

hurricane, damages = greatest_damages(hurricane_dict)

greatest_damages (hurricane_dict)

print("The greatest number of damages is:{damages} from hurricane {hurricane}".format(damages = damages, hurricane = hurricane))

# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def categorize_by_damage (hurricane_dictionary):
  hurricane_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[]}
  
  for hurricane in hurricane_dictionary.values():
    damages = hurricane.get("Damage")
    if type(damages)!=str:
      if damages == 0:
        hurricane_by_damage[0].append(hurricane.get("Name"))
      elif damages > 0 and damages < 100000000:
        hurricane_by_damage[1].append(hurricane.get("Name"))
      elif damages >=100000000 and damages < 1000000000:
        hurricane_by_damage[2].append(hurricane.get("Name"))
      elif damages >=1000000000 and damages < 10000000000:
        hurricane_by_damage[3].append(hurricane.get("Name"))
      elif damages >=10000000000 and damages <50000000000:
        hurricane_by_damage[4].append(hurricane.get("Name"))
  
  return hurricane_by_damage

hurricane = categorize_by_damage(hurricane_dict)
print("Damages list:",hurricane)
