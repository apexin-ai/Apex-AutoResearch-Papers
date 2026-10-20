# experiment llm judge continue

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llm-judge-continue_20260515T042640_result.json`
- **Structured JSON:** [`1d5dbaecb78918b3c7e4.json`](../../sessions/1d/1d5dbaecb78918b3c7e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `llm-judge-strengthened` 已在上一轮 Worker 完成，所有 5 个条件均已跑完全部 1824 windows。我已验证结果文件并补全了 registry 中缺失的详细指标。

**最终结果汇总：**

| Condition | macro_F1 | F1_stag | F1_prog | Parse Fail | Cost |
|---|---|---|---|---|---|
| claude_zeroshot | 0.6625 | 0.6055 | 0.7195 | 0 | $11.66 |
| claude_fewshot | 0.7514 | 0.6828 | 0.8199 | 0 | $36.08 |
| claude_cot | 0.7499 | 0.6808 | 0.8189 | 2 | $17.16 |
| **claude_fewshot_cot** | **0.7994** | 0.7306 | 0.8681 | 0 | $40.56 |
| gpt55_zeroshot | 0.7465 | 0.7110 | 0.7819 | 408 (22.4%) | $11.62 |

**总成本：$117.08**

核心发现：最佳 LLM 配置（Claude few-shot-cot, 0.799）仍比 structural GB cross-agent（0.967）低 16.8pp。LLM judge 天花板约 0.80，与 prompting 策略无关。无需恢复任何进程——实验已完成，registry 已更新为 DONE。

---
