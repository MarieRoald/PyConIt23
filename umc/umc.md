# The animal population in Norway

![Image of a wolf (by colfelly via Pixabay.)](images/wolf.jpg){width=400px}

It's important to have up-to-date statistics on the animal population to ensure a thriving ecosystem. For Norway, we can find this information at the [Norwegian Environmental Agency's webpage](https://miljostatus.miljodirektoratet.no/miljodata/?kategori=112) (only in Norwegian). In this exercise, we will use Python to explore the numbers from this webpage. 


## Part 1: Exploring population data

```python
import json
import matplotlib.pyplot as plt

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
```

1. Download the start-code and data files and place them in a folder on your computer and run the code. What does the yellow dot and dashed line in the plot represent?
2. Modify the code so the yellow dot shows the minimum population and the dashed line shows the year of the minimum population.
3. Modify the code so the yellow dot shows the year where the population decreased the most compared to the previous year. (**Hint:** Start by creating a variable `previous_population = 0` that you set equal to `population` at the end of each iteration).
4. Select one of the other data files from the project directory (e.g. `muskox_count.json`) and create a program that plots that animal population against time. **Note:** for all species except wolves, we only have data for Norway and consider the number of animals, not the number of mated pairs.

## Part 2: Creating functions for summary statistics

```python
def compute_max_population(yearly_population):
    max_population = 0
    year_of_max_population = 0
    
    for year, population in yearly_population.items():
        if population > max_population:
            max_population = population
            year_of_max_population = year
    
    return year_of_max_population, max_population

year_of_max_population, max_population = compute_max_population(wolf_count)
print(f"The highest population occured in {year} and was {population}.")
```

1. Read the two functions above. What do they do?
2. Copy the code snippet into your code and run it.
3. Create another function `compute_min_population(yearly_population)` that computes the minimum population and the year of the minimum population.
4. Print the result from calling `compute_min_population(yearly_population)`.
5. Repeat exercise 3. and 4. to create functions that compute the maximum increase and maxmium decrease in population and print this information too
6. Create a function `print_summary_statistics(yearly_population)` that computes the minimum and maximum population and maximum increase and decrease in population and prints out all these quantities.
