# paper consistency check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency_check_20260514T094613_result.json`
- **Structured JSON:** [`1cc458eb2260617e25d3.json`](../../sessions/1c/1cc458eb2260617e25d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/consistency_report.md`。

发现 **5 个关键问题**：

1. **introduction.tex Qwen Cohen's d 与 Table 3 矛盾** — intro 用 d=0.37/≥0.72，Table 3 用 d=0.28/0.55，两套数值来源不同
2. **全部 Cohen's d 与 task-spec 基准值不符** — 论文用 DS 0.44→0.80 / QW 0.28→1.02，基准为 DS 0.61→1.13 / QW 0.37→1.44，需确认哪套计算正确
3. **`\ref{sec:experiments}` 未定义** — intro 引用 3 次，实际 label 是 `sec:results`，编译产生 ??
4. **`eq:ii` 和 `eq:gradient` 重复定义** — background.tex 和 methodology.tex 各定义一次
5. **methodology.tex 称 "p < 0.0001"** — 但 s=0.15 的 Bonferroni p=0.0032

另有 3 个中等问题（正文用 unpaired 而非 paired median_diff、discussion 自引用、两张 figure 未被 \ref）。其余 14 项数字检查全部一致。

---
