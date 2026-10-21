# submit sft 3B d025 s42 a32 cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_sft_3B_d025_s42_a32_cuda2_20260515T183749_result.json`
- **Structured JSON:** [`a7d6f94619472d08fd28.json`](../../sessions/a7/a7d6f94619472d08fd28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**提交摘要：**

| 项目 | 值 |
|------|-----|
| exp_id | `exp_001_sft_3B_d025_s42_a32` |
| GPU | cuda:2, PID 612951, 12694 MiB |
| tmux | `exp_001_sft_3B_d025_s42_a32` |
| 模型 | Qwen2.5-3B |
| 数据 | `sft_dosage_025.jsonl` (54133 samples) |
| 关键参数 | `--lora-alpha 32`, `--seed 42`, `--lr 5e-5`, `--batch-size 1`, `--grad-accum 16` |
| 输出 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42/` |
| 进度 | 3384 steps, ~4.2s/it, 预计 ~4 小时 |
| Registry | RUNNING |

备注：GPU 5 上还有一个 `exp001_d025_3B_v3`（PID 589763）在跑相同参数但输出到 `Qwen2.5-3B_d025_v3_s42`，两者互不干扰。

---
