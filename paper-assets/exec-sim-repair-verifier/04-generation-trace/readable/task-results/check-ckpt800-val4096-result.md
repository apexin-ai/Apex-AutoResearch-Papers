# check ckpt800 val4096 result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ckpt800-val4096-result_20260514T154408_result.json`
- **Structured JSON:** [`280ee54ca2f5f6e9fd56.json`](../../sessions/28/280ee54ca2f5f6e9fd56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inference running smoothly — 22.5GB/32.6GB VRAM, no OOM risk. Here's the full report:

---

## ckpt-800 val@4096 最终结果

**结果不匹配**：PID 3125543 跑的实际是 **test@2048**（非 val@4096）。

实际跑出的 `repo_cls_seed123_ckpt800` 结果（test split, seq_len=2048, Qwen3-4B）：
- accuracy: 74.27%（仅比 majority baseline 72.96% 高 1.3pp）
- f1_macro: 66.03
- fail_f1: 49.31 / pass_f1: 82.76
- precision_fail: 52.8% / recall_fail: 46.3%
- unparseable: 132/9784 (1.35%)
- vs ckpt-600 test@2048 (80.73%): **-6.46pp，严重退化**

ckpt-800 比 ckpt-600 差很多，fail 检测能力几乎崩溃（fail_f1 从 68.49 降到 49.31）。但**这不是 val@4096 的结果**——val@4096 eval 从未实际执行。

## 8B s42 val@5120 sweep 状态

- 模型路径: `/home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B`（本地，16GB）
- tmux session: `eval_8b_val5120` on home cuda:0
- VRAM: 22.5GB/32.6GB，batch_size=4，无 OOM 风险
- **ckpt-400 (conda)**: 已启动，正在推理中（checkpoint: `checkpoints_repo_cls_8b_conda_westd/checkpoint-400`）
- **ckpt-3000 (主版本)**: 排队中，ckpt-400 完成后自动开始（checkpoint: `checkpoints_repo_cls_8b_westd/checkpoint-3000`）
- 输出目录: `results/repo_cls_8b_conda_ckpt400_val5120/` 和 `results/repo_cls_8b_ckpt3000_val5120/`

---
