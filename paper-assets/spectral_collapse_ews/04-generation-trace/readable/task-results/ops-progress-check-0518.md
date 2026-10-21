# ops progress check 0518

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-0518_20260518T052021_result.json`
- **Structured JSON:** [`cc148026a4dbafaf7e2d.json`](../../sessions/cc/cc148026a4dbafaf7e2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇报

### exp_006 — adaptive (k=10, seed=42)

**状态**: 运行中，GPU 0，已运行 ~11h 27m（01:53 UTC 启动）  
**完成**: gen 0–7 / 10

| Gen | PPL | Eff Rank | log_det | distinct_4 | mix_ratio |
|-----|------|----------|---------|------------|-----------|
| 0 | 9.55 | 417.5 | 2366.7 | 0.741 | — |
| 1 | 10.09 | 477.3 | 2365.1 | 0.710 | 0.5 |
| 2 | 10.42 | 487.1 | 2394.0 | 0.600 | 0.5 |
| 3 | 10.76 | 496.0 | 2423.8 | 0.490 | 0.5 |
| 4 | 11.14 | 501.2 | 2448.3 | 0.430 | 0.5 |
| 5 | 11.64 | 512.5 | 2488.1 | 0.373 | 0.5 |
| 6 | 12.14 | 518.9 | 2507.6 | 0.356 | 0.5 |
| 7 | 12.72 | 526.9 | 2526.2 | 0.290 | 0.5 |

**预计**: ~98 min/gen → 剩 2 gen → **ETA ~16:36 UTC**

---

### exp_004 — fixed_mix (seed=42)

**状态**: 运行中，GPU 1，已运行 ~11h 24m（01:56 UTC 启动）  
**完成**: gen 0–6 / 10

| Gen | PPL | Eff Rank | log_det | distinct_4 | mix_ratio |
|-----|------|----------|---------|------------|-----------|
| 0 | 9.55 | 417.5 | 2366.7 | 0.741 | — |
| 1 | 10.08 | 477.9 | 2366.6 | 0.669 | 0.5 |
| 2 | 10.41 | 487.9 | 2395.4 | 0.582 | 0.5 |
| 3 | 10.76 | 496.6 | 2425.6 | 0.456 | 0.5 |
| 4 | 11.14 | 502.0 | 2451.7 | 0.328 | 0.5 |
| 5 | 11.65 | 512.8 | 2486.3 | 0.235 | 0.5 |
| 6 | 12.16 | 519.8 | 2507.6 | 0.220 | 0.5 |

**预计**: ~114 min/gen → 剩 3 gen → **ETA ~19:02 UTC**

---

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 94% | 25017 / 97887 MiB |
| 1 | 72% | 25017 / 97887 MiB |

---

### log_det 趋势分析 (exp_006)

| Gen | log_det | Δ |
|-----|---------|-----|
| 5 | 2488.1 | — |
| 6 | 2507.6 | +19.5 |
| 7 | 2526.2 | +18.6 |

**仍在单调上升**，未见拐点。增幅从早期的 +25~+40 收窄到 +18~+19，有减速趋势但远未饱和。

### 关键观察

**controller_ratio 全程 = 0.5**。adaptive 条件的 k=10 意味着需要 10 个 gen 的信号才开始调整，但实验总共只跑 10 gen，所以 adaptive controller 实质上从未生效。两个实验在 mix_ratio 上完全相同，区别仅来自代码路径差异导致的随机性。distinct_4 在 exp_004 中下降更快（gen 6: 0.220 vs exp_006 gen 7: 0.290），但核心指标 (PPL, eff_rank, log_det) 两者走势几乎一致。

---
