# research training data sharegpt ultrachat

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_training-data-sharegpt-ultrachat_20260518T061027_result.json`
- **Structured JSON:** [`4fbbb41cecbe7ba5bbc7.json`](../../sessions/4f/4fbbb41cecbe7ba5bbc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/training_data_survey_report.md` 并注册。

**核心结论：**

- **推荐方案**：ShareGPT_Vicuna_unfiltered（1500 条）+ UltraChat 200k（1000 条）= 2500 条 ≥5 turns 对话
- **ShareGPT 为主**：真实用户对话，纯英文，Apache 2.0，预计 8k-13k 条 ≥5 turns 可选
- **UltraChat 补充**：MIT license，已清洗，预计 62k-103k 条 ≥5 turns 可选
- **不推荐**：LMSYS-Chat-1M（license 受限 + 多数单轮）、WildChat（需毒性过滤）、oasst2（树结构提取复杂）
- 报告包含完整的预处理 pipeline 代码（筛选、格式统一、token 长度过滤、采样、与 lost_in_conversation 去重）

---
