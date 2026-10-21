# analysis r12 task1b fallback precision recall

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_task1b_fallback_precision_recall_20260520T180440_result.json`
- **Structured JSON:** [`81b8432f18802eb82faf.json`](../../sessions/81/81b8432f18802eb82faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**DocRED** (1770 fallback / 15571 non-fallback triples):
| | Count | Precision | Recall Contrib |
|---|---|---|---|
| Fallback | 1,770 | **0.00%** | 0.00% |
| Non-fallback | 15,571 | **7.81%** | 9.87% |
| Delta P | | **-7.81pp** | |

**SciERC** (16 fallback / 1713 non-fallback triples):
| | Count | Precision | Recall Contrib |
|---|---|---|---|
| Fallback | 16 | **0.00%** | 0.00% |
| Non-fallback | 1,713 | **6.60%** | 11.60% |

**诊断细节** (DocRED 1770 fallback triples):
- 54.8% head 文本出现在 gold entities 中
- 13.4% tail 文本出现在 gold entities 中
- 仅 3.7% (65/1770) entity pair 匹配 gold，但这 65 个全部关系名错误

**核心结论**：Fallback triples（type-pair 约束违反）precision 为 0%，recall 贡献也为 0%。它们是纯噪声。在 DocRED 上，移除 fallback triples 可以消除 ~10% 的 false positives 且不损失任何 recall。Type-pair 约束违反是提取失败的可靠指标。

输出文件：
- JSON: `westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_precision_recall.json`
- 文本: `westd-16980:/root/autodl-tmp/schema_outputs/r12_fallback_pr_text.txt`
- 脚本: `westd-16980:/root/schema_semantic_constrained_ie/scripts/analyze_fallback_precision_recall.py`

---
