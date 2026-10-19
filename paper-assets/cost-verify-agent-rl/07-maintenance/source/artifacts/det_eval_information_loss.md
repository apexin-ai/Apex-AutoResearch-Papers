# Deterministic Eval: Information Loss from h=2 Windowing

**Date**: 2026-05-19
**Checkpoint**: qwen3_8b_sft_v1/checkpoint-231
**Eval Config**: temperature=0, do_sample=False (greedy decoding), 32 in-dist ALFWorld tasks, seed=123

## Results

| Metric | Full-context (T=0) | h=2 windowing (T=0) | Delta |
|--------|-------------------|---------------------|-------|
| **success** | **68.75% (22/32)** | **31.25% (10/32)** | **-37.50pp** |
| num_actions | 24.22 | 37.59 | +13.37 |
| action_is_valid | 92.60% | 91.88% | -0.72pp |
| pass@1 | 68.75% | 31.25% | -37.50pp |

**Information Loss = 37.50pp (absolute), 54.5% (relative)**

## Config Details

- Full-context: `_alfworld_8b_det_eval_full.yaml`, context_window_mode="full"
- h=2 windowing: `_alfworld_8b_det_eval_h2.yaml`, context_window_mode="step_independent", step_independent_history_length=2

## WandB Runs

- Full-context: `mb005ir1` (8b-det-eval-full)
- h=2 windowing: `qtxhh5ak` (8b-det-eval-h2)

## Analysis

1. h=2 windowing causes a 37.5pp drop in success rate, from 68.75% to 31.25%
2. h=2 agents use significantly more actions (37.6 vs 24.2), hitting the 50-step limit on failed tasks
3. Action validity is nearly identical (~92%), confirming the model generates valid ALFWorld commands
4. The performance gap is entirely due to information loss: without full conversation history, the agent cannot track task progression and revisits previously explored locations
5. These are deterministic results (T=0, greedy decoding) with zero sampling variance
