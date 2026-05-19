# Mission 03 — Yellow Square

## What you're building

Your robot will recognise a yellow square on the floor and perform a special action when it sees one — stopping, displaying a message, then moving off again. You'll add colour detection to the sensor readings and introduce a new MyBlock for the yellow square behaviour.

---

## What you need

- Everything from Mission 02
- The colour sensor on port **E** already reads colour as well as light

---

## Step 1 — Read the colour

First, create a new variable called **colour**.

Inside your `forever` loop, after the distance reading, add:

- `set colour to (colour sensor E) colour`

<img width="355" height="331" alt="image" src="https://github.com/user-attachments/assets/a6dc4e29-c0ff-45e1-afcd-9abb23455cde" />


> **Why store colour separately?** You're already storing `light` (reflected brightness). Colour is a different reading from the same sensor — it tells you *what colour* rather than *how bright*. Storing both lets you use each independently.

---

## Step 2 — Create the `yellow square` MyBlock

Create a new MyBlock called **yellow square**. Inside it, add:

```
if [E] is colour (yellow) then
  stop moving
  write Hello
  wait 2 seconds
  turn on (full brightness)
  start moving
  wait 0.5 seconds
else
  line follow
```

<img width="277" height="422" alt="image" src="https://github.com/user-attachments/assets/93ac6144-a431-4aac-89c0-2a6c2cab4901" />


> **Why check colour inside the MyBlock?** The MyBlock is called every loop iteration, but you only want the yellow square *behaviour* to run if yellow is actually detected. If it's not yellow, it falls through to `line follow` — so yellow square is the middle layer: colour event above, line following below.

> **Why move briefly after the wait?** This moves the robot past the yellow square so it doesn't detect yellow again on the very next loop and repeat the behaviour endlessly.

---

## Step 3 — Update the main loop

Your main loop now reads all three sensors and then calls `yellow square`, which handles the rest:

```
forever
  set light to [E] reflected light
  set distance to [C] distance in cm
  set colour to [E] colour
  if distance < 10 then
    water tower
  else
    yellow square
```

<img width="1079" height="480" alt="image" src="https://github.com/user-attachments/assets/bc2fd95c-4c67-48e2-8005-56be92e70d1e" />


> **Why have yellow square call line follow internally?** This is a deliberate pattern: each MyBlock calls the next layer down. `water tower` handles obstacles. `yellow square` handles colour events, then falls through to `line follow` as the default. The main loop only needs to know about the top layer — it stays clean and readable no matter how many behaviours you add.

---

## Expected result

Main loop:
```
forever
  set light to [E] reflected light
  set distance to [C] distance in cm
  set colour to [E] colour
  if distance < 10 then
    water tower
  else
    yellow square
```

`yellow square` MyBlock:
```
if [E] is colour yellow then
  stop moving / write Hello / wait / move off
else
  line follow
```

---

## Test it ✓

1. Place a yellow card or square on your line course.
2. Run the program and let the robot follow the line toward the yellow square.
3. When the colour sensor passes over the yellow square, the robot should stop, display "Hello", pause, then move off.
4. After the brief right turn, it should resume line following.

**If it doesn't detect yellow:** check the sensor height above the floor — too high and the colour reading becomes unreliable. Also check the lighting conditions; fluorescent lighting can affect colour readings.
