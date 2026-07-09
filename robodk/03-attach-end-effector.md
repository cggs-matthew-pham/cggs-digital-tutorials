# Attach an End-Effector and Set the Work-Area Frame

**Goal:** Add a tool (end-effector) to the robot and create a reference frame that represents your work surface, so targets are taught to the right point and stored in the right coordinate space.

**Prerequisites:**
- RoboDK open with `mycobot280_unit_station.rdk` loaded (see [01 — Launch and Open Station](./01-launch-and-open-station.md))
- Comfortable jogging the robot (see [02 — Jog and Place Targets](./02-jog-and-place-targets.md))

---

## Part A — Reference Frames

### 1. What is a reference frame?

A reference frame is a coordinate system — an origin point with X, Y, Z axes. When you teach a target, its position is stored *relative to the active reference frame*. If you later move the frame, all its targets move with it.

The station already has a **Work Area** frame positioned in front of the robot. In this section you'll inspect it and understand what it controls.

### 2. Inspect the Work Area frame

Double-click **Work Area** in the station tree. A panel opens showing its position relative to the station:

<!-- screenshot: Work Area frame panel showing X, Y, Z values -->

The six values are X, Y, Z (position in mm) and three rotation angles. The current values place the frame 200mm in front of the robot base — roughly where a tabletop work surface would sit.

### 3. See how frames affect targets

Try this experiment:

1. Note where your targets sit in the 3D view.
2. Double-click **Work Area** and change the **X** value by 50mm.
3. Watch the targets — they move with the frame, because they're stored relative to it.
4. Change X back to its original value.

This is why reference frames matter: they let you reposition an entire work area (and all its targets) without re-teaching every target individually.

---

## Part B — End-Effectors (Tools)

### 4. What is a tool / TCP?

A tool in RoboDK represents whatever is attached to the robot's flange — a gripper, suction cup, pen holder, etc. The **Tool Centre Point (TCP)** is the offset from the flange to the working tip. When you teach a target, RoboDK records where the *TCP* is, not where the flange is.

The station already has a **Gripper** tool attached. In this section you'll inspect it and understand the TCP.

### 5. Inspect the Gripper tool

Double-click **Gripper** in the station tree (nested under the robot). A panel opens:

<!-- screenshot: Gripper tool panel showing TCP values -->

Key fields:
- **Tool Center Point with respect to** — should show the robot flange
- **Z value** — the TCP offset along the tool axis (currently 70mm, estimating where gripper fingertips would sit)
- **Show TCP** checkbox — toggle this to see/hide the TCP marker in the 3D view

### 6. Understand TCP offset

The TCP offset tells RoboDK "the working point is 70mm out from the flange." This matters because:

- Targets are taught to the TCP, not the flange
- If you change the TCP (e.g. swapping to a longer tool), existing targets aim at a different physical point
- When the real gripper is measured, this value gets updated to match

### 7. Try swapping the active tool

The robot panel's **Tool Frame** dropdown (at the top, in the Cartesian Jog section) shows which tool is currently active:

<!-- screenshot: Tool Frame dropdown in robot panel -->

If you had multiple tools (gripper + suction + pen), you'd switch between them here. The active tool determines which TCP is used when teaching new targets.

---

## Part C — Adding your own (optional extension)

### 8. Add a new reference frame

1. Right-click **mycobot280_unit_station** (the station, at the top of the tree).
2. Select **Add Reference Frame...**

<!-- screenshot: right-click menu showing Add Reference Frame -->

3. A new frame appears. Rename it (e.g. `My Frame`).
4. Double-click it to position it — try X=150, Y=100, Z=0 to place it offset from the existing Work Area.

### 9. Add a new tool

1. Go to **Program → Add Tool (TCP)**.
2. A new tool appears under the robot. Rename it (e.g. `My Tool`).
3. Double-click it to see the TCP panel. Try setting Z to a different value (e.g. 50mm) and notice how it changes where targets would be taught.

**Important:** When you add a tool, make sure it's **nested under the robot** in the station tree. If it appears at the station level instead, drag it onto the robot so RoboDK treats it as an attached end-effector.

<!-- screenshot: correct vs incorrect tool placement in tree -->

---

## Key concepts

- **Reference frames** define coordinate spaces — targets are stored relative to them, so moving a frame moves all its targets
- **Tools / TCP** define the working point on the end-effector — targets are taught to the TCP, not the flange
- Always check the **active reference frame** and **active tool** before teaching targets — using the wrong one means targets end up in the wrong coordinate space
- A tool must be **nested under the robot** in the tree to be treated as an attached end-effector

## What's next

With frames, tools, and targets understood, you're ready to build programs that move the robot between targets automatically.
