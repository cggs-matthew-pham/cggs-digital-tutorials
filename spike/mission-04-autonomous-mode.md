# Mission 04 — Autonomous Mode Toggle

## What you're building

You'll add the ability to turn autonomous (self-driving) mode on and off using the hub's left and right buttons. This gives you a manual override — useful for testing, and for simulating a supervised robot that a human can pause and restart.

---

## What you need

- Everything from Mission 03
- No extra hardware — you're using the buttons built into the SPIKE Prime hub

---

## A new way of thinking about your program

So far your robot has run continuously from the moment the program starts. But real robots need to handle multiple situations — following a line, stopping at obstacles, responding to colour, and now responding to a human operator.

One approach is to write a long sequence: do this, then this, then this. This feels simple at first but breaks down quickly — while the robot is waiting on a timed step in a sequence, it can't respond to sensors. Students who tried this last year found it worked for simple cases, but as complexity grew it became very difficult to have the robot follow a preprogrammed route *and* respond to live sensor events at the same time.

The approach we've been building toward is different: the `forever` loop keeps running and reading sensors on every iteration, and a **mode variable** controls *what the robot does with those readings*. Switching modes is just changing a number — the sensing never stops.

This mission makes the mode pattern explicit.

---

## Step 1 — Create the `autonomous mode` variable

Create a new variable called **autonomous mode**.

In your **When Program Starts** block, add:

- `set autonomous mode to 0`

> **Why start at 0?** We're using 0 to mean "off" (stopped) and 1 to mean "on" (running). Starting at 0 means the robot waits for you to deliberately activate it — it won't just take off the moment you press play.

---

## Step 2 — Add button event blocks

Add two new hat blocks (these sit separately from your main stack):

**When Left button pressed:**
- `set autonomous mode to 0`

**When Right button pressed:**
- `set autonomous mode to 1`

> **Why use separate event blocks instead of checking buttons inside the loop?** Button presses can happen at any time — even while the robot is mid-movement. Event blocks respond immediately, regardless of where the main loop is up to. Checking inside the loop would mean the button only registers when the loop reaches that point. This is also what makes the mode pattern powerful: the event block changes the variable instantly, and the very next loop iteration picks up the change.

---

## Step 3 — Create the `run autonomous mode` MyBlock

Create a new MyBlock called **run autonomous mode**. Inside it:

```
if autonomous mode = 1 then
  turn on (full brightness)
  yellow square
else
  turn on (dim / off pattern)
  stop moving
```

> **Why a MyBlock for the mode check?** The main loop just calls `run autonomous mode` and doesn't need to know what's inside it. This is the same function-calling-function pattern from missions 2 and 3 — each MyBlock handles one layer, calling the next layer down. The benefit grows as your program gets more complex: to add a new mode, you add a new MyBlock and insert it into the chain. To remove one, you take it out. The rest of the program doesn't change.

> **Why no `else if`?** Word Blocks only has `if / else`, not `else if`. The function-calling-function pattern is our way of achieving multiple modes cleanly without nesting `if` blocks inside `if` blocks, which becomes very hard to read and debug.

---

## Step 4 — Update the main loop

Replace the old `if distance < 10` logic in the `forever` loop with a call to `run autonomous mode`:

```
forever
  set light to [E] reflected light
  set distance to [C] distance in cm
  set colour to [E] colour
  run autonomous mode
```

`run autonomous mode` now handles everything: if mode is 1, it passes control to `yellow square`, which checks colour and falls through to `line follow`; if mode is 0, it stops.

---

## Expected result

```
When Program Starts
  turn on (full brightness)
  set movement motors to A+B
  set movement speed to 20%
  set autonomous mode to 0
  forever
    set light / distance / colour
    run autonomous mode

When Left button pressed → set autonomous mode to 0
When Right button pressed → set autonomous mode to 1
```

---

## Test it ✓

1. Start the program. The robot should sit still (mode = 0).
2. Press the **Right** button. The robot should start line following.
3. Press the **Left** button. The robot should stop immediately.
4. Press Right again — it should resume.

**If the robot doesn't stop instantly:** check that your left button event block is correctly set to `set autonomous mode to 0`, and that `run autonomous mode` checks the variable on every loop iteration.
