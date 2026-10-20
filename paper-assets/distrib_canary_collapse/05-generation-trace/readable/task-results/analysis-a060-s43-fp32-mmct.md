# analysis a060 s43 fp32 mmct

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a060_s43_fp32_mmct_20260519T184441_result.json`
- **Structured JSON:** [`bbfcf88680f8eec00a01.json`](../../sessions/bb/bbfcf88680f8eec00a01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析结果。

---

## D105 MMCT 5-method 分析: `alpha_sweep_a060_s43_fp32`

**T=10 (gen_0-9), gen_10 timeout (EXIT_CODE=124)**

### 方法级汇总

| 方法 | s42 (α=0.60, T=11) | **s43 (α=0.60, T=10)** | α=0.50 s42 (T=11) |
|---|---|---|---|
| Naive xcorr | 7/8 | **7/8** | 8/8 |
| Diff xcorr (FDR) | 8/8 | **6/8** | 7/8 |
| Threshold (3σ) | 0/8 | **0/8** | 4/8 |
| PermG fwd (FDR) | 3/8 | **0/8** | 6/8 |
| PermG rev (FDR) | 0/8 | **0/8** | 0/8 |
| TY Granger | 8/8 | **4/8** | 4/8 |
| **K≥4 (3σ)** | **3/8** | **0/8** | **4/8** |
| **K≥3 (3σ)** | **7/8** | **3/8** | **6/8** |

### Pair-level (s43)

| Pair | K(3σ) | Naive | DiffX | Thr3σ | PermG | TY |
|---|---|---|---|---|---|---|
| te→d1 | 2 | Y | Y | n | n | n |
| te→d2 | 3 | Y | Y | n | n | Y |
| te→d3 | 3 | Y | Y | n | n | Y |
| te→mauve | 0 | n | n | n | n | n |
| ece→d1 | 3 | Y | Y | n | n | Y |
| ece→d2 | 2 | Y | Y | n | n | n |
| ece→d3 | 2 | Y | Y | n | n | n |
| ece→mauve | 2 | Y | n | n | n | Y |

Canary onset (3σ): token_entropy=gen1, ece=gen3. Downstream onset: **全部未达 3σ**。

### Drift (gen0→gen9)

| Metric | Drift |
|---|---|
| token_entropy | -28.61% |
| ece | +1530.81% |
| perplexity | +85.11% |
| distinct_1 | -31.02% |
| distinct_2 | -39.02% |
| distinct_3 | -37.30% |
| effective_rank | +61.00% |
| mauve | -10.96% |

### 非单调性判定

**CONFIRMED — 系统性现象，非 seed 噪声。**

- α=0.50 s42: PermG=6/8, K≥4=4/8, K≥3=6/8
- α=0.60 s42: PermG=3/8, K≥4=3/8, K≥3=7/8 (↓)
- α=0.60 s43: PermG=0/8, K≥4=0/8, K≥3=3/8 (↓↓)

s43 不仅未能恢复 s42 的信号，反而进一步下降。PermG 和 K≥4 均为 0/8。两个 seed 一致表明 α=0.60 的 lead-lag 信号弱于 α=0.50，非单调下降是 α=0.60 的固有特征。

注意：s43 比 s42 少 1 个时间点 (T=10 vs T=11)，对 Granger 类方法有功率损失，但 PermG 从 3/8 → 0/8、K≥3 从 7/8 → 3/8 的幅度无法仅由此解释。

---
