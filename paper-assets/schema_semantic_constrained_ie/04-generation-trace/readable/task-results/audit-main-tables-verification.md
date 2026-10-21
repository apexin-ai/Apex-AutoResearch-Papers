# audit main tables verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_main-tables-verification_20260523T102235_result.json`
- **Structured JSON:** [`cf3b7af83e3be954beb8.json`](../../sessions/cf/cf3b7af83e3be954beb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here is the complete audit report.

---

## Table 1 审计报告 (`tab:scierc-ablation`)
**SciERC 551 docs, Qwen3-8B, zero-shot**

Registry metrics use decimal (e.g., 0.1537 = 15.37%); vLLM experiment uses percent directly.

### Row: Unconstrained — `phase2_scierc_unconstrained`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 15.37 | 0.1537 → 15.37% | ✅ |
| ΔDR | --- | --- | ✅ |
| RV | 1.39 | 0.0139 → 1.39% | ✅ |
| ET | 0.40 | 0.004 → 0.40% | ✅ |
| CF | 0.08 | 0.0008 → 0.08% | ✅ |
| Tot. | 15.45 | 15.37+0.08=15.45 | ✅ |
| Rel. F1 | 8.23 | 0.0823 → 8.23% | ✅ |
| Ent. F1 | 31.01 | 0.3101 → 31.01% | ✅ |

### Row: Grammar — `phase2_scierc_grammar_only`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 14.84 | 0.1484 → 14.84% | ✅ |
| ΔDR | ↓3% | (15.37-14.84)/15.37=3.4%≈3% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 0.08 | 0.0008 → 0.08% | ✅ |
| Tot. | 14.92 | 14.84+0.08=14.92 | ✅ |
| Rel. F1 | 8.23 | 0.0823 → 8.23% | ✅ |
| Ent. F1 | 30.98 | 0.3098 → 30.98% | ✅ |

### Row: GCD-equiv.† — `vllm_guided_json_scierc_zs`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 15.26 | 15.26% | ✅ |
| ΔDR | ↓1% | (15.37-15.26)/15.37=0.7%≈1% | ✅ |
| RV | 0 | 0% | ✅ |
| ET | 0 | 0% | ✅ |
| CF | 0.04 | 0.04% | ✅ |
| Tot. | 15.30 | 15.26+0.04=15.30 | ✅ |
| Rel. F1 | 8.75 | 8.75% | ✅ |
| Ent. F1 | 30.91 | 30.91% | ✅ |

### Row: Semantic — `phase2_scierc_semantic_only`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 11.65 | 0.1165 → 11.65% | ✅ |
| ΔDR | ↓24% | (15.37-11.65)/15.37=24.2%≈24% | ✅ |
| RV | 1.51 | 0.0151 → 1.51% | ✅ |
| ET | 0.40 | 0.004 → 0.40% | ✅ |
| CF | 2.71 | 0.0271 → 2.71% | ✅ |
| Tot. | 14.36 | 11.65+2.71=14.36 | ✅ |
| Rel. F1 | 8.15 | 0.0815 → 8.15% | ✅ |
| Ent. F1 | 31.01 | 0.3101 → 31.01% | ✅ |

### Row: S1 — `phase2_scierc_full_s1`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 0.93 | 0.0093 → 0.93% | ✅ |
| ΔDR | ↓94% | (15.37-0.93)/15.37=93.9%≈94% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 9.90 | 0.099 → 9.90% | ✅ |
| Tot. | 10.83 | 0.93+9.90=10.83 | ✅ |
| Rel. F1 | 8.36 | 0.0836 → 8.36% | ✅ |
| Ent. F1 | 30.98 | 0.3098 → 30.98% | ✅ |

### Row: S2 — `phase2_scierc_full_s2`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 0.97 | 0.0097 → 0.97% | ✅ |
| ΔDR | ↓94% | (15.37-0.97)/15.37=93.7%≈94% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 8.03 | 0.0803 → 8.03% | ✅ |
| Tot. | 9.00 | 0.97+8.03=9.00 | ✅ |
| Rel. F1 | 8.03 | 0.0803 → 8.03% | ✅ |
| Ent. F1 | 31.90 | 0.319 → 31.90% | ✅ |

**Table 1 结论: 48/48 cells 全部通过 ✅**

---

## Table 2 审计报告 (`tab:composability`)
**Fine-tuning composability: LoRA × unconstrained vs. S1**

### Qwen3-8B × SciERC — `w5_lora_scierc_*_eval`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| Unconstr. DR | 1.95 | 0.0195 → 1.95% | ✅ |
| Unconstr. CF | 0 | 0 | ✅ |
| Unconstr. R-F1 | 43.86 | 0.4386 → 43.86% | ✅ |
| Unconstr. E-F1 | 67.05 | 0.6705 → 67.05% | ✅ |
| S1 DR | **0** | 0 | ✅ |
| S1 CF | 1.18 | 0.0118 → 1.18% | ✅ |
| S1 R-F1 | 43.77 | 0.4377 → 43.77% | ✅ |
| S1 E-F1 | 67.05 | 0.6705 → 67.05% | ✅ |
| S1 ΔDR | ↓100% | (1.95→0)/1.95=100% | ✅ |

**Qwen SciERC: 9/9 ✅**

### Llama 3.1-8B × SciERC — `w5_llama_lora_scierc_*_eval`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| Unconstr. DR | 1.11 | 0.0111 → 1.11% | ✅ |
| Unconstr. CF | 0 | 0 | ✅ |
| Unconstr. R-F1 | 45.45 | 0.4545 → 45.45% | ✅ |
| Unconstr. E-F1 | 67.76 | 0.6776 → 67.76% | ✅ |
| S1 DR | 0.09 | 0.0009 → 0.09% | ✅ |
| S1 CF | 0.46 | 0.0046 → 0.46% | ✅ |
| S1 R-F1 | 45.47 | 0.4547 → 45.47% | ✅ |
| S1 E-F1 | 67.76 | 0.6776 → 67.76% | ✅ |
| S1 ΔDR | ↓92% | (1.11-0.09)/1.11=91.9%≈92% | ✅ |

**Llama SciERC: 9/9 ✅**

### Qwen3-8B × DocRED — `w5_qwen_docred_lora_*_eval`

| Cell | Paper | Registry (corrected) | Verified |
|------|-------|---------------------|----------|
| Unconstr. DR | 0.56 | DR_pct=**0.76** | ❌ (diff=0.20) |
| Unconstr. CF | 0.08 | CF_pct=**0.12** | ❌ (diff=0.04) |
| Unconstr. R-F1 | 40.89 | R_F1=**40.86** | ❌ (diff=0.03) |
| Unconstr. E-F1 | 82.35 | E_F1=**82.15** | ❌ (diff=0.20) |
| S1 DR | 0.00 | DR_pct=**0.01** | ❌ (diff=0.01) |
| S1 CF | 0.22 | CF_pct=**0.41** | ❌ (diff=0.19) |
| S1 R-F1 | 40.79 | R_F1=**40.56** | ❌ (diff=0.23) |
| S1 E-F1 | 81.87 | E_F1=**81.43** | ❌ (diff=0.44) |
| S1 ΔDR | ↓100% | (0.76→0.01)=**↓98.7%** | ❌ |

**Qwen DocRED: 0/9 — 全部不一致 ❌**

### Llama 3.1-8B × DocRED — `w5_llama_docred_lora_*_eval`

| Cell | Paper | Registry (corrected) | Verified |
|------|-------|---------------------|----------|
| Unconstr. DR | 0.49 | DR_pct=**0.49** | ✅ |
| Unconstr. CF | 0.08 | **无 CF 字段** | ⚠️ 无法核实 |
| Unconstr. R-F1 | 44.55 | R_F1=**43.72** | ❌ (diff=0.83) |
| Unconstr. E-F1 | 84.77 | E_F1=**83.93** | ❌ (diff=0.84) |
| S1 DR | 0.00 | dr_violation_rate=**0.21** | ❌ (diff=0.21) |
| S1 CF | 0.26 | CF_pct=**0.21** | ❌ (diff=0.05) |
| S1 R-F1 | 44.70 | relation_f1_all_set=**43.78** | ❌ (diff=0.92) |
| S1 E-F1 | 84.71 | entity_f1=**83.94** | ❌ (diff=0.77) |
| S1 ΔDR | ↓100% | (0.49→0.21)=**↓57%** | ❌ |

**Llama DocRED: 1/9 通过, 1 无法核实, 7 不一致 ❌**

---

## 根因分析

Registry 有多条修正记录表明 `violation_checker.py` 和 `unified_f1_eval.py` 存在 **parse-failure bug**，已于 2026-05-20/22 用 `eval_d064.py` 修正：

- `w8_qwen_docred_ft_semantic_only`: "Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug)"
- `w5_llama_docred_lora_constrained_eval`: "P/R corrected 2026-05-20 per Director"
- `r16_trie_*_ft_scierc`: "CORRECTED: violation_checker.py parse-failure bug fixed. Old R-F1 was inflated (gold dropped for parse failures)"

**论文 Table 2 的 DocRED 四行使用了修正前的旧值**。SciERC 行不受影响（parse fail rate = 0%）。

## 不一致汇总

| 位置 | 论文值 | 正确值 (registry) | 严重程度 |
|------|--------|-------------------|----------|
| Qwen DocRED Unc. DR | 0.56 | **0.76** | 高 |
| Qwen DocRED Unc. CF | 0.08 | **0.12** | 中 |
| Qwen DocRED Unc. R-F1 | 40.89 | **40.86** | 低 |
| Qwen DocRED Unc. E-F1 | 82.35 | **82.15** | 中 |
| Qwen DocRED S1 DR | 0.00 | **0.01** | 低 |
| Qwen DocRED S1 CF | 0.22 | **0.41** | 高 |
| Qwen DocRED S1 R-F1 | 40.79 | **40.56** | 中 |
| Qwen DocRED S1 E-F1 | 81.87 | **81.43** | 中 |
| Qwen DocRED S1 ΔDR | ↓100% | **↓98.7%** | 中 |
| Llama DocRED Unc. R-F1 | 44.55 | **43.72** | 高 |
| Llama DocRED Unc. E-F1 | 84.77 | **83.93** | 高 |
| Llama DocRED S1 DR | 0.00 | **0.21** | 高 |
| Llama DocRED S1 CF | 0.26 | **0.21** | 低 |
| Llama DocRED S1 R-F1 | 44.70 | **43.78** | 高 |
| Llama DocRED S1 E-F1 | 84.71 | **83.94** | 高 |
| Llama DocRED S1 ΔDR | ↓100% | **↓57%** | 极高 |
| Llama DocRED Unc. CF | 0.08 | **缺失** | ⚠️ |

最严重问题：Llama DocRED S1 ΔDR 从 ↓100% 降为 ↓57%，且 DR 从 0.00 变为 0.21%。这会影响论文 "fine-tuning practically eliminates DR" 的核心结论强度。

Table 2 的 DocRED 四行全部需要用 `eval_d064.py` 的修正值重写。同时需检查正文中引用这些数字的段落（至少 `\paragraph{Composability with fine-tuning.}` 中的 "DR≤0.09%" 等表述）。

---
