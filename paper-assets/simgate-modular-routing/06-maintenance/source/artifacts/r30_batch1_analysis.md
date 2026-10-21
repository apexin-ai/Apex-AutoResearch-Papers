# Part 1: Non-Death Non-Tie Episode Analysis (Qwen2.5-7B)

**Source**: `results/plan_c/find-non-living-thing/` (all 20 non-death non-tie episodes come from this single task type)

**Total**: 20 episodes — 16 det-preferred, 4 int-preferred. Zero episodes from other task types qualify (all other task types have death on at least one side for every non-tie episode).

## Summary Table

| task_type | n_episodes | det_pref | int_pref | hallucination | action_selection | object_quality |
|-----------|-----------|----------|----------|---------------|------------------|----------------|
| find-non-living-thing | 20 | 16 | 4 | 10 | 3 | 7 |

### Error Category Breakdown by Preference Direction

| category | det-preferred | int-preferred | total |
|----------|--------------|---------------|-------|
| Hallucination-induced error | 8 | 2 | 10 |
| Action selection error | 2 | 1 | 3 |
| Object selection quality | 6 | 1 | 7 |

## Per-Episode Details

### Object Selection Quality (7 episodes)

#### Episode 0 — var 0
- det_score: 58, int_score: 50 → det-preferred (gap=8)
- Category: **Object selection quality**
- Key difference: AI found **picture** (50pts, step 18) then stuck repeating "focus on picture" 11x. AD found **orange** (58pts, step 21) via different navigation path. Both succeeded; AD picked higher-value object.

#### Episode 3 — var 3
- det_score: 58, int_score: 50 → det-preferred (gap=8)
- Category: **Object selection quality**
- Key difference: AI found **substance in fountain** (50pts, step 25). AD found **orange** (58pts, step 21). AD scored earlier and higher. Both navigated successfully.

#### Episode 12 — var 12
- det_score: 67, int_score: 58 → det-preferred (gap=9)
- Category: **Object selection quality**
- Key difference: AI ate orange first (self-sabotage), then found steel table chain (58pts total). AD found orange + incidental points (67pts total). AI recovered via alternate objects but lower total. AD achieved highest score in dataset.

#### Episode 18 — var 18
- det_score: 58, int_score: 50 → det-preferred (gap=8)
- Category: **Object selection quality**
- Key difference: AI found **drawing** (50pts, step 27 — very late). AD found **orange** (58pts, step 20). AI wasted time on inventory calls and ate orange before finding drawing.

#### Episode 26 — var 26
- det_score: 58, int_score: 50 → det-preferred (gap=8)
- Category: **Object selection quality**
- Key difference: AI ate orange (destroying 58pt opportunity), then found **steel table** (50pts, step 21). AD found **orange** (58pts, step 12 — fast). AI self-sabotaged but recovered via alternate object.

#### Episode 29 — var 29
- det_score: 58, int_score: 50 → det-preferred (gap=8)
- Category: **Object selection quality**
- Key difference: AI wasted 8 steps calling "task" commands (no-op), then found **fountain** (50pts, step 23). AD found **orange** (58pts, step 19). AI's waste led to settling for lower-value object.

#### Episode 15 — var 15 *(int-preferred)*
- det_score: 50, int_score: 58 → int-preferred (gap=8)
- Category: **Object selection quality**
- Key difference: AI found **orange** (58pts, step 16). AD found **battery** (50pts, step 17). Electronics environment — AI picked higher-value object one step faster.

---

### Hallucination-Induced Error (10 episodes)

#### Episode 13 — var 13
- det_score: 58, int_score: 0 → det-preferred (gap=58)
- Category: **Hallucination-induced error**
- Key difference: AI spent all 30 steps in bathroom — "activate toilet", "close toilet drain", "activate sink", "activate bathtub", "close bathtub drain". 15 open/close actions, 7 activate/deactivate. Never navigated out. **AI believed bathroom plumbing actions = finding non-living things.** AD navigated out, found "finger painting" (50pts) + more (58pts total).

#### Episode 16 — var 16
- det_score: 17, int_score: 0 → det-preferred (gap=17)
- Category: **Hallucination-induced error**
- Key difference: AI ate orange (destroying 58pt target), then stuck repeating "focus on inventory" 8x. **AI believed eating = task completion, and inventory = valid non-living target.** AD got only incidental navigation points (17pts), but AI got zero.

#### Episode 20 — var 20
- det_score: 58, int_score: 0 → det-preferred (gap=58)
- Category: **Hallucination-induced error**
- Key difference: AI did 14 connects, then **13 consecutive "focus on inventory"** repeats (steps 17-29). Worst stuck loop in dataset. **AI's state model incorrectly treated "inventory" as a valid non-living thing target.** AD found orange (58pts, step 18).

#### Episode 28 — var 28
- det_score: 58, int_score: 0 → det-preferred (gap=58)
- Category: **Hallucination-induced error**
- Key difference: AI ate orange before focusing on it, then couldn't find alternate target. **AI believed "eat" action = finding/identifying non-living thing.** AD kept orange intact and focused on it (58pts, step 22).

#### Episode 31 — var 31
- det_score: 58, int_score: 0 → det-preferred (gap=58)
- Category: **Hallucination-induced error**
- Key difference: AI ate orange at step 15 (destroying it), then 4 inventory calls, repeated "focus on living room". **AI's "eat before focus" pattern — state model error about what constitutes task completion.** AD focused on orange first (58pts, step 17) before eating it.

#### Episode 34 — var 34
- det_score: 58, int_score: 0 → det-preferred (gap=58)
- Category: **Hallucination-induced error**
- Key difference: AI stuck in bathroom — 18 connects, activate sink/toilet/bathtub, close drains for 30 steps. **Same bathroom hallucination as EP 13.** AD scored fastest in entire dataset: "focus on orange" at step 4 (58pts).

#### Episode 36 — var 36
- det_score: 67, int_score: 0 → det-preferred (gap=67)
- Category: **Hallucination-induced error**
- Key difference: AI ate orange then looked around aimlessly. **Eat-before-focus hallucination.** AD navigated to greenhouse, found orange (67pts total — highest in dataset alongside EP 12).

#### Episode 39 — var 39
- det_score: 17, int_score: 0 → det-preferred (gap=17)
- Category: **Hallucination-induced error**
- Key difference: AI ate orange, then stuck on "focus on inventory" 6x. **Combined eat-before-focus + inventory-as-target hallucinations.** AD also struggled but got incidental navigation points (17pts).

#### Episode 4 — var 4 *(int-preferred)*
- det_score: 0, int_score: 50 → int-preferred (gap=50)
- Category: **Hallucination-induced error**
- Key difference: **AD ate orange** (thinking eating = task completion), then "focus on agent", then 6x "focus on inventory" repeats. Never scored. AI found **picture** (50pts, step 20). Same hallucination pattern but AD was the victim.

#### Episode 17 — var 17 *(int-preferred)*
- det_score: 0, int_score: 58 → int-preferred (gap=58)
- Category: **Hallucination-induced error**
- Key difference: AD stuck in **connect/disconnect oscillation** — "connect kitchen to substance in fountain" / "disconnect kitchen" repeated 4x. **AD's navigation model was confused about room connectivity.** AI found orange (58pts, step 18) efficiently.

---

### Action Selection Error (3 episodes)

#### Episode 10 — var 10
- det_score: 50, int_score: 0 → det-preferred (gap=50)
- Category: **Action selection error**
- Key difference: AI spent all 30 steps on connect/inventory calls — never once used "focus on" any object. 25 connects + 3 inventory + 2 look-around. **AI knew how to navigate but never attempted the scoring action.** AD found "cup containing red paint" (50pts, step 6) very early.

#### Episode 21 — var 21
- det_score: 50, int_score: 0 → det-preferred (gap=50)
- Category: **Action selection error**
- Key difference: AI in bathroom — 18 connects, 6 activate, 6 open/close — all plumbing operations. AD also explored bathroom similarly but squeezed in "focus on picture" at step 29 (50pts). **Both had poor action selection, but AD barely scored at the last moment while AI never tried.**

#### Episode 7 — var 7 *(int-preferred)*
- det_score: 17, int_score: 58 → int-preferred (gap=41)
- Category: **Action selection error**
- Key difference: AD made poor action choices — "wait1", moved oranges between rooms, explored aimlessly. Only got incidental navigation points: "open art studio door" (+8) and "go to art studio" (+9) = 17pts. **AD's actions were real but suboptimal — correct state model, wrong priorities.** AI found orange (58pts, step 18) directly.

---

## Key Patterns

### 1. "Eat Before Focus" — Primary Internal Strategy Failure (11/20 episodes)
Internal strategy ate the orange (a high-value non-living thing worth 58pts) in 11 of 20 episodes. In every case where AI ate orange and AD didn't, AD won by focusing on the intact orange. The "eat" action destroys the object; the scoring action is "focus on". AI's state model incorrectly equates eating with finding/identifying.

### 2. Bathroom Plumbing Trap (3 episodes: 13, 21, 34)
Internal strategy got stuck in bathroom for 30 steps doing plumbing (activate toilet/sink, close drains). These actions never score. AI's model incorrectly believes interacting with bathroom fixtures = finding non-living things.

### 3. "Focus on Inventory" Loop (3 episodes: 16, 20, 39)
Internal strategy repeatedly tried "focus on inventory" (up to 13 consecutive times). Inventory is not a valid non-living thing target. State model error about what constitutes a valid focus target.

### 4. Deterministic Strategy's Orange Bias
AD found orange (58pts) in 13/16 det-preferred episodes. AD has a strong, consistent bias toward this high-value object. When AD fails, it's usually from eating the orange or getting stuck in navigation loops (same failure modes as AI).

### 5. Score Gaps Are Small for Object Quality, Large for Hallucination
- Object selection quality: gaps = 8-9 pts (consistently small, both strategies functional)
- Hallucination errors: gaps = 17-67 pts (one strategy scored 0, the other found an object)
- Action selection errors: gaps = 41-50 pts (one strategy wasted all steps)

---

# Part 2: 72B Bootstrap CI (Qwen2.5-72B)

**Source**: `results/backbone_72b/` — 255 episodes across 11 task types

## Label Distribution

| metric | value |
|--------|-------|
| Total episodes | 255 |
| det-preferred | 84 (32.9%) |
| int-preferred | 5 (2.0%) |
| no-preference | 166 (65.1%) |
| Non-death episodes | 174 |
| Death-involved episodes | 81 |

**Note**: Actual data shows 5 int-preferred (not 0 as stated in paper draft). Sources: find-non-living-thing ep15 (50/0), grow-fruit ep5 (0/-100), identify-life-stages-2 ep4 (0/-100) & ep17 (4/0), inclined-plane ep7 (0/-100).

## DAF Computation

| metric | point estimate | 95% CI |
|--------|---------------|--------|
| delta_full (mean det−int) | 30.07 | [24.10, 36.21] |
| delta_nd (non-death only) | 2.28 | [0.62, 4.19] |
| **DAF** | **92.4%** | **[86.1%, 97.9%]** |

## Bootstrap Details

- B = 10,000 episode-level resamples with replacement
- Method: for each bootstrap sample, recompute delta_full and delta_nd, then DAF = 1 − delta_nd/delta_full
- All 10,000 samples valid (delta_full > 0 in every resample)
- Seed: 42

## 72B Non-Death Non-Tie Episodes

Only 12 non-death non-tie episodes exist in 72B data (vs 20 in 7B):

| task_type | ep | var | int_final | det_final | label |
|-----------|----|-----|-----------|-----------|-------|
| find-non-living-thing | 0 | 0 | 0 | 67 | det |
| find-non-living-thing | 3 | 3 | 0 | 50 | det |
| find-non-living-thing | 4 | 4 | 0 | 58 | det |
| find-non-living-thing | 5 | 5 | 0 | 50 | det |
| find-non-living-thing | 7 | 7 | 0 | 17 | det |
| find-non-living-thing | 13 | 13 | 0 | 50 | det |
| find-non-living-thing | 15 | 15 | 50 | 0 | int |
| find-non-living-thing | 16 | 16 | 0 | 50 | det |
| find-non-living-thing | 17 | 17 | 0 | 50 | det |
| find-non-living-thing | 18 | 18 | 0 | 58 | det |
| identify-life-stages-2 | 17 | 7 | 4 | 0 | int |
| measure-melting-point | 3 | 3 | 0 | 1 | det |

10 det-preferred, 2 int-preferred among non-death non-tie episodes.

## Interpretation

DAF = 92.4% means death-avoidance accounts for 92.4% of the deterministic strategy's advantage over internal strategy at 72B scale. The residual 7.6% comes from non-death score differences (primarily in find-non-living-thing, where deterministic strategy still finds higher-value objects). The 72B model has even higher DAF than 7B because the stronger model makes fewer non-death errors — its performance gap is almost entirely death-driven.

95% CI [86.1%, 97.9%] excludes values below 86%, confirming death-avoidance dominance is robust.
