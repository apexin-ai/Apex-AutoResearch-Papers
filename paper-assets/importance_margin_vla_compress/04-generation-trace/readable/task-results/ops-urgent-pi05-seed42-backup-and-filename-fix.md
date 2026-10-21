# ops urgent pi05 seed42 backup and filename fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-pi05-seed42-backup-and-filename-fix_20260521T115127_result.json`
- **Structured JSON:** [`8784eeed8e54f9939c56.json`](../../sessions/87/8784eeed8e54f9939c56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都已修复。汇总：

### Step 1: 备份完成

`/root/autodl-tmp/importance_margin_vla_compress/eval_results/` 下已备份 7 个 pi05 文件：

| 原文件 | 备份文件 |
|--------|----------|
| `pi05_baseline_libero_object.json` | `pi05_baseline_libero_object_seed42_backup.json` |
| `pi05_l2norm_k0.30_libero_object.json` | `pi05_l2norm_k0.30_libero_object_seed42_backup.json` |
| `pi05_l2norm_k0.50_libero_object.json` | `pi05_l2norm_k0.50_libero_object_seed42_backup.json` |
| `pi05_l2norm_k0.70_libero_object.json` | `pi05_l2norm_k0.70_libero_object_seed42_backup.json` |
| `pi05_random_k0.30_libero_object.json` | `pi05_random_k0.30_libero_object_seed42_backup.json` |
| `pi05_random_k0.50_libero_object.json` | `pi05_random_k0.50_libero_object_seed42_backup.json` |
| `pi05_random_k0.70_libero_object.json` | `pi05_random_k0.70_libero_object_seed42_backup.json` |

### Step 2-3: 脚本修复

| 脚本 | 状态 | 修改 |
|------|------|------|
| `eval_pi05_pruning_libero.py` | 已有 `_seed{args.seed}` | 无需修改 |
| `eval_pi05_libero.py` | ~~无 seed~~ → 已修复 | `_seed{SEED}` 加入文件名 |
| `eval_openvla_libero.py` | ~~无 seed~~ → 已修复 | `_seed{args.seed}` 加入文件名 |

seed43 实验完成后会输出 `*_seed43.json`，不会覆写无后缀的 seed42 原文件。即使覆写也有 `_seed42_backup` 兜底。

---
