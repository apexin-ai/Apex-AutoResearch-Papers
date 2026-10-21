# paper fig update auroc

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig_update_auroc_20260515T222003_result.json`
- **Structured JSON:** [`2f5b4ff9284e3988d966.json`](../../sessions/2f/2f5b4ff9284e3988d966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**fig3** (`fig3_nve_diagnostic_d054.py`): 已经是 D054 最新数据，无需修改。AUROC=0.933, 7/8 accuracy, CI [0.47, 1.0], 008e_v3_s2 标为 FP (IRD)。PDF/PNG 已重新渲染。

**fig6** (`fig6_multiple_pathways.py`): 更新了 3 处：
1. 列标题添加 NVE 值 — Pathway A: `NVE = 4.13`, Pathway B: `NVE = 3.78 (FP — IRD)`
2. Pathway B value panel 标注从 "no explosion" 改为 "IRD, not CIVO"
3. 底部共享注释添加 D054 诊断摘要: `AUROC = 0.933, 7/8 accuracy, CI [0.47, 1.0]`

所有 PDF/PNG 已本地渲染，输出到 `figures/paper/` 和 `_project/chart/` 两个目录。

---
