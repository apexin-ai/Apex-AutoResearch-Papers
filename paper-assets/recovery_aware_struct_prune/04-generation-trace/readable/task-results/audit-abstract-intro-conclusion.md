# audit abstract intro conclusion

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_abstract_intro_conclusion_20260524T043209_result.json`
- **Structured JSON:** [`a2c8b0bdb74f53d150a3.json`](../../sessions/a2/a2c8b0bdb74f53d150a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data to compile the complete audit. Here's the full report:

---

## abstract.tex

| Line | Claim | Registry Source | Registry Value | Status |
|------|-------|----------------|----------------|--------|
| 5 | 20% sparsity | config parameter | — | ✅ |
| 5 | α=2.0 | config parameter | — | ✅ |
| 5 | 66.11% on GSM8K | eval_gsm8k_grpo_alpha2p0_20 | 872/1319 = 0.6611 | ✅ |
| 6 | 4.4× vs importance-only | grpo_cka_only_20 (0.354) / grpo_standard_20_fair (0.081) | 4.37× → rounds to 4.4× | ✅ |
| 7 | 1.5B scale | grpo_{cka_only,standard,rasp}_20_1p5b | experiments exist | ✅ |

---

## introduction.tex

| Line | Claim | Registry Source | Registry Value | Status |
|------|-------|----------------|----------------|--------|
| 7 | mean \|Δ\|=0.54 pp (4 criteria, 20%) | Table 2 values: \|0.48\|+\|0.55\|+\|0.61\|+\|0.53\| / 4 = 0.5425 | 0.54 pp | ⚠️ (see note 1) |
| 7 | max 0.61 pp | RASP α=1.0: \|803-811\|/1319 | 0.607 pp → 0.61 | ✅ |
| 7 | 1.34 pp (incl. MBPP) | MBPP CKA-only: \|0.1417-0.1283\| | 1.34 pp | ✅ |
| 17 | 66.11% at α=2.0 | eval_gsm8k_grpo_alpha2p0_20 | 872/1319 = 66.11% | ✅ |
| 17 | \|Δ\| ≤ 1.14 pp at every dose-response point | α=0.5: 0.45pp, α=2.0: 1.14pp, α=3.0: 0.68pp, α=4.0: 0.83pp | max 1.14 pp | ✅ |
| 22 | 66.11% GRPO on GSM8K | same as above | | ✅ |
| 23 | 4.4× Standard | same as abstract | 4.37× → 4.4× | ✅ |
| 24 | −1.36 pp (ShortGPT) | eval_gsm8k_{sft,grpo}_shortgpt_20: \|590-572\|/1319 | 1.365 pp → 1.36 | ✅ |
| 28 | 0.54 pp, 0.61 pp, 1.34 pp | repeated from line 7 | | ⚠️/✅/✅ |
| 28 | +1.51 pp at 15% | CKA-only 15% mean(GRPO−SFT) − Standard 15% mean(GRPO−SFT) = 0.58−(−0.93) | +1.51 pp | ✅ |
| 29 | α=2.0, 66.11% | repeated | | ✅ |

---

## conclusion.tex

| Line | Claim | Registry Source | Registry Value | Status |
|------|-------|----------------|----------------|--------|
| 5 | 0.54 pp, 1.34 pp | repeated from intro | | ⚠️/✅ |
| 5 | 4.4× gap | repeated | | ✅ |
| 6 | α=2.0, 66.11% | repeated | | ✅ |
| 6 | μ=0.62 (CKA-only) | — | not in registry | ❓ (note 2) |
| 6 | μ≥0.88 (collapsing methods) | — | not in registry | ❓ (note 2) |
| 10 | 2.89× gradient magnitude | gradient_flow_v3: cka_vs_standard_ratio | 2.89 | ✅ |
| 10 | f₀ > 0.5 | grpo_standard_20_fair: frac_zero_std trajectory | min=0.5, all steps ≥ 0.5 | ✅ |
| 15 | 4.62 pp SFT gap | Table 2: 63.91 − 59.29 | 4.62 pp | ⚠️ (see note 1) |
| 19 | \|Δ\| ≤ 1 pp at 15–25% | max across all = Standard 25%: 0.99 pp | ≤ 1 pp (marginal) | ✅ |

---

## limitations.tex

| Line | Claim | Registry Source | Registry Value | Status |
|------|-------|----------------|----------------|--------|
| 5 | N=200 (Qwen2.5-Math-7B) | eval_{grpo,sft}_{rasp,standard}_qwen_math | n_total=200 | ✅ |
| 11 | τ ∈ {0.3, 0.4, 0.5, 0.6} | floor_ablation experiments | config parameters | ✅ |
| 14 | 3 GRPO seeds | Table 2 shows ±std for CKA-only, Standard, Random | ✅ |
| 14 | N=1 (RASP) | Table 2: RASP has no ±std | ✅ |
| 15 | 3 benchmarks (GSM8K, MATH-500, MBPP) | eval experiments exist for all 3 | ✅ |

---

## 需关注的问题

### Note 1: Standard SFT 准确率差异（影响两个 claim）

Table 2 使用 Standard SFT = **59.29%**（隐含 782/1319），但 registry 中 `eval_gsm8k_sft_standard_20` = **781/1319 = 59.21%**。差 1 个样本。

这个差异影响两个数字：
- **mean \|Δ\| = 0.54 pp**：若用 registry 值 59.21%，Standard Δ 变为 0.63 pp，mean 变为 (0.48+0.63+0.61+0.53)/4 = **0.56 pp**
- **SFT gap = 4.62 pp**：若用 registry 值，gap 变为 63.91−59.21 = **4.70 pp**

建议：确认是否存在另一次 Standard SFT eval（得到 782/1319）未登记到 registry，或 Table 2 需要修正为 59.21%。若修正，需同步更新正文中所有 "0.54 pp" → "0.56 pp"，"4.62 pp" → "4.70 pp"。

### Note 2: CKA 相似度 μ 值无 registry 来源

`μ=0.62`（CKA-only）和 `μ≥0.88`（collapsing methods）来自离线 CKA 分析，未作为实验指标记录到 registry。建议在 artifacts 或 registry 中补录计算来源。

### Note 3: MATH-500 Fixed Eval 覆盖

Fixed eval 已完成大部分方法，但 **Standard SFT 20% 缺少 fixed eval 版本**。现有 Standard SFT MATH-500 evals 使用旧脚本（eval_math500_sft_standard_20: 130/500=26.0%）。如果论文表格中使用了 Standard SFT 的 MATH-500 数字，需要补跑 fixed eval。

---

## 总结

| 类别 | 数量 |
|------|------|
| ✅ 已核对一致 | 27 |
| ⚠️ 有差异（Standard SFT 59.29% vs 59.21%，影响 0.54pp 和 4.62pp） | 3 (实为 1 个根因) |
| ❓ 无 registry 来源（CKA μ 值，来自离线分析） | 2 |
| ❌ 无法追溯 | 0 |

**最关键 action item**：确认 Standard SFT 20% GSM8K 的真实值是 781 还是 782 correct（直接决定 0.54/0.56 pp 和 4.62/4.70 pp）。

---
