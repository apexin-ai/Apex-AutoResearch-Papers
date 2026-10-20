# eval contamination 60 uniform seed42 ood

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_contamination_60_uniform_seed42_ood_20260520T161543_result.json`
- **Structured JSON:** [`ecacc4020c42b2743e05.json`](../../sessions/ec/ecacc4020c42b2743e05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 确认 `contamination_60_uniform_seed42` 在 **westd-47453**（已释放）上训练，checkpoint 不在当前服务器上。

**结果：**
- **Checkpoint 不存在**。`contamination_60_uniform_seed42` 在旧服务器 westd-47453 上训练完成，该服务器已释放，checkpoint 丢失。
- 当前服务器只有 `contamination_60_uniform_seed456`（另一个 seed 的 uniform baseline）。
- Registry 记录的 metrics 只有 holdout PPL=17.766，无 OOD eval（openwebtext/wikipedia）。

**替代方案**（如果需要 ρ=0.6 uniform 的 OOD 数据）：
1. 用当前服务器上的 `contamination_60_uniform_seed456` checkpoint 跑 OOD eval（seed 不同但同为 uniform baseline）
2. 重训 seed42（约 3.6 小时 GPU 时间）

需要我用 seed456 跑 OOD eval 吗？

---
