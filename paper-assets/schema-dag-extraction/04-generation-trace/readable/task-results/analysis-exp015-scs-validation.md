# analysis exp015 scs validation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp015_scs_validation_20260515T152134_result.json`
- **Structured JSON:** [`ad9f51418cde91ea8f14.json`](../../sessions/ad/ad9f51418cde91ea8f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

## exp-015: SCS vs Empirical Confusion Rank Correlation

| Metric | Qwen3 | MiniLM |
|--------|-------|--------|
| **All pairs** (n=1953, 216 nonzero) | | |
| Spearman ρ | **0.1682** (p=7.3e-14) | 0.1439 (p=1.7e-10) |
| Kendall τ | **0.1351** (p=8.8e-14) | 0.1152 (p=2.0e-10) |
| **Nonzero-only** (n=216) | | |
| Spearman ρ | 0.2722 (p=5.0e-05) | **0.3060** (p=4.6e-06) |
| Kendall τ | 0.2001 (p=6.9e-05) | **0.2276** (p=6.0e-06) |

**结论：**

- 两个 embedding 的 SCS 都与 empirical confusion 显著正相关（所有 p < 1e-5），确认 SCS 是 confusion 的有效 proxy。
- **All pairs**：Qwen3 略优（ρ=0.168 vs 0.144），更大的 embedding 维度捕获了更多语义差异。
- **Nonzero-only**：MiniLM 反超（ρ=0.306 vs 0.272）。在实际发生混淆的 type pair 中，MiniLM 的 similarity ranking 与混淆程度更一致。
- 整体相关性中等偏弱（ρ ≈ 0.14–0.31），说明 SCS 能捕捉 confusion 趋势但非唯一因素——上下文、频率、mention ambiguity 等也影响混淆。

结果已保存到 `artifacts/exp015_scs_validation.json`。

---
