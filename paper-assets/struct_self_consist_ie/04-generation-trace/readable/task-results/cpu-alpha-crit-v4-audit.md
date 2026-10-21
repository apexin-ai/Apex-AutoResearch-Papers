# cpu alpha crit v4 audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_alpha_crit_v4_audit_20260521T132225_result.json`
- **Structured JSON:** [`85b803c5211e048d240e.json`](../../sessions/85/85b803c5211e048d240e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. α_crit 计算公式

| | 公式 | 来源 |
|---|---|---|
| **脚本** | `π_MV / (2 − π_MV)` 其中 π_MV = mv_f1 | 旧版推导残留，**错误** |
| **论文 Proposition 1** | `F₁^gr / 2` | theory.tex:36, appendix.tex:1121 |
| **论文 LaTeX 表** | `F₁^gr / 2` | appendix.tex:1145-1147，**正确** |

### 2. 论文 Proposition 1 定义
`Δ F₁ > 0` 当且仅当 `π_{M⁺} > α_crit ≜ F₁^gr/2`，其中 π_{M⁺} 是 MV 新增实体的 precision。

### 3. 修正后的 α_crit 值

| Dataset | greedy_f1 | 正确 α_crit (F₁^gr/2) | 旧值 (错误) |
|---------|-----------|----------------------|------------|
| FewNERD | 0.7912 | **0.396** | 0.618 |
| CoNLL | 0.9123 | **0.456** | 0.835 |
| SciERC | 0.6670 | **0.334** | 0.492 |

v4 markdown 表已修正并注册 (`art_20260521_ff5191`)。**论文 LaTeX 无需修改，本身就是正确的。**

### 4. CoNLL s42 数据来源
- 文件在 `autodl-5090-c` 上的 `conll_mf4v2_seed42/samples.jsonl`
- `autodl-5090` 上无此文件（仅有 seed123/456，今天新生成）
- `review_round9_experiments/freeform_conll/seed_42/` 是 freeform 实验数据，非 MF4v2

### 5. v3 vs v4 CoNLL s42 差异根因
**数据重新生成**，不是计算方法差异。证据：
- greedy_f1 变化 +0.48pp、degen 变化 −5.6pp，这些指标不受 MV 阈值影响
- v4 表自注："conll_mf4v2_seed42 data was regenerated since v3"
- 论文 LaTeX 表已规避：CoNLL 标 Seeds=2，仅用 v3 的 seed123+456（在 bjb2-11496 上，未重新生成）

**脚本 `recompute_alpha_crit_unified.py` 中的 `acrit()` 函数仍需修正**（改为 `greedy_f1 / 2`），但不影响论文 — 论文 LaTeX 表中的值是手动对齐到 Proposition 1 的。

---
