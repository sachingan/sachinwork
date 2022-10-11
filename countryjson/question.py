

import json

with open("countries.json",encoding="utf-8") as a:
    countries=json.load(a)
# print(countries)



#print total no. of country details

no_of_countries=len([country for country in countries])
print(no_of_countries)

#print language of ukraine


language_det=[country["languages"] for country in countries if country["name"]=="Ukraine"]
for lan in language_det[0]:
    print(lan["name"])


#print currency of china

currency_det=[country["currencies"] for country in countries if country["name"].lower().startswith("Palestine")]

# for currency in currency_det[0]:
#     print(currency["name"])

#print population of india

population_det=[country["population"] for country in countries if country["name"]=="India"]
# print(population_det[0])
#print neighbouring countries of australia

neighbouring_country_det=[country for country in countries if country.get("name")=="Australia"]
# if "borders" in neighbouring_country_det:
#     print(neighbouring_country_det)
# else:
#     print("NO Neighbouring countries")
# print(neighbouring_country_det)

def get_country_det(country_name):
    return [country for country in countries if country["name"].startswith(country_name)]

india_det=get_country_det("India")
country_borders=india_det[0].get("borders")
alpha_coe=[country["name"] for country in countries if country["alpha3Code"] in country_borders]
print(alpha_coe)

population_max=ma[country["Population"] for country in countrie
print(population_max)




