# paper claim3 revision

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_claim3_revision_20260514T210100_result.json`
- **Structured JSON:** [`2698dc09ec8a038950f1.json`](../../sessions/26/2698dc09ec8a038950f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，appendix.tex 无需改动（float32 validation 已存在于 lines 29-30）。汇总：

### 改动清单

**analysis.tex** (4 处)
1. **§5.1 开头**（L11-12）：插入机制洞察——"MCKP benefit requires *spread heterogeneity*—multiple heads with cross-bitwidth sensitivity gradients"，置于 Qwen 数据之前
2. **§5.1 Yi-1.5 段**（L17-22）：以 "critical counterexample" 开头，强调 "mechanism is clear from cross-bitwidth gradient structure"，"only one lever" 替代 "no gradient to exploit"
3. **§5.2 诊断条目**（L70-72）：显式阈值——Spread: `concentration ≳ 0.50, t₁/t₅ ≲ 0.70`；Spike: `t₁/t₅ ≳ 0.70, any concentration`；Flat: `concentration ≲ 0.50, low t₁/t₅`；Mistral/Gemma-2 加上浓度数值
4. **§5.2 阈值声明**（L76-77）：联合条件 "correctly separates the beneficial case from the four non-beneficial cases across all five architectures studied"，两个阈值均标注 illustrative

**abstract.tex**（L8）："can indicate" → "correctly identifies all five architectures studied"，加入 t₁/t₅ ratio 和 spike/flat 术语

**introduction.tex**（L53 Claim 3）："to indicate" → "correctly separates"，加 Yi-1.5 as critical test 说明

**conclusion.tex**（L9-10）：加显式阈值 (≳ 0.50, ≲ 0.70)，拆为两句，新增 practical guideline 表述

**appendix.tex**：无改动（float32 validation 已在 ¶Numerical precision）

---
