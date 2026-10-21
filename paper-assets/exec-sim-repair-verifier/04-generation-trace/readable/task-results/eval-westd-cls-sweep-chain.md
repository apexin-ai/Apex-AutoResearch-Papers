# eval westd cls sweep chain

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd-cls-sweep-chain_20260514T030256_result.json`
- **Structured JSON:** [`97c3619157e514612633.json`](../../sessions/97/97c3619157e514612633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总

### 任务 A: CLS v5-conda eval 结果

| 指标 | ckpt-400 | ckpt-600 |
|------|----------|----------|
| **accuracy** | **78.43%** | 76.37% |
| **f1_macro** | 68.41% | **71.17%** |
| **f1_fail** | 50.61% | **58.93%** |
| **f1_pass** | **86.21%** | 83.41% |
| precision_fail | 66.48% | 55.60% |
| recall_fail | 40.85% | **62.70%** |
| precision_pass | 80.82% | 85.49% |
| recall_pass | **92.36%** | 81.44% |
| unparseable | 132 (1.35%) | 132 (1.35%) |

ckpt-400 偏向 pass（高 recall_pass=92.4%，低 recall_fail=40.9%），accuracy 高但 f1_macro 低。ckpt-600 更均衡，f1_macro 高 2.8pp，fail 识别能力明显更强（recall_fail +22pp）。

### 任务 B: CLS 8B-conda eval 已启动

- `eval_8b_ckpt400` → GPU 2，batch_size=8，已开始推理（80/9784）
- `eval_8b_ckpt600` → GPU 3，batch_size=8，已开始推理
- base model: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- VRAM: ~21GB/GPU

### 任务 C: 8B checkpoint 列表

可用: checkpoint-200, checkpoint-400, checkpoint-600。**无 checkpoint-800**。

---
