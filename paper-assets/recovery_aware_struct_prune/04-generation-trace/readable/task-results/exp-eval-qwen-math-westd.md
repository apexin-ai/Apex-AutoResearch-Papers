# exp eval qwen math westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_eval_qwen_math_westd_20260516T101039_result.json`
- **Structured JSON:** [`84d47bb67f04c7672b70.json`](../../sessions/84/84d47bb67f04c7672b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 已成功启动并进入推理阶段：

| 实验 | tmux session | PID | GPU | 显存占用 |
|------|-------------|-----|-----|---------|
| eval_sft_rasp_qwen_math | `eval_sft_rasp_qwen_math` | 102641 | cuda:0 | 12509 MiB |
| eval_sft_standard_qwen_math | `eval_sft_standard_qwen_math` | 102643 | cuda:1 | 12467 MiB |

两个进程都已加载模型到 GPU，正在 Loading GSM8K test set（可能需要下载数据集）。1319 样本 eval 预计 20-40 分钟完成。

结果输出：
- `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math_n1319.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math_n1319.json`

---
