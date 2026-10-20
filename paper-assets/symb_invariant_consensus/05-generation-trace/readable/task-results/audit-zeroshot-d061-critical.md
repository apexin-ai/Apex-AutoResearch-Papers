# audit zeroshot d061 critical

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_zeroshot-d061-critical_20260522T194703_result.json`
- **Structured JSON:** [`879c552ca07d1a5b1258.json`](../../sessions/87/879c552ca07d1a5b1258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Let me now produce the final audit report.

---

## 审计结果

### Q1: Zero-shot combo 原始 eval 的 SC baseline

**结论：LLaMA SC 用的是旧 tiebreaking（70.00%），不是 D061（72.50%）。**

来源分析：
- `nli_recompute_exp091_exp092.json` 声称做了"D061 canonical tiebreaking recompute"，但只改了 **combo** tiebreaking，**没有重算 SC baseline**。SC 仍是 traces 中预计算的 `sc_answer` = 70.00%。
- `eval_finetuned_nli.py`（FT combo 脚本）用 `sc_answer()` 函数从 votes 重算 SC → D061 → 72.50%，这才是正确的。
- `exp092_llama8b_pw_nli_combo.py`（zero-shot combo 脚本）直接取 `r["sc_answer"]`（旧 tiebreaking）→ 70.00%。

Appendix Table (`tab:cross_generator_nli`) 当前状态不一致：
| Generator | 论文 SC | D061 SC | 用的是？|
|-----------|---------|---------|---------|
| Mistral-7B | 39.33% | 39.17%/39.33% | r11 canonical（D061 ✓，但数据源不同）|
| LLaMA-8B | **70.00%** | **72.50%** | **旧 tiebreaking ✗** |
| Qwen2.5-14B | **73.50%** | **74.00%** | **旧 tiebreaking ✗** |
| Qwen3-14B | 85.83% | 85.83% | D061 ✓ |

---

### Q2: Zero-shot DeBERTa combo D061 重跑结果

已用 D061（SC + combo 均 alphabetical sorted tiebreaking）重算全部 4 个 generator。结果（DeBERTa-large-mnli standalone = 55.00%）：

**LLaMA-3.1-8B × PW (D061):**
| w | Combo | Δ | p | sig |
|---|-------|---|---|-----|
| 1 | 73.33% | **+0.83pp** | 0.359 | n.s. |
| 3 | 73.33% | **+0.83pp** | 0.665 | n.s. |
| 5 | 72.00% | **-0.50pp** | 0.871 | n.s. |

旧值比对：SC 70→72.50%，combo w=1 Δ 从 +3.33pp (p=0.001) **降到 +0.83pp (p=0.359)**。

**Mistral-7B × PW (D061, votes file, N=600 含 2 缺失 PID):**
| w | Combo | Δ | p | sig |
|---|-------|---|---|-----|
| 1 | 40.33% | +1.17pp | 0.189 | n.s. |
| 3 | 46.17% | +7.00pp | 5e-6 | *** |
| 5 | 50.33% | +11.17pp | <1e-6 | *** |

**Qwen2.5-14B × PW (D061):**
| w | Combo | Δ | p | sig |
|---|-------|---|---|-----|
| 1 | 74.17% | +0.17pp | 1.000 | n.s. |
| 3 | 74.67% | +0.67pp | 0.503 | n.s. |
| 5 | 75.17% | +1.17pp | 0.360 | n.s. |

---

### Q3: Table 1 SC 39.33% vs combo SC 39.17% 差异原因

**根因：PID 不匹配（2 个问题）。**

- `mistral_pw600_sc_votes.json` 有 600 条，但其中 2 个 PID 是 Q4 变体（`_Q4`），而 `proofwriter_full.json` 对应的是 Q8 变体（`_Q8`）。
- `eval_finetuned_nli.py` 按 `proofwriter_full.json` 遍历 → 2 个 PID 查不到 votes → 算 wrong → SC = 235/600 = 39.17%
- `r11_3verifier_canonical.json` 有独立的 `sc_answer` 覆盖全部 600 PID → 其中 1 个额外正确 → SC = 236/600 = 39.33%
- 差异 = 1 个问题，来源是 `ProofWriter_AttNeg-OWA-D5-1176_Q8` 在 r11 中有正确的 SC answer (False=gold)，但在 votes file 中对应的 `_Q4` PID 找不到。

---

### 影响评估

**CRITICAL — 必须更新的数字：**

1. **Body text (solutions.tex L9)**：  
   "LLaMA-8B gains +3.33pp at w=3 (n.s.) but reaches significance at w=1 (p=0.001)"  
   → 改为：LLaMA-8B gains ≤+0.83pp (n.s. at all w)

2. **Body text (solutions.tex L12)**：  
   "LLaMA-8B (SC 70.00%, above the verifier) gains +3.33pp at w=3 (significant at w=1, p=0.001)"  
   → SC=72.50%, combo Δ=+0.83pp (n.s.)

3. **Table `tab:cross_generator_nli` (solutions.tex L24)**：  
   LLaMA: SC 70.00% → 72.50%, Gap -15.00 → -17.50, Δ(w=3) +3.33pp → +0.83pp, p .052 → .665

4. **Table `tab:cross_generator_nli` (solutions.tex L25)**：  
   Qwen2.5-14B: SC 73.50% → 74.00%, Gap -18.50 → -19.00, Δ(w=3) +1.17pp → +0.67pp

5. **Appendix Table lines 970-978**：全部 LLaMA 和 Qwen2.5-14B 行需要更新 SC、combo Δ、p 值、BH 校正

6. **FT combo paragraph (solutions.tex L32)**：  
   "~3.5× the zero-shot result" → 比率需要重算（FT LLaMA Δ=+11.67pp vs ZS LLaMA Δ=+0.83pp → 实际是 14×，不是 3.5×）

**MODERATE — Narrative 影响：**

- "Capability gap hypothesis" 核心故事仍然成立（Mistral 显著获益，强模型无获益），但 **LLaMA 不再是 bridge case**。LLaMA 的 significance at w=1 是核心论点之一（"above the verifier but still gains"），D061 后完全不显著。
- Spearman ρ=1.0 排序不变（Mistral > LLaMA > Qwen14b > Qwen3），但 LLaMA 和 Qwen14b 的 Δ 都非常小且不显著。
- FT combo 数据（`deberta_ft_combo_all.json`）已经用 D061，**无需修改**。

**NOT affected：**
- FT DeBERTa combo (Table `tab:finetuned-nli`): 已用 D061 ✓
- Mistral zero-shot combo: r11 canonical 已用 D061 ✓（但 SC=39.33% vs 39.17% 的 PID 对齐问题需决定用哪个值）
- Qwen3-14B: 已用 D061 ✓

---
