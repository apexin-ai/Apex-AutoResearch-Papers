# ops full status check 008f

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-check-008f_20260514T061900_result.json`
- **Structured JSON:** [`8898dd6257dddb42308c.json`](../../sessions/88/8898dd6257dddb42308c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU
| GPU | Util | VRAM | 占用实验 |
|-----|------|------|----------|
| 0 | 0% | 2751/97887 MiB | 008f (eval中，瞬时低) |
| 1 | 20% | 4167/97887 MiB | 008e_v3 |

### Tmux Sessions
- `exp_008e_v3_subsample_on_dt1_h15`
- `exp_008f_no_dt_embed_subsample_on_h8`

---

### 008f (no_dt_embed, subsample_on, h=8) — **最高优先级**
- **PID**: 127766, **ALIVE**: YES
- **Config**: fixed_dt=2, subsample_max_dt=2, h=8, **dt_embed_dim=0**
- **Latest step**: **35000** (eval 刚完成)

| Step | eval_return | value_mean | v/e ratio | baseline v/e | normalized |
|------|-------------|------------|-----------|-------------|------------|
| 15K | 182.03 | 2.99 | 1.6% | — | — |
| 25K | 196.78 | 17.51 | 8.9% | 8.7% | **1.02x** |
| **35K** | **206.67** | **36.28** | **17.6%** | **24.1%** | **0.73x** |

**C2 对比 (008f vs 008d @35K)**:
- 008d (有 dt_embed): v/e = 41.2% → **1.71x** baseline
- 008f (无 dt_embed): v/e = 17.6% → **0.73x** baseline
- **结论**: 去掉 dt_embed 后 v/e 从 1.71x 暴跌到 0.73x（低于 baseline），同时 eval_return 也大幅落后（206.67 vs 008a@35K 的 500.84）。**dt_embed 是 v/e 膨胀的主要驱动因素。**

---

### 008a (fixed_dt=2, no_subsample)
- **PID**: 无 python 进程, **ALIVE**: NO — **已完成**
- **Final step**: 105K, eval_return = **777.66**, value_mean = **300.27**, v/e = **38.6%**
- 完整 eval 曲线: 31→167→231→501→563→488→608→470→584→572→**778**

---

### 008e_v3 (subsample_on, dt=1, h=15)
- **PID**: 126115, **ALIVE**: YES
- **Config**: fixed_dt=1, subsample_max_dt=2, h=15
- **Latest step**: 45000

| Step | eval_return | value_mean | v/e ratio | baseline v/e | normalized |
|------|-------------|------------|-----------|-------------|------------|
| 15K | 131.17 | 4.00 | 3.1% | — | — |
| 25K | 155.69 | — (truncated) | — | 8.7% | — |
| 35K | 276.47 | 62.76 | 22.7% | 24.1% | **0.94x** |
| **45K** | **382.22** | **110.67** | **28.96%** | **33.1%** | **0.87x** |

008e_v3 的 v/e 持续略低于 baseline（0.87-0.94x），gate_dt 锁定在 dt=1（100% dt_1_frac），说明 fixed_dt=1 + subsample 配置没有产生 v/e 膨胀。

---
