# ops fix 008e duplicate and orphan

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_008e_duplicate_and_orphan_20260514T042205_result.json`
- **Structured JSON:** [`19edc56ab77b2a0feb7c.json`](../../sessions/19/19edc56ab77b2a0feb7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个目标 PID (121636, 122038, 107026) 都已不存在，logdir `exp_008e_subsample_on_fixed_dt1_h15` 也是空目录。这些进程已经自行退出了。

但发现了**新的重复进程问题**：PID 123422 和 123820 都在跑完全相同的 `008f_dryrun` 实验，共享 logdir `logdir/008f_dryrun`，同样会互相干扰 metrics。

当前 GPU 占用：
| GPU | PID | 实验 | 显存 |
|-----|-----|------|------|
| 0 | 106947 | exp_008a (正常) | 4158 MiB |
| 0 | 109524 | exp_008d (正常) | 2742 MiB |
| 0+1 | 123422 | 008f_dryrun (**重复**) | 552+794 MiB |
| 0+1 | 123820 | 008f_dryrun (**重复**) | 552+794 MiB |

008f_dryrun 的两个进程：
- PID 123422 — 由直接 `bash -c` 启动（父 PID 123417）
- PID 123820 — 由 `nohup` 启动（父 PID 123815）

需要 kill 其中一个。建议 kill PID 123820（nohup 启动的那个），保留 123422。要处理吗？

---
