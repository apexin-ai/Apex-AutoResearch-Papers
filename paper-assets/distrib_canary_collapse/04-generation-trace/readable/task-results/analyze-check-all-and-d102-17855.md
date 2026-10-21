# analyze check all and d102 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_check-all-and-d102-17855_20260522T004419_result.json`
- **Structured JSON:** [`e2c5568a63b5a800f88f.json`](../../sessions/e2/e2c5568a63b5a800f88f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All D102 analyses complete. Here's the summary:

## westd-17855 实验状态

```
Experiment              Gen Status     State       PermG fwd  PermG rev  Robust(≥3/5)
─────────────────────────────────────────────────────────────────────────────────────
t15_a045_s43_fp32       14/15 (gen14中) RUNNING     6/8*       0/8        2/8
t15_a060_s43_fp32       15/15          COMPLETED   0/8        0/8        2/8
t20_a060_s43_fp32       14/20          RUNNING     —          —          —
t25_a045_s43_fp32        2/25          RUNNING     —          —          —
t25_a050_s42_fp32       14/25          ❌ DISK FULL  6/8*       0/8        2/8
t25_a060_s42_fp32 ★     14/25          ❌ DISK FULL  0/8        0/8        0/8
```

*D102 on partial data (13 gens loaded for t25 experiments, 14 for t15_a045)

### ★ t25_a060 关键结果

**PermG fwd = 0/8, Robust = 0/8 → Scenario B (permanence)**  — 即便只有 13 gens (partial)，forward Granger 全部不显著，没有任何 pair 达到 ≥3/5 consensus。

### α 对比模式
- **α=0.45/0.50**: PermG fwd = 6/8（T=15 和 T=25 partial 一致）
- **α=0.60**: PermG fwd = 0/8（T=15 和 T=25 partial 一致）

### 磁盘问题
t25_a050 和 t25_a060 均因 `No space left on device` 在 gen_13→gen_14 checkpoint save 时崩溃。当前磁盘 231G/350G used (120G free)。需要清理空间后重启这两个实验才能拿到完整 25 gen 数据。

---
