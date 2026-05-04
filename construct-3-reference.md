# Construct 3 — Quick Reference

---

## 1. Link Event Sheet to Layout

> **Layout selected → Properties panel → Event sheet → select correct sheet**

<img width="425" height="244" alt="image" src="https://github.com/user-attachments/assets/5cbc07ae-5ea6-4850-9ba6-9220daa2fbcd" />
*Layout Properties showing Event sheet dropdown*

---

## 2. How the Event Sheet Works

Every event is a **trigger** + one or more **actions**.

> *"When this happens → do this"*

<img width="976" height="138" alt="image" src="https://github.com/user-attachments/assets/766ef094-ff6f-45ac-9f27-71be77602da7" />
*Event sheet showing trigger on left, actions indented on right*

**Common Triggers**

| Trigger | Meaning |
|---|---|
| `Button` → On clicked | User clicks a button |
| `System` → On start of layout | Layout has just loaded |
| `System` → Compare variable | A variable meets a condition |
| `System` → Repeat | Loop a set number of times |

**Common Actions**

| Action | What it does |
|---|---|
| `System` → Go to layout | Navigate to another layout |
| `System` → Set value | Set a variable to a value |
| `System` → Add to variable | Add a number to a variable |
| `TextObject` → Set text | Update what text displays |
| `Array` → Push | Add an item to the array |
| `List` → Add item | Add a row to a list |
| `List` → Clear all items | Empty the list |
| `Sprite` → Set visible | Show or hide a sprite |

---

## 3. Navigation

```
ButtonName   On clicked
  → System: Go to layout → Layout 2
```

<img width="973" height="73" alt="image" src="https://github.com/user-attachments/assets/0b56b9ad-1987-4afb-82c0-7c253a6ce6d1" />

*On clicked with Go to layout action*

---

## 4. Global Variables

**Right-click event sheet → Add global variable**

| Name | Type | Initial value |
|---|---|---|
| `CurrentValue` | Text | `""` |
| `HoursPracticed` | Number | `0` |

<img width="405" height="61" alt="image" src="https://github.com/user-attachments/assets/d72d5802-f3ef-4d0b-97cc-d6470d76a8e8" />

*Global variable declaration at top of event sheet*

> Global variables are accessible across **all layouts**.

---

## 5. Update and Display Variables

### 5a. Text Variables

Set a text variable when a button is clicked, carry it to another layout.

```
ButtonIntegrity   On clicked
  → System: Set CurrentValue = "Integrity"
  → System: Go to layout → Layout 2
```

<img width="984" height="156" alt="image" src="https://github.com/user-attachments/assets/2117e9a9-6e72-43ed-adce-0e5b39e8abae" />

*Set value action with a text string*

**Display it using `&` to join text:**

```
TextDisplay   Set text
  "You selected: " & CurrentValue
```

<img width="978" height="99" alt="image" src="https://github.com/user-attachments/assets/00ee9fcd-4099-495e-8707-70cbc123881d" />
*Set text action with & joining literal text and a variable*

> Literal text goes in `" "` — variables and expressions do not.

---

### 5b. Number Variables

Read a number from a text input using `int()`, add it to a variable.

```
ButtonSave   On clicked
  → System: Add to HoursPracticed   int(TextInput.Text)
  → TextDisplay: Set text
     "You have practiced for " & HoursPracticed & " hours"
```

<img width="985" height="179" alt="image" src="https://github.com/user-attachments/assets/da9cba3e-f9e2-4f2f-973a-4995bb81f4d4" />
*Add to variable + Set text in the same event*
> `TextInput.Text` is always a string. Wrap in `int()` before doing maths.

**Update the display in the same event as the variable change.**

---

### 5c. On Start of Layout

Use to initialise or refresh display text when a layout loads.

```
System   On start of layout
  → TextInstructions: Set text
     "What did you do to demonstrate " & CurrentValue & "?"

System   On start of layout
  → TextInput: Set text   ""
```

![](images/screenshot-on-start-layout.png)
*Two On start of layout events — update instructions, clear input field*

> Each use case is a **separate** event.

---

## 6. Compare Variable → Show/Hide

1. Select sprite → Properties → **Initial visibility: off**
2. Add event:

```
System   HoursPracticed ≥ 10
  → SpriteGreatWork: Set visible
```

![](images/screenshot-compare-variable.png)
*Compare variable condition + Set visible action*

---

## 7. If / Else Toggle

Two flat `On clicked` events cancel each other out — use sub-events.

```
Button_Bed   On clicked
  └─ Text = "⬜"  →  Set text "✅"
  └─ Else         →  Set text "⬜"
```

`S` = sub-event · `X` = Else · `B` = blank sub-event

![](images/screenshot-toggle-subevent.png)
*On clicked with sub-event + Else branch*

---

## 8. Array — Setup + Push

**Insert New Object → Array** → Width: `0`, Height: `1`, Depth: `1`

![](images/screenshot-array-properties.png)
*Array properties — Width 0 starts empty, grows at runtime*

```
ButtonSave   On clicked
  → ArrayJournal: Push → Back
     Value: CurrentValue & ": " & TextInput.Text   Axis: X
```

![](images/screenshot-array-push.png)
*Push action — Back, value expression, X axis*

---

## 9. Array → Display in List

Two separate events — **do not combine**.

```
System   On start of layout
  → List: Clear all items

System   On start of layout
  + System: Repeat  [ArrayJournal.Width]
  → List: Add item  [ArrayJournal.At(loopindex)]
```

![](images/screenshot-array-display.png)
*Clear event, then separate Repeat + Add item event*

> `loopindex` counts from 0 up to `ArrayJournal.Width - 1`.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Events don't fire | Check layout → Event sheet link |
| Toggle does nothing | Use sub-event + Else, not two flat events |
| List shows duplicates | Clear and loop must be **separate** events |
| Variable lost between layouts | Use a **global** variable |
| Maths gives wrong result | Wrap input with `int()` |
| Display doesn't update | Set text in the **same event** as variable change |
| `loopindex` always 0 | Repeat must be a **condition**, not an action |
