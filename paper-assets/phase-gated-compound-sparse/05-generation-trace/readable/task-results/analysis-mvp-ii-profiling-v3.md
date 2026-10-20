# analysis mvp ii profiling v3

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_ii_profiling_v3_20260513T224011_result.json`
- **Structured JSON:** [`dfff605a16171b004617.json`](../../sessions/df/dfff605a16171b004617.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析完成

**结论: negative** — 测量方法有效但假设不成立。

### 关键发现

**v3 技术修复成功:**
- 无 NaN/Inf（v2 有 Inf）
- Phase 分布均匀 30%/32.5%/37.5%（v2 极度偏斜 1.2%/8.1%/90.7%）

**假设不成立:**
- 所有 phase × sparsity 组合的 II 均为 super-additive（正值），无 sign reversal
- 所有 CI 重叠，无显著 cross-phase 差异
- v2 的 CI nonoverlap 被证实是分布偏斜的 artifact

**II 值摘要 (sparsity=0.2):**

| Phase | II Mean | 95% CI |
|-------|---------|--------|
| high_sparsity | +2.16 | [+1.06, +3.55] |
| low_sparsity | +1.13 | [+0.44, +1.96] |
| mid_sparsity | +0.30 | [-1.06, +1.30] |

三次迭代（v1/v2/v3）均未发现 phase-dependent compound sparsity interaction。Registry 已更新，分析报告已注册为 artifact `art_20260513_7a8b0f`。

---
