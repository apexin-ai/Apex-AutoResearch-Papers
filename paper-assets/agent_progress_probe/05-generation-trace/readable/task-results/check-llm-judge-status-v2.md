# check llm judge status v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llm-judge-status-v2_20260515T042415_result.json`
- **Structured JSON:** [`cc558056add7b68808c6.json`](../../sessions/cc/cc558056add7b68808c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. 汇总如下：

## LLM Judge 实验结果（全部完成，无运行中进程）

| Config | Macro F1 | Acc | F1_stag | F1_prog | Parse Fail | Cost |
|---|---|---|---|---|---|---|
| Claude Sonnet 4.6 / zero-shot | 0.6625 | 0.6721 | 0.6055 | 0.7195 | 0 | $11.66 |
| Claude Sonnet 4.6 / few-shot | 0.7514 | 0.7703 | 0.6828 | 0.8199 | 0 | $36.08 |
| Claude Sonnet 4.6 / cot | 0.7499 | 0.7689 | 0.6808 | 0.8189 | 2 | $17.16 |
| **Claude Sonnet 4.6 / few-shot-cot** | **0.7994** | **0.8229** | **0.7306** | **0.8681** | **0** | $40.56 |
| GPT-5.5 / zero-shot | 0.7465 | 0.7514 | 0.7110 | 0.7819 | 408 (22.4%) | $11.62 |

**总费用**: $117.08 | **最佳变体**: Claude few-shot-cot (F1=0.799)

关键发现：
- few-shot-cot 是最佳 prompting 策略，比 zero-shot 提升 +13.7pp
- CoT 单独加无明显收益（0.750 vs 0.751 few-shot），必须与 few-shot 结合才有效
- GPT-5.5 的 22.4% parse failure rate 是硬伤，但在有效窗口上 F1 接近 Claude few-shot
- 最佳 LLM (F1=0.799) 仍比结构化 GB cross-agent (F1=0.967) 低 16.8pp

`llm-judge-strengthened` 已标记为 DONE。

---
