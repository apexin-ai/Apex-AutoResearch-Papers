# analysis c4 perplexity stationarity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_perplexity_stationarity_20260517T175916_result.json`
- **Structured JSON:** [`7092bd08771f41b5f1fc.json`](../../sessions/70/7092bd08771f41b5f1fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Stationarity Report — C4 Pythia-1B (+ WikiText OPT-1B 对比)

### ADF Test (H0: 非平稳; p<0.05 拒绝 → 平稳)

| Series | ADF stat | p-value | Stationary? |
|---|---|---|---|
| **C4 ppl_raw** | **1.0697** | **0.9949** | **N** |
| C4 ppl_diff | -0.0689 | 0.9524 | N |
| C4 ppl_log | -1.6292 | 0.4679 | N |
| **C4 ppl_logdiff** | **-3.0403** | **0.0313** | **Y** |
| C4 entropy_raw | -0.2383 | 0.9338 | N |
| C4 entropy_diff | -2.9149 | 0.0436 | Y |
| C4 ece_raw | -2.8012 | 0.0581 | N (borderline) |
| C4 ece_diff | -3.0348 | 0.0318 | Y |
| Wiki ppl_raw | -1.5624 | 0.5024 | N |
| Wiki ppl_diff | -2.2544 | 0.1871 | N |
| **Wiki ppl_logdiff** | **-5.1817** | **0.0000** | **Y** |

### KPSS Test (H0: 平稳; p>0.05 不拒绝 → 平稳) — 交叉验证

| Series | KPSS stat | p-value | Stationary? |
|---|---|---|---|
| C4 ppl_raw | 0.6414 | 0.0189 | N |
| C4 ppl_diff | 0.4228 | 0.0673 | Y (borderline) |
| C4 ppl_logdiff | 0.4328 | 0.0630 | Y (borderline) |
| C4 entropy_raw | 0.3713 | 0.0895 | Y |
| C4 ece_raw | 0.4496 | 0.0558 | Y (borderline) |
| Wiki ppl_logdiff | 0.4567 | 0.0527 | Y (borderline) |

### 诊断细节

**C4 ppl 的严重性**：ADF stat = +1.07（正值！），说明序列是**爆炸性过程**(explosive)，不仅是单位根，而是比单位根更强的非平稳。

**log-diff 是唯一可行的变换**：
- 一阶差分无效（ADF p=0.95）：因为 raw diffs 的方差不稳定（gen0→1 跳 123.6，gen9→10 跳 230.0）
- log 变换无效（ADF p=0.47）：仍保留趋势
- log-diff 有效（ADF p=0.031, KPSS p=0.063）：**两个检验方向一致**

**但 log-diff 仍有衰减趋势**：
- 前半段 mean = 0.7267，后半段 mean = 0.1539
- 说明增长率本身在递减（指数增长在减速），log-diff 只是"勉强"平稳

**entropy 和 ECE 的特征**：
- 两者都有 gen0→gen1 的剧烈跳变（entropy 2.96→1.43, ECE 0.01→0.33）
- gen1 之后趋于平台期（entropy 1.19-1.43, ECE 0.33-0.46）
- 这种"level shift + 缓慢收敛"模式使 ADF 拒绝不了单位根，但 KPSS 认为是平稳的 → **结构性断点**问题，不是经典的单位根

### 结论

| 问题 | 答案 |
|---|---|
| perplexity 是否违反平稳性假设 | **是，严重违反**（爆炸性过程，ADF stat 为正） |
| 差分能否修复 | **不能**（一阶差分仍不平稳） |
| log-transform 能否修复 | **单独不能**，但 **log-diff 可以** (p=0.031) |
| entropy/ECE 是否平稳 | **边界情况**：ADF 不拒绝单位根，KPSS 不拒绝平稳 → 结构断点 |

### 建议

1. **perplexity 不能直接用于 VAR**，必须做 log-diff 变换（即 Δlog(ppl)，对应增长率）
2. **entropy 和 ECE** 建议也用一阶差分进入 VAR（差分后 ADF 均显著）
3. **T=11 下所有检验 power 极低**（ADF critical sample ~50+），log-diff 的 p=0.031 在边界。如实报告这个局限
4. **结构断点**（gen0→gen1 剧变）是所有指标的共性问题，可考虑从 gen1 开始建模（T=10），但样本会更短
5. WikiText 表现相同模式：raw 非平稳，log-diff 平稳（且 p<0.0001 更显著，因为 OPT-1B 增长更规律）

---
