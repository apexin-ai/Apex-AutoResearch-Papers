# ops deploy seed45 pair

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-seed45-pair_20260516T074348_result.json`
- **Structured JSON:** [`6b7676c01184a7449950.json`](../../sessions/6b/6b7676c01184a7449950.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 确认
- bjb1-32546:cuda:3 — 空闲 ✓ (0%, 2 MiB)
- bjb2-28827:cuda:5 — 空闲 ✓ (0%, 1 MiB)

## 部署
- **eval-obs-only-object-norm02-seed45**: PID=233544, running (GPU 23%, 5665 MiB)
- **eval-argmin-object-seed45**: PID=215932, running (加载环境中)

## 问题
- 指令中 `--mode argmin` 不存在，实际对应 `--mode reconvla`（ReconVLA baseline — scalar Euclidean argmin selection）。已用 reconvla 重新部署，输出文件名保持 `eval_object_argmin_seed45.json` 不变。

---
