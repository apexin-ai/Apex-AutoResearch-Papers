# paper reference bib audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_bib_audit_20260514T122828_result.json`
- **Structured JSON:** [`5a20a9f5a8cf38119cc7.json`](../../sessions/5a/5a20a9f5a8cf38119cc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，报告已直接写入产出目录。

审计结果：

- **30 条目 / 30 被引用 / 0 缺失 / 0 孤立**
- **0 条疑似虚构引用** — 全部 30 条通过 web search 验证真实
- **3 个格式问题：**
  1. `h2o2024` key 含 "2024" 但实际是 NeurIPS 2023 (year=2023)，建议改为 `h2o-neurips2023`
  2. Key 命名风格混用三种约定（`name-venue-year` / `name-year` / `authorYear`），建议统一
  3. `deepseek-r1` 的 title 用了 arXiv 版本，但 journal 字段标注为 Nature，应改用 Nature 发表标题

报告路径：`artifacts/reference_audit.md`

---
