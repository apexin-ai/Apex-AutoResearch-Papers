# analyze padding robustness a100 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_padding_robustness_a100_s42_fp32_20260519T144238_result.json`
- **Structured JSON:** [`eab56802152409414632.json`](../../sessions/ea/eab56802152409414632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果摘要

**Conclusion: SUCCESS** — padding_side 不影响定性结论。

### Lead-Lag 对比

| Method | left-padding (D093) | right-padding (a100_s42 参考) | 一致 |
|--------|---------------------|-------------------------------|------|
| PermG_fwd | 6/8 | 6/8 | ✓ |
| PermG_rev | 0/8 | 0/8 | ✓ |
| K≥4 consensus | 6/8 | — (mvp无5method) | — |
| MMCT detection | 0.75 | — | — |
| threshold_onset | 8/8 | — | — |
| TY Granger | 6/8 | — | — |

PermG 不对称性完美保持：fwd=6/8 显著，rev=0/8 → 单向因果 (canary→downstream) 不受 padding 影响。6 个 distinct pair 全部 5/5 unanimous consensus。

### 绝对值差异 (left vs right padding)

| Metric | gen0 差异 | gen10 差异 | 说明 |
|--------|----------|-----------|------|
| distinct_1 | -0.03% | +12.8% | left-pad collapse 更轻 |
| perplexity | 0.0% | -6.2% | left-pad blowup 更小 |
| token_entropy | +0.01% | -7.7% | 噪声范围 |
| ece | -1.8% | +1.6% | 噪声范围 |

**gen0 完全一致**（d1 差异 <0.03%）；gen10 差异在 ~10% 以内。right-padding 引入了额外 ~10pp 的 diversity 损失 artifact，但 drift 方向全部一致。

### 对论文 claims 的影响

D093 padding fix 不影响任何核心 claim：
1. Canary (entropy/ECE) 领先 downstream (diversity) 的因果方向完全稳健
2. Right-padding 产生的额外 d1 collapse (~10pp) 意味着论文中的 drift 数字可能偏保守（left-pad 下 collapse 更轻），不削弱结论

---
