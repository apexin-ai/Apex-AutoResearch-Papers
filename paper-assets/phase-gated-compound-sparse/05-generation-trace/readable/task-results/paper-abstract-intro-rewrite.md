# paper abstract intro rewrite

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract-intro-rewrite_20260516T034917_result.json`
- **Structured JSON:** [`7a8e4194e589cc9eb828.json`](../../sessions/7a/7a8e4194e589cc9eb828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。主要变更总结：

**Abstract:**
- "We present a systematic empirical investigation" → "We find that ... is not a fixed constant but an emergent property"
- 数字对齐 registry：DS 0.39→8.48 改为 0.32→9.94；QW 补全 0.048→2.619
- 15–17× 修正为 2.7–15×（含低 sparsity random NS 的情况）
- 新增 GSM8K 跨 benchmark + LLaMA 跨架构（含 strategy×phase 弱化限定）
- 结尾从 "actionable insights" 改为 "reveal ... challenging the assumption"
- 全文无 "novel"/"first"/"propose"，用 "find"/"identify"/"reveal"

**Introduction:**
- 删除 "What does compound interaction add" 独立段落和自我标签段（"This work is a systematic empirical investigation"）
- Finding 段明确 "three-way interaction among eviction strategy, reasoning phase, and sparsity level"
- 新增 GSM8K 交叉验证段落（DS 0.241→4.682; QW 0.039→2.092; specificity 衰减 15–36× → 2.3–3.8×）
- Contributions 从 3 条扩为 4 条：(1) phase-modulated gradient, (2) cross-model/architecture, (3) discrimination collapse, (4) GSM8K validation
- LLaMA 加限定：consistent direction, weaker strategy×phase contrast
- 引用新增 HIES `\cite{hies-2025}` 替换 `\cite{retentivekv-2026}` 在 gap 段

---
