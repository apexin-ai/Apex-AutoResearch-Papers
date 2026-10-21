# analyze eval humaneval sft rasp 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_humaneval_sft_rasp_20_2048_20260517T133712_result.json`
- **Structured JSON:** [`d765b0070795c7abf145.json`](../../sessions/d7/d765b0070795c7abf145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 W&B run ID。

## 结果

| 指标 | 值 |
|---|---|
| **pass@1** | **0.1037** |
| correct / total | 17 / 164 |
| stderr | ±0.0238 |
| wall_time | ~42 min 17s |
| W&B run ID | 无 |
| 异常 | 无（EXIT_CODE=0） |

**关键问题**：median_response_length = 2048（即中位数刚好触顶），大量样本仍被截断。很多错误是 thinking chain 泄漏到代码输出中（如 `"The function rolling_max takes..."` 直接作为 Python 被执行），以及 SyntaxError 占主导（括号未闭合、自然语言混入代码）。

**与 512-token 版本对比**：2048-token 版本 pass@1=0.1037 vs 512-token 版本 pass@1=0.0732，提升 41.7%（+5/164），但绝对值仍很低，主要瓶颈不在 token 长度截断，而是模型在 SFT 后倾向于输出 thinking/解释文本而非纯代码。

---
