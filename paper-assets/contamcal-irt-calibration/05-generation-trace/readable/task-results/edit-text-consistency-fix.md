# edit text consistency fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_edit_text-consistency-fix_20260522T180639_result.json`
- **Structured JSON:** [`331abab1de4c7465810e.json`](../../sessions/33/331abab1de4c7465810e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改已完成：

| # | 位置 | 原文 | 修改后 | 依据 |
|---|------|------|--------|------|
| 1 | results.tex L29 | `N=6 families` | `N=6 models (five families)` | Table 1 有 6 个模型但仅 5 个独立 family（Qwen 算一个），与 L4 和 intro 的 "five independent families" 一致 |
| 2 | results.tex L32 | `3/5 families` | `5/6 families` | Appendix §B 明确写 "directionally consistent with MMLU for five of six models"；Falcon3 ARC +4.0pp 与 MMLU +4.2pp 方向一致；唯一例外是 Gemma-2 |
| 3 | introduction.tex L10 | `Falcon3 in Table~\ref{tab:taxonomy}` | `LLaMA-3.1 at seed$=$0 with d000/d025/d100` | 图表生成脚本确认 Falcon3 已绘入 Fig 1；同时 LLaMA-3.1 使用 seed=0（非 seed=42）且仅有 3 个 dosage 点，需在 caption 中注明 |

---
