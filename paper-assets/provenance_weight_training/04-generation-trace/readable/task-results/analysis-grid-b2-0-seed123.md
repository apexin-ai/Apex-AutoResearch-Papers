# analysis grid b2 0 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b2_0_seed123_20260514T141614_result.json`
- **Structured JSON:** [`a6b84076b1fa494e50ab.json`](../../sessions/a6/a6b84076b1fa494e50ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

**grid_b2_0_seed123 实验结果**

| 指标 | 值 |
|---|---|
| train_loss | 10.6104 |
| total_steps | 6103 |
| train_runtime_s | 13,058.8 (~3.6h) |
| gpu_hours | 3.63 |
| checkpoint | `output/models/grid_b2_0_seed123/final/` (1.1GB model.safetensors, 完整) |

**eval_ppl_holdout / eval_loss / eval_holdout_tokens 均缺失** — trainer 配置了 `eval_steps=500` 但 `should_evaluate=false`，训练全程未执行 evaluation。需要单独跑 eval 才能获取这些指标。

**adaptive_fix_seed42 (PID 107404)**: 进程已不存在（ps 返回空），已结束。

---
