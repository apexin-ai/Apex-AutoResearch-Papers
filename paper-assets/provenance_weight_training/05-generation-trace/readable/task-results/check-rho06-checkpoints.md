# check rho06 checkpoints

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_rho06_checkpoints_20260524T044059_result.json`
- **Structured JSON:** [`9b2ce7e094668ddc7552.json`](../../sessions/9b/9b2ce7e094668ddc7552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ρ=0.6 三个 seed 的 uniform checkpoint 状态

| Checkpoint | 状态 | 路径 | model.safetensors 大小 |
|---|---|---|---|
| contamination_60_uniform_seed42 | **不存在** | — | — |
| contamination_60_uniform_seed123 | **不存在** | — | — |
| contamination_60_uniform_seed456 | **存在，完整** | `/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_uniform_seed456/final/` | 1.2G |

seed456 的 checkpoint 完整，包含 model.safetensors、tokenizer、config 等全部文件。seed42 和 seed123 的 uniform 版本不存在。

补充：`contamination_60_*` 下还有以下非 uniform 的 checkpoint：
- `contamination_60_adaptive_seed456`
- `contamination_60_adaptive_seed42_tau08`
- `contamination_60_adaptive_seed123_tau08`
- `contamination_60_ess_only_seed123`
- `contamination_60_ess_only_seed456`
- `contamination_60_random_seed123`
- `contamination_60_random_seed456`

---
