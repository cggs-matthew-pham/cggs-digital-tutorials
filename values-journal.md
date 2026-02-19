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
It should look like:

<img width="329" height="115" alt="image" src="https://github.com/user-attachments/assets/8a0de1c6-19b2-4d02-9160-fc0850613767" />


---

### **4. Add Value Sticker Sprites**
Insert 4 **Sprite** objects for each core value:

**Sprite 1:**
- **Name**: SpriteIntegrity
<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/1149009e-46dd-4a5a-b053-b920797d4679" />

**Sprite 2:**
- **Name**: SpriteCourage
<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/70a44180-a13f-425d-a81f-5d32ddda4c79" />

**Sprite 3:**
- **Name**: SpriteRespect
<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/f21b889a-71d7-4a9a-8fe1-4aaa86e15f0c" />

**Sprite 4:**
- **Name**: SpriteInclusion
<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/c48da57c-4405-45f4-a281-229c138e6643" />

<br/>

It should look like:

<img width="440" height="194" alt="image" src="https://github.com/user-attachments/assets/a77c9946-c345-4227-a02d-88cdff68eae6" />


---

### **5. Add Value Buttons**
Add text buttons below each sprite to make the values clear:

1. Insert **Button** object below SpriteRespect
2. Properties:
   - **Name**: ButtonRespect
   - **Text**: "Respect"
3. Repeat for the other three values:
   - Insert **Button** below SpriteIntegrity
     - **Name**: ButtonIntegrity
     - **Text**: "Integrity"
   - Insert **Button** below SpriteInclusion
     - **Name**: ButtonInclusion
     - **Text**: "Inclusion"
   - Insert **Button** below SpriteCourage
     - **Name**: ButtonCourage
     - **Text**: "Courage"
4. Position all buttons in a row below their corresponding sprites
It should look like:

<img width="471" height="254" alt="image" src="https://github.com/user-attachments/assets/2f06dff6-5d29-44ed-91c4-4ca1c6334128" />

---

## **Part 2: Create a Global Variable and Array**
The global variable will store the currently selected value.

The array will contain a list of journal logs in the format: _[value]: [description]_

### **6. Add Global Variables**
1. Open **Event Sheet 1**
2. Right-click → **Add global variable**
3. Create first variable:
   - **Name**: CurrentValue
   - **Type**: Text
   - **Initial value**: "" (empty)
It should look like:
   <img width="255" height="33" alt="image" src="https://github.com/user-attachments/assets/857eb91b-9432-40f7-8a70-8bd4db76d607" />

---

### **7. Add Array Object**
1. In Layout 1, right-click → **Insert New Object** → **Array**
2. Properties:
   - **Name**: ArrayJournal
   - **Width**: 0 (starts empty)
   - **Height**: 1
   - **Depth**: 1
<img width="551" height="173" alt="image" src="https://github.com/user-attachments/assets/9228f096-f9ea-4103-8eca-c1236534f61c" />
<img width="193" height="120" alt="image" src="https://github.com/user-attachments/assets/3048cd8a-3db2-4ace-9528-523099b25222" />


---

## **Part 3: Layout 1 Events - Value Selection**

### **8. Event: Click Integrity Button**
1. In Event Sheet 1, add event → **ButtonIntegrity** → **On clicked**
2. Add action → **System** → **Set value**
   - Variable: **CurrentValue**
   - Value: **"Integrity"**
3. Add action → **System** → **Go to layout**
   - Layout: **Layout 2**
It should look like:
<img width="644" height="69" alt="image" src="https://github.com/user-attachments/assets/7004592c-5ab3-4097-862a-ecf6f9bcaccc" />

---

### **9. Repeat for Other Value Buttons**
Create similar events for the other three buttons:

**ButtonRespect clicked:**
- Set CurrentValue to "Respect"
- Go to Layout 2

**ButtonCourage clicked:**
- Set CurrentValue to "Courage"
- Go to Layout 2

**ButtonInclusion clicked:**
- Set CurrentValue to "Inclusion"
- Go to Layout 2

It should look like:
<img width="651" height="319" alt="image" src="https://github.com/user-attachments/assets/cc341d56-057d-4ed1-9945-db61aa2cd6ed" />

---

## **Part 4: Layout 2 - Description Entry**

### **10. Create Layout 2**
1. Right-click in Project panel → **Add** → **Layout**
2. **Name**: Layout 2

---

### **11. Add Title and Instructions to Layout 2**
1. Select **TextTitle** and **TextInstructions** on Layout 1
2. Copy them (Ctrl+C or Cmd+C)
3. Switch to **Layout 2**
4. Paste (Ctrl+V or Cmd+V)
5. Position them at the top of Layout 2
6. Select **TextInstructions** and change its text to:
   - **Text**: "What did you do to demonstrate ...?"

**Note:** This text will be updated to show the selected value when the layout starts.

It should look like:
<img width="306" height="88" alt="image" src="https://github.com/user-attachments/assets/24e103d4-0557-4008-accc-57df4c8297b1" />


---

### **12. Add Description Text Input**
1. Insert **Text Input** object
2. Properties:
   - **Name**: TextInput
   - **Placeholder**: "Describe what you did..."
   - Make it large enough for multiple lines of text
3. Position in center of layout

---

### **13. Add Save Button**
1. Insert **Button** object
2. Properties:
   - **Name**: ButtonSave
   - **Text**: "Add to My Journal"
3. Position below text input
4. Resize if needed

It should look like:

<img width="288" height="196" alt="image" src="https://github.com/user-attachments/assets/2dd91633-9a7a-4954-ae73-cc0e50573381" />

---

## **Part 5: Layout 2 Events - Save to Array**

### **14. Event: Update Instructions on Layout Start**
1. In Event Sheet 2 (for Layout 2), add event → **System** → **On start of layout**
2. Add action → **TextInstructions** → **Set text**
   - Text: **"What did you do to demonstrate " & CurrentValue & "?"**

**What this does:** When you arrive at Layout 2, the instructions update to show which value you selected.

![SelectValueAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/SelectValueAnimation.gif)

---

### **15. Event: Save Entry and Navigate**
1. Add event → **ButtonSave** → **On clicked**
2. Add action → **ArrayJournal** → **Push**
   - Where: **Back**
   - Value: **uppercase(CurrentValue) & ": " & TextInput.Text**
   - Type: **X axis**
3. Add action → **System** → **Go to layout**
   - Layout: **Layout 3**

**What this does:** Combines the value name (in uppercase) with your description and saves it to the array, then shows your journal.

---

### **16. Test Part 1**
1. Press **F5** to run
2. Click a value button on Layout 1
3. Notice Layout 2 shows your selected value in the instructions
4. Type a description
5. Click **Add to My Journal**
6. Check the array in debugger (F12) - should show your entry

It should look like:

<img width="771" height="336" alt="image" src="https://github.com/user-attachments/assets/15ea755c-f025-4dd7-a5f2-c5555cbcda2e" />



---

## **Part 6: Layout 3 - Journal Display**

### **17. Create Layout 3**
1. Right-click in Project panel → **Add** → **Layout**
2. **Name**: Layout 3

---

### **18. Add Title and Subtitle to Layout 3**
1. Select **TextTitle** and **TextInstructions** on Layout 1
2. Copy them (Ctrl+C or Cmd+C)
3. Switch to **Layout 3**
4. Paste (Ctrl+V or Cmd+V)
5. Position them at the top of Layout 3
6. Select **TextInstructions** and change its text to:
   - **Text**: "My values in action"

It should look like:

<img width="201" height="73" alt="image" src="https://github.com/user-attachments/assets/a6a1cef0-2e6f-4d3b-9eb1-3d2c5356421e" />

---

### **19. Add List Object**
1. Insert **List** object
2. Properties:
   - **Name**: List
   - Position: Center of layout
   - Make it large enough to show multiple entries (tall and wide)

It should look like:

<img width="263" height="267" alt="image" src="https://github.com/user-attachments/assets/c89cd033-3223-4fc3-8ed0-1e2c7ea20332" />

---

### **20. Add Celebrate Button**
1. Insert **Button** object
2. Properties:
   - **Name**: ButtonCelebrate
   - **Text**: "Celebrate another moment!"
3. Position at bottom of layout

It should look like:

<img width="269" height="308" alt="image" src="https://github.com/user-attachments/assets/9a148bbb-eb6a-42fe-8215-513e6d7a9044" />

---

## **Part 7: Layout 3 Events - Display Journal**

### **21. Event: Clear and Display Journal Entries**
1. In Event Sheet 3 (for Layout 3), add event → **System** → **On start of layout**
2. Add action → **List** → **Clear all items**

3. Add sub-event → **System** → **Repeat**
   - Count: **ArrayJournal.Width**

4. Add action to the Repeat sub-event → **List** → **Add item**
   - Text: **ArrayJournal.At(LoopIndex)**

**What this does:** When you reach Layout 3, it clears the list, then loops through every entry in the array and adds it to the list for display.

---

### **22. Event: Return to Start**
1. Add event → **ButtonCelebrate** → **On clicked**
2. Add action → **System** → **Go to layout**
   - Layout: **Layout 1**

---

## **Part 8: Final Testing**

### **23. Test Complete App**
1. Press **F5** to run
2. On Layout 1, click **Integrity**
3. On Layout 2, type "I admitted when I made a mistake"
4. Click **Add to My Journal**
5. On Layout 3, see your entry displayed as "INTEGRITY: I admitted when I made a mistake"
6. Click **Celebrate another moment!**
7. Add 3-4 more entries with different values
8. View your growing journal on Layout 3

![CompleteValuesAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/CompleteValuesAnimation.gif)

---

## **Success Criteria**
✔ I can select which value I demonstrated  
✔ I can describe what I did to demonstrate that value  
✔ I can save my entries to an array  
✔ I can view all my entries in a journal list  
✔ I can navigate between all three screens  
✔ I understand how arrays store data sequentially

---

## **Reflection Questions**
- How does the array help organize your journal entries?
- What happens to your entries when you add more? Where do they appear in the list?
- Can you think of other apps that might use arrays to store lists of information?
