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

<img width="262" height="158" alt="image" src="https://github.com/user-attachments/assets/005054a6-60e5-41e8-b26d-8ae02f710df6" />

---

## Step 2 — Read the light sensor in a loop

First, create a new variable called **light**.

Add a `forever` loop. Inside it, add:

- `set light to (colour sensor E) reflected light`

This stores the current light reading into a variable called `light` each time the loop runs.

> **Why store it in a variable?** It makes your code easier to read — you use the word `light` instead of repeating the sensor block everywhere. Also, whenever you run a Spike Prime program, the current value of all variables is automatically tracked and displayed, which makes debugging much easier.

> **Why a `forever` loop?** This is the core of how the robot works. Rather than running a sequence of steps once, the loop keeps checking the sensor and reacting — over and over, many times per second. This allows the robot to respond to changing conditions in real time. As your program grows, all your sensor reading and decision-making will live inside this loop.

<img width="304" height="247" alt="image" src="https://github.com/user-attachments/assets/d74db580-91d4-43f3-8ed8-9c1d3dd9b707" />


---

## Step 3 — Steer based on the reading

Still inside the `forever` loop, add an `if / else` block:

- **If** `light > 60` **then**: `start moving left: -60`
- **Else**: `start moving right: 60`

> **Why 60?** White surfaces typically reflect 70–90%, black lines reflect 10–30%. A threshold of 60 sits in the middle. You may need to adjust this depending on your floor and lighting conditions.

Add a `wait 0.5 seconds` after the else branch (inside the else, after the move block).

> **Why the wait?** Without the pause, the robot loses its direction too easily — it switches so fast it never properly straddles the edge. The pause gives the rightward correction time to work, making it more forgiving when getting back onto the black line, especially on tight corners. The `right: 60` speed is also intentional — the deliberate aggressive zig-zag handles tight corners better than trying to move smoothly at a lower speed.

> **Why not use a timer here?** A short fixed `wait` is the right tool for a brief, predictable pause like this. Timer blocks are better suited to longer autonomous run durations — that's what missions 5 and 6 cover.

---

## Expected result

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
<img width="332" height="322" alt="image" src="https://github.com/user-attachments/assets/7f853658-e3c1-450c-816f-7f8f8d6c14d9" />

<img width="312" height="292" alt="image" src="https://github.com/user-attachments/assets/bbaf745c-f308-4209-a7a1-e1e2d6bb5ee6" />



---

## Test it ✓

1. Place your robot so the colour sensor is just to one side of the black line.
2. Start the program.
3. The robot should wobble along the line — steering left when it sees white, right when it sees black (or vice versa depending on which side you start on).

**If it spins in one direction constantly:** your threshold may be off — the variable display will show your live `light` readings to help you calibrate.

**If it moves but doesn't follow the line:** check the sensor is close enough to the floor and pointing straight down.
