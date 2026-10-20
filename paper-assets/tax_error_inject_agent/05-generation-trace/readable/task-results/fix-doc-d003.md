# fix doc d003

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_doc-d003_20260514T103713_result.json`
- **Structured JSON:** [`ab051db3ae240d30f6dc.json`](../../sessions/ab/ab051db3ae240d30f6dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 处修改：

| # | 位置 | 原文 | 替换为 |
|---|------|------|--------|
| 1 | 比较表 Recovery Signal 列 | `Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback` | `Recovery conditioned on corrupted history and original observation; recovery generated from the corrupted trajectory context` |
| 2 | §3 小节标题 | `Environment-Grounded Recovery with Structured Training Signal` | `History-Conditioned Recovery with Structured Training Signal` |
| 3 | §3 正文 pipeline 描述 | `execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback` | `construct corrupted trajectory context from the injection point, (3) generate recovery actions conditioned on the corrupted history and original observation` |
| 4 | §3 正文总结句 | `it reflects how an agent should actually recover given the true environmental state after corruption` | `it reflects how an agent should recover given the corrupted trajectory context and original observation` |

grep 验证：`environment.grounded` / `env.grounded` / `real environment feedback` / `true environmental state` 均已清零。备份保留在 `related_work_comparison.md.bak`。

---
