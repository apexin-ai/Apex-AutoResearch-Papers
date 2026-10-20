# Death-Proximal Labeling Router — Experiment Report

**Experiment ID**: death-proximal-labeling-router
**Date**: 2026-05-19
**Server**: westb-13313 (RTX 5090 32GB)
**Model**: Qwen3-0.6B + LoRA (r=16, α=32, q/k/v/o_proj)
**Status**: DONE (negative)

## Hypothesis

Training a router only on steps near the fatal step (death-proximal window k) will improve step-level balanced accuracy compared to training on all 30 steps per episode, because steps far from the fatal step carry less informative signal about route preference.

## Setup

### Data
- Source: 68 episodes from results/plan_c/, 2040 labeled steps total
- Train/test split: 85/15 at episode level (seed=42) → 58 train / 10 test episodes
- Eval set: 300 steps (270 deterministic, 30 internal) from 10 episodes (9 det, 1 int)

### Training Variants
| Variant | Train Steps | Det | Internal | Internal% |
|---------|-------------|-----|----------|-----------|
| full    | 1740        | 1560| 180      | 10.3%     |
| k10     | 903         | 799 | 104      | 11.5%     |
| k5      | 684         | 600 | 84       | 12.3%     |
| k3      | 596         | 520 | 76       | 12.8%     |
| k1      | 508         | 440 | 68       | 13.4%     |

### Training Config
- LoRA: r=16, alpha=32, targets=q_proj,k_proj,v_proj,o_proj
- Epochs: 3, LR: 2e-4, batch_size: 4, grad_accum: 8
- bf16, warmup_ratio=0.1, weight_decay=0.01

## Results

### Main Table
| Variant | Train | StepBA(all) | StepBA(death) | StepBA(prox) | EpBA   |
|---------|-------|-------------|---------------|--------------|--------|
| full    | 1740  | 0.5000      | 1.0000        | 1.0000       | 0.5000 |
| k10     | 903   | 0.4963      | 0.9905        | 0.9870       | 0.5000 |
| k5      | 684   | 0.4926      | 0.9857        | 0.9740       | 0.5000 |
| k3      | 596   | 0.4870      | 0.9857        | 0.9610       | 0.5000 |
| k1      | 508   | 0.4907      | 0.9952        | 0.9870       | 0.5000 |

### Per-Class Breakdown (Step BA All)
| Variant | Det Recall | Int Recall | Det Correct/Total | Int Correct/Total |
|---------|------------|------------|--------------------|--------------------|
| full    | 1.0000     | 0.0000     | 270/270            | 0/30               |
| k10     | 0.9926     | 0.0000     | 268/270            | 0/30               |
| k5      | 0.9852     | 0.0000     | 266/270            | 0/30               |
| k3      | 0.9741     | 0.0000     | 263/270            | 0/30               |
| k1      | 0.9815     | 0.0000     | 265/270            | 0/30               |

## Analysis

### Why This Failed

1. **Death-asymmetry episodes are mono-class**: All death_asymmetry steps are labeled "deterministic" (the surviving branch always wins). Internal labels come exclusively from score_comparison episodes. Death-proximal filtering only removes distant deterministic steps from death_asymmetry episodes — it does NOT increase internal representation.

2. **Class imbalance overwhelms signal**: Even with k=1 (most aggressive filtering), the training set is still 86.6% deterministic. The model learns to always predict deterministic, achieving high raw accuracy (~90%) but 0% internal recall.

3. **Proximal/death BA metrics are misleading**: The death_asymmetry and proximal eval subsets contain ONLY deterministic labels (210/210 and 77/77 respectively). The high BA on these subsets is trivially achieved and does not indicate routing quality.

4. **Evaluation design flaw**: Only 1 out of 10 test episodes is internal-preferred (30 steps). This is too small a sample for reliable internal-class evaluation.

### Structural Issue

The fundamental problem: death_asymmetry provides a strong unidirectional signal (always deterministic), while score_comparison provides the only bidirectional signal. Death-proximal filtering is the wrong axis — it operates on the already-unidirectional subset instead of addressing the class imbalance in score_comparison data.

## Technical Notes

- Qwen3-0.6B generates `<think>...</think>` tags before the actual response. The initial eval script failed to strip these, producing all-0.5 BA. Fixed with `re.compile(r"<think>[\s\S]*?</think>\s*")`.
- `skip_special_tokens=True` in tokenizer.decode() does NOT remove `<think>` tags.

## Artifacts
- Checkpoints: `checkpoints/death-proximal/{full,k10,k5,k3,k1}/final_adapter/`
- Eval JSONs: `results/death-proximal/eval_{variant}.json`
- Per-step predictions: `results/death-proximal/predictions_{variant}.jsonl`
- Summary: `results/death-proximal/summary.json`
- Data: `data/death-proximal/`

## Implications for Next Steps

- Class-balanced sampling or loss weighting needed before death-proximal filtering can be evaluated
- May need more score_comparison episodes to provide sufficient internal-class training signal
- Alternative: focus on score_comparison-only training data (remove death_asymmetry entirely)
