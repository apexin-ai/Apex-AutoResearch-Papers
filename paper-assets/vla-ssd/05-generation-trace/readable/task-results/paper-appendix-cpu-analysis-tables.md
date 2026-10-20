# paper appendix cpu analysis tables

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_cpu_analysis_tables_20260518T182523_result.json`
- **Structured JSON:** [`b98b4959402c0a1ab81c.json`](../../sessions/b9/b98b4959402c0a1ab81c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**添加的 3 个表格（appendix.tex L591-668）：**

| 表格 | 标签 | 内容 |
|---|---|---|
| Table: Attention Decomp | `tab:attention_decomp` | L1 注意力分解：instr-dom 24h (62.4% instr) vs control 8h (44.9% instr)，Δ=+17.5pp |
| Table: Per-Dim MAE | `tab:per_dim_mae` | 7 维 MAE 对比：translation dims 3-5× ratio，rotation 1.9-2.6×，gripper 2.07× |
| Table: Per-Task R² | `tab:per_task_r2` | 10 tasks 全部 Δ>0，range +0.007 ~ +0.235，mean Δ=+0.107 |

**主文引用（experiments.tex）：**
- L68: `Table~\ref{tab:per_task_r2}` — ablation paragraph
- L71: `Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}` — trajectory paragraph

编译通过，0 errors，0 undefined references。

---
