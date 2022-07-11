# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(name):
    return name["name"]
def get_total_cash(total):
    total = total["admin"]["total_cash"]
    return total
def add_or_remove_cash(total_petshop, cash):
    total_petshop["admin"]["total_cash"] += cash
def get_pets_sold(pets):
    return pets["admin"]["pets_sold"]
def increase_pets_sold(pets, pets_sold):
    pets["admin"]["pets_sold"] = pets_sold
    return pets
def get_stock_count(stock_update):
    return len(stock_update["pets"])
def get_pets_by_breed(pets, breed):
    total_pets = []
    for pet in pets["pets"]:
     if pet["breed"] == breed :
        total_pets.append(pet)
    return total_pets
   # def find_chicken_by_name( list, chicken_name ):
  #for chicken in list:
   # if chicken["name"] == chicken_name:
    #  return chicken
    #def find_chicken_by_name( list, chicken_name ):
  #found_chicken = None
  #for chicken in list:
   # if chicken["name"] == chicken_name:
    #  found_chicken = chicken
  #return found_chicken
#   def find_user_by_id( list, user_id ):
#   found_user = None
#   for user in list:
#     if user["user_id"] == user_id:
#       found_user = user
#   return found_user
   #for every individualpet in the list of pets
   # if that individualpet name is found in the list of pets that would be equal to
   # the pet_name (that we dropped in "arthur") and therefore we are asking this function
   # to return that individualpet that we have found's name
def find_pet_by_name(list, pet_name):
  for individualpet in list["pets"]:
    if individualpet["name"] == pet_name:
      return individualpet
## FUNCTION that is wants to go into a LIST and REMOVE petbyname
## if petbyname exists in list
 ## remove petbyname in list
# def remove_pet_by_name (list, petbyname):
#     if petbyname in list["pets"]:
#         f
#         petbyname.remove(list)
def remove_pet_by_name(list, pet_name):
    for individualpet in list["pets"]:
        if individualpet["name"] == pet_name:
            return list["pets"].remove(individualpet)
            
def add_pet_to_stock(shop_count, pet_name):
    for pet_name in shop_count["pets"]:
        shop_count["pets"].append(pet_name)
        
# looking for count and name
# for every new pet we need to add to petcount
#  total_petshop["admin"]["total_cash"] += cash
#   ratings = []
#     for cake in cakes:
#         ratings.append(cake["rating"])
#     ratings_total = sum(ratings)
#     number_of_cakes = len(cakes)
#     average = ratings_total / number_of_cakes
#     return average