# diag k8 s456 eval check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_k8_s456_eval_check_20260523T112548_result.json`
- **Structured JSON:** [`4618ece83315e1370d0a.json`](../../sessions/46/4618ece83315e1370d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程状态：正常运行，无需重新提交。**

| 项目 | 状态 |
|------|------|
| PID 137205 | 存活，运行 2m26s |
| Python PID 137210 | 115% CPU，2.3GB RAM，正在跑 eval |
| tmux session | `perlayer_kl_k8_s456_eval` 活跃 |
| cuda:0 | 100% util, 66099/97887 MiB（跑 k2_s123 + k8_s123） |
| cuda:1 | 100% util, 48203/97887 MiB（跑 k8_s456） |

**进度**：WikiText-2 已完成（PPL=8.9515），arc_challenge 已完成，当前在跑 MMLU（~34%, 1589/4687 loglikelihood requests）。后续还有 gsm8k、hellaswag、piqa。

Director 报告 cuda:1 空闲是误判——两张卡都在满载运行。

---
