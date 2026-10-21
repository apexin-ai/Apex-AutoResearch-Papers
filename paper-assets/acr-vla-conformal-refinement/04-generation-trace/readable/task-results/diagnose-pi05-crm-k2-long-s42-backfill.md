# diagnose pi05 crm k2 long s42 backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-crm-k2-long-s42-backfill_20260528T112923_result.json`
- **Structured JSON:** [`be6e45ae34ae6153a54c.json`](../../sessions/be/be6e45ae34ae6153a54c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：两个实验提交命令缺少 `--obs_dim 2048 --unified_obs_dim 2088`，导致 CRM 模型构造时 input_dim=990，与 checkpoint 的 input_dim=2118 不匹配（`RuntimeError: size mismatch`）。

**证据**：同一 checkpoint 在 spatial benchmark 上的成功实验（如 `pi05-crm-k2-spatial-s42-bjb2-r2`）均传了 `--obs_dim 2048 --unified_obs_dim 2088`。

**修复**：在命令中补上这两个参数后重新提交即可，不需要修代码。

---
