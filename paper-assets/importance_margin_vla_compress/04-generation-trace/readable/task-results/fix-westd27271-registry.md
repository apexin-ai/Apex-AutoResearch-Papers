# fix westd27271 registry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd27271_registry_20260525T074724_result.json`
- **Structured JSON:** [`7c1f9ac71935d9098d6a.json`](../../sessions/7c/7c1f9ac71935d9098d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 修复完成。

**状态汇总：**
- **PID**: 213708，GPU 1 (15.9GB VRAM)，tmux session `random_object`
- **命令**: `python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 42`
- **进度**: Task 10/10, Ep 10/50 — 预计 ~20 分钟完成
- **已完成 9 个 task 的 SR**: 271/450 (60.2%)
- **Registry**: `eval_openvla_random_k09_object_seed42` → RUNNING，已恢复（之前被 killed）
- **Cron**: 每 8 分钟检查完成状态，完成后自动更新 DONE

---
