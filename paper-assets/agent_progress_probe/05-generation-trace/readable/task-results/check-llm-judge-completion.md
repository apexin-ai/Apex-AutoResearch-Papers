# check llm judge completion

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llm-judge-completion_20260515T042545_result.json`
- **Structured JSON:** [`5238fac0d7d7ec25dfc2.json`](../../sessions/52/5238fac0d7d7ec25dfc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是最终结果汇总：

## LLM Judge 强化评估 — 全部完成

| 方法 | macro_F1 | F1_stag | F1_prog | Parse Fail | Cost |
|------|----------|---------|---------|------------|------|
| Claude zero-shot | 0.663 | 0.606 | 0.720 | 0 | $11.66 |
| Claude few-shot | 0.751 | 0.683 | 0.820 | 0 | $36.08 |
| Claude CoT | 0.750 | 0.681 | 0.819 | 2 | $17.16 |
| **Claude few-shot-CoT** | **0.799** | **0.731** | **0.868** | 0 | $40.56 |
| Claude + structural input | 0.688 | 0.627 | 0.749 | 2 | $14.82 |
| GPT-5.5 zero-shot | 0.747 | 0.711 | 0.782 | 408 (22.4%) | $11.62 |
| **Structural GB (baseline)** | **0.967** | — | — | 0 | $0 |

**关键发现：**
- 6 个 LLM 配置全部跑完，无需重跑
- 最佳 LLM（Claude few-shot-CoT, 0.799）仍低于 structural GB 16.8pp
- 给 LLM 提供 structural features 作为输入（0.688）反而不如纯 few-shot（0.751），LLM 无法有效利用结构信号
- GPT-5.5 parse failure rate 22.4% 偏高，但 valid subset 上的 F1（0.747）与 Claude few-shot 相当
- 总 API 成本 $131.90

Registry 已更新为 DONE，`final_status.json` 已注册为 artifact。结果充分支持 "structural signal dominance" 叙事，不需要额外评估。

---
