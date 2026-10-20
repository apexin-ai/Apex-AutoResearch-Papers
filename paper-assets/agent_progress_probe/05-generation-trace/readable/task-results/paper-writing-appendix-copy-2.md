# paper writing appendix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_appendix_20260514T235001_result.json`
- **Structured JSON:** [`ae292b5835d0482fbe48.json`](../../sessions/ae/ae292b5835d0482fbe48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Appendix 写入完成。4 个表格：

- **Table A.1** (`tab:encoder_ablation`): 3 个 encoder 对比，BGE-M3 最优但差距仅 0.5pp
- **Table A.2** (`tab:window_ablation`): k=3/5/7 窗口消融，k=5 最优
- **Table A.3** (`tab:multiseed`): 5-seed 稳定性，structural 零方差，probe σ=0.011
- **Table A.4** (`tab:cross_agent_cmdrep`): 双面板 subtable——(a) probe ZS/FT, (b) structural ZS，展示移除 cmd_rep 对两种范式的相反效果

已修复原 `tab:encoder_ablation_full` → `tab:encoder_ablation` 的断引用（experiments.tex line 105 引用的是 `tab:encoder_ablation`）。`\appendix` 由 main.tex line 44 声明，appendix.tex 不重复。

---
