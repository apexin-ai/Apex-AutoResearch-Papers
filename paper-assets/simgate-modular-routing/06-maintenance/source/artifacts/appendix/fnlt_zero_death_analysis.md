# Why find-non-living-thing Has 0% Death Rate: A Natural Control for Death Dominance

## Executive Summary

Among 11 tasks in the plan-012-full main experiment (N=245 episodes), find-non-living-thing is the only task with 0% death rate across both modalities (n=40 runs). Analysis of 105 `focus on` actions in find-non-living-thing reveals the mechanism: ScienceWorld implements task-dependent `focus on` semantics where the same action on the same target can be lethal or benign depending on the task context. In find-non-living-thing, `focus on` never triggers death because the target category (non-living things) is the overwhelming majority class in the environment, making wrong-answer penalties structurally impossible.

## 1. Death Mechanism Verification

### 1.1 `focus on` is the sole death mechanism across all tasks

| Task | focus_on deaths | non-focus_on deaths |
|------|:-:|:-:|
| find-non-living-thing | 0 | 0 |
| freeze | 14 | 0 |
| chemistry-mix | 17 | 0 |
| find-animal | 14 | 0 |
| grow-fruit | 13 | 0 |
| identify-life-stages-1 | 16 | 0 |
| identify-life-stages-2 | 13 | 0 |
| inclined-plane-determine-angle | 16 | 0 |
| lifespan-longest-lived | 15 | 0 |
| lifespan-longest-lived-then-shortest-lived | 13 | 0 |
| measure-melting-point-unknown-substance | 15 | 0 |

Every death across all 245 episodes is caused by `focus on`. No other action (connect, disconnect, activate, eat, look, etc.) ever causes death. This confirms `focus on` as the necessary and sufficient condition for death.

## 2. Task-Dependent `focus on` Semantics

### 2.1 The same target, different outcomes

The same `focus on` target produces opposite outcomes depending on task context:

| `focus on` target | find-non-living-thing | find-animal | freeze | chemistry-mix |
|---|:-:|:-:|:-:|:-:|
| inventory | 0 (neutral) | -100 (DEATH) | DEATH | DEATH |
| living room | 0 (neutral) | -100 (DEATH) | DEATH | DEATH |
| orange | +59 (score) | -108 (DEATH) | DEATH | DEATH |
| kitchen | 0 (neutral) | -100 (DEATH) | DEATH | - |
| workshop | 0 (neutral) | -100 (DEATH) | - | - |
| hallway | 0 (neutral) | -100 (DEATH) | DEATH | - |
| picture | +50 (score) | - | - | - |
| blue jay | - | +50 (score) | - | - |

The observations are identical (e.g., "You focus on the inventory.") but the consequences are task-determined.

### 2.2 Three categories of `focus on` behavior

ScienceWorld implements `focus on` as an **answer submission mechanism** for identification tasks, with task-dependent consequences:

1. **Identification tasks, correct target**: score+ (e.g., focus on blue jay in find-animal, focus on picture in find-non-living-thing)
2. **Identification tasks, wrong target**: death with score -100 (e.g., focus on inventory in find-animal)
3. **Non-identification tasks, any target**: death (e.g., focus on anything in freeze, chemistry-mix, grow-fruit)

**Exception**: find-non-living-thing treats non-target items (rooms, containers, etc.) as **neutral** (score_delta=0) rather than wrong answers, because these items are arguably non-living.

## 3. Why find-non-living-thing is Structurally Death-Immune

### 3.1 Target category is the majority class

In ScienceWorld environments, virtually all interactable objects are non-living:
- Rooms: living room, kitchen, hallway, greenhouse, workshop, bedroom, art studio, bathroom
- Furniture: bed, chair, table, cloth sittable
- Appliances: freezer, stove, oven, sink, bathtub, toilet
- Objects: picture, drawing, orange, wood, fountain, inventory, doors
- Tools: stopwatch, switch, light bulb, wire

Living things (animals, plants) are rare and task-specific (e.g., blue jay appears only in certain variations).

### 3.2 Score delta distribution in find-non-living-thing

Across 105 `focus on` actions (52 internal + 53 deterministic):

| Target type | Count | Score+ | Neutral | Death |
|---|:-:|:-:|:-:|:-:|
| Task-relevant objects (picture, orange, air, drawing, wood, chair, violet light bulb) | 34 | 17 | 17 | 0 |
| Rooms/containers (living room, kitchen, inventory, workshop, hallway, etc.) | 62 | 0 | 62 | 0 |
| Furniture (bed, cloth sittable, bathtub) | 5 | 0 | 5 | 0 |
| Other (freezer, door, art studio, fountain, greenhouse) | 4 | 0 | 4 | 0 |
| **Total** | **105** | **17** | **88** | **0** |

Zero negative score_deltas. The worst outcome of `focus on` in find-non-living-thing is scoring 0, never -100.

### 3.3 Contrast with find-animal (the structural inverse)

| Metric | find-non-living-thing | find-animal |
|---|---|---|
| Target category | non-living (majority class) | animal (minority class) |
| Environment objects matching target | ~95%+ | ~5% (blue jay only) |
| `focus on` total (both modalities) | 105 | 25 |
| `focus on` deaths | 0 (0%) | 14 (56%) |
| `focus on` correct answers | 17 (16%) | 7 (28%) |
| `focus on` neutral | 88 (84%) | 4 (16%) |
| Internal death rate | 0/20 (0%) | 9/20 (45%) |
| Deterministic death rate | 0/20 (0%) | 5/20 (25%) |

find-animal is the structural inverse: animals are rare, so random `focus on` overwhelmingly targets non-animals, triggering death.

## 4. Performance Statistics

### 4.1 Episode-level results

| Ep | Var | Internal Score | Det Score | Label |
|---|---|---|---|---|
| 0 | 0 | 50.0 | 50.0 | no-preference |
| 1 | 1 | 0.0 | 0.0 | no-preference |
| 2 | 2 | 8.0 | 8.0 | no-preference |
| 3 | 3 | 0.0 | 50.0 | det-preferred |
| 4 | 4 | 58.0 | 58.0 | no-preference |
| 5 | 5 | 0.0 | 50.0 | det-preferred |
| 6 | 6 | 0.0 | 0.0 | no-preference |
| 7 | 7 | 0.0 | 50.0 | det-preferred |
| 8 | 8 | 8.0 | 67.0 | det-preferred |
| 9 | 9 | 50.0 | 50.0 | no-preference |
| 10 | 10 | 0.0 | 0.0 | no-preference |
| 11 | 11 | 0.0 | 0.0 | no-preference |
| 12 | 12 | 67.0 | 58.0 | internal-preferred |
| 13 | 13 | 0.0 | 67.0 | det-preferred |
| 14 | 14 | 0.0 | 0.0 | no-preference |
| 15 | 15 | 0.0 | 0.0 | no-preference |
| 16 | 16 | 0.0 | 50.0 | det-preferred |
| 17 | 17 | 58.0 | 0.0 | internal-preferred |
| 18 | 18 | 58.0 | 75.0 | det-preferred |
| 19 | 19 | 0.0 | 0.0 | no-preference |

### 4.2 Aggregate statistics

| Metric | Internal | Deterministic | Delta |
|---|---|---|---|
| Mean score | 17.9 | 31.6 | +13.7 |
| Score=0 episodes | 12/20 (60%) | 8/20 (40%) | - |
| Score>0 episodes | 8/20 (40%) | 12/20 (60%) | - |
| Death episodes | 0/20 (0%) | 0/20 (0%) | 0 |
| Mean steps | 30.0 | 30.0 | 0 |
| Label: det-preferred | - | - | 7/20 |
| Label: internal-preferred | - | - | 2/20 |
| Label: no-preference | - | - | 11/20 |

All episodes reach max steps (30), confirming no early termination from death.

### 4.3 Action distribution

| Action type | Internal | Deterministic |
|---|---|---|
| connect | 396 (66.0%) | 441 (73.5%) |
| focus on | 52 (8.7%) | 53 (8.8%) |
| disconnect | 23 (3.8%) | 20 (3.3%) |
| inventory | 26 (4.3%) | 14 (2.3%) |
| other | 103 (17.2%) | 72 (12.0%) |

### 4.4 `focus on` usage rate comparison (per 20 episodes)

| Task | Internal focus on | Det focus on | Internal death eps | Det death eps |
|---|:-:|:-:|:-:|:-:|
| **find-non-living-thing** | **52** | **53** | **0/20** | **0/20** |
| freeze | 11 | 10 | 11/20 | 3/20 |
| chemistry-mix | 10 | 7 | 10/20 | 7/20 |
| find-animal | 9 | 16 | 9/20 | 5/20 |
| grow-fruit | 10 | 3 | 10/20 | 3/20 |
| identify-life-stages-1 | 10 | 6 | 10/20 | 6/20 |
| identify-life-stages-2 | 10 | 3 | 10/20 | 3/20 |
| inclined-plane-determine-angle | 11 | 5 | 11/20 | 5/20 |
| lifespan-longest-lived | 10 | 5 | 10/20 | 5/20 |
| lifespan-longest-lived-then-shortest-lived | 9 | 4 | 9/20 | 4/20 |
| measure-melting-point-unknown-substance | 10 | 5 | 10/20 | 5/20 |

find-non-living-thing uses `focus on` MORE than any other task (52+53=105 vs 10-21 range), yet has 0 deaths. In death-prone tasks, nearly every `focus on` kills.

## 5. Discussion: Implications for Death Dominance

### 5.1 Natural control group

find-non-living-thing serves as a natural control for the death dominance finding:
- It uses `focus on` more frequently than any death-prone task
- The `focus on` actions target the same objects (inventory, orange, living room, etc.)
- The only difference is task context, which determines whether `focus on` is lethal
- Result: 0% death, confirming that `focus on` lethality is task-determined, not action-determined

### 5.2 Strengthened causal claim

The conjunction of two facts:
1. **Every death across all tasks is caused by `focus on`** (0 non-focus deaths)
2. **find-non-living-thing uses `focus on` heavily yet never dies**

...establishes that death requires the conjunction of (a) the `focus on` action AND (b) a task context where `focus on` triggers the death penalty. find-non-living-thing lacks condition (b) because its target category is the majority class, making wrong-answer death structurally impossible.

### 5.3 Why the performance gap is purely non-death

The internal vs deterministic gap in find-non-living-thing (mean: 17.9 vs 31.6, delta=+13.7) is entirely driven by better task performance in deterministic mode (more episodes scoring >0: 12 vs 8), with zero contribution from death avoidance. This isolates the "pure routing quality" effect, free from the confound of differential death rates.

## Data Source

- Location: `westd-18266:/root/autodl-tmp/simgate-modular-routing/results/seed123-plan-c/find-non-living-thing/`
- Files: `episodes.jsonl` (20 episodes, each with always_internal + always_deterministic runs)
- Analysis date: 2026-05-18
