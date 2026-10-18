# paper research mixed precision rd

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_mixed_precision_rd_20260514T083730_result.json`
- **Structured JSON:** [`2e286a08eef8420d4cd1.json`](../../sessions/2e/2e286a08eef8420d4cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。literature_map.yaml 中已有 5 条 `category="Mixed-Precision Rate-Distortion"` 的 `verified=true` 条目：

| bibtex_key | 论文 | role | year |
|---|---|---|---|
| `zuo2026ratequant` | **RateQuant** (Zuo et al.) | direct-competitor | 2026 |
| `lei2026arkv` | **ARKV** (Lei & Ilager) | direct-competitor | 2026 |
| `li2025kvmix` | KVmix (Li et al.) | method-component | 2025 |
| `zhang2025mixkvq` | MixKVQ (Zhang et al.) | method-component | 2025 |
| `kim2024squeezellm` | SqueezeLLM (Kim et al.) | foundation | 2024 |

**RateQuant relevance 已记录**：Algorithm 1 (discrete greedy)、Theorem 2 (reverse waterfilling closed-form)、Proposition 6 (consecutive integer polymatroid optimality)。关键发现：论文本身未讨论 hardware-aligned {2,4,8,16} 的 greedy 失败——Proposition 6 仅证明连续整数最优，非连续情形是我们项目的贡献点。

---
