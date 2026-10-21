# analysis scs baseline comparison

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scs_baseline_comparison_20260518T084456_result.json`
- **Structured JSON:** [`4ce3e59ac9e9605f055a.json`](../../sessions/4c/4ce3e59ac9e9605f055a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**FewRel (80 types, 3160 pairs)**
| Metric | Spearman ρ | p-value | Sig |
|---|---|---|---|
| **SCS** | **0.218** | 2.2e-35 | *** |
| Same-parent (WordNet) | 0.097 | 5.4e-08 | *** |
| WordNet WuP | 0.073 | 4.3e-05 | *** |
| Levenshtein | 0.016 | 0.363 | ns |

**Few-NERD (63 types, 1953 pairs)**
| Metric | Spearman ρ | p-value | Sig |
|---|---|---|---|
| **SCS** | **0.166** | 1.5e-13 | *** |
| Levenshtein | 0.152 | 1.4e-11 | *** |
| Same-parent (prefix) | 0.146 | 7.8e-11 | *** |
| WordNet WuP | 0.054 | 0.070 | ns (42% pairs missing) |

核心发现：
- SCS 在两个数据集上都是最强预测指标
- FewRel 上 SCS (ρ=0.218) 远超所有 baseline，次优 same-parent 仅 0.097
- Few-NERD 上 SCS (ρ=0.166) 略优于 Levenshtein (0.152) 和 same-parent (0.146)，但差距较小，因为 Few-NERD 的层级命名结构（如 art-film, art-music）让字符串相似度和前缀匹配也有一定预测力
- WordNet WuP 在 Few-NERD 上效果差（ns），因为 42% 的复合类型名无法映射到 WordNet synset

---
