# analysis vota seed123 harvest

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vota_seed123_harvest_20260519T083640_result.json`
- **Structured JSON:** [`b481c6497cb7f4918f92.json`](../../sessions/b4/b481c6497cb7f4918f92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已被之前的 hook 自动清除。

## 结果汇总

**qwen7b_vota_seed123：成功**

| 指标 | 值 |
|---|---|
| Accuracy | **98.66%** (95% CI: [97.9%, 99.2%]) |
| Majority baseline | 71.5% |
| Lift | +27.1pp |
| pass | P=1.00, R=0.98, F1=0.99 |
| fail | P=0.95, R=1.00, F1=0.98 |
| train_loss | 0.0499 |
| 训练时长 | ~2h16m, 444 steps / 3 epochs |

**注意**：98.7% 远超预期的 84-92% 范围。假设预期基于 vota_seed42_v4 的结果，seed123 的表现异常高，可能需要核实 VOTA 条件 seed42 的原始结果是否存在差异来源（数据划分、训练配置等）。

**GPU 状态**：cuda:0 空闲（无进程），cuda:1 被其他任务占用（100% util）。

---
