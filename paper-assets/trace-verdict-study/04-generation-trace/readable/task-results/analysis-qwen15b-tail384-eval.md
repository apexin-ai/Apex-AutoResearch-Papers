# analysis qwen15b tail384 eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_tail384_eval_20260518T151617_result.json`
- **Structured JSON:** [`bac48fbb544a0004067a.json`](../../sessions/ba/bac48fbb544a0004067a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，结论为 **negative**。

## Qwen-1.5B tail-384 结果

| Metric | Value |
|---|---|
| **Accuracy** | **73.6%** (CI: 71.0–76.2%) |
| Majority baseline | 71.5% |
| **Lift over baseline** | **+2.1%** |
| Pass P / R / F1 | 80.7% / 83.0% / 81.8% |
| Fail P / R / F1 | 54.0% / 50.1% / 52.0% |
| N | 1190 |

## 对比

| Model | Accuracy |
|---|---|
| DeepSeek-6.7B tail-384 | **80.7%** |
| Qwen-7B tail-384 | **79.8%** |
| **Qwen-1.5B tail-384** | **73.6%** |
| Majority baseline | 71.5% |

**假设 80–90% 被否定。** Qwen-1.5B 在 tail-384 条件下几乎退化到 majority baseline，lift 仅 2.1%（CI 下界包含 0）。fail 类 F1 只有 52%，说明模型基本丧失了区分 fail 的能力。从 7B→1.5B 的 accuracy 下降幅度（~6pp）远大于 DeepSeek-6.7B→Qwen-7B 之间的差异，说明 1.5B 参数量在 tail-384 截断条件下已低于有效学习的门槛。

---
