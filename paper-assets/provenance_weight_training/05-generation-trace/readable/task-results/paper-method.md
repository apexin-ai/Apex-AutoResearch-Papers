# paper method

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method_20260515T233706_result.json`
- **Structured JSON:** [`88ba17102a8624a44425.json`](../../sessions/88/88ba17102a8624a44425.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 已保存至 `method.tex`（v3，provenance coverage 17/18）。

内容结构：
- **3.1 Problem Setup** — 语料定义、w=(1-q)^b 加权、与 Drayson grid search 的对比
- **3.2 Dual-Constraint Framework** — α_eff 和 ESS 定义、Proposition 1（单调性 + proof sketch）、双约束 + 最小干预准则 b*
- **3.3 Adaptive Exponent Selection** — Algorithm 1 伪代码（bisection-based）、三种 regime 详解（含实证统计：50% clean / 20% α-binding / 30% ESS-binding）、loss reweighting 公式、log-space 数值稳定性、复杂度分析
- **3.4 Hyperparameter Selection** — τ=0.8 默认值（[0.5,0.8] safe range，asymmetric sensitivity）、n_min=2 默认值（与 batch size 交互）

算法描述忠实于 `weighting/alpha_eff.py` 中 `find_optimal_b` 的逻辑：先检查 clean batch → bisection 求 b_τ 和 b_ESS → 比较确定 regime。论文呈现为 bisection（代码用 grid+bisection refinement，等价但更 robust）。10 个 provenance claims 已注册。

---
