# check post restart 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_post_restart_30476_20260518T162721_result.json`
- **Structured JSON:** [`e255dc512614361daf8f.json`](../../sessions/e2/e255dc512614361daf8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### westd-30476 (4× GPU)

| GPU | VRAM | Util | 状态 |
|-----|------|------|------|
| 0 | 0 MiB | 0% | 空闲 |
| 1 | 0 MiB | 0% | 空闲 |
| 2 | 0 MiB | 0% | 空闲 |
| 3 | 41757 MiB | 99% | 运行中 |

| 实验 | 状态 | 进度 | 备注 |
|------|------|------|------|
| epoch_matched_dr_seed123 | ✅ 完成 | final/ 已保存 | |
| epoch_matched_dr_seed456 | ✅ 完成 | final/ 已保存 | |
| detect_remove_q01_seed42 | 🔄 运行中 | 55% (3372/6103), ~1h36m | GPU 3 |
| detect_remove_q07_seed42 | ✅ 完成 | final/ + checkpoint-6103 | 之前已跑完 |
| detect_remove_q03_seed42 | ❌ 未启动 | 目录不存在 | 日志显示 `python: command not found` |

**问题**: q03 和 q07 的日志显示 `python: command not found` (EXIT_CODE=127)，说明重启后尝试恢复时 python 路径失效。q07 之前已跑完所以无影响，但 q03 从未成功启动。GPU 0-2 空闲，q01 跑完后 GPU 3 也会空闲。

---

### westd-41312 (4× GPU)

| GPU | VRAM | Util | 状态 |
|-----|------|------|------|
| 0 | 61693 MiB | 99% | 运行中 |
| 1 | 63511 MiB | 100% | 运行中 |
| 2 | 45643 MiB | 78% | 运行中 |
| 3 | 45643 MiB | 100% | 运行中 |

| 实验 | 状态 | 最新 checkpoint | 预估进度 |
|------|------|----------------|---------|
| uniform_1_7b_seed42 | 🔄 运行中 (GPU 0) | ckpt-3000 | 45% (2740/6103), ~2h08m |
| adaptive_1_7b_seed42 | 🔄 运行中 (GPU 1) | ckpt-4500 | ~74% |
| ngram_adaptive_seed42 | 🔄 运行中 (GPU 2) | ckpt-2500 | ~50% (3020/6103) |
| ngram_uniform_seed42 | 🔄 运行中 (GPU 3) | ckpt-3000 | ~50% (3025/6103) |
| uniform_1_7b_seed42_resumed (Plan B) | 🔄 运行中 | ckpt-1500 | ~25% |

westd-41312 全部 4 GPU 满载，5 个实验均在正常推进。

---

**需要处理**:
1. westd-30476 的 **detect_remove_q03_seed42** 需要手动启动（用 `/root/miniconda3/bin/python` 而非 `python`）
2. westd-30476 有 3 张空闲 GPU 可利用

---
