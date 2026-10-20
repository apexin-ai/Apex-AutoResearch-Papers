# analysis smollm3 3b wiki a100 s42 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smollm3_3b_wiki_a100_s42_v3_20260519T190410_result.json`
- **Structured JSON:** [`ad92fdd10e821fc7ad5f.json`](../../sessions/ad/ad92fdd10e821fc7ad5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 摘要

**smollm3_3b_wiki_a100_s42_v3** — SmolLM3-3B fp32 跨架构验证，EXIT_CODE=0，11 generations (gen_0–gen_10) 完整，18.7 GPU-hours。

### 5-Method Analysis (2σ threshold, unified)

| 指标 | 结果 |
|------|------|
| PermG fwd | **6/8** |
| PermG rev | 0/8 |
| Threshold onset | **8/8** |
| K≥3 | **7/8** |
| K≥4 | **6/8** |

Per-pair detail:
- **token_entropy→distinct_{1,2,3}**: K=4, PermG fwd 显著 (p=0.035–0.049)
- **token_entropy→perplexity**: K=3, PermG fwd 不显著 (p=0.31)
- **ece→distinct_{1,2,3}**: K=4, PermG fwd 显著 (p=0.006–0.011)
- **ece→perplexity**: K=2, PermG fwd 不显著 (p=0.17)

### MMCT Consensus Test (vs alpha=0.00 null)

所有模式均 0/8 significant。原因：仅 3 个 null runs，bootstrap 分布分辨率有限（最小可达 p=0.12），formal MMCT 缺 power。

### Table 7 意义

SmolLM3-3B 行可填入：5-method 层面 canary→diversity 关联强（6/8 pairs K≥4），方向性正确（fwd sig, rev ns），与其他架构（GPT-2m, OPT-1.3B, Pythia-1.4B）结果一致。MMCT formal test 的 ns 结果是所有 Table 7 conditions 共有的 power 限制，非 SmolLM3 特异。

---
