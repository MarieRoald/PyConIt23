import matplotlib.pyplot as plt
import json

with open("wolf_pair_count.json") as f:
    wolf_data = json.load(f)
wolf_count = wolf_data["count"]

max_population = 0
year_of_max_population = 0

for year, population in wolf_count.items():
    if population > max_population:
        max_population = population
        year_of_max_population = year

plt.plot(wolf_count.keys(), wolf_count.values())
plt.plot(year_of_max_population, max_population, 'o')
plt.axvline(year_of_max_population, linestyle='--')
plt.xlabel("Year")
plt.ylabel("Number of mated wolf pairs")
plt.title("Wolf population in Norway and Sweden")
plt.show()