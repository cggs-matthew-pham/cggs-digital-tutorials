# The Board Game Robot

A tutorial series for programming the myCobot 280 in RoboDK, using Python.
By the end, you'll have a robot cell that can pick up pieces, place them
on a board, rearrange them, and play a game against you, and you'll have
hit (and fixed) the same real problems a robotics engineer would.

Work through them in order. Each one builds on the last, and several
problems are planted early on purpose, so skipping ahead means missing
the setup for later payoffs.

## The tutorials

| # | Tutorial | What you'll do |
|---|---|---|
| 00 | [Hands on the Arm](00-hands-on-the-arm.md) | Move the arm by hand in RoboDK, no code yet |
| 01 | [The Same Program, in Python](01-python-program.md) | The exact Tutorial 00 program again, this time in code |
| 02 | [Meet the Arm](02-meet-the-arm.md) | Connect from Python and read the arm's state |
| 03 | [First Move](03-first-move.md) | One joint, then the limit that hits almost immediately, then a position, point at a real square |
| 04 | [A Real Board](04-a-real-board.md) | Build the board and a piece as solid objects you can see |
| 05 | [A Board Made of Numbers](05-a-board-made-of-numbers.md) | A whole board from two numbers and a formula |
| 06 | [Check Before You Move](06-check-before-you-move.md) | Test reachability before sending any motion |
| 07 | [Down to the Surface](07-down-to-the-surface.md) | Descend and lift, and why straight lines matter |
| 08 | [Pick It Up](08-pick-it-up.md) | The full pick-and-place cycle |
| 09 | [The Move That Refused](09-the-move-that-refused.md) | Diagnose a move the arm refuses to make |
| 10 | [Where Should the Board Go?](10-where-should-the-board-go.md) | Find a board position that works everywhere |
| 11 | [The Control Panel](11-the-control-panel.md) | A window with buttons instead of editing scripts |
| 12 | [Your Game](12-your-game.md) | Game logic, then make the cell play *your* game |

## What you need

- RoboDK installed, with the Elephant Robotics myCobot 280 loaded from
  its online library (Tutorial 00 walks through this).
- Python. RoboDK ships its own; Tutorial 02 covers connecting from it.
- No robot hardware. Everything here runs in simulation. Real hardware is
  a later, separate stage.

**If a diagram won't load** (shows a spinner that never finishes): this
happens on some school Chrome profiles because of a browser extension, not
because of anything wrong with the page. Open the tutorial in an incognito
window (Ctrl+Shift+N) and it should render fine.

## How to get help when something breaks

Things will break, some on purpose. Before asking:

1. Read the error message, bottom line first. It usually names the
   problem.
2. Check which tutorial taught the thing that's failing, and re-check
   your code against its block.
3. If a function seems to not exist, ask Python what does:
   `print(dir(the_module))`. Tutorial 02 shows this trick.

---

*Teacher notes: verification items live at the top of each tutorial.
For the whole-arc overview, dependencies, and completion status, see
[TEACHERS-GUIDE.md](TEACHERS-GUIDE.md). Known gaps in this set:
screenshot slots are placeholders pending capture; Tutorial 00's
generated-code sample and Tutorial 10's Step 5 outcome are unverified
against a live station; the arc's fast-lookup reference guide is not
yet written.*
