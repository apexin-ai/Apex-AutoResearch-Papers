# analysis llama weighted br

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-weighted-br_20260521T072708_result.json`
- **Structured JSON:** [`450ee6dd4fdf2ec0d730.json`](../../sessions/45/450ee6dd4fdf2ec0d730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**LLaMA weighted BR = 2.66x — 旧值是对的。** Mistral cross-check 也验证通过 (4.24x ✓)。

核心发现：raw BR=3.87 和 weighted BR=2.66 之间的大差距**不是因为 weighted BR 算错了**，而是因为两个数来自不同数据源：

| 指标 | 数据来源 | 轨迹数 | "错误"定义 | 错误数 | 值 |
|------|---------|--------|-----------|-------|-----|
| raw BR=3.87 | `llama_constraints_t0t3.json` | 4 traces | constraint-count majority ≠ gold | 86 | 3.87x |
| weighted BR=2.66 | `exp-063 results.json` | 12 traces (full SICA) | MaxSAT answer ≠ gold | 78 | 2.66x |

验证：用 4-trace 数据但采用 MaxSAT sica_answer 定义"错误"（78题），raw BR = 2.88x — 和 weighted BR 2.66x 的差距就很合理了（跟 Mistral 的 4.97 vs 4.24 比例一致）。

**给 Paper Agent 的建议**：如果表里要同时报 raw BR 和 weighted BR，两者必须用同一数据源。目前 raw 3.87 和 weighted 2.66 不可比。应该统一用 12-trace exp-063 的 sica_scores，报 weighted BR=2.66x [95% CI: 2.19, 3.28]。

---
