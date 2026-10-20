# eval westd41312 cuda3 continue

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd41312_cuda3_continue_20260520T071215_result.json`
- **Structured JSON:** [`7d898ca2fc10e98a8605.json`](../../sessions/7d/7d898ca2fc10e98a8605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 registry 全部更新成功。汇总：

## 状态

- **cuda:3**: 空闲，PID 427903 已死，无 GPU 进程
- **cuda:0/1/2**: rho06 训练中（各占 ~45.6GB）

## OOD eval 结果（全部已完成，已录入 registry）

| Experiment | Holdout PPL | OWText PPL | Wiki PPL |
|---|---|---|---|
| detect_remove_q03_seed42_r2 | 17.25 | 18.004 | 15.037 |
| detect_remove_q04_seed42 | 17.26 | 18.001 | 15.038 |
| detect_remove_q08_seed42 | 17.34 | 18.039 | 15.066 |
| qwen06b_uniform_seed42 | 17.69 | 18.365 | 15.335 |
| adaptive_fix_seed42 | 17.65 | 18.424 | 15.473 |

q08 的 downstream 也已补录：arc_easy=0.6086, arc_challenge=0.3592, hellaswag=0.4855, piqa=0.6937, winogrande=0.5817。

**之前 Worker context 耗尽时，实际上所有 eval 已经跑完产出了结果文件**，只是没来得及写入 registry。现在全部补齐，无需重跑任何 eval。cuda:3 处于空闲可用状态。

---
