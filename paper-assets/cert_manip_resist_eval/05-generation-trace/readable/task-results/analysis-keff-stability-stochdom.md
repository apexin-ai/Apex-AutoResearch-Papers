# analysis keff stability stochdom

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_keff-stability-stochdom_20260523T123019_result.json`
- **Structured JSON:** [`1954c5e2b6802f5ae203.json`](../../sessions/19/1954c5e2b6802f5ae203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已 SCP 到本地 `docs/paper/data/`。

---

## A3: K_eff Stability Split 结果

| Stability Tier | ρ 范围 | K=3 显著 | K=5 显著 |
|---|---|---|---|
| **Stable** (4 attacks, 8 conds) | ≥0.90 | **0/8** | **4/8** |
| **Moderate** (1 attack, 2 conds) | ~0.60 | **1/2** | **2/2** |
| **Unstable** (1 attack, 2 conds) | <0.10 on ARC | **0/2** | **1/2** |

K=3 整体只有 1/12 显著（prompt_injection on MMLU），K=5 提升到 7/12。Moderate tier（prompt_injection）在两个 K 下表现最稳定（K5 达 2/2）。

## A5: Stochastic Dominance Tier 分解

61/105 (58%) dominant, 44/105 (42%) non-dominant。

| Tier 组合 | 总 pairs | Non-dominant | 比例 |
|---|---|---|---|
| mid-mid | 15 | 11 | **73.3%** |
| frontier-frontier | 6 | 4 | 66.7% |
| lightweight-lightweight | 10 | 6 | 60.0% |
| lightweight-mid | 30 | 16 | 53.3% |
| frontier-mid | 24 | 6 | 25.0% |
| frontier-lightweight | 20 | 1 | **5.0%** |

- **Within-tier**: 21/31 non-dominant (67.7%)
- **Cross-tier**: 23/74 non-dominant (31.1%)

关键发现：non-dominance 主要集中在 **同 tier 内部**（67.7%），尤其 mid-mid（73.3%）。跨越距离越大的 tier 对（frontier-lightweight）几乎全部 dominant（95%），说明 stochastic dominance 违反主要发生在 capability 相近的 judge 之间。

---
