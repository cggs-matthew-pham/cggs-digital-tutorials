---
title: A Real Board
subtitle: "Tutorial 04, The Board Game Robot"
---

# A Real Board

> Tutorial 03 pointed at a square that doesn't exist yet, just a
> position in empty space. This tutorial gives it an actual shape you
> can see: a board, and a piece to go with it. Upgrading v1 again, the
> same square now has something real sitting where it points.

<details>
<summary>Teacher note</summary>

**Mode:** sync, whole class.

**Genuinely new:** `AddShape`, building geometry from a raw list of
triangle vertices. There is no `AddBox` shortcut in the API, the
triangle list *is* the work. The reason 3 points, not 4 or more: any
three points always describe exactly one flat plane, no ambiguity;
four points might not even lie flat. This is also why GPUs only ever
render triangles, not a RoboDK quirk.

**No deliberate error in the core path.** The genuine payoff of this
tutorial is Step 3, a raw hand-built shape compared against the same
shape via a general-purpose function, and finding they're *not* built
from the same number of triangles even though they look identical.
That's a real result, not a bug to fix, worth letting land as a
finding, not glossing over.

**Verify before teaching:** confirm `AddShape` accepts a plain Python
list of `[x, y, z]` triples directly on your RoboDK version (it does on
ours). Some versions may want an explicit `robodk.robomath.Mat` first.

</details>

## Before you start

RoboDK open, Tutorial 03's station.

## Step 1: A box, every point typed out

Create a new file called `04_a_real_board.py`.

```python
from robodk.robolink import Robolink, ITEM_TYPE_ROBOT
from robodk.robomath import transl

RDK = Robolink()
robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception('No robot found. Load the myCobot 280 into the station.')

OBJECT_NAMES = ['Board plate', 'Piece 0']   # Piece 0 doesn't exist yet,
for name in OBJECT_NAMES:                    # Step 3 builds it. Listed
    existing = RDK.Item(name)                # here now so reruns after
    if existing.Valid():                     # Step 3 clean up both.
        existing.Delete()

# A box has 6 flat faces. Each face is a rectangle, split into 2
# triangles. 6 faces x 2 triangles = 12 triangles, 36 points, in
# groups of 3. That's all AddShape wants, points grouped in threes,
# one group per triangle. It has no idea this is meant to be a board.

width, depth, height = 160, 160, 6
x, y = width / 2, depth / 2

triangles = [
    # bottom face
    [-x, -y, 0], [x, -y, 0], [x, y, 0],
    [-x, -y, 0], [x, y, 0], [-x, y, 0],
    # top face
    [-x, -y, height], [x, -y, height], [x, y, height],
    [-x, -y, height], [x, y, height], [-x, y, height],
    # front face
    [-x, -y, 0], [x, -y, 0], [x, -y, height],
    [-x, -y, 0], [x, -y, height], [-x, -y, height],
    # back face
    [-x, y, 0], [x, y, 0], [x, y, height],
    [-x, y, 0], [x, y, height], [-x, y, height],
    # left face
    [-x, -y, 0], [-x, y, 0], [-x, y, height],
    [-x, -y, 0], [-x, y, height], [-x, -y, height],
    # right face
    [x, -y, 0], [x, y, 0], [x, y, height],
    [x, -y, 0], [x, y, height], [x, -y, height],
]

board = RDK.AddShape(triangles)
if not board.Valid():
    raise Exception('AddShape failed. Check the triangle list.')

board.setName('Board plate')
board.Recolor([0.75, 0.7, 0.6, 1.0])
board.setPose(transl(150, 0, 94))

print('Board built.')
```

Run it. You should see a flat plate appear in the 3D view, roughly
where square 5 was pointing back in Tutorial 03.

## Step 2: The same idea, wrapped in a function

Retyping those 36 points for every different-sized shape would get old
fast. Add this function above your board code, then replace the raw
`triangles = [...]` list with a call to it:

```python
def box_triangles(width, depth, height):
    """Exactly the same 36 numbers as the raw version above, just
    given a name so we don't retype them every time."""
    x, y = width / 2, depth / 2
    bottom = [(-x, -y, 0), (x, -y, 0), (x, y, 0), (-x, y, 0)]
    top = [(-x, -y, height), (x, -y, height), (x, y, height), (-x, y, height)]
    triangles = []

    def quad(a, b, c, d):
        for point in (a, b, c, a, c, d):
            triangles.append(list(point))

    quad(*bottom[::-1])
    quad(*top)
    for i in range(4):
        a, b = bottom[i], bottom[(i + 1) % 4]
        c, d = top[(i + 1) % 4], top[i]
        quad(a, b, c, d)
    return triangles
```

Change `triangles = [...]` to `triangles = box_triangles(width, depth,
height)`. Run it again. Same board, same position, nothing about the
result should change, and it doesn't, for a box, the function produces
exactly the same 36 points either way.

## Step 3: A round piece, and a genuine surprise

A piece doesn't need independent width and depth the way a board does,
it just needs a radius. Add this function too:

```python
from math import cos, sin, pi

def prism_triangles(radius, height, segments=16):
    """A round-based prism. High segment counts, the default 16, read
    as a smooth cylinder. Low counts give regular polygon prisms
    instead, segments=3 is a triangular prism, segments=6 a hexagonal
    one."""
    angles = [2 * pi * i / segments for i in range(segments)]
    bottom = [(radius * cos(a), radius * sin(a), 0) for a in angles]
    top = [(radius * cos(a), radius * sin(a), height) for a in angles]
    centre_bottom, centre_top = (0, 0, 0), (0, 0, height)
    triangles = []
    for i in range(segments):
        j = (i + 1) % segments
        triangles += [list(bottom[i]), list(bottom[j]), list(top[j])]
        triangles += [list(bottom[i]), list(top[j]), list(top[i])]
        triangles += [list(centre_bottom), list(bottom[j]), list(bottom[i])]
        triangles += [list(centre_top), list(top[i]), list(top[j])]
    return triangles

piece = RDK.AddShape(prism_triangles(radius=12, height=15))
piece.setName('Piece 0')
piece.Recolor([0.2, 0.4, 0.9, 1.0])
piece.setPose(transl(100, -120, 100))

print('Piece built.')
```

Run it. A round piece appears. `segments=3` instead of the default
would give you a triangular piece from the exact same function, no new
code needed, a "cylinder" is really just a many-sided prism.

Here's the surprise, worth checking rather than trusting: at
`segments=3`, does this function build a piece from the same number of
triangles a hand-typed triangular prism would? A triangle base has only
3 corners, one flat triangle, no splitting required. But
`prism_triangles` always fans every cap from a centre point, since
that's the only approach that still works once a shape has more than 3
sides. For 3 sides specifically, that fan is 3 small triangles doing a
job one already could.

```python
hand_typed = 8      # 2 flat caps + 6 side-wall triangles
via_function = len(prism_triangles(15, 20, segments=3)) // 3
print('Hand-typed count:', hand_typed)
print('Function count:', via_function)
```

Run it. The counts differ, 8 versus 12, even though both build the
exact same visible shape. **Correct and identical-looking are not
the same claim as identical.** A general-purpose function can cost more
than a hand-built one, in exchange for working on shapes the hand-built
version never could.

## What you built

A real board and a real piece, both visible objects in the station,
not points you have to trust are somewhere. And a genuine result about
the cost of generality: functions built to handle many cases aren't
always the cheapest way to handle one specific case, worth checking,
not assuming.

**Next:** Tutorial 05, turning one board and one piece into a whole
grid of squares, using nothing but a formula.
