# research d145 fol datasets

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d145-fol-datasets_20260519T131524_result.json`
- **Structured JSON:** [`13b81c5aeb2270704e32.json`](../../sessions/13/13b81c5aeb2270704e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是汇总报告。

---

## 自带 FOL 标注的逻辑推理数据集调研

### 必查候选

| 数据集 | 大小 | FOL 标注 | 兼容性 | 备注 |
|--------|------|----------|--------|------|
| **FOLIO** (tasksource/folio) | 1,203 | `premises-FOL` + `conclusion-FOL` | **5/5** | 已在用，人工标注，质量最高 |
| **ProofFOL** | 10,424 | `Premise_FOL` + `Conclusion_FOL`，**原生 Prover9 语法** | **5/5** | GPT-4o 翻译 ProofWriter depth-5 + Prover9 验证，~70% 保留率。最佳新发现 |
| **ProntoQA** (renma/ProntoQA) | 500 | `raw_logic_programs` 自定义 DSL | **4/5** | 仅一元谓词，转 Prover9 ~20 行 regex。逻辑片段太窄 |
| **FLD v2 / FLDx2** | 40K / 110K | `hypothesis_formula` + `context_formula` + `proofs_formula` | **4/5** | 匿名谓词 `{A}x`，需 regex 重写为 Prover9 语法。规模最大 |
| **ProverQA** | 6,500 | NL-to-FOL 映射 + 结论 FOL，Prover9 生成验证 | **4/5** | Unicode 符号 (∀∃→∧∨) 替换为 ASCII 即可 |
| **LogicNLI** | 20,000 | 无，纯 NL 模板 | **2/5** | 模板规律可 regex 解析 ~95%，但工程量 2-3 天 |
| **LogicBench** | ~2,000 | 无 | **1/5** | 纯 NL，需完整语义解析 |
| **FLD** 见上 | — | — | — | — |
| **RuleTaker/ProofWriter** 原版 | ~59K | 无原生 FOL，但生成器有双向映射 | 见 ProofFOL | 用 ProofFOL 即可 |

### 额外发现

| 数据集 | 大小 | FOL 标注 | 兼容性 | 备注 |
|--------|------|----------|--------|------|
| **FOL-nli** | 102,774 | TPTP 格式 FOL (premise + hypothesis) | **3/5** | TPTP→Prover9 系统转换，规模大 |
| **MALLS** | 34,000 | 标准 FOL (Unicode) | **3/5** | `∀x(P(x)→Q(x))` 需 Unicode→ASCII |
| **text2log** | 100,000 | Lambda DCS via ccg2lambda | **3/5** | 需清理前缀下划线和量词语法 |

### 推荐

**首选：ProofFOL**（兼容性 5/5）
- 10K+ 条，原生 Prover9 语法，零转换成本
- 基于 ProofWriter（与我们 pipeline 同源），有 premise/conclusion/label 结构
- 来源：`github.com/RamyaKeerthy/Translation-NL2FOL`

**次选：FLD v2/FLDx2**（兼容性 4/5）
- 规模最大（40K-110K），含完整证明链的 FOL
- 谓词匿名化 (`{A}`, `{B}`)，需 ~50 行转换脚本
- 逻辑复杂度可控（depth 0-3, steps 1-8）

**备选：FOL-nli**（兼容性 3/5）
- 10 万条 TPTP 格式，覆盖面广
- TPTP 到 Prover9 有成熟工具链

**结论**：ProofFOL 是跨数据集验证的最优候选——与 FOLIO 互补（ProofWriter 域 vs WikiLogic 域），Prover9 直接兼容，无需任何格式转换。

---
