# check home 8b val5120 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-8b-val5120-status_20260514T171903_result.json`
- **Structured JSON:** [`a98cbeef9e63da7bbd80.json`](../../sessions/a9/a98cbeef9e63da7bbd80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 8B val@5120 Sweep 状态汇总

### tmux session `eval_8b_val5120`
**存在，正在运行。** 当前在跑 ckpt-3000 的 eval。

### GPU 状态
- GPU 0: 22509/32607 MiB, 利用率 100%
- 进程: python3 (PID 3145070, 22500 MiB)

### ckpt-400 (conda) — 已完成 ✓

| 指标 | 值 |
|------|-----|
| Accuracy | **80.47%** |
| Majority baseline | 75.88% |
| Gap vs majority | +4.6pp |
| F1 macro | **75.84%** |
| F1 fail | 65.27% (P=57.2%, R=76.1%) |
| F1 pass | 86.42% (P=91.5%, R=81.9%) |
| Truncated | 234/9335 |

### ckpt-3000 — 正在运行

- 进度: **5400/9335** (57.9%)
- Running accuracy: **89.2%**
- 预计剩余: ~3960 samples, 按当前速度约 25-30 分钟

### 结论

**Sweep 尚未完成。** ckpt-400 已完成（acc=80.5%），ckpt-3000 正在跑（进度 58%，running acc=89.2%）。ckpt-3000 的 running accuracy 显著高于 ckpt-400 的最终 accuracy，说明更多训练步数有明显提升。

---
