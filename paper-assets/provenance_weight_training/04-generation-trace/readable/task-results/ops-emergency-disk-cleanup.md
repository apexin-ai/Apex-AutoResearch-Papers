# ops emergency disk cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_20260524T164239_result.json`
- **Structured JSON:** [`386d56c3509dada8adf2.json`](../../sessions/38/386d56c3509dada8adf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

---

## 磁盘清理

- **释放 ~26GB**，从 250G/250G (200K free) → 224G/250G (27G free, 90%)
- 清理了 14 个 DONE 实验的 checkpoint-*（uniform_seed789, uniform_seed234, adaptive_seed789, adaptive_seed234, adaptive_fix_seed42, rho03_uniform_seed42, rho03_adaptive_seed42, random_reweight_baseline_seed42, ess_only_seed123, ess_only_seed456, bs16_adaptive_tau07_seed42/123/456, bs8_nmin4_adaptive_seed42）

## 4 个实验状态

| 实验 | GPU | 状态 | 进度 | 备注 |
|------|-----|------|------|------|
| **random_subset_epoch_seed42** | GPU 0 | ✅ 运行中 | step 3999/6103 (65%) | PID 944565, 正常 |
| **detect_remove_q05_seed42** | GPU 2 | ✅ 运行中 | 5270/8477 (62%) | PID 962199, 正常 |
| **p0_nmin_5** | - | ❌ 已崩溃 | 500/6103 (8%) | `RuntimeError: [enforce fail at inline_container.cc:668] unexpected pos 86016 vs 85908` — checkpoint 写入时磁盘满导致文件损坏 |
| **permuted_score_control_seed42** | - | ❌ 已崩溃 | 500/6103 (8%) | `OSError: [Errno 28] No space left on device` — 保存 checkpoint-500 时磁盘满 |

两个崩溃实验的进程已不存在，tmux session 也已退出。GPU 1 和 GPU 3 空闲，可用于重启。

---
