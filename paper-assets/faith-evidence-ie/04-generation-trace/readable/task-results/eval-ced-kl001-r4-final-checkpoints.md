# eval ced kl001 r4 final checkpoints

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ced-kl001-r4-final-checkpoints_20260514T181012_result.json`
- **Structured JSON:** [`c325cb9d7a4ff6ed2815.json`](../../sessions/c3/c325cb9d7a4ff6ed2815.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 不空闲，无法启动新任务。** 当前 4 张 GPU 全部被占用：

| GPU | PID | 显存 | 任务 |
|-----|-----|------|------|
| cuda:0 | 80799 | 8482 MiB | eval checkpoint-100 (`grpo_ced_kl001`) |
| cuda:1 | 75587 | 10430 MiB | eval checkpoint-50 (`grpo_ced_kl001`) |
| cuda:2 | 78857 | 9400 MiB | eval checkpoint-10 (`grpo_ced_kl001`) |
| cuda:3 | 76958 | 13638 MiB | GRPO 训练 (`grpo_flatnli_r6`) |

checkpoint-90 和 checkpoint-100 的情况：
- **checkpoint-100**：已在 cuda:0 上评估中
- **checkpoint-90**：目前没有任何 GPU 在评估

已有评估结果目录：`checkpoint-10`, `checkpoint-50`, `summary.json`（在 `eval_results/grpo_ced_kl001/`）

等某张 GPU 空闲后可立即提交 checkpoint-90 的评估。是否需要我监控 GPU 状态，一旦空闲就提交？

---
