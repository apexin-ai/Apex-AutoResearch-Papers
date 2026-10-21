# check eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-progress_20260514T181627_result.json`
- **Structured JSON:** [`a4ef6f2fdf8d985d73a8.json`](../../sessions/a4/a4ef6f2fdf8d985d73a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写到 `artifacts/report_eval_progress.md`。关键发现：

**5 个 Eval 全部存活，无挂死。**

| 实验 | 进度 | 成功率 | 预计剩余 |
|------|------|--------|---------|
| eval-vla-mean-spatial (bjb2) | 7.5/10 | 40% (28/70) | ~5h |
| eval-acr-spatial-v3 (bjb1) | 4/10 | **2.5%** (1/40) | ~9h |
| eval-acr-object-v3 (bjb1) | 4/10 | **0.0%** (0/40) | ~9h |
| eval-argmin-only-spatial (bjb1) | 0/10 | 刚开始 | ~14h |
| eval-tiny-correction-spatial (bjb1) | 0.5/10 | task1: 4/5 (80%) | ~9h |

**最严重的问题：acr-spatial-v3 和 acr-object-v3 用 crm_v2/perdof 做 correction，成功率反而比 vla_only baseline 暴跌**（2.5% / 0% vs 40%）。CRM 修正在伤害性能。

**积极信号：tiny-correction (max_correction_norm=0.05) 初步 80% 成功率**，说明限制修正幅度是对的。

**CRM v3 训练**：三个变体都在 epoch 29/50，val_loss 持续下降，约 8 分钟内完成。

---
