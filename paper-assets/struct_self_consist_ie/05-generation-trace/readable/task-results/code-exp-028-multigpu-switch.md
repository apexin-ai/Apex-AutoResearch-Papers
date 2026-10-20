# code exp 028 multigpu switch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_028_multigpu_switch_20260517T122517_result.json`
- **Structured JSON:** [`a3ae55d733eb7c85c73f.json`](../../sessions/a3/a3ae55d733eb7c85c73f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，速度已稳定。

**汇总报告：**

| 项目 | 值 |
|---|---|
| 最新 checkpoint | step 7000 (已成功 resume) |
| 当前进度 | step 7100/41180 (17.2%) |
| Loss | 0.0516 (与 resume 前 ~0.054 一致，无异常) |
| GPU 使用 | 4× RTX 5090, 21-23 GB, 73-100% 利用率 |
| Effective batch size | 4×2×2 = 16（不变）|

**速度对比：**

| | 单卡 | 4 卡 |
|---|---|---|
| 速度 | ~0.51 steps/s | ~1.79 steps/s |
| 剩余时间 | ~18.6h | **~5.3h** |
| 预计完成 | — | ~凌晨 2:00 |

加速比约 3.5x，通信开销导致未达理论 4x，属正常水平。

**配置文件：** `train_config_fewnerd_5epoch_4gpu.yaml`（原配置未修改）
**日志：** `logs/exp_028_4gpu_train.log`
**tmux session：** `exp_028`

---
