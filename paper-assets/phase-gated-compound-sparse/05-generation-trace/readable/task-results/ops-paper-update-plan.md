# ops paper update plan

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_paper-update-plan_20260514T235803_result.json`
- **Structured JSON:** [`8cffc877cb2e652f9edd.json`](../../sessions/8c/8cffc877cb2e652f9edd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计划已写入 `artifacts/n500_paper_update_plan.md`。

汇总：
- **15 个 tex 文件**全部扫描，其中 **12 个**需要修改（background.tex、related_work.tex、main.tex 无需改动）
- **~150+ 个独立数值**需替换（含表格单元格）
- **30+ 个 `\placeholder{}`** 需填入
- **4 个图表 PDF** 需重新生成
- **"marginal at s=0.15"** 出现 4 处，全部需删除
- 2 组重复段落（appendix_results ↔ appendix_moved）需同步修改

---
