# Mission 02 — Water Tower (Obstacle Detection)

## What you're building

Your robot will stop when it detects an obstacle close in front of it — representing a water tower it needs to deliver to. You'll add a distance sensor and restructure your main loop to check for obstacles first, then line follow if the path is clear.

---

## What you need

- Everything from Mission 01
- Distance sensor connected to port **C** (pointing forward)

---

## Step 1 — Read the distance sensor

First, create a new variable called **distance**.

Inside your `forever` loop, after the light reading, add:

- `set distance to (distance sensor C) distance in cm`

This stores the current distance reading each loop.

> **Why cm?** It gives you a human-readable number to work with. 10 cm is roughly a hand-width — close enough to mean "obstacle right in front."

<img width="399" height="439" alt="image" src="https://github.com/user-attachments/assets/27788be0-1107-4545-aae4-5658f05e01ca" />



---

## Step 2 — Create the `water tower` MyBlock

Create a new MyBlock called **water tower**. Inside it, add just one block:

- `stop moving`

<img width="180" height="133" alt="image" src="https://github.com/user-attachments/assets/4fd3485b-975c-45dd-a37c-291da563fffd" />


> **Why a MyBlock?** Right now the water tower just stops. Later you might want it to do more — flash a light, wait, then reverse. Putting it in a MyBlock means you only change the code in one place.

---

## Step 3 — Create the `line follow` MyBlock

Move your existing `if light > 60` steering logic (including the wait) into a new MyBlock called **line follow**.

Your `line follow` MyBlock should contain:
```
if light > 60 then
  start moving left: -60
else
  start moving right: 60
  wait 0.5 seconds
```

<img width="216" height="281" alt="image" src="https://github.com/user-attachments/assets/cbbc4556-84de-43b3-a0ca-5c7f2a911ba9" />

> **Why move it to a MyBlock?** Your main loop is about to get more decisions. Keeping each behaviour in its own named block makes the main loop readable at a glance. This is the beginning of a pattern you'll build on — each MyBlock represents one mode of behaviour, and the main loop decides which mode to run.


 

---

## Step 4 — Update the main loop

Replace the old steering logic in your `forever` loop with:

```
if distance < 10 then
  water tower
else
  line follow
```

<img width="846" height="446" alt="image" src="https://github.com/user-attachments/assets/f2c3b805-e86f-4b1d-913f-a64ecb708f69" />



> **Why check distance first?** The obstacle is more urgent than the line. If you checked the line first, the robot might steer itself into the obstacle before the distance check ran. Priority order matters — and by calling named MyBlocks rather than writing everything inline, it's easy to read what the robot will do in each situation.

---

## Expected result

```
When Program Starts
  set movement motors to A+B
  set movement speed to 20%
  forever
    set light to [E] reflected light
    set distance to [C] distance in cm
    if distance < 10 then
      water tower
    else
      line follow
```

---

## Test it ✓

1. Run your line-following test from Mission 01 — it should still work exactly the same.
2. While the robot is line following, place your hand in front of the distance sensor.
3. The robot should stop.
4. Remove your hand — it should resume line following.

**If it stops too early or too late:** adjust the `10 cm` threshold to suit your sensor and environment.
