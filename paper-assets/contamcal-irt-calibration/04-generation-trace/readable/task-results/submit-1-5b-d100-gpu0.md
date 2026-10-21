# submit 1 5B d100 gpu0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_1_5B_d100_gpu0_20260514T005157_result.json`
- **Structured JSON:** [`23dd0ae8ff69c29a255f.json`](../../sessions/23/23dd0ae8ff69c29a255f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两步都完成：

**步骤 1 — exp_001_sft_d100_05B 分析完毕**
| 指标 | 值 |
|---|---|
| train_loss | 1.5662 |
| mean_token_accuracy | 0.6661 |
| training_time | 68.9 min (1.19 GPU-hr) |
| steps | 4159 |
| epoch | 1.0 |
| status | **DONE** (conclusion=success) |

**步骤 2 — exp_001_sft_d100_15B 已在 GPU 0 启动**
- PID: 248993，正在 tokenize 数据集
- 参数: Qwen2.5-1.5B, batch_size=1, grad_accum=16, 66533 samples, seed=42
- Registry: RUNNING

---
