# analysis d120 recalc 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d120_recalc_19828_20260520T052145_result.json`
- **Structured JSON:** [`82b669d7325a9d7ef4a5.json`](../../sessions/82/82b669d7325a9d7ef4a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D120 全量重算完成。26/27 实验成功（accumulate_a050_s43 因 T=0 跳过）。

**核心结果：**

| α | K≥3 均值 | PermG 趋势 | Thr3σ 趋势 |
|---|---------|-----------|-----------|
| 0.0 | 0.3 | 0/8 | 1-3/8 |
| 0.10 | 0.0 | 0/8 | 0/8 |
| 0.25 | 0.0 | 0/8 | 0/8 |
| 0.50 | 1.4 | 0-8/8 | 0/8 |
| 0.75 | 3.5 | 0-8/8 | 0-2/8 |
| 1.0 | 4.7 | 0-8/8 | 0-8/8 |

**D105 true 3σ 关键发现：**
- 比旧 `3x_sigma_drift` 显著保守 — α≤0.50 几乎全部 Thr3σ=0/8
- downstream 指标很少跨过 true 3σ 阈值（d_onset 多为 None）
- 只有 intervention 实验（reactive/predictive）达到 8/8，因为有强人工干预信号
- K≥3 consensus 主要依赖 PermG + DiffXCorr 两个方法驱动，threshold 贡献弱

汇总已写入服务器 `d120_recalc_19828.md` 并注册为 artifact `art_20260520_f6b559`。

---
