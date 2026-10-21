# ops fill cuda0 cuda3 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-cuda0-cuda3-signals_20260516T210448_result.json`
- **Structured JSON:** [`9dbc1568bc69f3dc071d.json`](../../sessions/9d/9dbc1568bc69f3dc071d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. cuda:0 — 无法提交
已被 PID 863173 占用：`compute_signals Llama-3.2-3B_d100_s42 MMLU`（运行 14 分钟）

### 2. cuda:3 — 无法提交
已被 PID 831033 占用：`evaluate.py Llama-3.2-3B_d100_s42 aligned`（运行 2h41m）

两个目标 GPU 均不空闲，按 C001/C002 约束不提交。

---

### 3. Cross-family pooled IRT（PID 863562）— 已完成

模型：**2PL+γ**，RRF signal exposure，pooling 0.5B + 1.5B + 3B（含 Llama-3.2-3B）

| Benchmark | N_mod | N_item | γ̂ | 95% CI | R̂ | ESS | PPP | rawMAE | calMAE | ΔMAE |
|-----------|-------|--------|------|--------|------|------|------|--------|--------|------|
| **gsm8k** | 25 | 300 | **-0.0097** | [-0.4409, 0.4125] | 1.009 | 1373 | 0.676 | 0.1755 | **0.0069** | 0.1686 |
| **arc_challenge** | 17 | 300 | **0.5538** | [-0.1212, 1.2275] | 1.006 | 1523 | 0.024 | 0.0435 | **0.0162** | 0.0273 |

**解读：**
- **GSM8K**: γ≈0，CI 宽泛包含零 → 跨模型家族后无污染信号。校准极好（calMAE=0.007）。
- **ARC**: γ=0.55 偏正但 CI 包含零 → 不显著。PPP=0.024 偏低，说明模型拟合有轻微张力（N=17 可能仍不够）。校准仍可接受。

结果路径：`/root/autodl-tmp/exp006/results_cross_family_irt/pooled_rrf_irt_results.json`

---
