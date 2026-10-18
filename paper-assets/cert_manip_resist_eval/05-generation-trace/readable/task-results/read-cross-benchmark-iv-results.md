# read cross benchmark iv results

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_cross-benchmark-iv-results_20260523T084727_result.json`
- **Structured JSON:** [`f0e4d9eed484469fb511.json`](../../sessions/f0/f0e4d9eed484469fb511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，结果完整。下面是汇总：

---

## Cross-Benchmark IV 分析结果

### Cross Correlations (K_eff_MMLU vs K_eff_ARC)

| K | r(K_eff) | cross η | within η | cross < within | n |
|---|----------|---------|----------|----------------|---|
| K3 | 0.784 | 0.383 | 0.479 | ✓ | 455 |
| K5 | 0.762 | 0.386 | 0.807 | ✓ | 3003 |
| K7 | 0.763 | 0.349 | 0.781 | ✓ | 6435 |

所有 K 值下 cross-benchmark η 都低于 within-benchmark η，说明跨 benchmark 预测力弱于 within-benchmark。

### Reduced Form 显著性总结

| K | Direction | keff sig | η sig |
|---|-----------|----------|-------|
| K3 | mmlu→arc | 5/6 | 6/6 |
| K3 | arc→mmlu | 6/6 | 6/6 |
| K5 | mmlu→arc | 6/6 | 6/6 |
| K5 | arc→mmlu | 6/6 | 6/6 |
| K7 | mmlu→arc | 6/6 | 6/6 |
| K7 | arc→mmlu | 6/6 | 5/6 |

Reduced form 几乎全显著（唯一例外：K3 mmlu→arc sycophancy 的 keff 不显著 p=0.108；K7 arc→mmlu authority_bias 的 η 不显著 p=0.077）。

### 2SLS（已作废，仅记录）

IV exclusion restriction violated（Spearman ρ=0.90 > 0.8），2SLS 结果不可信。技术上所有 18 个 first-stage F 统计量都远超 10（K3: F=820, K5: F=4508, K7: F=9232），instrument 很强，但 exclusion restriction 失败意味着 2SLS 估计有偏。

### Bootstrap 推断（cluster-robust, FDR-corrected）

**K3** — 大部分 keff 和 η 的 bootstrap p-value 在 FDR 校正后仍显著（≤0.05），两个方向都稳健。

**K5** — mmlu→arc 方向 keff 多数显著（5/6 FDR p<0.05），但 η 多数不显著。arc→mmlu 方向 keff 更弱（2-3/6 显著），η 也弱。

**K7** — mmlu→arc 方向 keff 4/6 显著，η 仅 verbosity_bias 显著。arc→mmlu 方向 keff 仅 1-2/6 显著，η 几乎全不显著。

**Bootstrap 结论**：K3 最稳健；K5 和 K7 的 OLS 显著性在 cluster-robust bootstrap 下明显衰减，尤其 arc→mmlu 方向和 η 系数。

---
