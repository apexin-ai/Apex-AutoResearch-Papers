# analysis qwen14b uniform eval 4task

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_uniform_eval_4task_20260518T012306_result.json`
- **Structured JSON:** [`c1535bc7cabdfeb5a5ae.json`](../../sessions/c1/c1535bc7cabdfeb5a5ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常完成 (`EXIT_CODE=0`)，无错误。唯一的 warning 是 `fatal: not a git repository`，无影响。

## 14B Uniform Allocation 评测结果

| Metric | KL Predictor (uniform) | TEAL Vanilla (uniform) | Delta |
|---|---|---|---|
| WikiText-2 PPL ↓ | **7.63** | 8.01 | KL 好 0.38 |
| ARC-Challenge acc | 49.49% | **51.28%** | TEAL 好 1.8pp |
| ARC-Challenge acc_norm | 54.44% | **55.29%** | TEAL 好 0.9pp |
| WinoGrande acc | **72.45%** | 69.85% | KL 好 2.6pp |
| MMLU acc | 64.49% | **66.34%** | TEAL 好 1.9pp |

## 与之前 global_topk 结果对比

| Metric | KL global_topk | KL uniform | TEAL global_topk | TEAL uniform |
|---|---|---|---|---|
| MMLU | 63.72% | 64.49% (+0.8pp) | 71.83% | 66.34% (-5.5pp) |

## 关键发现

1. **KL uniform MMLU = 64.49%，未能恢复到 >70%。** 相比 global_topk 仅提升 0.8pp，假设不成立。
2. **TEAL uniform MMLU = 66.34%，比 global_topk 暴跌 5.5pp。** Uniform allocation 对 TEAL 反而有害。
3. **PPL 上 KL 依然优于 TEAL**（7.63 vs 8.01），但 MMLU/ARC 等下游任务 TEAL 更好。
4. **KL 与 TEAL 的 MMLU 差距在 uniform 下缩小到 1.9pp**（global_topk 下是 8.1pp），但这主要是因为 TEAL 也大幅下降了。

---
