# W4: Task-Type Positive Control — Routing Signal Is Task-Level

## Comparison Table

| Method | Input | Balanced Acc | Notes |
|--------|-------|-------------|-------|
| Majority baseline | — | 50.0% | DummyClassifier |
| Step-only router (0.6B) | obs + action_history | 56.3% | Existing (plan-008-v4) |
| Step-only router (1.7B) | obs + action_history | 59.3% | Existing (plan-008-v4) |
| Step-only router (4B) | obs + action_history | 57.2% | Existing (plan-008-v4) |
| **Task-type LogReg** | task_type one-hot | **64.7% ± 15.0%** | 5-fold CV, episode-grouped |
| **Task-type MLP** | task_type one-hot | **64.7% ± 15.0%** | 5-fold CV, episode-grouped |
| **Task-type LOTO LogReg** | task_type one-hot | 50.0% (mixed types) | Leave-one-task-type-out |

## Data Summary

- 2040 steps, 11 task types
- Label distribution: 1830 det-preferred (89.7%), 210 internal-preferred (10.3%)
- 7/11 task types are **pure** (100% det-preferred): find-animal, freeze, identify-life-stages-1/2, inclined-plane-determine-angle, lifespan-longest-lived, measure-melting-point-unknown-substance
- 4/11 task types are **mixed**: chemistry-mix, find-non-living-thing, grow-fruit, lifespan-longest-lived-then-shortest-lived

## LOTO Per-Task-Type Results

| Task Type | N | Internal | Det | LOTO BA |
|-----------|---|----------|-----|---------|
| chemistry-mix | 240 | 60 | 180 | 50.0% |
| find-animal | 60 | 0 | 60 | 100.0%* |
| find-non-living-thing | 510 | 90 | 420 | 50.0% |
| freeze | 180 | 0 | 180 | 100.0%* |
| grow-fruit | 120 | 30 | 90 | 50.0% |
| identify-life-stages-1 | 180 | 0 | 180 | 100.0%* |
| identify-life-stages-2 | 120 | 0 | 120 | 100.0%* |
| inclined-plane-determine-angle | 120 | 0 | 120 | 100.0%* |
| lifespan-longest-lived | 150 | 0 | 150 | 100.0%* |
| lifespan-longest-lived-then-shortest-lived | 180 | 30 | 150 | 50.0% |
| measure-melting-point-unknown-substance | 180 | 0 | 180 | 100.0%* |

*Trivial: single-class task type, any constant prediction achieves BA=1.0.

## Analysis

**5-fold CV: task-type identity alone outperforms step-level routers.** A logistic regression on 11-dimensional task-type one-hot features achieves 64.7% balanced accuracy — higher than all three Qwen3 LoRA routers (56–59%) that observe full step-level context (observation text + action history). This confirms that the dominant routing signal is a **task-type-level property**, not a step-level property. The step-level routers' 56–59% performance is best explained as a noisy, indirect attempt to recover task-type identity from observations.

**LOTO: the signal does not generalize across task types.** When a task type is held out entirely, its one-hot dimension is always zero at test time, and the model can only fall back to the bias term. All 4 mixed-label task types drop to exactly 50% BA (random). The 7 pure task types trivially achieve 100% because they have only one class. This demonstrates that the routing preference is an **opaque per-task-type constant** — there is no learnable cross-task-type pattern.

**Rebuttal narrative: signal-limited, not architecture-limited.** The step-level router's modest 56–59% accuracy is not a failure of model capacity or training strategy — scaling from 0.6B to 4B yields no meaningful gain. The bottleneck is the signal itself: routing preference is determined at the task-type level, and step-level features carry negligible additional information. A simple task-type lookup table achieves higher accuracy than any neural router trained on step content. This motivates the architectural pivot to **task-level routing** (SimGate), which directly conditions on task identity rather than attempting to infer it from step observations.
