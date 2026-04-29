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

---

## Step 1 — Set up timer count

In your **When Right button pressed** block, add:

- `set timer count to 0`

(alongside the existing `set autonomous mode to 1`)

> **Why reset to 0 here?** Each time the robot activates, you want the countdown to start fresh from zero.

---

## Step 2 — Create the repeating 1-second tick

Add a new hat block:

```
when timer > 1
  timer tick
  reset timer
```

> **Why reset the timer to 1 instead of 5?** You're no longer waiting for a single 5-second event. Instead, you reset every 1 second — creating a repeating pulse. Each time the timer exceeds 1 second, `timer tick` runs and the clock resets, so it fires again after another second.

---

## Step 3 — Create the `timer tick` MyBlock

Create a new MyBlock called **timer tick**. Inside it:

```
set timer count to (timer count + 1)
write timer count
if timer count > 5 then
  set autonomous mode to 0
```

Breaking this down:

- `set timer count to (timer count + 1)` — increments the counter by 1 each tick
- `write timer count` — displays the current count on the hub's LED display so you can see it counting up
- `if timer count > 5` — after 5 ticks (5 seconds), turn off autonomous mode

> **Why increment first, then check?** If you checked first, on tick 1 the count would still be 0 — you'd never reach your threshold accurately. Incrementing first means tick 1 → count = 1, tick 5 → count = 5, tick 6 → count = 6 and the condition fires.

> **Why use a MyBlock?** Keeping the tick logic separate means you can easily change what happens each second — add a sound, change the light colour, anything — without touching the timer structure.

---

## Removing the old `when timer > 5` block

You no longer need the simple timer block from Mission 05:

```
when timer > 5       ← delete this
  set autonomous mode to 0
```

The `timer tick` MyBlock now handles the 5-second cutoff via the counter.

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
