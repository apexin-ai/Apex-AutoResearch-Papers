# analysis exp 011 truncation bias

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-011-truncation-bias_20260517T083218_result.json`
- **Structured JSON:** [`2c99ec91392310170633.json`](../../sessions/2c/2c99ec91392310170633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Truncation bias 不成立。** 核心发现:

- "44 truncated traces" 是 44 条个体 trace（720 条中的 6.1%），影响 16/60 题
- 5 个 SICA 胜出的 discordant pairs 中，**4 个完全没有 truncation**
- 唯一有 truncation 的 discordant pair（problem 24）的 3 条截断 trace 均未提取出答案，对 SC 投票和 SICA 约束均无贡献
- Discordant pairs 截断率 (16.7%) 反而**低于** concordant pairs (27.8%)，Fisher exact test p=1.0
- 84.1% 的截断 trace 无法提取答案，对两种方法都不可见

**结论: +6.67pp 的 SICA 优势由无截断问题驱动，是真实信号，不是 truncation artifact。无需增大 max-tokens 重跑来验证。**

报告已注册: `art_20260517_8ac5e3`

---
