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

<img width="380" height="313" alt="image" src="https://github.com/user-attachments/assets/80046fc4-5d8c-4fee-8a80-aaea6151388f" />

2. Button event → On clicked
<img width="186" height="309" alt="image" src="https://github.com/user-attachments/assets/21707aac-41d6-4720-84ef-aa42f7c44780" />

<img width="535" height="260" alt="image" src="https://github.com/user-attachments/assets/8726cdb7-d62e-47c9-acaa-c78dd0a4e223" />

<img width="539" height="172" alt="image" src="https://github.com/user-attachments/assets/1f5c9c3d-5248-4de8-bf56-6c789816fd85" />

<img width="689" height="30" alt="image" src="https://github.com/user-attachments/assets/926712d4-ac27-4ab7-9642-aa224626c2ae" />


3. Action for System → Add 1 to hours
<img width="374" height="35" alt="image" src="https://github.com/user-attachments/assets/a514768c-5c7b-4721-b5d9-798e7cbc697a" /><br/>



<img width="573" height="248" alt="image" src="https://github.com/user-attachments/assets/adb210d1-c949-46b7-9530-74211c2dfb9a" />


<img width="550" height="448" alt="image" src="https://github.com/user-attachments/assets/83cad1b6-99f3-4d1f-b680-40867e607319" />


<img width="459" height="280" alt="image" src="https://github.com/user-attachments/assets/e0a00d68-2947-4f7d-944a-746fd8554cab" />

<img width="557" height="41" alt="image" src="https://github.com/user-attachments/assets/7b76f562-2bae-476b-abe6-18d8bc7ccfb3" />

4.  Action for TextDisplayHours→ Update visible total hours

<img width="546" height="241" alt="image" src="https://github.com/user-attachments/assets/39308941-df43-4d41-ae50-dfd1c1e5848a" /><br/>
<img width="554" height="210" alt="image" src="https://github.com/user-attachments/assets/ebdf643a-5b5b-4854-8b72-0366f4e6e097" />
<img width="451" height="273" alt="image" src="https://github.com/user-attachments/assets/7fd9c2e5-e7f8-4038-b3c0-bab0a2e54a20" />

5. Update System Action

<img width="456" height="275" alt="image" src="https://github.com/user-attachments/assets/2da31d4f-96e6-4e3b-b8b2-296166552c84" />


# **7. Add a "Great Work Animation" GIF**

### **Download and Insert the GIF**

1. Drag and drop the Great Work Animation file below into your Construct 3 layout
   
![GreatWorkAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/GreatWorkAnimation.gif)

### **Configure the Sprite**

1. Double-click the sprite on the layout
2. In the **Animation** window under **Animation Properties (on the right)**:
    - Set **Speed**: **12** (frames per second)
    - Set **Repeat**: **Loop** (or **Repeat count** if you want it to play once)
3. Close the Animations window

<img width="201" height="222" alt="image" src="https://github.com/user-attachments/assets/7670c479-a329-4020-831d-9b6f903d94a1" />

### **Test the Animation**

1. Press **F5** to run the project
2. You should see the animation playing

### **Add Conditional Logic**

Now we will configure the program to only show the Great Work Animation when the hours practiced is greater or equal to 10.

1. Click on the sprite to select it
2. Under **Properties** to the left, untick **Initial visibility**

<img width="289" height="189" alt="image" src="https://github.com/user-attachments/assets/f84a6524-9c6c-49f0-b897-9ceb1fe998f2" />

Open the **Event Sheet**.

3. Right-click → **Add event** → **System** → **Compare variable**
    - Variable: **HoursPracticed**
    - Comparison: **≥ (Greater or equal)**
    - Value: **10**
4. Add **Action** → **GreatWorkAnimation** → **Set visible**
3. Your event should read: _"System: HoursPracticed ≥ 10 → SpriteGreatWork: Set visible"_

![CompareVariableAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/CompareVariableAnimation.gif)

![SetVisibleAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/SetVisibleAnimation.gif)

### **Test Your Prototype**

1. Press **F5** to run
2. Enter practice hours and click **Save**
3. When total reaches 10 or more, the celebration animation should appear!

![CompleteAppAnimation.gif](https://raw.githubusercontent.com/cggs-matthew-pham/cggs-digital-tutorials/refs/heads/main/CompleteAppAnimation.gif)
