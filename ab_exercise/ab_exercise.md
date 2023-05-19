# Task A: Placing a planet in orbit

## Part 1 - Making the program

![](images/planet_square.jpg){width=200px height=200px}

As an evil scientist, you want to create a new artificial planet that orbits the sun. To ensure that your nefarious planet stays in orbit, you need to shoot it off with the correct speed, $v$. After doing some calculations, you find that the speed (measured in km/s) must be 
$$v = \frac{365\ 000}{\sqrt{d}},$$
where $d$ is the distance between the sun and the artificial planet measured in kilometres. 

### Example runs:

```raw
How many km between the sun and your nefarious planet? 150000000
The velocity is: 29.802125203862 km/s
```

```raw
How many km between the sun and your nefarious planet? 228000000
The velocity is: 24.172715516437048 km/s
```

```raw
How many km between the sun and your nefarious planet? 108000000
The velocity is: 35.122141375702235 km/s
```

### Task:

1. Create a program that asks the user for the distance between a planet and the sun and prints out the velocity of that planet.
2. Test your code by computing the velocity of the Earth ($d=150\ 000\ 000$), Mars ($d=228\ 000\ 000$) and Venus ($d=108\ 000\ 000$). Compare with the above example runs to see if your implementation is correct.
3. **Bonus exercise:** Create a utility that takes the velocity as input and prints the distance to the sun.

<div style="page-break-after: always; visibility: hidden">
```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```
</div>

# Task A: Placing a planet in orbit

## Part 2 - Discussing the code

Find a partner that solved Task B and present your task and your solution. It's not necessary to have completely solved the problem – the discussion is more important. Here are some example questions you could discuss together.

 * What does your code do? Explain what each line does and why you included it.
 * What are the different variables you use in your program, and what are they used for?
 * Does the code work correctly?
   - If yes, how did you test this?
   - If no, what's wrong?

<div style="page-break-after: always; visibility: hidden">
```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```
</div>

# Task B: Escaping a new planet

## Part 1 - Making the program

![](images/astronaut_square.jpg){width=200px height=200px}


Your nemesis, an evil scientist, keeps placing you on foreign planets, and to get back to Earth, you first need to know how far the artificial planet you're stuck on is from the sun.

Luckily, you got your watch, and from physics class, you remember that the distance, $d$, between the sun and a planet (measured in km) is given by
$$d = 2\ 930\ 000 \ T^\frac{3}{2},$$
where $T$ the duration of a year measured in earth days. 

## Example runs:

```raw
What is the duration of a year on the artificial planet (measured in earth days)? 365.25
The distance to the sun is: 149713548.26702362 km
```

```raw
What is the duration of a year on the artificial planet (measured in earth days)? 687
The distance to the sun is: 228124595.49833688 km
```

```raw
What is the duration of a year on the artificial planet (measured in earth days)? 225
The distance to the sun is: 108390020.66682415 km/s
```

### Task:

1. Create a program that asks the user for the duration of a year and prints out the distance between the sun and the planet.
2. Test your code by computing the distance between the sun and the Earth ($T=365.25$), Mars ($T=687$) and Venus ($T=225$). Compare with the above example runs to see if your implementation is correct.
3. **Bonus exercise:** Create a utility that takes the distance to the sun as input and prints the duration of a year.

<div style="page-break-after: always; visibility: hidden">
```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```
</div>

# Task B: Escaping a new planet

## Part 2 - Discussing the code

Find a partner that solved Task A and present your task and your solution. It's not necessary to have completely solved the problem – the discussion is more important. Here are some example questions you could discuss together.

 * What does your code do? Explain what each line does and why you included it.
 * What are the different variables you use in your program, and what are they used for?
 * Does the code work correctly?
   - If yes, how did you test this?
   - If no, what's wrong?

<div style="page-break-after: always; visibility: hidden">
```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```
</div>

# Example solutions

## Task A:

```python
from math import sqrt

distance_to_sun = float(input("How many km between the sun and your nefarious planet? "))
velocity = 365_000 * sqrt(distance_to_sun)

print(f"The velocity is: {velocity} km/s")
```

## Task B:

```python
year_duration = float(input("What is the duration of a year on the artificial planet (measured in earth days)? "))
distance_to_sun = 2_930_000 * (year_duration**(2/3))

print(f"The distance to the sun is: {velocity} km")
```