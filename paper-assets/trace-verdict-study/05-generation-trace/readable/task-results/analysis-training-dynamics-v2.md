# analysis training dynamics v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training_dynamics_v2_20260522T063924_result.json`
- **Structured JSON:** [`0aa8a3b7ba606ec3e1f6.json`](../../sessions/0a/0aa8a3b7ba606ec3e1f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 报告

**1. 数据来源**: `dynamics_log.jsonl`（checkpoint eval accuracy + train_loss），训练日志（44个细粒度loss数据点，每~10步一个）

**2. 生成文件**:
| 文件 | 大小 |
|------|------|
| `training_dynamics_full.pdf` | 35 KB |
| `training_dynamics_full.png` | 265 KB |
| `oscillation_metrics.json` | 1.2 KB |

路径: `/root/autodl-tmp/trace-verdict-study-checkpoints/training_dynamics/`

**3. Oscillation Metrics 关键数值**:

| 指标 | Exception-Only | Full-Trace |
|------|---------------|------------|
| Accuracy CV (全程) | 0.0024 | 0.0234 |
| Accuracy CV (最后100步) | 0.0000 | 0.0031 |
| 最后3个checkpoint std | 0.0000 | 0.0028 |
| Max drop | 0.0 pp | **−5.29 pp** (step 50→100) |
| Recovery steps | N/A | 100步 (step 200恢复) |
| Best accuracy | 99.83% @ step 200 | 88.82% @ step 350 |
| Final loss | 0.0329 | 0.0085 |

**4. 主要观察**:
- Exception-Only 在 step 200 达到 99.83% 后完全饱和，zero oscillation
- Full-Trace 在 step 50→100 出现最大跌落（87.39%→82.10%，−5.29pp），200步后恢复，但全程 CV 是 exception-only 的 ~10x
- Full-Trace 最终 loss (0.0085) 远低于 Exception-Only (0.0329)，但 accuracy 低 11.6pp — 典型的 "lower loss ≠ better generalization" 现象

---
