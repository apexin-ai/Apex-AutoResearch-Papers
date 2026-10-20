# code dino probe rerun

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dino-probe-rerun_20260515T132727_result.json`
- **Structured JSON:** [`fa64edf81d6fafb2dd46.json`](../../sessions/fa/fa64edf81d6fafb2dd46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果对比

| 指标 | 旧版 | 新版 | Δ |
|------|------|------|---|
| pooled_rho | 0.8331 | 0.9001 | **+0.0670** |
| per_task_mean_rho | (缺失) | 0.9008 | — |
| R² | 0.6865 | 0.8030 | +0.1165 |
| MAE | 0.1272 | 0.0990 | -0.0282 |
| epochs_trained | 9 | 15 | +6 |

**异常标记**：pooled ρ 差异 0.067 >> 0.01 阈值。新版代码训练了 15 个 epoch（旧版 9），所有指标显著提升。这不是随机波动，而是新版 `train_probes.py` 的训练逻辑（数据对采样、早停策略、或学习率等）发生了变化导致的系统性提升。

新结果已包含 `per_task_rho`（10 个 task，范围 0.840–0.927）和 `per_task_mean_rho = 0.9008`。旧结果备份在 `temporal_distance_old_backup/`。

需要确认：是否接受新版结果作为 DINO baseline（ρ 从 0.833 → 0.900），还是需要排查代码变更原因？

---
