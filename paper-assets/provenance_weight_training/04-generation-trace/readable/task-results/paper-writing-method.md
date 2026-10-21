# paper writing method

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260515T202140_result.json`
- **Structured JSON:** [`347aa4f6e3b46ad017ed.json`](../../sessions/34/347aa4f6e3b46ad017ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 已写入 `sections/method.tex`。结构：

- **3.1 Problem Setup** — 语料定义、加权公式 (cite Drayson)、目标
- **3.2 Dual-Constraint Framework** — α_eff 和 ESS 定义，Proposition 1 (α_eff 单调递增，proof via Cov_w(r, ln(1-q)))，Proposition 2 (ESS 单调递减)，quality/stability 约束，最小干预原则，与 ESS-only 的对比
- **3.3 Algorithm** — Algorithm 1 伪代码 (bisection)，三种 regime，loss reweighting vs SIR，复杂度分析
- **3.4 Hyperparameter Selection** — τ 的理论 motivation + empirical safe range [0.5, 0.8]，n_min 的默认值和边界行为，与 Drayson 固定 b 的对比

---
