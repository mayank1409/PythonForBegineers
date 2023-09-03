from operator import attrgetter

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr(
            (self.name, self.population, self.area)
        )

countries = [Country('India', 140, 10000),
             Country('China', 180, 20000),
             Country('USA', 30, 40000)]


print('Countries: ', countries)
print('Countries[0] ', countries[0])
print('Countries[0:2] ', countries[0:2])

countries.append(Country('Russia', 100, 30000))
print('After appending Russia, Countries: ', countries)

countries.sort(key=attrgetter('area'))
print('Countries after sorting on area: ', countries)

countries.sort(key=attrgetter('population'), reverse=True)
print('Countries after reverse sorting on population: ', countries)

print()

print('country with max population ', max(countries, key=attrgetter('population')))
print('country with min population ', min(countries, key=attrgetter('population')))
print('country with max area ', max(countries, key=attrgetter('area')))
print('country with min area ', min(countries, key=attrgetter('area')))