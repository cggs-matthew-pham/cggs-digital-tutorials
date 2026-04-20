# **Year 7 Digital Design**

## **Create a Prototype Using Construct 3**

---

## **Learning Intention**

Students understand what a prototype is and learn how to build one using a layout and event sheet in Construct 3 for a **Daily Chores Checklist**.

## **Success Criteria**

✔ I can follow a tutorial in Construct 3 to create a basic prototype using a layout and event sheet.

---

# **1. What Is a Prototype?**

A **prototype** is a simple, early version of an app showing how it will look and work.  
It helps test ideas before building the complete product.

### **Construct 3 Components**

**Layout**  
– The visual screen where you place objects, text, buttons, and images.  
– It shows what the user will see.

**Event Sheet**  
– Contains **events and actions** that tell the app what to do.  
– Example: _"When checkbox clicked → show a tick."_

---

# **2. Create a New Project**

1. Open **Construct 3**
2. Click **New Project**
3. Project name: **Daily Chores Checklist**
4. Click **Create**

<!-- Screenshot: New Project dialog -->

---

# **3. Add a Title**

1. Double‑click the layout
2. Search for or choose **Text**
3. Click near the top of the screen
4. In the **Text** property, type: **My Daily Chores**
5. In **Properties**, update:
    - **Font size:** 28–36
    - **Horizontal Alignment:** Centre

<!-- Screenshot: Title text on the layout with properties panel -->

---

# **4. Plan Your Chores**

Decide on 3–5 chores, for example:

- Make my bed
- Feed the pet
- Homework
- Clean room
- Brush teeth

Add a new **Text** object for each chore on your list.

For each text box, update the **Name** property so it is clear which box is which (e.g. `Text_Bed`, `Text_Pet`).

<!-- Screenshot: Layout with list of chore text boxes, properties panel showing Name field -->

---

# **5. Create a Checkbox (Using a Button)**

### **Add the Checkbox Button**

1. Double‑click the layout
2. Choose **Button**
3. Place a button next to the first chore text box
4. In **Properties → Text**, paste the empty-box character: **⬜**
5. Resize the button to look like a small square

### **Rename the Button**

1. Click the button to select it
2. In **Properties**, find **Name**
3. Rename it to: **Checkbox_Bed**

<!-- Screenshot: Button placed next to chore text, properties panel showing Name and Text -->

---

# **6. Add the Tick (Event Sheet)**

Open **Event Sheet 1** from the **Project** panel.

### **Create the Event**

1. Click **Add event**
2. Choose **Checkbox_Bed**
3. Select **On clicked**

### **Add the Action**

1. Click **Add action**
2. Choose **Checkbox_Bed**
3. Select **Set text**
4. Set the text to: **"✅"** (between the quote marks)

This makes the checkbox show a tick when clicked.

<!-- Screenshot: Event sheet showing On clicked → Set text event -->

---

# **7. Repeat for Each Chore**

Repeat **Steps 5 and 6** for every chore in your list.

Make sure each button has a unique **Name** (e.g. `Checkbox_Pet`, `Checkbox_Homework`) and that each event uses the matching checkbox.

<!-- Screenshot: Event sheet with multiple On clicked events, one per checkbox -->

---

# **8. Test Your App**

1. Click the **Play** button (or press **F5**)
2. Click each checkbox
3. Check that each one shows a tick when clicked

<!-- Screenshot or GIF: App running, user clicking checkboxes -->

---

# **9. Optional Improvements**

Try one or more of these extensions:

- Change the colours of the text or background
- Add a **Reset** button that clears all ticks
- Show a message when all chores are done
- Make the tick **toggle off** when the checkbox is clicked again
