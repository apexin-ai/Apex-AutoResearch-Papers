# check eval status westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-status-westd_20260514T012706_result.json`
- **Structured JSON:** [`48015d57cbb58564e92b.json`](../../sessions/48/48015d57cbb58564e92b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete status:

---

## westd-48478

### 1. eval_cwm_seed123 (GPU 0) — RUNNING
- **Progress**: 376/9784 (3.8%)
- **Running accuracy**: 56.9%
- **Speed**: ~8 samples/52s → ETA ~130h
- **GPU**: 88%, 13.0/31.8 GB

### 2. eval_cwm_v12 (GPU 1) — RUNNING
- **Progress**: 376/9784 (3.8%)
- **Running accuracy**: 60.4%
- **Speed**: ~8 samples/52s → ETA ~130h
- **GPU**: 88%, 13.0/31.8 GB

### 3. eval_cls_v5 (GPU 2) — NOT FOUND
- tmux session 不存在, GPU 2 空闲 (0%, 0 MiB)
- 未找到任何 `*v5*` 结果文件
- 该 session 可能从未启动或启动后立即崩溃

### 4. eval_cls_8b (GPU 3) — NOT FOUND
- tmux session 不存在, GPU 3 空闲 (0%, 0 MiB)
- `eval_results/` 下有 **May 13 的旧结果** (可能来自之前的 run):

| 文件 | accuracy | fail_f1 | pass_f1 | f1_macro | unparseable |
|------|----------|---------|---------|----------|-------------|
| cls8b_seed42 | **90.48** | 90.06 | 90.86 | 90.46 | 0% |
| cls8b_seed123 | **89.37** | 89.19 | 89.54 | 89.37 | 0% |

这些是 May 13 01:24-01:25 的文件，不确定是否为今天 eval_cls_8b session 的产出。

---

## home-1x5090

### eval_cls_seed123 — COMPLETED
- tmux session 仍在，但最后一行日志停在 **May 13 18:43** (8960/9784)
- 结果文件 `eval_cls_seed123_with_preds.json` 已存在，eval 已完成:

| 指标 | 值 |
|------|-----|
| accuracy | **89.52** |
| fail_f1 | 89.40 |
| pass_f1 | 89.64 |
| f1_macro | 89.52 |
| unparseable_pct | 0% |
| confusion | tn=835, fp=77, fn=121, tp=857 |

---

**要点**: GPU 2/3 空闲且无 CLS session — 需要重新启动 eval_cls_v5 和 eval_cls_8b（如果它们是今天该跑的任务）。两个 CWM eval 刚开始跑，按当前速度大约需要 5.5 天完成。

---
