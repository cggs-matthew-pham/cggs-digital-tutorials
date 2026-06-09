# **Dino Stats: Character Creator**

**Build a data-driven character viewer using instance variables**

---

## **Learning Intention**

Students understand how objects, instances, and instance variables work in Construct 3, and can use them to build an app that displays different data depending on user selection.

## **Success Criteria**

✔ I can create a sprite with multiple animation frames to represent different characters.  
✔ I can add instance variables to a sprite and set different values for each instance.  
✔ I can use layers to switch between screens without changing layouts.  
✔ I can scale a progress bar sprite based on a data value.  
✔ I can explain what "object type," "instance," and "instance variable" mean.

---

# **Part 1: Project Setup**

## **1. Create New Project**

1. Open Construct 3
2. Click **New Project**
3. Project name: **Dino Stats**
4. Click **Create**

<!-- SCREENSHOT: New project dialog -->

---

## **2. Set Up the Layout**

1. Select the layout by clicking the background
2. In Properties, set:
   - **Layout size**: 500 × 600

---

## **3. Rename the Layer**

1. In the **Layers** panel (right side), double-click **Layer 0**
2. Rename it to **Selection**

<!-- SCREENSHOT: Layers panel showing "Selection" -->

---

## **4. Add Title and Subtitle**

**Title:**
1. Right-click layout → **Insert New Object** → **Text**
2. Properties:
   - **Name**: TextTitle
   - **Text**: "Dino Stats"
   - **Font size**: 32, bold, centered
3. Position at the top of the layout

**Subtitle:**
1. Insert another **Text** object
2. Properties:
   - **Name**: TextSubtitle
   - **Text**: "Choose your dinosaur"
   - **Font size**: 16, centered
3. Position below the title

<!-- SCREENSHOT: Layout with title and subtitle -->

---

# **Part 2: Dinosaur Sprite and Animation Frames**

You're going to create **one** sprite object with three animation frames — one frame per dinosaur. Then you'll place **three instances** of that sprite on the layout. Each instance will show a different frame.

## **5. Create the SpriteDino Object**

1. Right-click layout → **Insert New Object** → **Sprite**
2. The image editor opens. Draw or import an image for the **T-Rex** (this will be frame 0)
3. Close the image editor
4. Rename the sprite to **SpriteDino**
5. Resize to roughly **120 × 120**

<img width="500" height="500" alt="T-Rex" src="https://github.com/user-attachments/assets/356ca42a-dbd0-438d-b306-e8d5a0bcf360" />

> **Tip:** Keep the art simple — a coloured silhouette or placeholder rectangle works fine. You can upgrade the art later.

---

## **6. Add Animation Frames**

1. Double-click **SpriteDino** to reopen the image editor
2. In the **Animation Frames** panel (bottom), right-click → **Add frame**
3. Draw or import an image for the **Velociraptor** (frame 1)
4. Right-click → **Add frame** again
5. Draw or import an image for the **Pterodactyl** (frame 2)
6. Close the image editor

<img width="500" height="500" alt="Velociraptor" src="https://github.com/user-attachments/assets/09890b37-8f36-4d7c-8fdb-e75abc3cc07f" />

<img width="500" height="500" alt="Pterodactyl" src="https://github.com/user-attachments/assets/9f264fe8-ead4-49f1-a5fd-011dda51b6ab" />





You should now have three frames:

| Frame | Dinosaur |
|---|---|
| 0 | T-Rex |
| 1 | Velociraptor |
| 2 | Pterodactyl |

---

## **7. Set Animation Speed to 0**

You don't want the sprite cycling through frames automatically.

1. Select **SpriteDino** on the layout
2. In Properties, find **Animations** → click to expand
3. Set **Speed** to **0**

---

## **8. Place Three Instances**

1. You already have one instance on the layout (frame 0 — T-Rex). Position it on the left side, below the subtitle.
2. **Copy and paste** the sprite twice (Ctrl+C, Ctrl+V) to create two more instances
3. Position all three in a row with space between them
4. Select the **middle** instance → in Properties, set **Initial frame** to **1**
5. Select the **right** instance → in Properties, set **Initial frame** to **2**

You should now see three different dinosaurs side by side.

<!-- SCREENSHOT: Three SpriteDino instances showing different frames in a row -->

---

## **9. Add Name Labels**

Add a text label below each dinosaur so players know what they're clicking.

1. Insert a **Text** object → rename to **TextLabel1**
   - Text: "T-Rex" | Font size: 14, centered
   - Position below the first dinosaur

2. Insert another **Text** → rename to **TextLabel2**
   - Text: "Velociraptor"
   - Position below the second dinosaur

3. Insert another **Text** → rename to **TextLabel3**
   - Text: "Pterodactyl"
   - Position below the third dinosaur

<!-- SCREENSHOT: Three dinosaurs with name labels underneath -->

---

# **Part 3: Instance Variables**

This is the key concept. You're going to add **instance variables** to the SpriteDino object type. Every instance shares the same variable *names*, but each instance holds its own *values*.

> **Think of it this way:** SpriteDino is like a template (in programming, this is called a *class*). Each dinosaur on the layout is an *instance* — a specific copy with its own data. The instance variables are *properties* that describe each one.

## **10. Add Instance Variables**

1. Select any **SpriteDino** instance on the layout
2. In Properties, find **Instance variables** → click **Add**
3. Add the following variables one at a time:

| Name | Type | Description |
|---|---|---|
| dinoName | Text | Display name |
| tier | Text | Tier ranking (S, A, B, etc.) |
| attack | Number | Attack stat (0–100) |
| defense | Number | Defense stat (0–100) |
| hp | Number | Hit points stat (0–100) |
| speed | Number | Speed stat (0–100) |
| ability | Text | Special ability |
| weakness | Text | Main weakness |

<!-- SCREENSHOT: Instance variables dialog showing the list -->

> **Note:** You add instance variables to the *object type*, not individual instances. All three dinosaurs will now have these variables — you just need to fill in different values for each.

---

## **11. Set T-Rex Values**

1. Click the **first** SpriteDino instance (frame 0 — T-Rex) on the layout
2. In Properties, under Instance variables, set:

| Variable | Value |
|---|---|
| dinoName | T-Rex |
| tier | S |
| attack | 95 |
| defense | 80 |
| hp | 90 |
| speed | 40 |
| ability | Bone Crusher — bite shatters armour |
| weakness | Tiny arms, slow turning radius |

<!-- SCREENSHOT: Properties panel showing T-Rex instance variable values -->

---

## **12. Set Velociraptor Values**

1. Click the **second** SpriteDino instance (frame 1)
2. Set instance variables:

| Variable | Value |
|---|---|
| dinoName | Velociraptor |
| tier | A |
| attack | 65 |
| defense | 35 |
| hp | 30 |
| speed | 90 |
| ability | Pack Tactics — damage scales with nearby allies |
| weakness | Turkey-sized, fragile |

---

## **13. Set Pterodactyl Values**

1. Click the **third** SpriteDino instance (frame 2)
2. Set instance variables:

| Variable | Value |
|---|---|
| dinoName | Pterodactyl |
| tier | B |
| attack | 40 |
| defense | 25 |
| hp | 35 |
| speed | 95 |
| ability | Dive Bomb — high-speed aerial strike |
| weakness | Helpless on ground, weak up close |

---

# **Part 4: Stats Display Layer**

Now you'll build the screen that shows a dinosaur's stats. This will be on a **separate layer** that starts hidden.

## **14. Create the Stats Layer**

1. In the **Layers** panel, click the **+** button to add a new layer
2. Rename it to **Stats**
3. In Properties, set **Initially visible** to **No**

> **Why layers instead of layouts?** Layers keep everything on one layout. This means the SpriteDino instances and their instance variables stay accessible — you can read their data directly without copying it elsewhere.

<!-- SCREENSHOT: Layers panel showing Selection and Stats layers, Stats set to invisible -->

---

## **15. Add the Dinosaur Name and Tier**

Make sure **Stats** is the active layer (selected in the Layers panel) before inserting objects.

1. Insert a **Text** object → rename to **TextDinoName**
   - Text: "Dinosaur Name"
   - Font size: 28, bold
   - Position at the top of the layout

2. Insert a **Text** object → rename to **TextTier**
   - Text: "Tier: —"
   - Font size: 20
   - Position below the name

---

## **16. Add Stat Labels**

Insert four **Text** objects for the stat labels. Position them in a column on the left side:

| Object Name | Text | Position |
|---|---|---|
| TextStatAttack | "Attack: 0" | Below tier |
| TextStatDefense | "Defense: 0" | Below attack |
| TextStatHP | "HP: 0" | Below defense |
| TextStatSpeed | "Speed: 0" | Below HP |

Set each to font size **14**.

<!-- SCREENSHOT: Stats layer with name, tier, and four stat labels stacked -->

---

## **17. Add Stat Bars**

This uses the same technique as the progress bar in the Water Tracker — a coloured sprite whose width scales to match a data value.

### **Bar backgrounds**

1. Insert a **Sprite** → rename to **BarBG**
2. In the image editor, draw a **grey rectangle**
3. Close the editor
4. Set size to **200 × 16**
5. Position it next to **TextStatAttack**
6. **Copy and paste** three times
7. Align one background bar next to each stat label

> **Note:** Construct 3 treats all copies of BarBG as the same object type. Since they don't change dynamically, this is fine.

### **Bar foregrounds**

You need a **separate object type** for each stat bar, because each one will be set to a different width.

1. Insert a **Sprite** → rename to **BarAttack**
   - Draw a **red rectangle**
   - Size: **200 × 16**
   - Position on top of the first BarBG

2. Insert a **Sprite** → rename to **BarDefense**
   - Draw a **blue rectangle**
   - Size: **200 × 16**
   - Position on the second BarBG

3. Insert a **Sprite** → rename to **BarHP**
   - Draw a **green rectangle**
   - Size: **200 × 16**
   - Position on the third BarBG

4. Insert a **Sprite** → rename to **BarSpeed**
   - Draw a **yellow rectangle**
   - Size: **200 × 16**
   - Position on the fourth BarBG

<!-- SCREENSHOT: Four stat bars with coloured foregrounds on grey backgrounds -->

---

## **18. Add Ability, Weakness, and Back Button**

1. Insert a **Text** object → rename to **TextAbility**
   - Text: "Special: —"
   - Font size: 14
   - Position below the stat bars

2. Insert a **Text** object → rename to **TextWeakness**
   - Text: "Weakness: —"
   - Font size: 14
   - Position below ability

3. Insert a **Button** → rename to **ButtonBack**
   - Text: "← Back"
   - Position at the bottom of the layout

<!-- SCREENSHOT: Complete Stats layer showing all elements -->

---

# **Part 5: Events — Dinosaur Selection**

This is where instance variables show their power. When you click a SpriteDino instance, Construct 3 automatically knows *which* instance was clicked. You can read that specific instance's variables to populate the stats display.

## **19. Add the Selection Event**

Open the **Event Sheet**.

1. Add event → **SpriteDino** → **On clicked**
2. Add the following **actions** to this event:

### **Set text displays**

| Action | Object | Property | Value |
|---|---|---|---|
| Set text | TextDinoName | Text | `SpriteDino.dinoName` |
| Set text | TextTier | Text | `"Tier: " & SpriteDino.tier` |
| Set text | TextStatAttack | Text | `"Attack: " & SpriteDino.attack` |
| Set text | TextStatDefense | Text | `"Defense: " & SpriteDino.defense` |
| Set text | TextStatHP | Text | `"HP: " & SpriteDino.hp` |
| Set text | TextStatSpeed | Text | `"Speed: " & SpriteDino.speed` |
| Set text | TextAbility | Text | `"Special: " & SpriteDino.ability` |
| Set text | TextWeakness | Text | `"Weakness: " & SpriteDino.weakness` |

### **Scale stat bars**

| Action | Object | Property | Value |
|---|---|---|---|
| Set width | BarAttack | Width | `SpriteDino.attack / 100 * 200` |
| Set width | BarDefense | Width | `SpriteDino.defense / 100 * 200` |
| Set width | BarHP | Width | `SpriteDino.hp / 100 * 200` |
| Set width | BarSpeed | Width | `SpriteDino.speed / 100 * 200` |

### **Switch layers**

| Action | Object | Property | Value |
|---|---|---|---|
| Set layer visible | System | Layer "Selection" | Invisible |
| Set layer visible | System | Layer "Stats" | Visible |

> **Why does `SpriteDino.attack` give the right value?** When you click an instance, Construct 3 "picks" that instance for the rest of the event. So `SpriteDino.attack` refers to the *clicked* dinosaur's attack — not all of them. This is instance-level data in action.

<!-- SCREENSHOT: Complete event with all actions listed -->

---

# **Part 6: Events — Back Button**

## **20. Add the Back Event**

1. Add event → **ButtonBack** → **On clicked**
2. Add actions:

| Action | Object | Property | Value |
|---|---|---|---|
| Set layer visible | System | Layer "Stats" | Invisible |
| Set layer visible | System | Layer "Selection" | Visible |

<!-- SCREENSHOT: Back button event -->

---

# **Part 7: Test Your App**

1. Press **F5** to run the project
2. Click the **T-Rex** — you should see:
   - Name: "T-Rex"
   - Tier: S
   - Attack bar nearly full (95%), speed bar less than half (40%)
3. Click **← Back**
4. Click the **Velociraptor** — stats should change:
   - Speed bar nearly full (90%), defense bar small (35%)
5. Click **← Back**
6. Click the **Pterodactyl** — different stats again
7. Verify every dinosaur shows its own unique data

<!-- GIF: Clicking through all three dinosaurs and seeing stats change -->

---

# **Part 8: Extend the Dino Stats App**

Before starting the main challenge, try adding to your existing project:

### **Add more stats**
Add `stealth` and `intelligence` instance variables to SpriteDino. Create new bar sprites and text labels on the Stats layer, then add actions to the click event.

### **Add a 4th dinosaur**
Add a new animation frame, place a new instance, and fill in its instance variables. You shouldn't need to touch the event sheet at all — test it and see why.

### **Colour the tier badge**
Add a **Sprite** called **SpriteTierBadge** on the Stats layer with animation frames for each tier colour (frame 0 = gold for S, frame 1 = red for A, frame 2 = blue for B). In the click event, set the frame based on the tier value.

---

# **Part 9: Challenge — Build Your Own Character Creator**

Now that you know the pattern, create your own character creator from scratch. Choose one of the categories below, or pitch your own idea to your teacher.

### **Option A: Fantasy / Mythical Creatures**
Dragons, phoenixes, griffins, unicorns, krakens...  
Example stats: Magic, Strength, Speed, Defence, Wisdom, Stealth

### **Option B: Celebrity / Artist / Athlete**
Musicians, athletes, or performers with skill-based profiles.  
Example stats: Talent, Influence, Consistency, Versatility, Stamina, Creativity

### **Option C: Pet Breeds**
Dog breeds, cat breeds, or a mix.  
Example stats: Energy, Affection, Trainability, Independence, Chaos Factor, Fluffiness

### **Option D: Your Own Idea**
Any category where you can define at least 3 characters with meaningful stats. Get approval from your teacher first.

### **Requirements**

- At least **3 characters** using a single sprite with animation frames and instance variables
- At least **4 stats** displayed with scaled bars
- A **selection screen** and a **stats screen** using layers
- Each character must have a **special ability** and a **weakness**
- Your stat values must be **justified** — be ready to explain why you gave each character those numbers

### **Stretch goals**

- Add a **comparison mode** that shows two characters side by side
- Animate the stat bars using the **Tween** behaviour so they grow from 0 when the stats screen appears
- Add a **tier ranking** system with colour-coded badges
- Include **build options** — different ways to play or spec each character (like skill trees or loadouts)

---

## **Key Vocabulary**

| Term | Construct 3 | Programming |
|---|---|---|
| SpriteDino | Object type | Class |
| Each dinosaur on the layout | Instance | Object |
| dinoName, attack, defense... | Instance variable | Property / Attribute |
| On clicked → set text | Event + Action | Method call |

---

## **Reflection Questions**

- What is the difference between an *object type* and an *instance*?
- Why did you use **instance variables** instead of global variables for the dinosaur data?
- If you added a 4th dinosaur, what would you need to change in the event sheet? (Think carefully — the answer might surprise you.)
- How is this pattern similar to how apps like Pokédex or character select screens work in real games?
