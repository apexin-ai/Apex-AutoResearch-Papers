# ops prepare eval scripts gemma2 qwen14b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-eval-scripts-gemma2-qwen14b_20260521T001753_result.json`
- **Structured JSON:** [`9d3b652c4ead5157b4da.json`](../../sessions/9d/9d3b652c4ead5157b4da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本已创建并赋权。

### 产出

| 脚本 | 路径 | 关键参数 |
|------|------|---------|
| Gemma-2 d100 MMLU | `scripts/seed0/eval_gemma2_d100_s0_mmlu.sh` | `CUDA=0`, model=gemma-2-9b, benchmark=mmlu, batch=8 |
| Gemma-2 d100 ARC | `scripts/seed0/eval_gemma2_d100_s0_arc.sh` | `CUDA=0`, model=gemma-2-9b, benchmark=arc_challenge, batch=8 |
| Qwen-14B 全dosage | `scripts/seed0/eval_qwen14b_s0_batch.sh` | `CUDA=1`, model=Qwen2.5-14B, benchmark=mmlu+arc_challenge, batch=4, dosage=000/005/025/050/100 |

所有脚本包含：C009 md5 校验、C004 显式 CUDA_VISIBLE_DEVICES、C006 lora_alpha=32 检查、adapter 存在性检查。参数格式与现有 `scripts/eval_gemma2_s0_mmlu.sh` / `eval_qwen14b_s0_mmlu.sh` 完全一致。

启动时需根据实际 GPU 空闲情况调整 `CUDA_VISIBLE_DEVICES`（Gemma-2 训练完后 cuda:0 释放可直接用；Qwen-14B 需等 cuda:1 或 cuda:3 释放）。

---
