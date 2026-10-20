# Death Failure Taxonomy (245 Episodes, 11 Tasks)

**Data source**: `results/plan_c/` filtered to match `baseline_245eps/` (245 episodes, seed=42)
**Analysis date**: 2026-05-18

## 1. Death Count Summary

| Strategy | Deaths | Total | Death Rate |
|---|---|---|---|
| Internal (LLM) | 105 | 245 | 42.9% |
| Deterministic | 40 | 245 | 16.3% |

## 2. Fatal Action Classification

| Fatal Action Category | Count | % |
|---|---|---|
| focus on [X] | 105 | 100.0% |

**100.0% of fatal actions are `focus on [X]`**

## 3. Focus-on Target Distribution (Fatal Actions)

| Target | Count | % of focus-on deaths |
|---|---|---|
| workshop | 21 | 20.0% |
| inventory | 18 | 17.1% |
| kitchen | 11 | 10.5% |
| orange | 11 | 10.5% |
| living room | 5 | 4.8% |
| picture | 4 | 3.8% |
| fountain | 3 | 2.9% |
| greenhouse | 3 | 2.9% |
| door | 3 | 2.9% |
| agent | 2 | 1.9% |
| freezer | 2 | 1.9% |
| bed | 2 | 1.9% |
| orange wire | 2 | 1.9% |
| outside | 2 | 1.9% |
| table | 2 | 1.9% |
| hallway | 2 | 1.9% |
| closet | 1 | 1.0% |
| drawing | 1 | 1.0% |
| air | 1 | 1.0% |
| violet light bulb | 1 | 1.0% |

## 4. Per-Task Death Rate

| Task | Int Deaths | Int Total | Int Rate | Det Deaths | Det Total | Det Rate |
|---|---|---|---|---|---|---|
| chemistry-mix | 9 | 20 | 45.0% | 5 | 20 | 25.0% |
| find-animal | 10 | 20 | 50.0% | 5 | 20 | 25.0% |
| find-non-living-thing | 0 | 40 | 0.0% | 0 | 40 | 0.0% |
| freeze | 11 | 20 | 55.0% | 5 | 20 | 25.0% |
| grow-fruit | 9 | 20 | 45.0% | 4 | 20 | 20.0% |
| identify-life-stages-1 | 11 | 20 | 55.0% | 2 | 20 | 10.0% |
| identify-life-stages-2 | 10 | 20 | 50.0% | 4 | 20 | 20.0% |
| inclined-plane-determine-angle | 11 | 20 | 55.0% | 4 | 20 | 20.0% |
| lifespan-longest-lived | 14 | 25 | 56.0% | 4 | 25 | 16.0% |
| lifespan-longest-lived-then-shortest-lived | 9 | 20 | 45.0% | 2 | 20 | 10.0% |
| measure-melting-point-unknown-substance | 11 | 20 | 55.0% | 5 | 20 | 25.0% |

## 5. Action Category Distribution (Internal)

| Category | Death Episodes (%) | Non-Death Episodes (%) |
|---|---|---|
| focus on [X] | 5.4% | 3.4% |
| connect [X] to [Y] | 82.0% | 72.0% |
| disconnect [X] | 1.8% | 4.3% |
| move [X] to [Y] | 0.0% | 0.0% |
| movement | 0.0% | 0.0% |
| object interaction | 3.4% | 13.1% |
| observation | 7.1% | 5.6% |
| other | 0.3% | 1.6% |

## Key Findings

1. Internal strategy: 105/245 episodes end in death (42.9%), vs deterministic 40/245 (16.3%)
2. 105/105 fatal actions (100.0%) are `focus on [X]`
3. ALL deaths caused by `focus on [X]` (100%)
4. Top focus-on targets: `workshop` (21), `inventory` (18), `kitchen` (11)
5. `find-non-living-thing` has 0% death rate (both strategies)