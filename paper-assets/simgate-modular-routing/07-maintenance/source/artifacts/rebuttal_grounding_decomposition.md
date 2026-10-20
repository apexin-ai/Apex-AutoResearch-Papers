# Rebuttal P1: Post-Grounding Counterfactual Decomposition

## Data Summary
- **N episodes**: 183 (10 task types, matched by variation index)
- **Baseline source**: `results/plan_c/{task}/episode_summary.jsonl` (paired internal+det, filtered to `internal_final` entries only)
- **Grounding source**: `results/grounding_prompt_ablation/{task}/episode_summary.jsonl` (internal only, with "CRITICAL SAFETY RULE" system prompt patch)
- **Pairing**: Grounding internal scores paired with plan_c deterministic scores on the same variation (det strategy is unaffected by grounding prompt)
- **Per-task episode counts**: chemistry-mix=20, find-animal=20, freeze=20, grow-fruit=20, identify-life-stages-1=14, identify-life-stages-2=10, inclined-plane-determine-angle=20, lifespan-longest-lived=19, lifespan-longest-lived-then-shortest-lived=20, measure-melting-point-unknown-substance=20

## Main Result

| Metric | Baseline (10 tasks) | Post-Grounding | Δ |
|--------|---------------------|----------------|---|
| Internal DR | 50.3% | 35.0% | −15.3pp |
| Det DR | 20.2% | 20.2% | 0 |
| ΔDR (Int−Det) | 30.1% | 14.8% | −15.3pp |
| Δ\_full (det−int mean) | 31.79 | 15.32 | −16.47 |
| Δ\_nd (both-alive gap) | 0.00 | 0.09 | +0.09 |
| DAF (P=100) | 100.0% | 99.4% | −0.6pp |
| Label fraction (death-driven / disambiguating) | 100.0% | 93.2% | −6.8pp |
| death\_asymmetry signals | 65 | 69 | +4 |
| score\_comparison signals | 0 | 5 | +5 |
| both\_dead signals | 32 | 16 | −16 |
| tied\_alive signals | 86 | 93 | +7 |
| Det-preferred | 60 (32.8%) | 51 (27.9%) | −9 |
| Internal-preferred | 5 (2.7%) | 23 (12.6%) | +18 |
| No-preference | 118 (64.5%) | 109 (59.6%) | −9 |

## Per-Task Breakdown

| Task | N | BL Int DR | GR Int DR | Det DR | BL DAF | GR DAF | BL LF | GR LF |
|------|---|-----------|-----------|--------|--------|--------|-------|-------|
| chemistry-mix | 20 | 45% | 20% | 25% | 1.000 | 1.000 | 1.000 | 1.000 |
| find-animal | 20 | 50% | 20% | 25% | 1.000 | 1.315† | 1.000 | 0.714 |
| freeze | 20 | 55% | 40% | 25% | 1.000 | 1.000 | 1.000 | 1.000 |
| grow-fruit | 20 | 45% | 35% | 20% | 1.000 | 1.000 | 1.000 | 1.000 |
| identify-life-stages-1 | 14 | 50% | 43% | 14% | 1.000 | 1.000 | 1.000 | 1.000 |
| identify-life-stages-2 | 10 | 50% | 80%‡ | 20% | 1.000 | 1.000 | 1.000 | 1.000 |
| inclined-plane-determine-angle | 20 | 55% | 20% | 20% | 1.000 | N/A§ | 1.000 | 1.000 |
| lifespan-longest-lived | 19 | 53% | 32% | 16% | 1.000 | 0.867 | 1.000 | 0.875 |
| lifespan-longest-lived-then-shortest-lived | 20 | 45% | 40% | 10% | 1.000 | 1.000 | 1.000 | 1.000 |
| measure-melting-point-unknown-substance | 20 | 55% | 45% | 25% | 1.000 | 1.196† | 1.000 | 0.800 |

† DAF > 1.0: grounding internal scores better than det when both alive, so Δ\_nd is negative—death effect more than explains the gap.  
‡ identify-life-stages-2 grounding increased death rate (50→80%); only 10 matched episodes—interpret cautiously.  
§ DAF undefined: Δ\_full = 0 (grounding equalized the strategies).

## Per-Task Label Distribution

| Task | N | BL dp/ip/np | GR dp/ip/np |
|------|---|-------------|-------------|
| chemistry-mix | 20 | 6/2/12 | 2/3/15 |
| find-animal | 20 | 5/0/15 | 3/4/13 |
| freeze | 20 | 6/0/14 | 5/2/13 |
| grow-fruit | 20 | 6/1/13 | 5/2/13 |
| identify-life-stages-1 | 14 | 5/0/9 | 6/2/6 |
| identify-life-stages-2 | 10 | 3/0/7 | 6/0/4 |
| inclined-plane-determine-angle | 20 | 7/0/13 | 4/4/12 |
| lifespan-longest-lived | 19 | 8/1/10 | 6/2/11 |
| lifespan-longest-lived-then-shortest-lived | 20 | 8/1/11 | 7/1/12 |
| measure-melting-point-unknown-substance | 20 | 6/0/14 | 7/3/10 |

(dp = det-preferred, ip = internal-preferred, np = no-preference)

## Interpretation

Even after the grounding prompt reduces internal death rate by 15.3 percentage points (50.3%→35.0%), death remains the overwhelmingly dominant routing signal. The DAF drops only marginally from 100.0% to 99.4%, and the label fraction (death-driven / total disambiguating labels) decreases from 100% to 93.2%. Out of 183 episodes, only 5 disambiguation labels arise from non-death score comparison (all in the post-grounding condition); baseline has zero such labels. The Δ\_nd (both-alive gap) stays near zero (0.00→0.09), confirming that when both strategies survive, their performance is essentially identical regardless of grounding.

The primary structural change is in the label distribution: internal-preferred episodes jump from 5 to 23, because the grounding prompt reduces internal deaths, creating more cases where internal survives but det dies. Paradoxically, death\_asymmetry signals actually increase (65→69) because the number of both\_dead episodes halves (32→16)—fewer mutual deaths means more asymmetric outcomes. This reinforces the central claim: reducing death rate does not diminish death's role as the routing signal; it simply shifts the direction of the asymmetry, producing more internal-preferred labels while preserving death as the dominant signal source.

**Bottom line for reviewers**: Grounding reduces death rate from ~50% to ~35%, but the counterfactual decomposition structure is essentially unchanged—DAF ≥ 99%, label fraction ≥ 93%. Death is not merely a "bug" that can be prompted away; even with a 30% relative reduction in deaths, the routing signal remains death-dominated.

## Note on Baseline Numbers

The baseline numbers here (Internal DR=50.3%, DAF=100.0%) are computed on the 10 death-prone tasks with plan\_c data only (20 episodes/task). The paper's main decomposition uses all 30 task types across prescreening+research+plan\_c (249 episodes total), yielding aggregate Internal DR=49%, DAF=98.75%, label fraction=90.3%. The per-subset difference arises because the 10 death-prone tasks are a more extreme subset—baseline Δ\_nd is exactly 0 (strategies are perfectly equivalent when both alive), making DAF=100%.
