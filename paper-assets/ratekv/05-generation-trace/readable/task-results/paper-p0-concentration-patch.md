# paper p0 concentration patch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p0-concentration-patch_20260514T221709_result.json`
- **Structured JSON:** [`9d9144d0886dd5584151.json`](../../sessions/9d/9d9144d0886dd5584151.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**核查结果**：
- `docs/paper/` 下所有 .tex 文件中 Qwen 的 top-5% concentration 值已全部为 **0.61**（共 6 处：`analysis.tex` ×4、`introduction.tex` ×1、`conclusion.tex` ×1）
- 旧值 `0.59--0.66` / `0.59-0.66` / `0.5856` / `0.5909` / `0.66` / `0.6156` / `0.6104` 已无残留
- 其他模型值未动：Yi=0.71、Llama=0.57、Mistral=0.22、Gemma-2=0.23
- 5-model table（`analysis.tex:40`）Qwen 行 concentration 列为 `0.61`，未标 float32/range
- 无 "bf16 range" 表述

**Commit**: `bfaea4e P0: unify Qwen concentration to 0.61 (float32 verified)` — 7 files changed (含 `related_work.tex` 引用更新一并提交)。

---
