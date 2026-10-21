# analysis metrics compilation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metrics-compilation_20260516T002456_result.json`
- **Structured JSON:** [`f43721f8398abe6459fc.json`](../../sessions/f4/f43721f8398abe6459fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已生成并注册：

**核心结果排序 (Rel-F1)**：
| 方法 | Rel-F1 | Evi-F1 |
|------|--------|--------|
| CED Reranker (N=8) | 0.4864 | 0.8188 |
| CED RSFT top_k=1 (3-seed mean) | 0.4596±0.013 | 0.8143±0.005 |
| GRPO bf16 best | 0.4549 | 0.8086 |
| flat-NLI RSFT (2-seed mean) | 0.4531±0.001 | 0.8101±0.008 |
| RSFT top_k=3 | 0.4454 | 0.8088 |
| SFT baseline | 0.4106 | 0.8013 |
| DPO 1ep | 0.4034 | 0.8088 |
| DPO 3ep | 0.3429 | 0.8403 |
| GRPO QLoRA (catastrophic) | 0.2167 | 0.5746 |

**关键发现**：
- DPO 和 GRPO QLoRA 在 registry 中标记为 `negative`，非 `success`，但仍有指标数据，已纳入表格
- Registry 中无 DPO/topk3 的 `success` 条目，用 `negative` 结论的实验数据代替
- flat-NLI 只有 2 个 full-dev seed（s44/s45 full eval 未完成或被 killed）

文件路径：
- `artifacts/metrics_summary_table.md` (Markdown)
- `artifacts/metrics_summary.csv` (CSV)

---
