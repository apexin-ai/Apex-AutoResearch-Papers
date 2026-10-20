# audit paper placeholder map

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_placeholder_map_20260515T014315_result.json`
- **Structured JSON:** [`c135d3e4966d632b8657.json`](../../sessions/c1/c135d3e4966d632b8657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，文件已直接写入 `artifacts/paper_placeholder_audit.md`。

审计完成。核心发现：

**48 处 `\placeholder{}`**，分布在 8 个文件中，涉及 10 个唯一数据源：
- 24 处需 n=500 数据填入（QW rand Δ̃、NULL_PCT、Qwen effective-n 表等）
- 19 处是 LLaMA 数据（已有但从未填入正文）
- 4 处是 C5b pilot 实验数据（独立于 n=500）

**~118 处硬编码数值**需用 n=500 数据替换（6 个表格 ~110 cells + ~72 处内联统计）

**5 处间接 LLaMA 比率**需重算（DS/QW Δ̃ 变化导致 ~40×/~7× 比率失效）

**与已有清单的差异（4 处新发现）**：
1. **limitations.tex:2** 的 `$\sim$1/40 of DeepSeek` 比率声明被遗漏（清单 §10 只列了 abstract/results/discussion/conclusion）
2. **discussion.tex:10** 的 4 个 C5b placeholder（ORACLE_PCT/P, HEUR_PCT/P）清单 §11 标注"无需改"但实际需要填入数据
3. **appendix_moved.tex:16** fig3 caption 中的 `$5.3×$` 倍数被遗漏
4. **appendix_moved.tex:48/68** "one-fifth" 比率引用位置不完整

总替换位置 **~170+**。

---
