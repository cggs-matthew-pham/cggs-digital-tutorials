# **Year 7 Digital Design**

## **Create a Water Tracker App Using Construct 3**

---

## **Learning Intention**

Students understand how to use global variables, events, and actions in Construct 3 to build a functional app that tracks data and responds to user input.

## **Success Criteria**

✔ I can create a new Construct 3 project and set up the layout with UI objects.  
✔ I can create global variables to store and update data.  
✔ I can write events and actions that respond to button clicks.  
✔ I can use a condition to prevent values exceeding a set limit.  
✔ I can display dynamic feedback to the user based on their progress.

---

# **1. Create a New Project**

1. Open Construct 3 at **https://editor.construct.net**
2. Click **New Project**
3. Set Project name: **Daily Water Intake Tracker**
4. Click **Create**

<!-- SCREENSHOT: New project dialog with name field filled in -->

---

# **2. Create Global Variables**

Open the **Event Sheet**.

Right-click → **Add global variable** and create the following two variables:

**Variable 1**
- Name: **waterCount**
- Type: Number
- Initial value: **0**

**Variable 2**
- Name: **dailyGoal**
- Type: Number
- Initial value: **10**

These will track the number of glasses consumed and the daily target.

<!-- SCREENSHOT: Global variable dialog showing waterCount setup -->
<!-- SCREENSHOT: Event sheet showing both variables listed -->

---

# **3. Design the User Interface (UI)**

Go to the **Layout**.

### **Water Count Text**

1. Right-click → **Insert new object** → choose **Text**
2. Place near the top of the screen
3. Set default text: `Glasses of water today: 0 / 10`
4. Rename the object to **WaterText**

<!-- SCREENSHOT: Layout with WaterText placed near the top -->

### **Add Water Button**

1. Right-click → **Insert new object** → choose **Button**
2. Set button text: **Add Glass**
3. Resize and place near the middle of the screen
4. Rename to **AddWaterButton**

<!-- SCREENSHOT: Layout showing WaterText and AddWaterButton positioned -->

---

# **4. Create the Progress Bar**

1. Right-click → **Insert new object** → choose **Sprite**
2. Name it **ProgressBar**
3. Draw a horizontal rectangle and fill it blue
4. Set its width to **400px** — this represents a full glass count

Add a background bar:

1. Insert another Sprite — name it **ProgressBG**
2. Make it grey and the same size as ProgressBar
3. Right-click **ProgressBG** → **Send to back**, then align it behind ProgressBar

<!-- SCREENSHOT: Layout showing ProgressBG (grey) behind ProgressBar (blue) -->

---

# **5. Add a Reset Button**

1. Right-click → **Insert new object** → choose **Button**
2. Set button text: **Reset Day**
3. Place at the bottom of the screen
4. Rename to **ResetButton**

<!-- SCREENSHOT: Completed layout showing all UI elements: WaterText, AddWaterButton, progress bars, ResetButton -->

---

# **6. Add Logic – Drinking Water**

Open the **Event Sheet**.

### **Increase Water Count**

1. Right-click → **Add event** → **AddWaterButton → On clicked**
2. Add **Action**: **System → Add to variable**
   - Variable: **waterCount**
   - Value: **1**
3. Add a **sub-condition** to cap the count at the daily goal:
   - Click the condition to select it, then press **S**
   - Choose **System → Compare Variable**
   - Variable: **waterCount** | Comparison: **<** | Value: **dailyGoal**

This prevents the count from going above 10 glasses.

<!-- SCREENSHOT/GIF: Click the condition block, press S, then select System → Compare Variable -->

---

# **7. Reset Button Logic**

1. Right-click → **Add event** → **ResetButton → On clicked**
2. Add **Action**: **System → Set value**
   - Variable: **waterCount**
   - Value: **0**

<!-- SCREENSHOT: Reset event in the event sheet -->

---

# **8. Update the Display Every Tick**

1. Right-click → **Add event** → **System → Every tick**
2. Add **Action**: **WaterText → Set text**
   - Text: `"Glasses: " & waterCount & " / " & dailyGoal`

The display will now update automatically whenever the count changes.

<!-- SCREENSHOT: Every tick event showing the Set text action with the expression -->

---

# **9. Goal Completion Feedback**

### **Add a Motivational Message**

In the **Layout**:

1. Right-click → **Insert new object** → choose **Text**
2. Name it **MotivationalMessage**
3. Place it below the progress bar

In the **Event Sheet**:

1. Right-click → **Add event** → **System → Compare variable**
   - Variable: **waterCount** | Comparison: **=** | Value: **dailyGoal**
2. Add **Action**: **MotivationalMessage → Set text**
   - Text: `"🎉 Daily water goal achieved! Great job!"`
3. Click the condition to select it, then press **X** to add an Else branch
4. Add **Action**: **MotivationalMessage → Set text**
   - Text: `"Keep drinking water to reach your goal"`

<!-- SCREENSHOT/GIF: Click condition, press X, Else branch appears -->

---

# **10. Progress Bar Logic**

In the **Event Sheet**, find the **AddWaterButton → On clicked** event from Step 6.

Add another **Action**:
- **ProgressBar → Set width**
- Value: `(waterCount / dailyGoal) * 400`

This scales the blue bar to show how close the user is to their goal.

<!-- SCREENSHOT: On clicked event showing all actions including Set width -->

---

# **Test Your App**

1. Press **F5** to run the project
2. Click **Add Glass** — the count and progress bar should update
3. At 10 glasses, the success message should appear
4. Click **Reset Day** — the count should return to 0

<!-- SCREENSHOT: Running app showing progress bar partially filled and motivational message -->
