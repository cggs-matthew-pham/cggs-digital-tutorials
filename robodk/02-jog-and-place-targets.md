# Jog the Robot and Place Targets

**Goal:** Move the simulated robot using joint sliders and teach target positions that a program can move between.

**Prerequisites:**
- RoboDK open with `mycobot280_unit_station.rdk` loaded (see [01 — Launch and Open Station](./01-launch-and-open-station.md))

---

## 1. Open the robot panel

Double-click the robot (**Elephant Robotics myCo...**) in the station tree. The robot panel opens, showing Cartesian Jog controls at the top and **Joint axis jog** sliders at the bottom.

<!-- screenshot: robot jog panel with joint sliders visible -->

You'll see six sliders labelled **θ1** through **θ6** — one per joint. Each shows the current angle and its limits.

## 2. Jog using joint sliders

Drag a slider or type a value to move a single joint:

- **θ1** rotates the base (swings the whole arm left/right)
- **θ2** tilts the shoulder (raises/lowers the upper arm)
- **θ3** bends the elbow
- **θ4, θ5, θ6** orient the wrist

Try moving **θ1** to 30° and back to 0° to see the base swing. Then try **θ2** — notice how the arm rises and falls.

<!-- screenshot: arm in a different pose after jogging θ1 and θ2 -->

**Tip:** Click **Home** in the panel to return all joints to their default position.

## 3. Check the active reference frame

Before teaching a target, make sure the **Reference Frame** dropdown (in the Cartesian Jog section) is set to **Work Area**. Targets are stored relative to whichever frame is active — using the wrong one means the target moves if the frame moves.

<!-- screenshot: Reference Frame dropdown showing Work Area selected -->

## 4. Teach your first target

1. Jog the arm to a position where the gripper is over the work area — try **θ1 ≈ 20°**, **θ2 ≈ -25°**, **θ3 ≈ -66°** as a starting point.
2. Go to **Program → Teach Target** (or press **Ctrl+T**).

<!-- screenshot: Program menu with Teach Target highlighted -->

3. A new target appears in the station tree under **Work Area**. Rename it (double-click the name or press **F2**) — call it something descriptive like `MyTarget1`.

<!-- screenshot: new target in station tree, renamed -->

## 5. Teach more targets

Repeat for two more targets:

1. **A higher position** — keep θ1 the same, raise the arm by increasing θ2 (try -10°). Teach Target → rename `MyTarget2`. This could serve as an approach or retract pose.
2. **A position to one side** — swing θ1 to about 60–70° so the base rotates. Teach Target → rename `MyTarget3`. This could be a "place" position.

You should now have three targets under Work Area, each at a different position.

<!-- screenshot: three new targets in station tree -->

**Tip:** Click on any target in the tree — the arm snaps to that pose so you can check where it is.

## 6. Verify your targets

Click through your targets one by one. For each one, check:

- The arm reaches the position without turning red or showing a warning (that means it's out of reach or hitting a joint limit)
- The targets are clearly separated — they should represent distinct positions the arm would move between

If a target is unreachable, double-click it, then jog to a better pose and go to **Program → Teach Target** to re-record it at the current position.

---

## Key concepts

- **Joint jog** moves one motor at a time — useful for big repositioning
- **Targets** record the arm's full pose (all six joint angles) relative to the active reference frame
- Targets taught relative to **Work Area** stay consistent if the work-area frame is repositioned later — they move with it
- The arm's reach is 280mm, so keep targets reasonably close to the base

## What's next

In the next tutorial you'll add these targets to a program so the arm moves between them automatically.
