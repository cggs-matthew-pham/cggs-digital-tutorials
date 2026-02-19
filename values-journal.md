# **Values Journal Tutorial**

**Celebrate moments when you demonstrate our core values**

---

## **Part 1: Setup and Layout**

### **1. Create New Project**
1. Open Construct 3
2. Click **New**
3. Project name: **Values Journal**
4. Click **Create**

<img width="376" height="297" alt="image" src="https://github.com/user-attachments/assets/54f3e345-be0a-4886-a8ce-7c6505968722" />

---

### **2. Add Title Text**
1. Right-click layout → **Insert New Object** → **Text**
2. Properties:
   - **Name**: TextTitle
   - **Text**: "Values Journal"
   - **Size**: 36, centered
3. Position at top of layout

![ValuesTitleAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/ValuesTitleAnimation.gif)

---

### **3. Add Instructions Text**
1. Insert another **Text** object
2. Properties:
   - **Name**: TextInstructions
   - **Text**: "Which value did you demonstrate today?"
   - **Size**: 18, centered
3. Position below title

<img width="329" height="115" alt="image" src="https://github.com/user-attachments/assets/8a0de1c6-19b2-4d02-9160-fc0850613767" />


---

### **4. Add Value Sticker Sprites**
Insert 4 **Sprite** objects for each core value:

**Sprite 1:**
- **Name**: SpriteRespect
<img width="445" height="397" alt="image" src="https://github.com/user-attachments/assets/f21b889a-71d7-4a9a-8fe1-4aaa86e15f0c" />



**Sprite 2:**
- **Name**: SpriteIntegrity
<img width="354" height="359" alt="image" src="https://github.com/user-attachments/assets/1149009e-46dd-4a5a-b053-b920797d4679" />



**Sprite 3:**
- **Name**: SpriteInclusion
<img width="412" height="409" alt="image" src="https://github.com/user-attachments/assets/490614ef-bd36-4614-bacd-32cf538bd3da" />


**Sprite 4:**
- **Name**: SpriteCourage
<img width="378" height="399" alt="image" src="https://github.com/user-attachments/assets/70a44180-a13f-425d-a81f-5d32ddda4c79" />


![[Screenshot - Value Stickers]]

---

### **5. Add Description Text Input**
1. Insert **Text Input** object
2. Properties:
   - **Name**: TextInputDescription
   - **Placeholder**: "What did you do? (e.g., I helped a friend)"
3. Position below stickers

![[Screenshot - Description Input]]

---

### **6. Add Save Button**
1. Insert **Button** object
2. Properties:
   - **Name**: ButtonSave
   - **Text**: "Add to My Journal"
3. Position below text input

![[Screenshot - Save Button]]

---

### **7. Add View Journal Button**
1. Insert **Button** object
2. Properties:
   - **Name**: ButtonViewJournal
   - **Text**: "View My Journal"
3. Position below Save button

![[Screenshot - View Journal Button]]

---

## **Part 2: Create Array and Global Variable**

### **8. Add Array Object**
1. Right-click layout → **Insert New Object** → **Array**
2. Properties:
   - **Name**: ArrayValueEntries
   - **Width**: 0 (starts empty)
   - **Height**: 1
   - **Depth**: 1

![[Screenshot - Array Object]]

---

### **9. Add Global Variable**
1. Open **Event Sheet**
2. Right-click → **Add global variable**
3. Properties:
   - **Name**: SelectedValue
   - **Type**: Text
   - **Initial value**: "" (empty)

![[Screenshot - Global Variable]]

---

## **Part 3: Event Logic - Selecting Values**

### **10. Event: Click Respect Sticker**
1. Add event → **SpriteRespect** → **On clicked**
2. Add action → **System** → **Set value**
   - Variable: **SelectedValue**
   - Value: **"Respect"**

![[Screenshot - Respect Event]]

---

### **11. Repeat for Other Values**
Create similar events for:
- **SpriteIntegrity** → Set SelectedValue to "Integrity"
- **SpriteInclusion** → Set SelectedValue to "Inclusion"
- **SpriteCourage** → Set SelectedValue to "Courage"

![[Screenshot - All Value Events]]

---

## **Part 4: Saving to Array**

### **12. Event: Save Button Clicked**
1. Add event → **ButtonSave** → **On clicked**
2. Add action → **ArrayValueEntries** → **Push**
   - Where: **Back**
   - Value: **SelectedValue**
   - Type: **X axis**
3. Add action → **ArrayValueEntries** → **Push**
   - Where: **Back**
   - Value: **TextInputDescription.Text**
   - Type: **X axis**
4. Add action → **TextInputDescription** → **Set text**
   - Text: **""** (clear the input for next entry)

**What this does:** Saves the value name first, then saves the description. Each journal entry uses two array slots.

![[Screenshot - Save Event]]

---

### **13. Test Part 1**
1. Press **F5** to run
2. Click a value sticker
3. Type a description in the text input
4. Click **Add to My Journal**
5. Add several more entries
6. Check array in debugger (F12) - should show values and descriptions alternating

![[Screenshot - Debug Array]]

---

## **Part 5: Create Journal Layout**

### **14. Add Second Layout**
1. Right-click in Project panel → **Add** → **Layout**
2. Name: **LayoutJournal**

![[Screenshot - Add Layout]]

---

### **15. Add Journal Title**
1. On LayoutJournal, insert **Text** object
2. Properties:
   - **Name**: TextJournalTitle
   - **Text**: "My Values Journal"
   - **Size**: 48, centered, bold
3. Position at top

![[Screenshot - Journal Title]]

---

### **16. Add List Object**
1. Insert **List** object
2. Properties:
   - **Name**: ListValueHistory
   - Position: Center of layout
   - Make it large enough to show multiple entries

![[Screenshot - List Object]]

---

### **17. Add Back Button**
1. Insert **Button** object
2. Properties:
   - **Name**: ButtonBack
   - **Text**: "Back"
3. Position at bottom

![[Screenshot - Back Button]]

---

## **Part 6: Navigation and Display Logic**

### **18. Event: Navigate to Journal**
1. Switch to Event Sheet (for Layout 1)
2. Add event → **ButtonViewJournal** → **On clicked**
3. Add action → **System** → **Go to layout**
   - Layout: **LayoutJournal**

![[Screenshot - Navigate Event]]

---

### **19. Event: Display Value History**
1. Add event → **System** → **On start of layout**
2. Add action → **ListValueHistory** → **Clear**
3. Add sub-event → **System** → **For each ArrayValueEntries**
   - This creates a loop through every item
4. Add action to sub-event → **ListValueHistory** → **Add item**
   - Text: **ArrayValueEntries.At(loopindex)**

**Note:** This will display all entries in order - values and descriptions will appear on separate lines. It's a simple approach that shows how arrays store data sequentially.

![[Screenshot - Display Logic]]

---

### **20. Event: Navigate Back**
1. Add event → **ButtonBack** → **On clicked**
2. Add action → **System** → **Go to layout**
   - Layout: **Layout 1**

![[Screenshot - Back Event]]

---

## **Part 7: Final Testing**

### **21. Test Complete App**
1. Press **F5**
2. Click a value sticker
3. Type what you did (e.g., "I helped someone in class")
4. Click **Add to My Journal**
5. Add at least 3-4 more entries with different values and descriptions
6. Click **View My Journal**
7. Notice how the list shows values and descriptions on separate lines
8. Click **Back** and add more entries

![[Screenshot - Final Result]]

---

## **Success Criteria**
✔ I can click value stickers to select which value I demonstrated  
✔ I can type a description of what I did  
✔ I can save values and descriptions to an array  
✔ I can view a list showing all my entries  
✔ I can navigate between the main screen and my journal

---

## **Reflection Questions**
- What do you notice about how the list displays your entries?
- Can you think of ways to make the display clearer (hint: grouping values with their descriptions)?
- Why might storing data this way become challenging as you add more entries?
