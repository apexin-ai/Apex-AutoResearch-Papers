# code std calculation audit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_std-calculation-audit_20260521T052300_result.json`
- **Structured JSON:** [`708c63446887f88e3791.json`](../../sessions/70/708c63446887f88e3791.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是审计报告：

---

## A. 代码实际使用的 std 类型

### 全部使用 `np.std(vals)` (ddof=0, **population std, n divisor**) 的脚本：

| 脚本 | 行号 | 调用 | 用途 |
|------|------|------|------|
| `statistical_tests.py` | 125 | `np.std(f1s)` | 3-seed F1 bootstrap std |
| `evaluate_actorattack_ood.py` | 283 | `np.std(vals)` | 3-seed F1 (注释明确写了 `# population std`) |
| `aggregate_exp2_missing.py` | 28 | `np.std(vals)` | 3-seed F1 (注释写了 `# population std (N divisor)`) |
| `vanilla_multiseed_dd_ood.py` | 212 | `np.std(vals)` | 3-seed F1 |
| `eval_exp16.py` | 167 | `np.std(f1s)` | 3-seed F1 |
| `exp3_probing.py` | 161 | `np.std(scores)` | 3-seed probing accuracy |
| `exp3_roberta_probing.py` | 297 | `np.std(scores)` | 3-seed probing accuracy |
| `evaluate_actorattack_ood_all.py` | 277 | `np.std(vals)` | 3-seed F1 |
| `exp4_vanilla_perturbation_mcnemar.py` | 254 | `np.std(vals)` | 3-seed F1 |
| `fix_exp6_reeval.py` | 144 | `np.std(vals)` | 3-seed F1 |
| `exp8_mhj_human_eval.py` | 326 | `np.std(vals)` | 3-seed metrics |
| `exp8_human_jailbreak_verazuo.py` | 345 | `np.std(vals)` | 3-seed metrics |
| `exp8_recalc_macro_f1.py` | 345 | `np.std(vals)` | 3-seed metrics |
| `meanpool_multiseed.py` | 257 | `np.std(vals)` | 3-seed F1 |
| `eval_cross_llm.py` | 186 | `np.std(vals)` | 3-seed F1 |
| `eval_cross_llm_control.py` | 190 | `np.std(vals)` | 3-seed F1 |
| `analyze_predictions.py` | 239 | `np.std(vals)` | 3-seed metrics |
| `exp15_roberta_large.py` | 401 | `np.std(vals)` | 3-seed metrics |
| `exp15b_roberta_large_lr1e5.py` | 403 | `np.std(vals)` | 3-seed metrics |
| `exp15c_roberta_large_mlm.py` | 429 | `np.std(vals)` | 3-seed metrics |
| `eval_exp17.py` | 225 | `np.std(vals)` | 3-seed metrics |
| `eval_toxicchat_balanced.py` | 118 | `np.std(f1_list)` | 3-seed F1 |
| `eval_toxicchat_balanced_mlm.py` | 92 | `np.std(f1_list)` | 3-seed F1 |
| `eval_exp17_toxicchat_balanced.py` | 75 | `np.std(f1s)` | 3-seed F1 |
| `reeval_exp16_balanced.py` | 199 | `np.std(f1s)` | 3-seed F1 |
| `turn_shuffle_ablation.py` | 175, 177 | `np.std(orig/shuf)` | 3-seed F1 |
| `exp28b_supplement.py` | 581,583,585 | `np.std(vals)` | 3-seed F1 |
| `exp28c_vanilla_supplement.py` | 293,295,297 | `np.std(vals)` | 3-seed F1 |
| `exp30_length_stratified.py` | 212 | `np.std(recalls)` | 3-seed recall |
| `exp29_inference_efficiency.py` | 129, 217 | `np.std(latencies)` | latency std (非 seed F1) |
| `exp32_strategy_prediction.py` | 424,427-429 | `np.std(vs)` | 3-seed metrics |
| `exp33_strategy_prediction_plan002.py` | 378 | `np.std(vs)` | 3-seed metrics |
| `exp35_cross_seed_ensemble.py` | 276 | `np.std(seed_f1s)` | 3-seed F1 |
| `exp36_frozen_mlm_probing.py` | 369 | `np.std(vals)` | 3-seed metrics |
| `exp37_length_matched_benign.py` | 168,246,255,354,359 | `np.std(...)` | 3-seed FPR |
| `exp38_wildcat_calibration.py` | 210,264,287,303,376 | `np.std(...)` | 3-seed AUC/FPR |

`.std()` 调用（numpy array 方法，默认 ddof=0 = population）：
| `sanity_check.py` | 70 | `scores.std()` | CV F1 (非论文数字) |
| `step3_sanity_check.py` | 59, 69 | `scores.std()` | CV F1 (非论文数字) |
| `sanity_check_v4b.py` | 32, 49 | `scores.std()` | CV F1 (非论文数字) |

### 唯一例外 — **sample std (ddof=1)**：

| 脚本 | 行号 | 调用 | 用途 |
|------|------|------|------|
| `exp12_toxicchat_bootstrap.py` | 127 | `np.std(seed_f1s, ddof=1)` | 3-seed ToxicChat F1 seed std |

**无 `torch.std` 调用。无 pandas `.std()` 调用。**

---

## B. 论文三处描述

1. **experiments.tex:29** — "All standard deviations are computed over 3 random seeds using the **population formula ($n$ divisor)**; Bessel-corrected estimates ($n{-}1$ divisor) are ≈22% larger but do not alter any significance conclusions."

2. **checklist.tex:19** — "All OOD results report 3-seed mean±std (**sample standard deviation with Bessel's correction, $N{-}1$ divisor**)."

3. **appendix.tex** — 表格 caption 中均写 "3-seed mean±std"，**未指定 population 或 sample**。appendix.tex 内无 "Bessel"、"divisor"、"n-1"、"deviation" 等关键词。Table 26（自动编号）的 caption 中没有明确标注 std 类型。

---

## C. 一致性判断

| 对比 | 结果 |
|------|------|
| 代码 (population) vs experiments.tex (population) | **一致** |
| 代码 (population) vs checklist.tex (sample) | **矛盾** |
| experiments.tex (population) vs checklist.tex (sample) | **矛盾** |
| exp12 脚本 (sample, ddof=1) vs 其他所有脚本 (population, ddof=0) | **exp12 是唯一异类** |

**结论：代码绝大多数使用 population std (n divisor)，experiments.tex 描述正确，checklist.tex 描述错误。**

`exp12_toxicchat_bootstrap.py` 是唯一用 sample std 的脚本，它的 seed_std 值会比其他脚本大 22.5%，这可能导致该脚本产生的数字与论文整体不一致。

---

## D. 影响分析

**换算关系** (n=3 seeds):
- `sample_std = population_std × √(3/2) ≈ population_std × 1.2247`
- sample std 比 population std 大 **~22.5%**

**对论文数字的影响**：
- 论文中所有 ±std 数字实际来自 population std（除 exp12）
- 典型 std 值范围：0.005–0.115（从 appendix 表格数据看）
- 如换成 sample std，例如 `.026` → `.032`，`.115` → `.141`
- **数量级和相对排序不变**

**对 significance 结论的影响**：
- 论文的 significance 判断基于 **bootstrap CIs** 和 **permutation tests**（不依赖 std 值），因此 std 类型不影响任何 significance 结论
- experiments.tex 中已正确声明"do not alter any significance conclusions"

**exp12 的异常**：
- `exp12_toxicchat_bootstrap.py:127` 用 `ddof=1`，其 `seed_std` 比同口径 population std 大 22.5%
- 如果该数字出现在论文中（ToxicChat 的 seed std），它与其他表格的 std 口径不一致
- 建议统一为 `ddof=0` 或全部改为 `ddof=1`，并修正 checklist.tex 使三处描述一致

---

**修复建议**（不修改文件，仅列出）：
1. **checklist.tex:19** — 改为 "population standard deviation ($N$ divisor)" 以匹配代码和 experiments.tex
2. **exp12_toxicchat_bootstrap.py:127** — 将 `ddof=1` 改为 `ddof=0` 以匹配其他所有脚本（或反过来全部统一为 ddof=1，但改动面更大）
3. 如果选择全部统一为 sample std (ddof=1)，则需重跑所有脚本并更新 experiments.tex 的描述

---
