# ops d024 exp002v2 recalib restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d024-exp002v2-recalib-restart_20260519T063655_result.json`
- **Structured JSON:** [`fb0e86a3cdf24c1dcd3f.json`](../../sessions/fb/fb0e86a3cdf24c1dcd3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Per-strength 数据出来了！train step 510（reward step 10）：

- **r1_medium_mean = -0.0556** (n=10)
- **r1_strong_mean = -0.0474** (n=6)
- weak 这批没出现（n=0 该 batch 中）

R1 非零且有分化。确认完成。

---

## D024 完成报告

| 项目 | 结果 |
|------|------|
| **Kill 确认** | PID 130467 已终止 (SIGTERM, force_killed=false) |
| **新 d_syc (checkpoint-500 recalibration)** | 保存至 `results/exp002v2/directions_recalib_step500.pt` |
| **Per-layer cosine/AUROC** | Layer 19: cos=0.975, AUROC=0.805 / Layer 20: cos=0.977, AUROC=0.804 / Layer 24: cos=0.976, AUROC=0.777 / Layer 27: cos=0.979, AUROC=0.801 / Layer 32: cos=0.966, AUROC=0.811 / Layer 33: cos=0.963, AUROC=0.809 / Layer 35: cos=0.863, AUROC=0.797 / **Mean cosine=0.957** |
| **新 PID** | 172838 (tmux session: `exp002v2-recalib`) |
| **Step 510 R1 (per-strength)** | medium=-0.056 (n=10), strong=-0.047 (n=6). R1 非零，有方差，有 strength 分化 |
| **配置变更** | `direction_path` → recalib_step500.pt, `recalibration_interval=500`, `calibration_data_path=DATA_PATH`, resume_from_checkpoint=checkpoint-500 |
| **问题** | 无。d_syc 在 checkpoint-500 处漂移很小 (mean cosine=0.957)，Layer 35 偏移最大 (0.863)。recalibration 每 500 步自动触发保障后续稳定性 |

---
