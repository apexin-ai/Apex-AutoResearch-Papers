# exp029 Per-Task-Type Breakdown Analysis

**Experiment**: exp029_seed1 (Cell C: episode-level advantage + full context)
**Checkpoint**: global_step_15 (`/root/autodl-tmp/checkpoints/exp029_hf`)
**Eval split**: eval_out_of_distribution (134 tasks)
**Temperature**: 0.0 (greedy decoding)
**Date**: 2026-05-19

## Per-Task-Type Results

| Task Type | Count | Success | Rate | Avg Actions | Avg Valid Rate | Avg Success Actions |
|---|---|---|---|---|---|---|
| look_at_obj_in_light | 18 | 5 | **27.8%** | 39.1 | 0.731 | 10.8 |
| pick_clean_then_place_in_recep | 31 | 8 | **25.8%** | 40.3 | 0.682 | 12.4 |
| pick_and_place_simple | 24 | 5 | **20.8%** | 41.6 | 0.612 | 9.8 |
| pick_cool_then_place_in_recep | 21 | 2 | 9.5% | 46.7 | 0.729 | 15.5 |
| pick_two_obj_and_place | 17 | 1 | 5.9% | 47.7 | 0.566 | 11.0 |
| pick_heat_then_place_in_recep | 23 | 1 | **4.3%** | 48.2 | 0.577 | 8.0 |
| **Total** | **134** | **22** | **16.4%** | — | — | — |

## T=0.0 vs T=0.4 Comparison

| Setting | Success | Rate |
|---|---|---|
| T=0.4 (prior eval) | 32/134 | 23.88% |
| T=0.0 (this eval) | 22/134 | 16.4% |
| **Delta** | **-10** | **-7.5pp** |

Greedy decoding is substantially worse. The model benefits from sampling diversity — likely to escape repetitive action loops that dominate failed episodes (all failures hit the 50-action cap).

## Key Findings

### 1. Binary solve-or-fail behavior
All failed episodes exhaust the 50-action budget. Successful episodes are extremely short (8–15.5 actions avg). There is no middle ground — the model either immediately finds the right action sequence or gets stuck in loops.

### 2. Task-type performance clusters into two tiers

**Tier 1 (≥20%)**: look_at_obj (27.8%), pick_clean (25.8%), pick_and_place (20.8%)
**Tier 2 (≤10%)**: pick_cool (9.5%), pick_two_obj (5.9%), pick_heat (4.3%)

The gap between tiers is >2x.

### 3. Information loss hypothesis: partially supported, with nuance

By task complexity:
- **Simple (1-step)**: pick_and_place 20.8%, look_at_obj 27.8% → avg ~24%
- **2-step (transform + place)**: pick_clean 25.8%, pick_heat 4.3%, pick_cool 9.5% → avg ~14%
- **Complex (2 objects)**: pick_two_obj 5.9%

The overall trend supports the hypothesis — more steps → lower success. But `pick_clean` is a major outlier: it's a 2-step task that outperforms the 1-step `pick_and_place`.

**Refined interpretation**: The bottleneck is not step count per se, but **appliance interaction difficulty**:
- Cleaning (sinkbasin) is well-generalized — success rate comparable to simple tasks
- Heating (microwave) and cooling (fridge) are poorly generalized — possibly because these appliance interactions are more location-specific and less frequently encountered in diverse configurations during training
- The valid action rate supports this: pick_heat has the lowest valid rate (0.577), suggesting the model frequently generates invalid microwave interaction commands

### 4. Valid action rate correlates with success, but imperfectly

| Task Type | Success Rate | Valid Action Rate |
|---|---|---|
| look_at_obj | 27.8% | 0.731 (highest) |
| pick_cool | 9.5% | 0.729 |
| pick_clean | 25.8% | 0.682 |
| pick_and_place | 20.8% | 0.612 |
| pick_heat | 4.3% | 0.577 |
| pick_two_obj | 5.9% | 0.566 (lowest) |

`pick_cool` breaks the correlation — high valid rate (0.729) but low success (9.5%). The model generates valid actions for fridge interactions but still can't compose the full sequence correctly. This points to a **planning** failure rather than an **action grounding** failure for cool tasks.

### 5. Implications for the paper

The per-task breakdown provides evidence for the claim that episode-level advantage (Cell C) struggles with heterogeneous task difficulty:
- A single scalar reward for the entire episode cannot distinguish whether a heat-task failure is due to the agent's poor policy vs. the task being inherently harder
- Step-level credit assignment (the paper's proposed solution) would allow the model to learn specifically from the successful sub-steps (e.g., picking up the object) even when the overall episode fails at the appliance interaction step

## W&B

No W&B run link in the log — this was an offline eval script.

## Errors/Anomalies

- **Tokenizer regex warning**: cosmetic, from Mistral tokenizer pattern in Qwen3 checkpoint. Does not affect generation.
- **EngineCore shutdown warning**: standard vLLM cleanup, not an error.
- **Exit code**: 0 (clean)
- No other errors or anomalies.

## Result Files

- JSON: `/root/autodl-tmp/tmp/exp029_per_task_type_breakdown.json` (full per-episode data with valid_action_rate)
- Log: `/root/runs/cost-verify-agent-rl/exp029_per_task_breakdown.log`
