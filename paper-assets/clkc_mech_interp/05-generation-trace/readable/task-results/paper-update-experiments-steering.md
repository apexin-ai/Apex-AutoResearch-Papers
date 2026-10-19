# paper update experiments steering

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update-experiments-steering_20260522T155330_result.json`
- **Structured JSON:** [`55aae235908bc6660349.json`](../../sessions/55/55aae235908bc6660349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。改动摘要：

**文本** (L137-146):
- "Detection ≠ Decision" 段改为 Llama-specific framing，补充 L13 all-position = last-token 的结论
- 新增 "Cross-model steering" 段，报告 Qwen L14 (p=0.682) 和 L23 (p=1.0) 均 negative，强调 detectability ≠ causality，用 "suggesting" hedging 跨模型结论

**Table 3** (L148-174):
- Caption 去掉 "(Llama-3.1-8B)"，改为两模型通用
- 按模型分组（Llama / Qwen），增加 L13 (all)、Qwen L14、Qwen L23 三行，共 7 个配置全覆盖
- 脚注补充 "(Llama L13)" 限定 α=+20 reversal 的适用范围

---
