# code plan 009 judge calibration framework

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_009_judge_calibration_framework_20260520T160834_result.json`
- **Structured JSON:** [`3b5a18b07ae0085d1b18.json`](../../sessions/3b/3b5a18b07ae0085d1b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 009 完成。产出汇总：

| 产出 | 路径 | 说明 |
|------|------|------|
| `sampled_episodes.json` | `plan_009/` | 100 条分层采样，覆盖 6 types × 2 conditions × 2 models |
| `annotation_guidelines.md` | `plan_009/` | 标注指南 + 8 个 gold examples（每级 2 个） |
| `annotation_sheet.jsonl` | `plan_009/` | 100 条标注表格，含 trajectory、隐藏 LLM 标签 |
| `llm_baseline_gpt-54.jsonl` | `plan_009/` | gpt-5.4 对 100 条的独立判定 |
| `llm_baseline_gpt-41.jsonl` | `plan_009/` | gpt-4.1 对 100 条的独立判定 |
| `llm_agreement.json` | `plan_009/` | 两模型一致性指标 |

关键指标：
- **Weighted Cohen's κ = 0.685**（substantial agreement）
- **Binary agreement (moderate+) = 0.90，Binary κ = 0.74**
- 采样分布：none=71, moderate=16, critical=9, minor=4
- 0 parse failures，200 条 baseline 全部成功

---
