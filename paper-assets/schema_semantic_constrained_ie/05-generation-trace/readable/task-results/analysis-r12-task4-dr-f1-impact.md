# analysis r12 task4 dr f1 impact

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_task4_dr_f1_impact_20260520T174639_result.json`
- **Structured JSON:** [`6f60b1d3c27ddc539fad.json`](../../sessions/6f/6f60b1d3c27ddc539fad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `westd-16980:/root/autodl-tmp/schema_outputs/r12_dr_f1_impact.json`。

## 核心发现

Constrained decoding 通过**两种机制**消除 DR violations，两者都不损害 R-F1：

### 机制 1：Type Correction（主导 SciERC）

| Setting | DR Violations | Type Corrected | Removed | Still Violating |
|---------|:---:|:---:|:---:|:---:|
| SciERC Qwen FT | 22 | **22 (100%)** | 0 | 0 |
| SciERC Llama FT | 12 | **11 (91.7%)** | 0 | 1 |

同一个 triple `(head, tail, relation)` 保留不变，只修正了 `head_type`/`tail_type` 到合法组合。R-F1 按 `(head, tail, relation)` 计算，因此完全不受影响。

### 机制 2：Triple Removal（DocRED 部分）

| Setting | DR Violations | Type Corrected | Removed | FP | TP Wrong | TP Correct |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|
| DocRED Qwen FT | 164 | 80 (48.8%) | **83** | 81 (97.6%) | 2 (2.4%) | **0** |
| DocRED Llama FT | 104 | 37 (35.6%) | **42** | 42 (100%) | 0 | **0** |

被移除的 DR-violating triples 中 **97.6–100% 是 false positives**（gold 中完全不存在），0 个正确 triple 被误删。移除 FP 不降 recall。

### 结论

DR constraint enforcement 是 "free lunch"：SciERC 靠 type correction 保留全部 triple；DocRED 靠移除几乎纯粹的 hallucinated triples。这解释了 Table 2 中 constrained 消除 DR violations 但 R-F1 ±0.5pp 的现象。

---
