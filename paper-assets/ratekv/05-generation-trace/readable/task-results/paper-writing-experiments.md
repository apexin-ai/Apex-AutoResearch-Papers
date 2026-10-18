# paper writing experiments

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260514T090525_result.json`
- **Structured JSON:** [`23fc768be2561ad592ba.json`](../../sessions/23/23fc768be2561ad592ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`experiments.tex` 已写入，1173 words（含 LaTeX 标记），§4.1–4.5 完整覆盖。

核查清单：
- 所有数字严格来自提供数据，无编造
- Mistral 负向结果如实呈现（+0.4% worse than uniform, near-zero sensitivity differences）
- PPL 两位小数，accuracy 三位小数
- 无 "consistently outperforms"/"significantly"/"state-of-the-art" 等强度词
- Llama/Mistral unconstrained 标 "---" 并解释原因
- 未提及 C4 cross-dataset
- Figure 3 引用完整
- 5 张表/图均有 `\label` 和自包含 caption

---
