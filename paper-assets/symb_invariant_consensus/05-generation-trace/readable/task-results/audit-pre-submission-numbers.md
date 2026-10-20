# audit pre submission numbers

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json`
- **Structured JSON:** [`e164dc6809367b051825.json`](../../sessions/e1/e164dc6809367b051825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both edits applied correctly. Now let me compile the full audit report.

---

### 审计结果摘要

**扫描文件数**: 11 (abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, limitations_content.tex, appendix.tex, + 2 figure scripts; diagnosis.tex/conclusion.tex excluded — not \input'd in main.tex)

**提取数值数**: ~280+ (accuracy %, Δ, p-value, BR, κ, K_eff, n, sample sizes, etc.)

**可追溯到 registry 的数值**: 核心数值全部可追溯；registry 部分实验含旧值（D064 校正前），paper 内部使用校正后值，自洽。

---

### 已修复的不一致

1. **experiments.tex:50** — `κ ∈ [0.41, 0.51]` → `κ ∈ [0.45, 0.51]` | appendix tab:independence 显示 s789 κ=0.45（非 0.41；0.41 来自已弃用的 diagnosis.tex） | **已修复**

2. **method.tex:56** — "five frontier models (gpt-4o, ...)" 声称全部使用 cross-model extraction，但 Table 2 标注 gpt-4o 为 $^a$（self-extraction）且遗漏 R1-Distill-8B | 重写为准确描述各模型的 extraction type | **已修复**

---

### 跨位置一致性验证（通过）

| Claim | 位置 1 | 位置 2 | 一致 |
|---|---|---|---|
| BR 1.66–4.97× | abstract | Table 2 (analysis.tex) | ✓ |
| +6.67pp, p<0.001 | abstract | solutions.tex tab:cross_generator_nli | ✓ |
| 27 training-free variants | abstract | analysis.tex, appendix tab:additional_interventions | ✓ |
| Oracle +29.90/+13.73pp FOLIO | experiments.tex | appendix app:oracle, conclusion area in discussion.tex | ✓ |
| Oracle +17.17pp PW | experiments.tex | appendix tab:pw_oracle_subtype | ✓ |
| 83.3% wrong constraints, BR=4.97× | analysis.tex | registry exp-confirmation-bias | ✓ |
| 96.1% agreement (n=804) | analysis.tex | appendix tab:ablation (773/804) | ✓ |
| Multi-seed Mistral FOLIO: +0.16±2.70 | experiments.tex | appendix tab:multi-seed | ✓ |
| Qwen14B 4-seed: Δ∈[0.00, -2.01] | experiments.tex | appendix tab:multi-seed | ✓ |
| DRC 83–90% recovery, ~35% cost | solutions.tex | appendix tab:drc | ✓ |
| DeBERTa standalone 49.51%/55.00% | solutions.tex | registry, appendix tables | ✓ |
| Finetuned +12.67/+11.67pp | solutions.tex | appendix tab:finetuned-nli | ✓ |
| κ range 0.21–0.82, K_eff 1.20–3.62 | experiments.tex | appendix tab:independence | ✓ |
| Mistral PW all 4 seeds negative | appendix tab:multi-seed | all seed Δ: -2.83, -3.33, -1.33, -1.67 | ✓ |
| LLaMA PW all 4 seeds negative | appendix tab:multi-seed | all seed Δ: -7.50, -7.33, -5.50, -4.67 | ✓ |
| Table arithmetic (SC+Δ=SICA) | all tables | spot-checked ~30 rows | ✓ |

---

### Figure 验证

- **f6_kappa_accuracy_scatter.py**: 7 data points 全部与 appendix tab:kappa_generalization 一致（κ 精度 3 位小数，table 2 位取整吻合） ✓ | PDF date: 5/22 ✓
- **capability_gap_scatter.py**: 11 data points（6 DeBERTa primary + 1 LLaMA + 2 multi-NLI + 2 finetuned）全部与 paper tables 一致 ✓ | PDF date: 5/23 ✓
- 数据源文件路径: 两个脚本均使用硬编码数据，无外部文件依赖，数据直接来自 paper tables

---

### 需要 Director 决策的项目

1. **BH correction p-value (experiments.tex:5)** — Paper says "both reach adjusted p = 0.066" for m=6 BH correction on raw p=0.011 and p=0.014. Standard BH step-down procedure gives adjusted p=0.042 for both (0.042 < 0.05 → significant). The paper's 0.066 appears to use rank-1 formula (0.011×6/1) for both tests. **If standard BH is correct, both negative Δ conditions (Mistral-7B PW -2.83pp, Qwen14B PW -2.50pp) remain significant after correction.** This doesn't affect the core claim ("no significant *positive* effect") but changes "No condition shows a significant SICA effect after FDR control" to "Two conditions show significant *negative* effects after FDR control." 需要确认统计方法。

2. **Abstract word count** — ~202 words, slightly above 200-word limit. Borderline — may pass ARR check or may need trimming 1-2 words.

3. **"14× over zero-shot" (solutions.tex)** — This ratio (11.67/0.83) applies only to LLaMA-8B. For Mistral-7B, the ratio is 12.67/6.67 ≈ 1.9×. The sentence "for Mistral-7B/LLaMA-8B (14× over zero-shot)" implies 14× applies to both. 建议改为 "up to 14×" 或明确标注 LLaMA-only。

4. **Registry vs paper baseline discrepancies** — Several registry experiments (exp-040, exp-090, exp-deberta-ft-combo) show SC baselines differing from paper values by 0.17–2.50pp, likely pre-D064 correction. Registry was not updated after corrections. 不影响 paper 内部一致性，但建议更新 registry 以备 camera-ready。

---
