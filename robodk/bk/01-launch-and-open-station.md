# Launch RoboDK and Open the Provided Station

**Goal:** Open RoboDK, load the unit station file, and get oriented — find the robot, its targets, and the program in the station tree so you can run the demo.

**Prerequisites:**
- RoboDK installed ([download here](https://robodk.com/download))
- The provided station file: `mycobot280_unit_station.rdk`

---

## 1. Launch RoboDK

Open RoboDK from your Applications folder (Mac) or Start menu (Windows). You'll see an empty station with just a station item at the top of the tree.

## 2. Open the station file

Go to **File → Open** (or **Ctrl+O** / **⌘+O**), browse to `mycobot280_unit_station.rdk`, and open it.

Alternatively, drag and drop the `.rdk` file into the RoboDK window.

## 3. Read the station tree

The station tree (left panel) shows everything in the station. You should see:

<img width="261" height="386" alt="image" src="https://github.com/user-attachments/assets/bbb5fe65-97a7-4dd1-8eea-78e8edbd9997" />


From top to bottom:
- **mycobot280_unit_station** — the station itself
- **Elephant Robotics myCobot-...** — the robot's base reference frame
  - **Elephant Robotics myCo...** — the robot arm
    - **Gripper** — the tool (end-effector) attached to the flange
- **Work Area** — the reference frame for the work surface
  - **Pick** — a target pose (where the arm picks up)
  - **Approach** — a target pose (hovering above Pick)
  - **Place** — a target pose (where the arm places down)
- **PickAndPlace** — the demo program

## 4. Explore the 3D view

The 3D view shows the arm and all the targets. Use the mouse to navigate:
- **Scroll wheel** — zoom in/out
- **Middle-click + drag** — pan
- **Right-click + drag** — rotate the view

Try clicking each target in the tree — the arm snaps to that position so you can see where each one is.

<img width="253" height="120" alt="image" src="https://github.com/user-attachments/assets/30f67530-90f2-434c-875d-de73f1a6077b" />


## 5. Run the demo program

Double-click **PickAndPlace** in the station tree (or right-click it → **Run**).

The arm moves through the sequence: Approach → Pick → Approach → Place. A simulation bar and estimated cycle time appear at the bottom.

**Success check:** the arm moves smoothly through all four targets with no error dialog.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Station opens but the arm isn't visible | Try **View → Fit to screen** or scroll out to zoom the view |
| `.rdk` file won't open | Check your RoboDK version matches the one the file was saved with |
| Exclamation marks on targets | The tool or reference frame is mismatched — ask your teacher |
