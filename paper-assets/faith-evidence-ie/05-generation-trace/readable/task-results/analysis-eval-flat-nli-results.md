# analysis eval flat nli results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_flat_nli_results_20260515T180038_result.json`
- **Structured JSON:** [`0649a26291106b677399.json`](../../sessions/06/0649a26291106b677399.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已有详细 notes（hook 自动填充）。metrics 已更新完毕。

**Flat-NLI RSFT 结果汇总：**

| 指标 | Flat-NLI | CED RSFT (3-seed mean) | Δ |
|------|----------|----------------------|---|
| rel_f1 | 0.4539 | 0.4596 ± 0.0128 | -0.57pp |
| evi_f1 | 0.8043 | 0.8126 | -0.83pp |
| edcr | 0.6431 | — | — |
| format_ok | 100% | 100% | — |
| truncated | 199/985 | ~170/985 | — |

**结论：CED contrastive margin 对 RSFT filtering 无显著增益。**

- rel_f1 差距仅 0.57pp，远在 CED 3-seed 标准差（σ=0.0128）范围内
- flat-NLI 单 seed=42 的 0.4539 甚至高于 CED seed=42 的 0.4449（+0.90pp）
- 两种 RSFT 均大幅超过 SFT baseline（+4.8pp），说明 RSFT 本身有效，但 contrastive margin 不是关键因素
- 论文中 CED 的价值应聚焦在 reranker/GRPO reward 等其他用途，而非 RSFT filtering 的 margin 设计

---
