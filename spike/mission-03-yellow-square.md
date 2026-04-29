# Mission 03 — Yellow Square

## What you're building

Your robot will recognise a yellow square on the floor and perform a special action when it sees one — stopping, displaying a message, then moving off again. You'll add colour detection to the sensor readings and introduce a new MyBlock for the yellow square behaviour.

---

## What you need

- Everything from Mission 02
- The colour sensor on port **E** already reads colour as well as light

---

## Step 1 — Read the colour

Inside your `forever` loop, after the distance reading, add:

- `set colour to (colour sensor E) colour`

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
  start moving right: 20
  wait 0.5 seconds
else
  water tower
```

> **Why check colour again inside the MyBlock?** The MyBlock is called every loop, but you only want the yellow square *behaviour* to run if yellow is actually detected. The else branch hands off to `water tower` (obstacle stop) if it turns out the colour wasn't yellow after all — acting as a fallback.

> **Why move right briefly after the wait?** This nudges the robot off the yellow square so it doesn't detect yellow again on the very next loop and repeat the behaviour endlessly.

---

## Step 3 — Update the main loop

Add a call to `yellow square` in your `forever` loop. Your main loop now reads sensors and then decides:

```
forever
  set light to [E] reflected light
  set distance to [C] distance in cm
  set colour to [E] colour
  yellow square
```

Wait — this always calls `yellow square` now. You need to restructure slightly. The `yellow square` MyBlock handles its own colour check internally, so this works, but consider the order of priority: obstacle > yellow square > line follow.

Restructure the main loop as:

```
forever
  set light to [E] reflected light
  set distance to [C] distance in cm
  set colour to [E] colour
  if distance < 10 then
    water tower
  else
    yellow square   ← yellow square now contains the colour check and falls back to water tower / line follow
```

Actually, make `yellow square` the middle layer:

```
define yellow square
  if [E] is colour yellow then
    stop moving
    write Hello
    wait 2 seconds
    turn on (full brightness)
    start moving right: 20
    wait 0.5 seconds
  else
    line follow      ← fall through to line following if not yellow
```

> **Why have yellow square fall through to line follow?** It means your main loop stays clean: check distance first (urgent), then check colour (special event), then line follow (default). Each MyBlock only needs to know about the next layer down.

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
