# cpu table1 data compilation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_table1-data-compilation_20260519T120146_result.json`
- **Structured JSON:** [`0663e8d95eeb7f1186ae.json`](../../sessions/06/0663e8d95eeb7f1186ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `memory.md`。汇总结果：

**Table 1 主表数据：**
- **FOLIO-204**: 9 条（Mistral 4seeds 其中 s789 metrics 待补、LLaMA-8B、Qwen2.5-7B ×2、Qwen2.5-14B、Qwen3-14B）
- **ProofWriter-600**: 3 条有效 + 1 条 incomplete（exp-034 仅 93/600，不纳入）
- **LogiQA-200**: 2 条（Mistral-7B、Qwen2.5-14B）

**补充表：** 温度消融 5 点、K 敏感性 5 点

**覆盖率：** 10/21 格 DONE (48%)，5 格 RUNNING (24%)，6 格无实验 (28%)。RUNNING 全部完成后 71%。

**待处理：**
1. exp-067 (Mistral s789) metrics 为空，需从服务器提取
2. exp-035 vs exp-061 (Qwen2.5-7B FOLIO) 两次结果不一致，需选定
3. DeepSeek-R1-8B 全缺、Gemma-27B 仅 FOLIO 在跑

---
