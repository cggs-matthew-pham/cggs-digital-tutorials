# Hands on the Arm: A First Look at RoboDK

> You're building a robot that plays board games: it picks up a piece and
> puts it exactly where a game needs it, square by square, move by move.
> Everything in this arc is one app, growing. Today's job is the
> smallest one: touch the arm by hand and see it move, before any of that
> is code. This tutorial is short on purpose, just enough to have
> something real to compare against once Tutorial 01 starts typing.

---

**Teacher note**

- **Mode:** sync, whole class. One session, well under a full lesson.
- **Genuinely new:** nothing conceptual, this is orientation. The one idea
  worth naming out loud: everything here is *simulation*, the arm on
  screen, not physical hardware yet.
- **No deliberate errors this tutorial.** Save that pattern for Tutorial 01
  onward, once code is involved.
- **Verify before teaching:** confirm "Generate Robot Program" still
  produces pymycobot-flavoured output on the deployed RoboDK version. If
  the target vendor differs, the generated code sample below needs
  swapping.

---

## Before you start

- RoboDK open, station loaded with the myCobot 280.
- Nothing to install, nothing to type yet.

## Step 1: Move a joint by hand

Open the robot's control panel (double-click the robot in the station
tree). Find **Joint axis jog**.

- Drag one slider. Watch the arm move in the 3D view.
- Drag it back. Try a different joint.

> 📷 **Screenshot slot:** the Joint axis jog panel, one slider mid-drag,
> arm visibly moved in the 3D view behind it.

Six sliders, six joints. That's the whole idea: each one turns one motor.

## Step 2: Move by typing a position instead

Same panel, find **Cartesian Jog**, the section showing X, Y, Z and
rotation values.

- Change the X value. Press Enter.
- Watch the arm move, and watch the joint sliders from Step 1 update on
  their own.

> 📷 **Screenshot slot:** the Cartesian Jog panel, X field edited,
> highlighting that the joint values below changed too.

You didn't choose new joint angles. You typed *where you want the tool
tip to be*, and the arm worked out the angles itself. Keep that feeling in
mind, it's the whole point of Tutorial 01's second half.

## Step 3: One thing to notice, not explain yet

In the same panel, find **Other configurations**, near the bottom. It
shows a set of six numbers in brackets.

> 📷 **Screenshot slot:** the Other configurations section, dropdown
> visible.

Don't open it. Don't explain it. Just notice it's there. It'll matter a
lot more a few tutorials from now, in a way that'll make more sense once
you've hit the problem it solves.

## Step 4: Create two targets

- Right-click the robot → **Add Target**, at the arm's current position.
- Move the arm somewhere else (drag a slider or edit a coordinate).
- **Add Target** again.

You now have two targets in the station tree, two saved positions.

> 📷 **Screenshot slot:** station tree showing both targets, named and
> visible.

## Step 5: Build a two-move program

- Right-click the robot → **Add Program**.
- Select the program, then select Target 1 → click **Move Joint**.
- Select Target 2 → click **Move Joint** again.
- Press play. The arm should move between your two targets.

> 📷 **Screenshot slot:** the program in the tree with both move
> instructions listed, play button visible.

## Step 6: Turn it into Python

Right-click the program → **Generate Robot Program**. Pick pymycobot as
the target.

Open the file it creates. Somewhere in there, you'll see something close
to this:

```python
target_1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]      # your six numbers here
target_2 = [30.0, 0.0, -90.0, 0.0, 0.0, 0.0]   # and here

mc.send_angles(target_1, speed)
mc.send_angles(target_2, speed)
```

You didn't write that. Clicking built it.

> 📷 **Screenshot slot:** the generated file open in a text editor,
> the two move commands visible.

## What just happened

- Two ways to move the arm by hand: joint by joint, or by typing a
  position and letting the arm solve the angles.
- Two clicked targets became a real program, and that program became
  real Python.

Clicking works. It also doesn't scale, imagine doing this for nine board
squares by hand, then again if the board shifts two millimetres. Tutorial
01 onward writes the *positions* as numbers in code instead, the same
app, upgraded.

**Next:** Tutorial 01, the arm's turn to tell you where it is.
