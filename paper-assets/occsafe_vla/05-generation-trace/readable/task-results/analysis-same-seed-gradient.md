# analysis same seed gradient

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_same_seed_gradient_20260525T031735_result.json`
- **Structured JSON:** [`1320fb3f1bdb2e4874c5.json`](../../sessions/13/1320fb3f1bdb2e4874c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并在运行中：

- **实验 ID**: `gradient_analysis_same_seed`
- **服务器**: westd-10894, PID=9218
- **GPU**: cuda:0
- **4 个条件** (均 seed=42, 50K checkpoint, 200 batches):
  1. Vanilla — `vanilla_retrain_s0`
  2. Full OCC + BN — `full_occ_retrain_s0`
  3. Detach + BN — `ablation_occ_detach_s0_retrain`
  4. Full OCC + LN — `full_occ_ln_s0`
- **产出路径**:
  - `/root/autodl-tmp/analysis/gradient_same_seed/gradient_results.json`
  - `/root/autodl-tmp/analysis/gradient_same_seed/gradient_analysis.pdf`
- **Cron 监控**: 每 10 分钟检查进度

第一个条件 (Vanilla) 已在处理中，模型加载完毕，正在跑 gradient analysis。预计 4 个条件总计 2-4 小时完成。

---
