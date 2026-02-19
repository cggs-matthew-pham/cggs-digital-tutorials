# **Year 7 Digital Design**

## **Create a Prototype Using Construct 3**


---

## **Learning Intention**

Students understand what a prototype is and learn how to build one using a layout and event sheet in Construct 3 for a **Music Practice Tracker**.

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
– Example: _“When button clicked → add practice time.”_

---

# **2. Sign Up for Construct 3**

Go to: **https://editor.construct.net**

1. Click **Register**
2. Select **Sign in with Google**

<img width="1300" height="304" alt="image" src="https://github.com/user-attachments/assets/3c6703ba-2ee9-4080-8dd0-1cfaf607ee57" />

<img width="401" height="247" alt="image" src="https://github.com/user-attachments/assets/34529d87-cf1f-4ffc-b8b8-76aab56f7c9d" />

---

# **3. Update Save & Backup Settings**

Inside Construct 3:

1. Open **Menu → Settings**
2. Under **Cloud**:
    - Tick **Enable Cloud Saving**
    - Select **OneDrive**
    - Set backup interval to **every 5 minutes**

_(You may be prompted to sign in with your Microsoft account.)_

<img width="602" height="170" alt="image" src="https://github.com/user-attachments/assets/d30598e9-39b8-4410-b580-7553432181ee" /><br/>

<img width="188" height="596" alt="image" src="https://github.com/user-attachments/assets/c42cda8f-0177-4373-b4cd-b76eb6d49a2b" />

<img width="408" height="468" alt="image" src="https://github.com/user-attachments/assets/cd03da7f-ff03-45c4-9fb7-2600fa25ec7b" />

---
# **4. Create a New Project**

1. Click **New**
2. Project name: **Music Practice Tracker**
3. Click **Create**

<img width="1238" height="176" alt="image" src="https://github.com/user-attachments/assets/42b8d058-bafa-408f-bb36-817577d89aa4" />

<img width="630" height="494" alt="image" src="https://github.com/user-attachments/assets/2cb2c919-11c4-4628-9cb0-c5e0cee08081" />

---

# **5. Design the User Interface (UI)**

On the **Layout** screen:

### **Insert Objects**

Right‑click → **Insert New Object**

Add:

- Text
- Text
- Text Input
- Button
- Text

HINT: use the search icon to find objects

<img width="266" height="300" alt="image" src="https://github.com/user-attachments/assets/eae93cb0-b3a2-440d-9b8d-51904084bfee" />


<img width="908" height="758" alt="image" src="https://github.com/user-attachments/assets/720cd479-55d3-4dc1-b321-d7815560d7f4" />

### **Update Text Properties**

Click each object and update its **Text** property:

- **Music Practice Tracker**
- **Hours practiced:**
- **Save**
- **You have practiced for ... hours**

Optional: Adjust **size**, **alignment**, or other visual properties.

<img width="374" height="552" alt="image" src="https://github.com/user-attachments/assets/94526a4d-b48b-4c3a-9526-a879213f8bc4" />

<img width="460" height="388" alt="image" src="https://github.com/user-attachments/assets/df1195d1-f44f-4f5e-82ac-935ccc35c651" />


<img width="548" height="434" alt="image" src="https://github.com/user-attachments/assets/d40dad1f-7653-4362-980c-7a7a28e7a287" />

---

# **6. Event Sheet – Adding Logic**

Open the **Event Sheet**.

### **Create Variables & Events**

1. Right‑click → **Add global variable**
    - Name: **HoursPracticed**
2. Right-click → Add an **Event** → Button → On clicked:
    - _When Button is clicked_
3. Add **Action**: add 1 to *HoursPracticed*:
    - **System → Add to variable** → add 1 to _HoursPracticed_
4. Add **Action:** update TextDisplay 
    - **TextDisplay → Set text** → update visible total hours
    - Test the program to add 1 hour at a time
5. Update **Action:** add value from the TextInput to hours
	- **System → Add to variable** → add *int(TextInput.Text)* to *HoursPracticed*
	- Test the program to add X hours depending on what the user typed

This makes the Save button store the number of hours and display the total.

1. Global Variable

<img width="268" height="490" alt="image" src="https://github.com/user-attachments/assets/e520683f-e561-4e7c-90ee-3e23d3cd49bf" />

2. Button event → On clicked
![[Pasted image 20260219120254.png]]
![[Pasted image 20260219120419.png]]
![[Pasted image 20260219120408.png]]
![[Pasted image 20260219120357.png]]

3. Action for System → Add 1 to hours
<img width="909" height="163" alt="image" src="https://github.com/user-attachments/assets/f3d4d6fc-a225-46cf-947d-3a0567e122b7" />


![[Pasted image 20260219120930.png]]

![[Pasted image 20260219121006.png]]

![[Pasted image 20260219121023.png]]
![[Pasted image 20260219121052.png]]
4.  Action for TextDisplayHours→ Update visible total hours

![[Pasted image 20260219121254.png]]

![[Pasted image 20260219121325.png]]

![[Pasted image 20260219121405.png]]
5. Update System Action

![[Pasted image 20260219121507.png]]

# **7. Add a "Great Work Animation" GIF**

### **Download and Insert the GIF**

1. Drag and drop the Great Work Animation file below into your Construct 3 layout
   
![GreatWorkAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/GreatWorkAnimation.gif)

### **Configure the Sprite**

1. Select the sprite on the layout
2. In the **Properties** panel:
    - **Name**: Change to **SpriteGreatWork**
    - **Initial visibility**: Set to **Invisible**
3. Right-click the sprite in the layout → **Animations**
4. In the **Animations** window:
    - Set **Speed**: **12** (frames per second)
    - Set **Repeat**: **Loop** (or **Repeat count** if you want it to play once)
5. Close the Animations window

![[Screenshot - Sprite Properties]] ![[Screenshot - Animation Settings]]

### **Test the Animation**

Before adding the condition, let's test the animation works:

1. Temporarily set **Initial visibility** to **Visible**
2. Press **F5** to run the project
3. You should see the animation playing
4. Close the preview and set **Initial visibility** back to **Invisible**

### **Add Conditional Logic**

Open the **Event Sheet**.

1. Right-click → **Add event** → **System** → **Compare variable**
    - Variable: **HoursPracticed**
    - Comparison: **≥ (Greater or equal)**
    - Value: **10**
2. Add **Action** → **SpriteGreatWork** → **Set visible**
3. Your event should read: _"System: HoursPracticed ≥ 10 → SpriteGreatWork: Set visible"_

![[Screenshot - Conditional Event]]

### **Test Your Prototype**

1. Press **F5** to run
2. Enter practice hours and click **Save**
3. When total reaches 10 or more, the celebration animation should appear!
