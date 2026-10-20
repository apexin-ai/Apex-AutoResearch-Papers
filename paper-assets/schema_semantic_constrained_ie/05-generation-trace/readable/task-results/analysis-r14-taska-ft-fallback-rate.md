# analysis r14 taskA ft fallback rate

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_taskA_ft_fallback_rate_20260520T201621_result.json`
- **Structured JSON:** [`8f2a442f1a90007b1773.json`](../../sessions/8f/8f2a442f1a90007b1773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

## R14 FT Fallback Rate 分析结果

### FT Fallback Rate（DR-constrained positions）

| Config | ZS | FT | Reduction |
|--------|------|------|-----------|
| SciERC Qwen | 0.46% (16/3458) | **0.00%** (0/2256) | -100% |
| SciERC Llama | 0.04% (1/2630) | 0.05% (1/2162) | ~0 (noise) |
| DocRED Qwen | 5.68% (1970/34682) | **0.01%** (2/31126) | -99.9% |
| DocRED Llama | 1.41% (461/32736) | **0.11%** (34/32148) | -92.5% |

### 关键发现

1. **FT 几乎消除了所有 DR fallback**：Qwen FT 在 SciERC 上零违反，DocRED 上仅 2 个（31126 个位置）
2. **根因分析**：ZS 违反 100% 是 model preference（模型不了解 relation-specific DR 约束），0% tokenizer collision，0% schema coverage gap
3. **Token-level 36.6% 的真实含义**：该数字被多 token type 名称（如 "OtherScientificTerm"）的续写 token 位置膨胀。在语义上有意义的 first-token 位置，ZS DR 违反率仅 ~0.5%（SciERC）和 ~5.7%（DocRED）。FT 将其降至接近零

### 输出

完整 JSON：`westd-16980:/root/autodl-tmp/schema_outputs/r14_ft_fallback_rate.json`

---
