# diagnosis exp009 eval result

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp009-eval-result_20260520T083120_result.json`
- **Structured JSON:** [`83bc30bac751d5e67b16.json`](../../sessions/83/83bc30bac751d5e67b16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态：进行中

| 项目 | 状态 |
|------|------|
| PID 227017 | 运行中，已运行 1h13m |
| 进度 | **200/362** pairs (~55%) |
| 速率 | 180 pairs / 63 min ≈ 2.86 pairs/min |
| 剩余 | 162 pairs ≈ **57 分钟** |
| 预计完成 | ~17:25 CST |

结果目录 `/root/contrastive_entrain_calib/results/exp009_ckpt500_eval/` 目前为空，eval 脚本在全部 362 pairs 处理完后才写结果文件。

## GPU 状态

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | 0% | 5/32607 MiB | **空闲** |
| 1 | 100% | 31432/32607 MiB | exp-009 训练 |
| 2 | 100% | 30668/32607 MiB | exp-009 训练 |
| 3 | 49% | 16766/32607 MiB | eval 运行中 |

## 决策

**无法判断是否 kill**——ToF/NoF 尚无数据。需等 eval 完成（约 57 分钟后）再读取结果做判断。

---
