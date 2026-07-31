# A Board Made of Numbers

> One square from a position. Nine squares from a formula. This tutorial
> turns a board into arithmetic instead of nine typed positions, the same
> move as Tutorial 03, just applied to a whole grid.

---

**Teacher note**

- **Mode:** sync, whole class.
- **Genuinely new:** deriving a set of positions from two constants and a
  loop, instead of typing each one.
- **The plant, ship this exactly:** `ORIGIN_X = 90.0` below is not a safe
  choice. It works for every tutorial up to Tutorial 09, then fails there
  on purpose. Do not fix it early, and do not let students fix it early
  even if they ask why the board sits close to the base. The honest
  answer at this point in the arc is genuinely "we'll get to that", not a
  dodge.
- **Verify before teaching:** confirm these exact constants still keep
  squares reachable at hover height on your install (they should; this
  was checked against real hardware). If your station's mounting differs
  enough that squares are unreachable even at hover, the trap needs
  different numbers and Tutorial 09's diagnosis needs re-checking too.

---

## Before you start

RoboDK open, Tutorial 03's station.

## Step 1: One square, from a formula

Create a new file, `04_board_grid.py`. Step 2's block ADDS to the end
of this file.

```python
from robodk.robolink import Robolink, ITEM_TYPE_ROBOT
from robodk.robomath import xyzrpw_2_pose

RDK = Robolink()
robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception('No robot found. Load the myCobot 280 into the station.')

home = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
robot.MoveJ(home)

# The board's whole geometry lives in these two numbers.
ORIGIN_X = 90.0
ORIGIN_Y = -45.0
PITCH = 45.0
HOVER_Z = 150.0
ORIENTATION = [180.0, 0.0, 0.0]

def square_xy(index):
    """Squares numbered 1-9, near-left to far-right."""
    row = (index - 1) // 3
    col = (index - 1) % 3
    return ORIGIN_X + row * PITCH, ORIGIN_Y + col * PITCH

def square_pose(index, z=HOVER_Z):
    x, y = square_xy(index)
    return xyzrpw_2_pose([x, y, z] + ORIENTATION)

x, y = square_xy(1)
print(f'Square 1 computed at X {x:.1f}  Y {y:.1f}')
robot.MoveJ(square_pose(1))
```

Run it. Nothing about square 1's position was typed directly, it fell out
of `ORIGIN_X`, `ORIGIN_Y`, and the formula.

## Step 2: Nine squares, one loop

```python
print('Visiting all nine squares.')
for index in range(1, 10):
    robot.MoveJ(square_pose(index))
    print(f'  at square {index}')

robot.MoveJ(home)
```

Run it, watching the 3D view.

```mermaid
flowchart LR
    A["ORIGIN_X, ORIGIN_Y, PITCH<br>(two positions, one gap)"] --> B["square_xy(index)"] --> C["nine positions,<br>none typed by hand"]
```

**Try this:** change `PITCH` to `30` and re-run. Every square moves.
Nothing else in the script changed.

## What you built

A whole board from two numbers and a formula, instead of nine hand-placed
targets, the exact thing Tutorial 00 made you feel the cost of doing by
hand.

**One honest note before you move on:** we haven't picked `ORIGIN_X = 90`
for any deep reason, it's a placeholder. Choosing a genuinely good board
position turns out to be a real, non-obvious problem. We're setting it
aside for now and coming back to it properly a few tutorials from here.

**Next:** Tutorial 05, checking whether a position is actually reachable
before sending the arm there.
