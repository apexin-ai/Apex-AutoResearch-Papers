# eval westd41312 cuda3 prep and downstream

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd41312_cuda3_prep_and_downstream_20260520T051914_result.json`
- **Structured JSON:** [`8466ccd660c5ccb47153.json`](../../sessions/84/8466ccd660c5ccb47153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Task A — downstream eval 结果：**

| Experiment | arc_easy | arc_challenge | hellaswag | piqa | winogrande | mean |
|---|---|---|---|---|---|---|
| adaptive_fix_seed42 | 0.6157 | 0.3430 | 0.4785 | 0.6866 | 0.5777 | **0.5403** |

已更新到 registry。

**注意：** adaptive_fix_seed123 和 adaptive_fix_seed456 的 checkpoint **不在 westd-41312 上**，无法在此服务器 eval。seed123 没有记录 server，seed456 在 westd-47453 上训练。

**Task B — 3 个 rho06 eval 脚本已写到服务器：**
- `/root/provenance_weight_training/scripts/eval_rho06_ppl.sh` — holdout PPL eval
- `/root/provenance_weight_training/scripts/eval_rho06_downstream.sh` — lm_eval downstream
- `/root/provenance_weight_training/scripts/eval_rho06_ood.sh` — OOD eval (openwebtext + wikipedia)

用法：`bash scripts/eval_rho06_ppl.sh 3` (GPU ID 作为第一个参数)。每个脚本会串行跑 3 个 seed，跳过未就绪的 checkpoint。

---
