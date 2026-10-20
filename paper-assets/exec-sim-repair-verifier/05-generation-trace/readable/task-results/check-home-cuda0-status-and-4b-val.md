# check home cuda0 status and 4b val

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-cuda0-status-and-4b-val_20260514T210018_result.json`
- **Structured JSON:** [`4639da4a8b91e3f6d026.json`](../../sessions/46/4639da4a8b91e3f6d026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇报如下：

---

## home-1x5090 cuda:0 状态

**占用中** — PID 3165829 正在跑 `eval_repo_cls.py` seed123 ckpt-600 val@5120，已运行 ~58 min，进度 7856/9335 (84.2%)，预计 ~10-15 min 完成。

---

## 4B seed123 Val Sweep 完整结果

### Val @ seq_len=2048 (`val_eval_results/`)
n=9335, unparseable=1883 (全部来自截断)

| Ckpt | Accuracy | F1_macro | F1_pass | F1_fail | P_fail | R_fail | P_pass | R_pass |
|------|----------|----------|---------|---------|--------|--------|--------|--------|
| 200 | 62.51 | 55.54 | 73.14 | 37.94 | 31.58 | 47.51 | 80.12 | 67.27 |
| 400 | 80.72 | 67.03 | 88.27 | 45.78 | 71.16 | 33.75 | 81.95 | 95.65 |
| 600 | 76.78 | 66.81 | 85.00 | 48.63 | 52.13 | 45.56 | 83.36 | 86.70 |
| **800** | **81.81** | **69.14** | **88.91** | **49.37** | 75.14 | 36.77 | 82.70 | 96.13 |
| 1000 | 82.30 | 67.63 | 89.42 | 45.84 | 87.59 | 31.04 | 81.81 | 98.60 |

### Val @ seq_len=4096 (`val_eval_results_4096/`)
n=9335, unparseable=truncated=1406

| Ckpt | Accuracy | F1_macro | F1_pass | F1_fail | P_fail | R_fail | P_pass | R_pass |
|------|----------|----------|---------|---------|--------|--------|--------|--------|
| 400 | 82.57 | 71.24 | 89.29 | 53.18 | 75.55 | 41.03 | 83.63 | 95.78 |
| 600 | 79.18 | 70.73 | 86.45 | 55.00 | 57.45 | 52.75 | 85.36 | 87.58 |
| **800** | **83.70** | **73.31** | **90.00** | **56.70** | 79.00 | 44.20 | 84.40 | 96.30 |

### Val @ seq_len=5120 (`results/repo_cls_seed123_ckpt*_val5120/`)
n=9335, unparseable=0, truncated=234

| Ckpt | Accuracy | F1_macro | F1_pass | F1_fail | P_fail | R_fail | P_pass | R_pass |
|------|----------|----------|---------|---------|--------|--------|--------|--------|
| **400** | **86.01** | **79.66** | **91.02** | **68.30** | 75.32 | 62.48 | 88.68 | 93.49 |
| 600 | 进行中 (84.2%) | — | — | — | — | — | — | — |

### Val @ seq_len=6144 — 已挂
ckpt-400 完成（日志显示约 86%），但未生成结果 JSON。ckpt-600 在 2040/9335 停止，进程已死。

---

## 关键发现

1. **seq_len 对 F1_macro 影响极大**：2048→4096→5120 从 69.14 → 73.31 → 79.66（ckpt-800 vs 400 对比），unparseable 从 1883 → 1406 → 0
2. **最佳 ckpt 随 seq_len 变化**：2048 下 ckpt-800 最优 (F1_macro=69.14)，5120 下 ckpt-400 已达 79.66
3. ckpt-600 val5120 完成后，还需跑 ckpt-200/800/1000 的 val5120 才能做完整 sweep

---

## 4B v5-conda Val Sweep

未找到任何 v5-conda 相关结果文件。现有 v5 结果（`val_eval_results/checkpoints_repo_cls_v5_*`）是不同 checkpoint 系列（ckpt-600/4000/4200/4400/4600），不含 "conda"。

**cuda:0 预计 ~15 min 后可用**，ckpt-600 val5120 完成后即可启动 v5-conda val sweep。

---
