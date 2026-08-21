# Getting started — no Git required

This guide gets you from "nothing installed" to "the app running in your
browser," using a downloaded ZIP instead of `git clone`. Follow it top to
bottom the first time; after that you'll only need the "Every time after
setup" section at the end.

Works on Windows and Mac — steps that differ are labelled.

---

## 1. Install Visual Studio Code

1. Go to https://code.visualstudio.com/
2. Click the big **Download** button (it detects your OS automatically).
3. Run the installer.

   * **Windows:** during install, tick **"Add to PATH"** if it's offered —
     it usually is, by default.
   * **Mac:** drag VS Code into your Applications folder.
4. Open VS Code once to confirm it launches, then close it again — we'll
   come back to it after Python is installed.

<img width="1889" height="724" alt="image" src="https://github.com/user-attachments/assets/e915138d-56e0-4d68-8426-c4d7438ae51b" />

<img width="897" height="668" alt="image" src="https://github.com/user-attachments/assets/e5e714ee-dde5-4cd7-832f-f0e7be300905" />

<img width="907" height="678" alt="image" src="https://github.com/user-attachments/assets/e53df687-c270-4d80-a4e0-1bff0522b3a7" />

---

## 2. Install Python

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/release/python-3150rc1/)
2. For **Windows** if the Python install manager doesn't work, you can also download Python through the Microsoft Store.
3. Download the version 3.13 **Python 3** installer for your OS.
4. Run the installer.

   * **Windows — important:** on the first install screen, tick the box at
     the bottom that says **"Add python.exe to PATH"** *before* clicking
     Install. If you miss this, Python won't be recognised in the terminal
     and you'll need to reinstall.
   * **Mac:** the default install options are fine.
5. Check it worked. Open:

   * **Windows:** the Start menu → type `cmd` → open Command Prompt
   * **Mac:** Spotlight (`Cmd+Space`) → type `terminal` → open Terminal

   <img width="1822" height="337" alt="image" src="https://github.com/user-attachments/assets/deed15c4-de2f-4432-b0ff-094a35204f31" />

   Then type:

   ```
   python --version
   ```

   (On Mac, if that says "command not found," try `python3 --version`
   instead — Mac sometimes only registers `python3`.)

   You should see something like `Python 3.13.x`. If you see an error,
   Python isn't on PATH — reinstall and make sure the checkbox in step 4
   was ticked.

---

## 3. Download the repo as a ZIP (no Git needed)

1. Go to the repo's GitHub page.
2. Click the green **`< > Code`** button.
3. Click **Download ZIP**.
4. Find the downloaded file (usually in your **Downloads** folder) and
   **extract it**:

   * **Windows:** right-click the ZIP → **Extract All...** → choose a
     location you'll remember (e.g. Desktop or Documents) → Extract.
   * **Mac:** double-click the ZIP — it extracts automatically into the
     same folder.
5. You should now have a normal folder (not a `.zip`) containing files
   such as `requirements.txt` and the example `.py` apps.

> Rename the extracted folder if you like (GitHub ZIPs often add
> `-main` to the name) — just remember where it is, you'll need it in
> the next step.

---

## 4. Open the folder in VS Code

1. Open VS Code.
2. **File → Open Folder...** (Mac: **File → Open...**)
3. Select the extracted folder from step 3 and open it.
4. VS Code will ask if you trust the authors — click **Yes, I trust the
   authors**.
5. Open a terminal *inside* VS Code: **Terminal → New Terminal** (or
   `` Ctrl+` ``). This terminal automatically starts inside your project
   folder — no need to `cd` anywhere.

<img width="511" height="822" alt="image" src="https://github.com/user-attachments/assets/4494ca24-e29d-44fb-ae77-217c311e01d4" />

---

## 5. Create a virtual environment (venv)

A venv keeps this project's Python packages separate from everything
else on your computer. In the VS Code terminal you just opened, run:

**Windows:**

```
python -m venv venv
venv\Scripts\activate
```

**Mac:**

```
python3 -m venv venv
source venv/bin/activate
```

After activating, you should see `(venv)` appear at the start of your
terminal prompt — that's confirmation it worked.

> **Windows note:** if activation fails with a message about "running
> scripts is disabled," run this once, then try activating again:
>
> ```
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

> VS Code may also pop up a message asking "Do you want to select this
> environment for the workspace?" — click **Yes**. This makes VS Code use
> the venv automatically from then on.

<img width="1380" height="330" alt="image" src="https://github.com/user-attachments/assets/b51d5c45-eb05-4925-be3d-185313d9c5fb" />

---

## 6. Install the requirements

With `(venv)` showing in your terminal, run:

```
pip install -r requirements.txt
```

This downloads and installs everything the apps need. It can take a few
minutes the first time — that's normal.

<img width="1336" height="277" alt="image" src="https://github.com/user-attachments/assets/ef8d5a6b-977e-4340-a875-46226b74fabf" />

---

## 7. Run one of the example apps

Still in the same terminal (with `(venv)` showing), choose one of the starter
apps to run.

For example:

```bash
python image_classifier.py
```

Other starter apps include:

```text
text_3class.py
text_tone_checker.py
image_classifier.py
image_trained_yours.py
image_read_text.py
audio_sound_events.py
audio_keyword_spotter.py
```

Run any starter by typing `python` followed by its filename. For example:

```bash
python text_3class.py
```

or:

```bash
python audio_sound_events.py
```

The first time you run some machine-learning starters, they may need to
download a pretrained model. This can take a little while.

When the app is ready, you should see a line similar to:

```text
Running on local URL:  http://127.0.0.1:7860
```

Open that link in your browser (Ctrl/Cmd-click it in the terminal, or
copy-paste it) — the app should load.

To stop the app, click back in the terminal and press `Ctrl+C`.

> Some starters need extra files. For example, `image_trained_yours.py`
> needs a compatible trained model file. Start with one of the pretrained
> examples such as `text_3class.py`, `image_classifier.py`, or
> `audio_sound_events.py` if you just want to check that your setup works.

---

## Every time after setup

Once you've done steps 1–6 once, you don't need to repeat them. Each new
session:

1. Open VS Code → **File → Open Folder...** → your project folder.
2. Open a terminal (`` Ctrl+` ``).
3. Activate the venv:

   * Windows: `venv\Scripts\activate`
   * Mac: `source venv/bin/activate`
4. Run the starter you are working on, for example:

   ```
   python image_classifier.py
   ```

---

## Troubleshooting

| Problem                                                 | Likely fix                                                                                                                                                           |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `python` not recognised                                 | Python wasn't added to PATH — reinstall Python and tick the PATH checkbox (Windows), or use `python3` (Mac)                                                          |
| `(venv)` doesn't appear after activating                | Make sure you're in the project folder in the terminal, and that `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac) ran without an error above it |
| `pip install` fails partway                             | Re-run the same command — it usually resumes; if it keeps failing on one package, note the exact error message                                                       |
| Browser says "can't connect" at the localhost link      | Check the terminal — the app may still be starting, downloading a model, or may have crashed with an error above the "Running on" line                               |
| Downloaded ZIP folder has a weird name like `repo-main` | Fine to leave as-is, or rename it — just open *that* folder in VS Code, not the ZIP file itself                                                                      |
| A machine-learning app takes a while on its first run   | Some pretrained models are downloaded the first time they are used. Leave the terminal running and wait for the download/startup to finish                           |
