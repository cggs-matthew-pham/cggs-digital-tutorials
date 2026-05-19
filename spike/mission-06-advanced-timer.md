# Mission 06 — Advanced Timer

## What you're building

The simple timer from Mission 05 only tells you when a total time has elapsed. This mission adds a **tick-based timer** — an event that fires once per second, letting you do something each second (like display a countdown) and then trigger a final action when the count reaches a target.

---

## Why not just use `when timer > X` again?

The built-in timer block fires once when a threshold is crossed. If you want something to happen *every second*, you need to build that yourself using a counter variable and a repeating reset pattern.

---

## What you need

- Everything from Mission 05
- A new variable: **timer count**

Create the **timer count** variable before you begin.

---

## Step 1 — Set up timer count

In your **When Right button pressed** block, add:

- `set timer count to 0`

(alongside the existing `set autonomous mode to 1`)

<img width="263" height="161" alt="image" src="https://github.com/user-attachments/assets/b910bd09-5d72-4bf2-8390-095fef3c2d53" />


> **Why reset to 0 here?** Each time the robot activates, you want the countdown to start fresh from zero. Because `timer count` is a variable, you'll also be able to watch it update live on the hub display as the program runs.


---

## Step 2 — Create the `timer tick` MyBlock

Create a new MyBlock called **timer tick**. Inside it:

```
change timer count by 1
if timer count > 5 then
  set autonomous mode to 0
```

Breaking this down:

- `set timer count to (timer count + 1)` — increments the counter by 1 each tick
- `write timer count` — displays the current count on the hub's LED display so you can see it counting up
- `if timer count > 5` — after 5 ticks (5 seconds), turn off autonomous mode

> **Why increment first, then check?** If you checked first, on tick 1 the count would still be 0 — you'd never reach your threshold accurately. Incrementing first means tick 1 → count = 1, tick 5 → count = 5, tick 6 → count = 6 and the condition fires.

> **Why use a MyBlock?** Keeping the tick logic separate means you can easily change what happens each second — add a sound, change the light colour, anything — without touching the timer structure. It also fits the same function-calling-function pattern used throughout: each named block handles one responsibility.

---

## Step 3 — Create the repeating 1-second tick

Edit the when `timer > 5 block`:

```
when timer > 1
  timer tick
  reset timer
```

<img width="245" height="206" alt="image" src="https://github.com/user-attachments/assets/77f2f801-19bb-4cb9-b258-aae6289021ca" />


> **Why reset the timer to 1 instead of 5?** You're no longer waiting for a single 5-second event. Instead, you reset every 1 second — creating a repeating pulse. Each time the timer exceeds 1 second, `timer tick` runs and the clock resets, so it fires again after another second. This event fires independently of the forever loop, just like the button events — the robot keeps sensing and reacting while the ticks happen in the background.

---



## Expected result

```
When Right button pressed
  set autonomous mode to 1
  set timer count to 0
  reset timer

when timer > 1
  timer tick
  reset timer

define timer tick
  set timer count to (timer count + 1)
  write timer count
  if timer count > 5 then
    set autonomous mode to 0
```
<img width="1068" height="846" alt="image" src="https://github.com/user-attachments/assets/c6c9dc91-427f-408c-b740-7303b876f66f" />

---

## Test it ✓

1. Press **Right**. The hub display should show **1**, then **2**, then **3**... each roughly one second apart.
2. At **6** (when count exceeds 5), the robot should stop automatically.
3. Press **Right** again — the display should reset to **1** and count up again.

**If the count jumps or skips numbers:** the `when timer > 1` block may be firing multiple times before the reset catches up. This is a known quirk — try reducing the threshold slightly (e.g. `when timer > 0.9`) or restructuring so the reset is the very first block inside the hat.

**If the count never resets:** make sure `set timer count to 0` is in the **Right button** block, not just in `timer tick`.

---

## Extension challenge

Can you make the robot display a countdown instead of a count-up? Hint: display `(5 - timer count)` instead of `timer count`, and stop when it reaches 0.
