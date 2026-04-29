# Mission 01 — Line Following

## What you're building

Your robot will follow a black line on the floor using a colour/light sensor. It works by constantly checking how much light is reflected — a white surface reflects a lot, a black line reflects very little. Based on that reading, the robot steers left or right to stay on the edge of the line.

---

## What you need

- SPIKE Prime hub
- Two drive motors connected to ports **A** and **B**
- Colour sensor connected to port **E** (pointing down at the floor)

---

## Step 1 — Set up movement

When the program starts, you need to tell the hub which motors to use and how fast to go.

Add these blocks under **When Program Starts**:

- `set movement motors to A+B`
- `set movement speed to 20 %`

> **Why 20%?** It's slow enough that your sensor readings have time to respond. Faster speeds mean the robot overshoots the line before it can correct.

---

## Step 2 — Read the light sensor in a loop

Add a `forever` loop. Inside it, add:

- `set light to (colour sensor E) reflected light`

This stores the current light reading into a variable called `light` each time the loop runs.

> **Why store it in a variable?** It makes your code easier to read — you use the word `light` instead of repeating the sensor block everywhere.

---

## Step 3 — Steer based on the reading

Still inside the `forever` loop, add an `if / else` block:

- **If** `light > 60` **then**: `start moving left: -60`
- **Else**: `start moving right: 60`

> **Why 60?** White surfaces typically reflect 70–90%, black lines reflect 10–30%. A threshold of 60 sits in the middle. You may need to adjust this depending on your floor and lighting conditions.

Add a `wait 0.5 seconds` after the else branch (inside the else, after the move block).

> **Why the wait?** Without a small pause, the robot switches direction so rapidly it barely moves. The wait gives each steering correction a moment to take effect.

---

## Expected result

Your program should look like this:

```
When Program Starts
  set movement motors to A+B
  set movement speed to 20%
  forever
    set light to [E] reflected light
    if light > 60 then
      start moving left: -60
    else
      start moving right: 60
      wait 0.5 seconds
```

---

## Test it ✓

1. Place your robot so the colour sensor is just to one side of the black line.
2. Start the program.
3. The robot should wobble along the line — steering left when it sees white, right when it sees black (or vice versa depending on which side you start on).

**If it spins in one direction constantly:** your threshold may be off — try printing the `light` value to the hub display to see what readings you're actually getting.

**If it moves but doesn't follow the line:** check the sensor is close enough to the floor and pointing straight down.
