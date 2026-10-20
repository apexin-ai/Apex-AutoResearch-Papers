# research confirm 3 nli architectures

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_confirm-3-nli-architectures_20260522T135816_result.json`
- **Structured JSON:** [`5714d019c30f9a7b8c19.json`](../../sessions/57/5714d019c30f9a7b8c19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data located. Here's the complete answer:

---

## 三个 NLI 架构

1. **DeBERTa-large-MNLI** (microsoft/deberta-large-mnli, 406M)
2. **RoBERTa-large-MNLI** (37.67% standalone on PW)
3. **BART-large-MNLI** (46.17% standalone on PW)

## ProofWriter Mistral-7B combo 结果 (n=600, SC=39.33%)

| Verifier | Standalone | w=1 Δpp (p) | w=3 Δpp (p) | w=5 Δpp (p) |
|----------|-----------|-------------|-------------|-------------|
| DeBERTa-MNLI | 55.00% | +0.83 (n.s.) | **+6.67** (p<0.001) | **+11.00** (p<0.001) |
| RoBERTa-MNLI | 37.67% | -0.17 (n.s.) | **+4.17** (p=0.003) | **+4.33** (p=0.037) |
| BART-MNLI | 46.17% | +0.00 (n.s.) | **+5.17** (p<0.001) | **+6.33** (p=0.003) |

BH 校正后 (m=15): 10/15 条件显著，所有 w≥3 条件均通过。

## 论文中 claim 的原文

`solutions.tex:12` — "all three NLI architectures produce gains at w ≥ 3"

## 数据位置

- **主表 (Table 3)**: `solutions.tex` — cross-generator comparison，仅 DeBERTa × 4 generators，w=3
- **附录 Table 26** (`appendix.tex:888`, Appendix W): 3 verifiers × 3 weights 完整矩阵（上表数据）
- **附录 BH Table** (`appendix.tex:917`): 3 verifiers × 5 weights BH 校正
- **Artifact**: `artifacts/_project/data/nli_multi_verifier_recomputed.json`
- **Figure 7** (`appendix.tex:938`): capability gap scatter, 6 points across 3 architectures

## 数据来源实验

registry 中对应 `exp-wave3-dir-r-nli-verifier` (DeBERTa) 和 `exp-wave3-dir-r-combo-extended`。RoBERTa/BART 数据在 `nli_multi_verifier_recomputed.json` 中，经 alphabetical tiebreaking 重算。

**Claim 成立**: 三个 NLI 架构在 ProofWriter Mistral-7B 上 w≥3 均产生显著正增益（p<0.05），BH 校正后仍然成立。

---
