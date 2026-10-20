# cpu paper n500 audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_paper-n500-audit_20260515T005319_result.json`
- **Structured JSON:** [`9cc8f65b80ef872fb890.json`](../../sessions/9c/9cc8f65b80ef872fb890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/paper_n500_update_checklist.md`。

要点：
- **~120+ 处**需要数值更新，分布在 11 个 .tex 文件中
- 其中 ~30 处已用 `\placeholder{}` 标记，~90 处是硬编码的 n=50 数值
- **4 张图**需用 n=500 数据重新生成（fig1/3/4/5）
- 最密集的文件是 `results.tex`（~40 处）和 `appendix_moved.tex`（~25 处）
- 还有 ~6 处**条件性更新**，取决于 n=500 结果是否改变了定性结论（如 Qwen s=0.15 是否不再 marginal、random 7/8 是否变为 8/8）

---
