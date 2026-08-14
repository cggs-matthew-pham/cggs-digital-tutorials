# Production Notes (internal, not for students)

Living log of decisions made while building this set. Purpose: apply in
bulk later, not re-litigate each one per file. Only Tutorial 02 currently
matches everything below. 00, 02 through 12 are still in the earlier
draft style and need this pass.

## House style, apply to every tutorial

- **Frontmatter:** `title:` / `subtitle:` at the top, no em dash in the
  subtitle (use a comma).
- **Teacher notes:** `<details><summary>Teacher note</summary>...</details>`,
  not a bold heading. Collapses by default, keeps it out of students' way.
- **Width tiers:** `### Going further` as a plain heading, not
  `:::typical` / `:::wider`. Visible, not collapsed, students choose in.
- **No `{{field}}` / `{{lines}}` / `{{columns}}` / `{{break}}` anywhere.**
  These are Prepare/print conventions and Liquid (Jekyll, what GitHub
  Pages runs) will try to parse `{{...}}` as its own templating syntax.
  For "record this" moments, use a plain prompt: "**Record this in your
  notes:**", pointing at the student's own doc (OneNote), not an
  embedded blank.
- **No em-dashes anywhere**, standing preference, not just this project.
  Use a comma, colon, or full stop instead.
- **Every code block says what to do with it**, explicitly, every time:
  "Add this below what you have," "Add this at the top," "Replace your
  function with this," "Delete the two lines you just added." Never rely
  on students remembering an earlier blanket instruction, restate it at
  each block. This was the single biggest confusion source in the Y9 set
  per their own authoring guide, and Tutorial 02 had five blocks missing
  this before the pass just done, worth checking for on every file.
- **Warmer, connected prose over clipped bullets.** Bullets are fine for
  genuinely list-shaped content (checklists, quick option comparisons),
  not as a default register. Match the Y9 set's voice: short sentences,
  full sentences, not fragments.
- **Dependency simplification, not dependency teaching, by default.**
  This arc's subject is robotics, not Python, so prefer plain code over
  clever code: a counter variable instead of `enumerate`, `round()` plus
  string concatenation instead of f-string format specs, explicit
  `if`/`else` instead of a one-line conditional trick. Only exception:
  when the "clever" construct genuinely IS the concept being taught (the
  `//` / `%` grid formula in Tutorial 05 is the concept, so it gets a
  proper isolate-then-apply step, not a workaround).
- **Screenshot slots:** `> 📷 **Screenshot slot:** description. Caption:
  "..."` for anything needing a real capture from the actual station.
  Never fabricate what a panel looks like.

## Open decision, not yet resolved

- **"v1 app early, then iterate" restructuring: done.** See "Sequence
  restructure, done" above for the actual executed result and final
  numbering. This bullet used to hold the pre-execution plan, in now-
  stale old numbering; removed rather than left to confuse later
  reading.

- **f-strings are avoided throughout** per the simplification rule above,
  but by Tutorial 08 to 10 (nested functions, more string building) plain
  concatenation starts to feel genuinely clunky rather than just less
  elegant. Decide: add one proper isolate-then-apply f-string step early
  (around Tutorial 03, where both joints and positions are now taught),
  then use them freely after, matching how
  the Y9 set handles `.lower()` and `.split()`. Leaning yes, not yet done
  anywhere.

## Verified gotchas, safe to reuse as deliberate errors

These were hit for real against the actual myCobot/RoboDK station this
session, not invented. Safe to use as planted mistakes elsewhere in the
arc if it ever needs a second instance of the same class of bug.

- **Pattern to check on any `dir()`-based step, deliberate bug or not:**
  a `dir()` check only teaches cleanly if it resolves to ONE obvious
  right answer. `robodk.robomath`'s xyzrpw-related names actually return
  two candidates, `pose_2_xyzrpw` and `xyzrpw_2_pose`, both plausible at
  a glance. This surfaced when Tutorial 02 still had this as a
  deliberate broken-import bug; removed since (see below), but the
  disambiguation teaching, the `thing_2_otherthing` naming convention,
  moved into the proactive check-before-importing version instead and
  is still real content. If any tutorial adds a similar `dir()` step,
  check the real output first, don't assume it resolves to a single
  obvious name.

- **Tutorial 02's Step 4 changed: no longer a deliberate bug.** Used to
  have students type `Pose_2_xyzrpw` (wrong casing) on purpose, hit the
  ImportError, then `dir()` their way to the fix. Changed to a proactive
  check instead, `dir()` before importing, never typing the wrong name
  at all. Reasoning: the risk of typing something wrong, even briefly
  and even corrected immediately after, is that it becomes the thing a
  student remembers rather than the lesson. The real fact,
  `robodk.robomath.Pose_2_xyzrpw` doesn't exist, the real name is
  lowercase `pose_2_xyzrpw`, is unchanged and still worth knowing if
  building anything else that touches this module.
- `Item.JointLimits()` can return a third value depending on RoboDK
  version, index rather than unpack.
- `Item.Tool().Pos()` returns `[0, 0, 0]` with no tool set, not an error.
- `AttachClosest()` / `DetachAll()` must be called on a *tool* item, not
  the robot item, or RoboDK raises "Invalid item provided." Used in
  Tutorial 08.
- A board position close to the base (radius ~90mm at this layout) can
  make hover height and surface height resolve to different IK branches,
  causing `MoveL` to raise `TargetReachError` even though both endpoints
  solve individually. Used in Tutorial 09, real joint numbers from our
  own diagnostic run (J1 12.5° vs J1 114.4°, same X/Y).
- A layout that scores clean on a flip-jump metric alone can still sit at
  ~94% of nominal reach, nearly fully extended. Used in Tutorial 10.

## Tooling gotchas (teacher-facing, not student-facing content)

- RoboDK's embedded Python (`Python-Embedded\python.exe`) needs `pip`
  bootstrapped and `import site` uncommented in the `._pth` file before
  any package install will actually be importable.
- IDLE is currently the reliable path. Confirmed working, repeatedly,
  this session.
- VS Code works, but: (1) RoboDK's own "External Python editor" launcher
  hung once tonight trying to spawn an editor, don't rely on that
  integration; open VS Code independently instead. (2) RoboDK's bundled
  VS Code has no Python extension by default, no run button, use the
  integrated terminal (`python file.py`, or the full path to RoboDK's
  python.exe if the wrong interpreter is on PATH) or install the Python
  extension separately.
- `AttachClosest` in a Tkinter panel: clicking a button works without OS
  keyboard focus (Tk delivers mouse events regardless), but typing needs
  real focus, and clicking away and back doesn't reliably restore it for
  a window spawned from another process. Fix if this recurs: on click,
  call `window.focus_force()` then `event.widget.focus_set()`, in that
  order, both, not just the first.
- `EmbedWindow()` docking had unreliable keyboard focus routing on our
  install. Standalone Tkinter window only, don't rely on docking.
- Mermaid renders fine on plain `github.com` blob view. Confirmed broken
  specifically by a school-managed Chrome extension throwing errors
  during React's render (`contentScript.js`, a `'sentence'` TypeError),
  not by anything in our diagram syntax. Incognito sidesteps it. Noted in
  the student README. If this resurfaces, don't re-diagnose Mermaid
  syntax first, check the browser profile.

## Delivery decision (settled, for now)

Staying on plain GitHub (github.com), not Prepare, not GitHub Pages.
Mermaid diagrams stay as Mermaid, not static images. Students hitting the
school-extension rendering issue are told to use incognito (in README).

A PDF export path (graphviz-rendered diagrams + wkhtmltopdf) was explored
and mostly built before this decision, build artifacts exist in the
working environment if a PDF version is ever wanted again, but nothing
was shipped and this isn't a current priority.

## Tutorials 03 and 04 merged, done

Second structural change, executed after the first restructure above.
Old Tutorial 03 (First Move: raw joint list, one joint change, homing,
parking spot) and old Tutorial 04 (Positions, Not Angles: pose plus IK,
the v1 milestone) merged into one file, still numbered 03. Everything
from old 05 onward shifted down by one to close the gap. New count: 13
files, 00 through 12.

**Why:** both were genuinely light, 132 and 129 lines, 3 and 2 steps,
neither flagged with a special pacing note, no deliberate error in
either. The narrative already wanted to be continuous, old 03 ended
"giving the arm a position instead of a joint angle," old 04 opened
"Tutorial 03 chose a joint angle by hand, this tutorial gives the arm a
position instead," one thought split across a file boundary for no
strong reason. This was also a natural continuation of the "moving by
joints, then targets, then positions" sequence already established by
Tutorials 01 and 02.

**Risk managed on purpose:** the v1 milestone ("you just built the
smallest useful version of this robot") lived in old Tutorial 04 and is
explicitly flagged elsewhere as needing to land as its own moment, not
pass as "another step." Merging risked burying it as the back half of a
longer lesson. Mitigated by keeping an explicit internal structure in
the merged file, "Part one: moving by joints" and "Part two: the limit
of joints, and the fix," with a stated limitation bridging them ("joint
numbers don't tell you where the tool is in space"), and the milestone
section kept as its own clearly marked heading, not folded quietly into
the flow.

**Final numbering after both restructures:**
00 GUI orientation, 01 Python bridge, 02 read state, 03 joints then
positions (merged, the v1 seed), 04 real geometry, 05 grid formula
(plants `ORIGIN_X = 90`), 06 reachability checking, 07 MoveJ vs MoveL,
08 pick and place, 09 the plant detonates, 10 the plant resolved, 11
GUI control panel, 12 game logic finale.

**Verified during the merge, same rigour as the first restructure:**
- Assembled all four of the merged file's code blocks in order and
  confirmed the resulting script parses as one coherent program, imports
  and variables connecting correctly across what used to be a file
  boundary.
- Same whole-arc verification sweep as before: em-dashes, Python syntax,
  Next-chain integrity, bare-number-range sweep. The bare-number bug
  class from the first restructure recurred, predictably, four more
  instances caught: `Tutorial 08 and 11` should have been `08 and 10`,
  `Tutorial 05 and 05` should have been `05 and 04`, and two in this
  notes file itself referencing now-merged tutorial numbers. All fixed
  and re-verified.
- README and TEACHERS-GUIDE.md (table, Mermaid dependency diagram,
  pacing signals, pre-lesson checklist) all rebuilt for the new count
  and cross-checked against the actual files, not assumed consistent.

## Sequence restructure, done

Executed this session, full renumbering, not just a plan. Board and
shape-building moved from their old slot (after the grid formula and
reachability checking) to right after the arm can point at one real
square, before the grid formula generalises it. Final numbering, 14
files, 00 through 13:

00. Hands on the Arm (GUI, unchanged)
01. **New.** The Same Program, in Python, the bridge tutorial, calling
    the GUI-made Home/Drop/Rotate targets by name, the missing link
    between clicking and code that the old sequence skipped entirely
02. Meet the Arm (was 01, read state)
03. First Move (was 02, home plus one joint)
04. Positions, Not Angles (was 03, IK handoff, point at square 5, the
    v1 milestone)
05. **New.** A Real Board (shapes, moved up from its old slot at 07).
    Trimmed per the scope note below, box raw only, straight to the
    wedge raw-vs-function comparison, the mesh-count mismatch, since
    that's the one with a genuine payoff
06. A Board Made of Numbers (was 04, grid formula, now checkable
    against the literal board object built in 05 rather than trusted
    on faith)
07. Check Before You Move (was 05, reachability)
08. Down to the Surface (was 06, MoveJ vs MoveL)
09. Pick It Up (was 08, transfer cycle, AttachClosest bug)
10. The Move That Refused (was 09, TargetReachError diagnosis)
11. Where Should the Board Go? (was 10, layout sweep)
12. The Control Panel (was 11, Tkinter)
13. Your Game (was 12, finale)

**Scope note on the shapes tutorial, applied:** the full session-long
box-raw, box-function, wedge-raw, wedge-function sequence was trimmed
down for the actual student-facing Tutorial 04. Kept: box raw (the
honest opener, every triangle typed out), box wrapped in a function
(proven identical), a round piece via a second function, then the
wedge-at-segments=3 comparison, real 8-vs-12 triangle mismatch, same
visible shape. Cut: the separate reuse-payoff stage and the standalone
wedge-raw file, folded into one tutorial rather than kept as five
separate files.

**Verified during the rebuild, not just asserted:**
- Every geometry claim in the new Tutorial 04 (36-point box, the 8 vs
  12 triangle mismatch, both reach positions) independently recomputed
  and confirmed correct before shipping.
- A real bug caught in the renumbering script itself: the first regex
  pass required a literal space between "Tutorial" and the number,
  which missed references broken across a line wrap ("Tutorial\n01").
  Silent, would have shipped a wrong reference. Fixed by using `\s+`
  instead of a literal space, then re-verified with a whitespace-
  tolerant scan that nothing was missed a second time.
- Four "insertion point" content bugs, not just numbering, caught by
  a full Next-chain audit: Tutorial 00's closing line pointed at the
  wrong next tutorial once the bridge was inserted before it; Tutorial 02's "before you start" line needed the same fix; Tutorial 03's
  closing line still pointed at the old grid-formula tutorial instead
  of the newly-inserted shapes one; Tutorial 07's closing line
  described shapes as something still ahead, when they'd already
  happened three tutorials earlier. All four are the kind of error
  that mechanical renumbering alone cannot catch, since the mapping is
  correct at the level of "what old content does this refer to" while
  being wrong at the level of "does this still make sense in the new
  running order." Checked by building a script that follows every
  Tutorial N's Next line and confirms it lands on N+1, catching both
  of these error classes at once.

## Still not done, queued for the bulk pass

- **00 through 05 done** (across this and the previous session), full
  house style, app-first framing, v1-continuity chain, on the final
  numbering. 06 through 13 are mechanically renumbered and internally
  consistent (verified, see above), but still in the earlier bullet-
  style draft format, not yet given the full house-style pass.
- **Watch for content dependencies verification scripts can't see.**
  Tutorial 00 was rewritten with an "upgrading v1" closing line
  referencing "Home, Drop, Rotate" before Tutorial 01 existed to give
  that line meaning, then Tutorial 01 was written assuming three named
  targets existed, but Tutorial 00's actual Step 4/5 content was never
  updated to match, it still built two generically-named targets. Every
  automated check (em-dash, syntax, Next-chain, bare-number sweep) passed
  clean throughout, because this isn't a numbering error, it's two files
  making incompatible assumptions about station state. Caught by a
  person reading both files together, not by any script. Worth a manual
  "does file N+1 assume something file N doesn't actually provide"
  read on any pair of tutorials with a real state handoff between them
  (station objects, file variables, named targets), not just the
  mechanical checks.
- **Watch for untaught syntax creeping in during rewrites**, not just in
  original drafts. Caught previously in what's now Tutorial 05:
  `pose_2_xyzrpw(robot.Pose())[:3]` used list slicing, never taught
  anywhere in this arc, introduced while editing rather than present in
  the first draft. Fixed to reuse the six-value unpacking pattern from
  Tutorial 02 and Tutorial 03 instead. Worth a dependency check on every file as it gets
  rebuilt, not just the ones still in original-draft form.
- Apply every house-style item above, plus the v1-continuity pattern
  established in 02 through 05, to: 06, 07, 08, 09, 10, 11, 12, 13. (00
  through 05 done, use them as the template.)
- Decide and apply the f-string open decision above, arc-wide, once
  decided. 01 through 05 currently avoid them.
- Six screenshot slots need real captures from an actual RoboDK session
  (listed in each file where they appear).
- Tutorial 00's "Generate Robot Program" pymycobot code sample is a
  plausible reconstruction, never confirmed against a real generated
  file. Check and correct before this reaches students.
- Tutorial 10 (was 10), Step 5's "MoveL now works at the new layout"
  outcome was never actually run end to end in our session, flagged
  in-file, still needs a real test.
- The arc-wide fast-lookup reference guide (named in the original plan,
  `00b`-style, one artefact for the whole set) doesn't exist yet. Will
  need its own code examples re-checked against final numbering once
  written.
