# fix gsm8k reextract nan and rerun

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gsm8k_reextract_nan_and_rerun_20260521T134714_result.json`
- **Structured JSON:** [`163a3bed65377029d072.json`](../../sessions/16/163a3bed65377029d072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

NaN bug 已修复，脚本成功运行。结果汇总：

| 指标 | 值 |
|---|---|
| GSM8K 总记录数 | 230,400 |
| 答案差异数 | 225,672 (97.95%) |
| 原始准确率 | 0.5558 |
| 重提取准确率 | 0.0177 |
| 准确率变化 | **-0.5381** |
| 翻对→错 | 125,452 |
| 翻错→对 | 1,484 |

**注意**：stop-sequence 截断（`\n\n` 等）导致准确率从 55.6% 暴跌到 1.8%。从样本看，GSM8K 的 chain-of-thought 推理步骤之间大量使用 `\n\n` 分隔，截断后只保留了第一步的中间数字，丢失了最终答案。这说明 `\n\n` 作为 stop sequence 对 GSM8K 的 CoT 格式是不适用的——原始提取逻辑反而更合理。

输出文件：
- 报告：`results/analysis/gsm8k_answer_reextract.json`
- 修正 JSONL：`results/analysis/gsm8k_corrected.jsonl`

---
