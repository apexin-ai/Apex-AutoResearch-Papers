# Death Failure Mode Taxonomy — ScienceWorld (245 Episodes)

**Source**: westb-13313:/root/autodl-tmp/simgate-modular-routing/artifacts/death_failure_taxonomy_245eps.md
**Data**: `results/plan_c/` filtered to `baseline_245eps/` (245 episodes, 11 tasks, seed=42)

## Key Finding

ALL 105 deaths out of 245 internal-strategy episodes (42.9% death rate) share a single trigger: **`focus on [wrong object]`**.

In ScienceWorld, `focus on` is the **answer-submission action**. The LLM agent misuses it as a generic interaction command, targeting rooms (workshop 20%, kitchen 10.5%), containers (inventory 17.1%), and irrelevant objects (orange 10.5%, etc.). The deterministic agent has only 40 deaths (16.3%) across the same episodes.

## Fatal Action Classification

| Fatal Action Category | Count | % |
|---|---|---|
| focus on [X] | 105 | 100.0% |

## Focus-on Target Distribution (Top 5)

| Target | Count | % |
|---|---|---|
| workshop | 21 | 20.0% |
| inventory | 18 | 17.1% |
| kitchen | 11 | 10.5% |
| orange | 11 | 10.5% |
| living room | 5 | 4.8% |

## Per-Task Death Rate (Internal vs Deterministic)

| Task | Int Rate | Det Rate |
|---|---|---|
| find-non-living-thing | 0.0% | 0.0% |
| chemistry-mix | 45.0% | 25.0% |
| grow-fruit | 45.0% | 20.0% |
| lifespan-longest-lived-then-shortest-lived | 45.0% | 10.0% |
| find-animal | 50.0% | 25.0% |
| identify-life-stages-2 | 50.0% | 20.0% |
| freeze | 55.0% | 25.0% |
| identify-life-stages-1 | 55.0% | 10.0% |
| inclined-plane-determine-angle | 55.0% | 20.0% |
| measure-melting-point-unknown-substance | 55.0% | 25.0% |
| lifespan-longest-lived | 56.0% | 16.0% |

## Paper Implications

The death asymmetry is NOT because the internal agent faces more danger. It's because it **systematically self-destructs through incorrect answer submission**, while the deterministic agent avoids the death trigger more effectively. This is an **action-space grounding failure**: the LLM misuses `focus on` as a generic interaction command.

## Narrative
"A single action-space grounding failure (misusing focus-on as interaction) is the root cause of catastrophic failure, making death the dominant and structurally unavoidable routing signal"