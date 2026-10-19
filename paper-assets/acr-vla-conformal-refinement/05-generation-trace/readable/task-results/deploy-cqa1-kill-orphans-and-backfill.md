# deploy cqa1 kill orphans and backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-kill-orphans-and-backfill_20260523T175500_result.json`
- **Structured JSON:** [`ed536d4c9d38ba41c682.json`](../../sessions/ed/ed536d4c9d38ba41c682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果

| 项目 | 状态 |
|------|------|
| **Kill 孤儿进程** | PID 345585 (Long K2mean s44) 和 345660 (Long Reconvla s44) 已 kill -9 终止，tmux sessions 已清理 |
| **新实验 PID** | s45: PID 359721 (cuda:0, 2030 MiB) / s46: PID 359798 (cuda:3, 1223 MiB)，模型加载正常 |
| **3-suite checkpoint** | `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` 不存在于 cqa1-32758 |
| **Registry** | `eval-supp-k2mean-obj-s45` 和 `eval-supp-k2mean-obj-s46` 均已注册并转为 RUNNING |

cqa1-32758 当前 GPU 使用：0 (2030M), 1 (3714M), 2 (2131M), 3 (1223M), 4 (空闲), 5 (3347M)。

---
