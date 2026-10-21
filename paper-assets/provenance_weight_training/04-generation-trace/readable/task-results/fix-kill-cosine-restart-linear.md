# fix kill cosine restart linear

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_cosine_restart_linear_20260521T121101_result.json`
- **Structured JSON:** [`922f6232c3a3f225b27c.json`](../../sessions/92/922f6232c3a3f225b27c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本默认 `warmup_ratio=0.05`，`lr_scheduler_type="linear"`。一切确认。

---

**汇总：**

| 项目 | 结果 |
|------|------|
| **cuda:1 (D&R)** lr_scheduler_type | `linear`（命令行无 `--lr_scheduler_type`，脚本默认 `linear`）✓ |
| **cuda:2 cosine 实验** | 已 kill（tmux session `uniform_epoch_matched_indep_lr_seed42`）✓ |
| **错误输出** | 已删除 ✓ |
| **新实验 PID** | 606291，cuda:2，无 `--lr_scheduler_type` 参数，使用默认 `linear` ✓ |
| **当前进度** | step 465/2533，运行正常 |
| **Registry** | status=RUNNING，hypothesis 已更新 |

脚本源码确认：`--lr_scheduler_type` 默认值为 `"linear"`（`pretrain_weighted.py:328`），`warmup_ratio=0.05`。

---
