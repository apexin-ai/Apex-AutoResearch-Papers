# verify grasp eval json

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_grasp-eval-json_20260515T163844_result.json`
- **Structured JSON:** [`d115bb8ba45bfc43c75b.json`](../../sessions/d1/d115bb8ba45bfc43c75b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. JSON 文件完整性

| 文件 | 路径 | 大小 | accuracy | n_total | 完整 |
|------|------|------|----------|---------|------|
| **GraSP post-SFT** | `results/eval_sft_grasp_20_n100.json` | 76KB, 919行 | **0.41** (41/100) | 100 | ✓ JSON 头尾闭合，含 per-example results |
| **GraSP pre-SFT** | `results/eval_pruned_graspune_20_greedy.json` | 98KB, 919行 | **0.07** (7/100) | 100 | ✓ JSON 头尾闭合，含 per-example results |

两个 JSON 均有 `accuracy`, `stderr`, `model_path`, per-example results，结构完整。

### 2. Eval 链状态

**无活跃 eval 进程。** `ps aux` 无 eval/python 训练进程，无 tmux session。所有 eval 任务已完成。

当前 `results/` 目录下已完成的 eval：
- `eval_sft_alpha_0.0_n100.json` — α=0.0 post-SFT
- `eval_sft_alpha_1.0_n100.json` — α=1.0 post-SFT
- `eval_sft_alpha_2.0_n100.json` — α=2.0 post-SFT
- `eval_alpha_4.0_greedy.json` — α=4.0
- `eval_sft_grasp_20_n100.json` — GraSP post-SFT (**0.41**)
- `eval_pruned_graspune_20_greedy.json` — GraSP pre-SFT (**0.07**)
- `reeval_pruned_rasp_20_definitive_n100.json` — RASP re-eval

`eval_sft_alpha_0.5_n100.log` 存在（1.3KB）但无对应 JSON，可能未完成或被中断。

---
