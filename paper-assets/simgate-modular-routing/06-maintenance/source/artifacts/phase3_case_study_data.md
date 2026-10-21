# Non-Death Episode Case Studies (find-non-living-thing)

Source: `results/gemma_scienceworld_counterfactual/find-non-living-thing/` on westd-18266
All episodes use ScienceWorld task "find non living thing" with different variations (room layouts, object placements).
Key: all episodes are `both_alive` (no death in either strategy). Routing preference comes purely from task performance.

---

## Episode 3 (det-preferred, gap=67)

- **Task**: "Find a non-living thing. First, focus on the thing. Then, move it to the orange box in the kitchen." (variation 3)
- **Det score: 67, Internal score: 0**
- **Det key actions** (30 steps):
  - Steps 0–10: systematic exploration — connects agent to inventory, checks task, explores objects (orange, axe, blue jay, etc.)
  - **Step 11: `focus on orange` [0→58]** — correctly identifies "orange" as a non-living thing
  - Step 13: `pick up fountain` — continues exploring
  - **Step 22: `open door to kitchen` [58→67]** — makes progress on the transport subtask (moving object toward kitchen)
  - Remaining steps: further exploration attempts (mix, connect)
- **Internal key actions** (30 steps):
  - Steps 0–18: entirely nonsensical `connect` actions — "connect air to outside", "connect axe to door to foundry", "connect blue jay to door to greenhouse", "connect fountain to butterfly", "connect fire pit to dove", etc. No navigation, no `focus`, no `pick up`.
  - Steps 19–29: repeated `look around` / `focus on door to kitchen` loop — recognizes it should go to the kitchen but never focuses on any non-living object
- **Why det wins**: Internal misuses the ScienceWorld action space — it issues random `connect` commands (which create electrical/physical connections between objects) instead of navigation and interaction actions. It never identifies any non-living thing. Det follows a more systematic pattern: checks the task, identifies "orange" as a valid non-living thing, focuses on it (+58), then opens the kitchen door to begin transport (+9). The 67-point gap comes from Det both finding the target AND making progress toward the goal location.

---

## Episode 17 (det-preferred, gap=8)

- **Task**: "Find a non-living thing. First, focus on the thing. Then, move it to the purple box in the living room." (variation 17)
- **Det score: 58, Internal score: 50**
- **Det key actions** (30 steps):
  - Steps 0–20: exploration — connects to objects, checks task (6 `task` actions), navigates kitchen/greenhouse area
  - **Step 21: `focus on orange` [0→58]** — identifies "orange" as the target non-living thing
  - Steps 22–29: attempts to move orange (inventory, connect), checks task again
- **Internal key actions** (30 steps):
  - Steps 0–17: random `connect` actions — "connect air to outside", "connect axe to inventory", "connect orange to greenhouse", "connect fountain to ground"
  - **Step 18: `focus on fountain` [0→50]** — identifies "fountain" as a non-living thing
  - Steps 19–29: stuck — repeated `focus on substance in fountain`, `look at air` loop
- **Why det wins**: Both strategies successfully find a non-living thing, but they choose different objects. Det picks "orange" (58 pts) while Internal picks "fountain" (50 pts). In ScienceWorld's scoring, more canonical/manipulable non-living objects score higher. This 8-point gap illustrates that even in no-death scenarios, object selection quality creates a routing signal — Det's knowledge retrieval yields a better target choice.

---

## Episode 12 (internal-preferred, gap=−9)

- **Task**: "Find a non-living thing. First, focus on the thing. Then, move it to the red box in the living room." (variation 12)
- **Internal score: 67, Det score: 58**
- **Internal key actions** (30 steps):
  - Steps 0–11: exploration — connects agent to inventory/living room, explores objects (book shelf, chair, cloth, steel table, door, hallway), checks inventory
  - **Step 12: `focus on orange` [8→67]** — correctly identifies "orange" as the target non-living thing (+59 points)
  - Steps 13–15: attempts to move — `connect orange to inventory`, `connect red box to orange`
  - Steps 16–29: stuck in `inventory` / `look around` / `look in red box` loop
- **Det key actions** (30 steps):
  - Steps 0–7: exploration — connects agent to living room/object, checks task, explores
  - **Step 8: `focus on red box` [8→58]** — focuses on the RED BOX (the destination container!) instead of finding a separate non-living thing
  - Steps 9–22: wanders — focuses on hallway, drawing, door; tries `eat orange`; explores steel table
  - Steps 23–29: stuck in look around loop
- **Why internal wins**: Det makes a **semantic error** — it focuses on the "red box," which is the destination container mentioned in the task ("move it to the red box in the living room"). While the red box is technically a non-living thing (scoring 58 pts), the task intends for the agent to find a *different* non-living object and transport it *to* the red box. Internal correctly distinguishes between the target object and the destination container, choosing "orange" (67 pts). This case demonstrates that Internal's reasoning can catch semantic subtleties that Det's pattern-matching misses.

---

## Episode 16 (internal-preferred, gap=−58)

- **Task**: "Find a non-living thing. First, focus on the thing. Then, move it to the yellow box in the living room." (variation 16)
- **Internal score: 58, Det score: 0**
- **Internal key actions** (30 steps):
  - Steps 0–19: exploration via `connect` actions — navigates through outside, foundry, greenhouse, kitchen area. Connects objects (axe, blue jay, butterfly, dove, fire pit, fountain, orange)
  - **Step 20: `focus on orange` [0→58]** — successfully identifies "orange" as a non-living thing
  - Steps 21–29: stuck — `eat orange`, then repeated `look around`
- **Det key actions** (30 steps):
  - Steps 0–29: complete failure — alternates between `connect` actions and `task` checks (9 `task` actions total!). Actions: "connect axe to inventory", "focus on foundry", "connect greenhouse to foundry", "connect shovel to kitchen", "disconnect substance in fountain", "move shovel to greenhouse", etc.
  - **No score-changing action ever taken** — never focused on any valid non-living thing
- **Why internal wins**: Det is trapped in a pathological loop — it repeatedly checks the task description (9 times) but never translates that understanding into a correct action. It tries random connects and movements but never issues a `focus on [object]` command for a valid non-living thing. Internal, despite also using many random `connect` actions, eventually focuses on "orange" and scores. This case shows that Det's systematic approach can sometimes fail catastrophically when its action templates don't match the environment state.

---

## Summary Statistics (find-non-living-thing, Gemma model, 20 episodes × 2 runs)

| Label | Count (run 1) | Score gaps |
|-------|--------------|------------|
| det-preferred | 7 | 58, 67, 50, 50, 50, 58, 8 |
| internal-preferred | 3 | −8, −9, −58 |
| no-preference | 10 | 0 (tied) |

All 20 episodes: `both_alive` (no death). Signal source: `score_comparison` or `tied_alive`.

## Key Findings for Paper

1. **Non-death routing signals exist**: In find-non-living-thing (a safe task with no death risk), 50% of episodes show a clear routing preference (10/20 non-tied).
2. **Det-preferred dominance**: 7/10 non-tied episodes favor deterministic, primarily because Det's knowledge retrieval correctly identifies higher-scoring non-living objects.
3. **Internal wins on semantic reasoning**: The 3 internal-preferred cases show Internal catching semantic subtleties (e.g., distinguishing target from destination container) or recovering from exploration where Det gets stuck.
4. **Object selection quality matters**: Even when both strategies find a valid non-living thing, the *choice* of object creates a scoring gap (e.g., orange=58 vs. fountain=50 vs. air=50 vs. red box=58).
5. **Bidirectional signal**: The framework correctly captures both directions — it's not a one-way bias toward deterministic.
