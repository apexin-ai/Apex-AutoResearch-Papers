# paper consistency audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency_audit_20260514T094456_result.json`
- **Structured JSON:** [`6e1cdc401a8cf86b06ed.json`](../../sessions/6e/6e1cdc401a8cf86b06ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/consistency_audit_report.md`。

**结论: FAIL — 3 个 CRITICAL 问题需修复。**

关键发现：

1. **introduction.tex** 有 3 处 `\ref{sec:experiments}` 引用了不存在的 label（应为 `sec:results`），编译会出 "??"
2. **discussion.tex:86** 把 Table cohens-d 的 CI 值 ([0.20→8.39], [8.39, 16.65]) 标注为 "permutation CIs" 并引用了 Table permutation，实际 permutation CI 是 [0.19→6.70], [6.70, 16.29]
3. **paper_framing.md** 的 Cohen's d 用的是 pooled d（0.61→1.13），论文全文用的是 d_z（0.44→0.80）——论文内部一致，但与 paper_framing 不一致

另有 3 个 WARNING（重复 equation label、Qwen Δ 精度舍入、s=0.35 无来源数据）和 4 个 stale 文件待归档。数字一致性、claim 表述、引用完整性均通过。

---
