# ssh 14b cls eval immediate

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-cls-eval-immediate_20260523T074031_result.json`
- **Structured JSON:** [`97fb60ec841da295340a.json`](../../sessions/97/97fb60ec841da295340a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## CLS 14B bf16 Eval 结果

| Seed | Best Checkpoint | Accuracy | F1 (pass) | F1 (fail) | Unparseable |
|------|----------------|----------|-----------|-----------|-------------|
| **s123** | checkpoint-956 | **90.79%** | 90.99% | 90.58% | 0 |
| **s456** | checkpoint-478 | **89.79%** | 90.11% | 89.45% | 0 |

对比 s42-v2 NF4 eval (89.47%)：
- s123 bf16: +1.32pp
- s456 bf16: +0.32pp
- 3-seed 平均 (s42 bf16 待跑): s123/s456 平均 **90.29%**

## Prediction JSONL 路径
- `/root/autodl-tmp/eval_results/cls14b_func_s123/eval_results_predictions.json` (212KB, 1890 samples)
- `/root/autodl-tmp/eval_results/cls14b_func_s456/eval_results_predictions.json` (212KB, 1890 samples)

## CWM 14B 训练进度
两个 seed 都已完成训练（checkpoint-1434 + best/）：
- `cwm14b-func-s123`: best 在某个中间 step（有 best/ 目录）
- `cwm14b-func-s456`: 同上

CWM 14B eval 可以随时启动。

---
