# data fig6 wandb fetch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fig6_wandb_fetch_20260518T204516_result.json`
- **Structured JSON:** [`b5d60c99fd8ef6794dfe.json`](../../sessions/b5/b5d60c99fd8ef6794dfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Saved to `artifacts/fig6_wandb_data.json` (64KB).

Summary:

| Run ID | Name | Steps | Key Findings |
|---|---|---|---|
| `7o9bjszm` | hsweep-h2-seed1 | 15 | train/success collapses to 0, manager_invalid_action spikes to ~0.99 |
| `6liw7fm1` | factorial-h2-episode-adv | 15 | train/success stays ~0.05-0.20, action_is_valid stable ~0.84 |
| `6d4oml60` | exp029-episode-level | 1 | Only 1 val-only row (crashed early), val/success=0.125 |
| `jhwyg4tc` | hsweep-h2-seed2 | 15 | train/success variable 0-0.27, action_is_valid rises to ~0.99 |

Standardized metric keys used: `train/success`, `train/action_is_valid`, `train/manager_invalid_action`, `val/success`, `val/action_is_valid`, etc. Original W&B column names (e.g., `train/AlfworldSG/success`) are stored in `metric_name_mapping`. Full `available_metrics` list included per run.

Note: `6d4oml60` crashed before any training steps were logged (only 1 eval row exists).

---
