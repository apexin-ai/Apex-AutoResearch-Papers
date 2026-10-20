# prep paper update plan

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_paper_update_plan_20260514T220436_result.json`
- **Structured JSON:** [`8a06453f2e3a2a32515f.json`](../../sessions/8a/8a06453f2e3a2a32515f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计划已写入并注册。核心内容：

**覆盖范围**: §1-§8 + Abstract + Appendix，共识别 ~77 处数值替换、10 处 D059 违规修复、4 张图重绘、8 张表更新。

**关键决策点**:
- **Qwen s015 CI**: 若排除零→onset 改为 `s ≥ 0.15`；若仍跨零→保持 `s ≥ 0.20` + 触发 5 处 caveat
- **C8**: 仅 results.tex:79 一处需从 `replicates` 改为 `is directionally consistent`；LLaMA/DS 倍数需用 n=500 DS Δ 重算
- **C5b**: discussion.tex 和 conclusion.tex 均过于乐观（未提 pilot 失败），需插入 oracle 18% < 30% gate 结果 + heuristic > oracle 悖论
- **Table 3 重构**: imp-vs-rand d_z 列违反 D059，需改为 within-imp d_z 或 Wilcoxon p + median_diff

本计划与已有 `n500_paper_patch_plan.md`（逐行替换清单）互补使用。

---
