# knowledge zs vs fs table template

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_zs-vs-fs-table-template_20260520T000637_result.json`
- **Structured JSON:** [`915139d4dc6211a1abf1.json`](../../sessions/91/915139d4dc6211a1abf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已创建。

**表格结构 (`tab:zs_vs_fs`)**：
- 6列：Dataset, Regime, Greedy F1, Oracle F1, LP ρ, Degen%, Construction Δ
- 3个数据集 × 2 regime = 6行，FewNERD FS 用 `\newcommand` 占位
- SciERC ZS construction 标 `$^{*}$` 表示 p<0.01

**核心 narrative（2段）**：

1. **Regime 不决定 construction 成败**：Few-shot 提升了 greedy F1（SciERC +6.2pp, CoNLL +3.3pp），但唯一 construction 显著的配置反而是 SciERC zero-shot（+1.53pp, p=0.008），对应 few-shot 为 -0.08pp n.s.。更好的 prompt 不等于更好的 self-consistency refinement。

2. **Dual-gating（degeneracy + LP alignment）**：Construction 成功需同时满足低 degeneracy 和有效 LP。SciERC ZS 两者皆满足→成功；SciERC FS degeneracy 更低(16.6%)但 LP 太弱(0.06)→失败；CoNLL FS LP 恢复(0.106)但 degen 饱和(70%)→失败。两个 gate 缺一不可。

---
