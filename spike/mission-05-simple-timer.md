# Mission 05 — Simple Timer

## What you're building

You'll add a time limit to autonomous mode. When the Right button is pressed, the robot activates and starts a timer. After 5 seconds, it automatically switches back to mode 0 and stops — as if the autonomous run has a fixed duration.

---

## What you need

- Everything from Mission 04
- No extra hardware — SPIKE Prime has a built-in timer

---

## How the SPIKE timer works

The SPIKE Prime hub has a built-in timer that starts counting from 0 when the program begins (or when you reset it). You can:

- `reset timer` — set it back to 0
- `when timer > X` — a hat block that fires once the timer exceeds X seconds

> **Important:** `when timer > X` is an event block, like a button press. It fires independently of your main loop — you don't need to check it inside `forever`. This means the timer can trigger events without pausing or interrupting your sensor-based loop. The robot keeps reading sensors and reacting while the timer runs in the background — another benefit of the forever loop + modes pattern over a sequential approach.

---

## Step 1 — Reset the timer when autonomous mode starts

In your **When Right button pressed** block, add `reset timer` after `set autonomous mode to 1`:

```
When Right button pressed
  set autonomous mode to 1
  reset timer
```

<img width="264" height="131" alt="image" src="https://github.com/user-attachments/assets/fd99ffe8-08d0-4992-b287-57bd05b9afc2" />


> **Why reset here?** You want the 5-second countdown to start from the moment the robot is activated, not from when the program started. Resetting on button press gives you a fresh count each time.

---

## Step 2 — Add the timeout event

Add a new hat block:

```
when timer > 5
  set autonomous mode to 0
```

That's it. When the timer exceeds 5 seconds, autonomous mode turns off automatically.

> **Why is this so simple?** The `when timer > X` block handles the waiting for you — you don't need a loop or a counter. The hub checks the timer in the background and triggers this stack when the condition is met, without blocking anything else.

---

## Expected result

```
When Right button pressed
  set autonomous mode to 1
  reset timer

When Left button pressed
  set autonomous mode to 0

when timer > 5
  set autonomous mode to 0
```

<img width="535" height="139" alt="image" src="https://github.com/user-attachments/assets/ae8d16d2-6a7e-49d0-bff3-c84241b4d617" />


The main loop and all other code stays the same.

<img width="1081" height="813" alt="image" src="https://github.com/user-attachments/assets/66481fd8-a4a7-4088-b300-ec055d80a5a5" />


---

## Test it ✓

1. Start the program. Robot sits still.
2. Press **Right**. Robot starts line following.
3. After 5 seconds, the robot should stop automatically without you pressing anything.
4. Press **Right** again — it should run for another 5 seconds.
5. Press **Left** at any point — it should stop immediately (before the 5 seconds is up).

**If it doesn't stop after 5 seconds:** make sure `reset timer` is in the Right button block. If the timer was already past 5 when you pressed Right, the `when timer > 5` event would fire almost immediately — resetting ensures a clean run each time.
