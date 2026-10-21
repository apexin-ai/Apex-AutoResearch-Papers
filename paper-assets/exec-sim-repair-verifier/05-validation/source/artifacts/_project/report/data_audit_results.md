# Data Audit Results — ARR Submission Pre-Check

**Date**: 2026-05-23  
**Scope**: All numerical claims in abstract.tex, experiments.tex, introduction.tex, method.tex, conclusion.tex, appendix.tex  
**Sources**: experiment registry (152 experiments), artifact JSON files, computation verification

---

## ✅ 已核对一致

### Abstract
- "≤8B LoRA" qualifier — consistent throughout paper ← protocol description
- "TOST, 5 seeds" — CLS/CWM function-level use 5 seeds (42/123/456/789/0) ← registry: multi-seed-core + cls-seed789 + cls-seed0 + cwm-seed* entries
- "3.11pp (4B) to 1.07pp (14B)" — scaling table: CLS 4B mean 88.68, TRAJ 4B mean 85.57, gap=3.11; CLS 14B mean 89.93, TRAJ 14B mean 88.86, gap=1.07 ← registry 14b seeds verified
- "18–26pp across 2-3 seeds" — Table 2 gaps: 25.59pp (4B), 18.35pp (8B), 26.08pp (DeepSeek) → range 18.35–26.08 ← registry cls/cwm repo experiments
- "95.83% variant accuracy (+14.58pp)" — 46/48=95.83; best CLS variant=81.25; 95.83−81.25=14.58 ← exp-a-routing: oracle_best_pair=95.83
- "$<$0.4pp routing heuristic" — max routing gain=+0.37pp ← artifacts/routing_analysis_report.md

### Table 1 (function-level, n=1,890)
- **CLS 4B**: 88.43 ± 0.78 — seeds: 87.83, 89.52, 87.88, 89.00, 87.94 → mean=88.434, std=0.777 ← multi-seed-core (s42=87.83, s123=89.52, s456=87.88) + cls-seed789 (89.00) + cls-seed0 (87.94)
- **CWM 4B**: 87.19 ± 0.37 — seeds: 87.51, 87.20, 86.98, 86.67, 87.57 → mean=87.186, std=0.375 ← per-test-precision-recall, cwm-seed123, cwm-seed456, cwm-seed789, cwm-seed0
- **TRAJ 4B**: 86.30 ± 0.97 — seeds: 85.66, 85.47, 87.40, 87.31, 85.66 → mean=86.30, std=0.967 ← traj-level-finetuned, traj-level-seed123/456/789/0
- **DeepSeek CLS 6.7B**: 86.85 ± 0.11 — seeds: 86.93, 86.77 → mean=86.85, std=0.113 ← deepseek-cls-func (s42), deepseek-cls-func-s123
- **DeepSeek CWM 6.7B**: 86.83 ± 1.49 — seeds: 85.77, 87.88 → mean=86.825≈86.83, std=1.492 ← deepseek-cwm-func (s42), deepseek-cwm-func-s123
- **DeepSeek TRAJ 6.7B**: 84.16 ± 1.30 — seeds: 83.24, 85.08 → mean=84.16, std=1.301 ← deepseek-traj-func-v2 (s42), deepseek-traj-func-v2-s123
- **0-shot 8B (Qwen3)**: 60.53 ← 8b-baseline-rerun: 0shot_accuracy=60.53
- **0-shot 14B (Qwen3)**: 66.24 ← 14b-baseline-0shot-3shot-v2: 0shot accuracy=66.24
- **ZS LLM-as-judge 8B**: 64.40 ← llm-judge-8b-zeroshot: overall_accuracy=64.40
- **ZS LLM-as-judge 32B NF4**: 71.69 ← llm-judge-32b-zeroshot: overall_accuracy=71.69
- **3-shot ICL 8B**: 60.42 ← 8b-baseline-rerun: 3shot_accuracy=60.42
- **3-shot ICL 14B**: 73.12 ← 14b-baseline-0shot-3shot-v2: 3shot accuracy=73.12
- **Majority (pass)**: 51.75% ← dataset description (pass:fail ≈ 52:48)

### Table 2 (repo-level, n=9,784 per-test / n=48 variant)
- **Qwen3-4B CLS**: 83.63 ← cls4b-v5-ckpt4600-test-eval: accuracy=83.63
- **Qwen3-4B CWM**: 58.04 ← cwm4b-s42-mutation-breakdown: overall_accuracy=58.04
- **Qwen3-4B TRAJ**: 72.92 ← qwen3-4b-traj-repo-s42-eval: variant_accuracy=72.92
- **Qwen3-8B CLS**: 84.83 ± 0.67 — seeds: 84.48 (s42), 85.60 (s123), 84.40 (s456) → mean=84.827, std=0.671 ← cls8b-s42-resume-ckpt3600-test-v2, cls8b-seed123-ckpt3000-test8192-eval, cls8b-repo-s456-eval-v2
- **Qwen3-8B CWM**: 66.48 ± 1.15 — seeds: 65.17 (s42 ckpt400), 67.33 (s123), 66.93 (s456) → mean=66.477, std=1.149 ← qwen3-8b-cwm-repo-s42-ckpt400 (seq8192 inferred), qwen3-8b-cwm-repo-s123-eval, qwen3-8b-cwm-repo-s456-eval
- **Qwen3-8B TRAJ**: 72.91 ± 3.61 — seeds: 70.83 (s42 epoch 3), 77.08 (s123), 70.83 (s456) → mean=72.913, std=3.608 ← qwen3-8b-traj-repo-s42-best-eval, qwen3-8b-traj-repo-s123, qwen3-8b-traj-repo-s456
- **DeepSeek CLS**: 84.38 ± 2.50 — seeds: 82.61 (s42 epoch 1), 86.15 (s456) → mean=84.38, std=2.503 ← deepseek-cls-repo-v5-ckpt2105-eval, deepseek-cls-repo-s456-eval-v2 (s123 excluded per footnote)
- **DeepSeek CWM**: 58.30 ± 2.82 — seeds: 61.49 (s42), 57.31 (s123), 56.11 (s456) → mean=58.303, std=2.825 ← deepseek-cwm-repo-s42-seq4096-eval, deepseek-cwm-repo-s123-e3-eval, deepseek-cwm-repo-s456-e3-eval
- **DeepSeek TRAJ**: 77.08 ± 3.61 — seeds: 81.25, 75.0, 75.0 → mean=77.083, std=3.608 ← deepseek-traj-repo-8k (s42/s123/s456)
- **0-shot Qwen3-8B**: 49.90 ← repo-level-0shot-baseline: accuracy=0.499
- **0-shot DeepSeek**: 48.54 ← deepseek-0shot-repo-baseline: accuracy=0.4854
- **Majority**: 72.96 ← dataset specification

### Scaling Table (Table 3)
- **CLS 4B**: s42=87.83, s123=89.52, mean=88.68 ← multi-seed-core
- **CLS 8B**: s42=90.48, s123=89.40, mean=89.94 ← model-size-scaling-cls8b, cls8b-seed123
- **CLS 14B**: s42=89.21, s123=90.79, s456=89.79, mean=89.93±0.80 ← 14b_seed_level_stats.json (bf16 eval values)
- **CWM 4B**: s42=87.51, s123=87.20, mean=87.36 ← per-test-precision-recall, cwm-seed123
- **CWM 8B**: s42=87.67, s123=86.98, mean=87.33 ← model-size-scaling-cwm8b, cwm8b-seed123
- **CWM 14B**: s42=89.26, s123=88.99, s456=90.26, mean=89.50±0.67 ← 14b_seed_level_stats.json
- **TRAJ 4B**: s42=85.66, s123=85.47, mean=85.57 ← traj-level-finetuned, traj-level-seed123
- **TRAJ 8B**: s42=87.60, s123=87.79, mean=87.70 ← qwen3-8b-traj-func-s42, qwen3-8b-traj-func-s123
- **TRAJ 14B**: s42=89.73, s123=88.57, s456=88.28, mean=88.86±0.77 ← traj14b-func-s42/s123/s456
- All Δ values verified: +1.27, −0.03, +2.13, −0.01, +2.17, +1.16 ✓
- Max gap 14B: CLS−TRAJ = 89.93−88.86 = 1.07pp ✓
- Fig 2 caption gaps: 1.32, 2.62, 0.43 all verified ✓

### Holm-Bonferroni (Table in Appendix I)
All 5 rows match `artifacts/holm_bonferroni_results.json` exactly:
1. Repo CLS vs CWM: raw p=0.003, adj p=0.015 ✓
2. Func CLS vs CWM TOST: raw p=0.007, adj p=0.028 ✓
3. Func CLS vs TRAJ TOST: raw p=0.025, adj p=0.075 ✓
4. Repo CWM vs TRAJ: raw p=0.039, adj p=0.078 ✓
5. Repo CLS vs TRAJ: raw p=0.385, adj p=0.385 ✓

### Bayesian ROPE (Appendix G.1)
All values match `artifacts/bayesian_rope_results_reproduced.json`:
- CLS-CWM per-test: P(ROPE)=0.975, HDI=[+0.10, +2.00] ✓
- CLS-TRAJ per-test: P(ROPE)=0.542, HDI=[+0.35, +3.52] ✓
- CLS-TRAJ variant: P(ROPE)=0.970, HDI=[−2.00, +1.03] ✓

### 14B Seed-Level Stats (§4.2 + Appendix G.1)
All values match `artifacts/14b_seed_level_stats.json`:
- CLS-CWM TOST p=0.076 ✓, P(ROPE)=0.887 ✓
- CLS-TRAJ TOST p=0.187 ✓, P(ROPE)=0.780 ✓
- CLS 14B seed values: 89.21, 90.79, 89.79 ✓ (bf16; NF4 s42=89.47 noted separately)
- CWM 14B seed values: 89.26, 88.99, 90.26 ✓ (bf16; NF4 s42=89.30)

### Inference Efficiency (Appendix F, paragraph i)
All values match `artifacts/inference_benchmark_results.json`:
- 217× speedup (217.75 in artifact) ✓
- 853 vs 3.9 inferences/min (853.45 vs 3.92) ✓
- ~477 tokens avg output (477.1) ✓
- 48ms median CLS (48.09) ✓
- 16.3s median CWM (16.3s = 16299.85ms) ✓

### Oracle Analysis
- Function: 90.63% = 1713/1890 correct, +2.80pp over CLS s42 (87.83) ← appendix extended analysis (a)
- Repo: 95.83% = 46/48 variants ← exp-a-routing: oracle_best_pair=95.83
- Repo per-test 3-seed oracle: 94.27±2.59 ← compute_oracle_3seed.py documented values

### Downsample Ablation (Appendix O)
- 80.74% downsampled CLS ← exp-downsample-cls-func-v3-eval: accuracy=80.74 ✓

### 3-shot Repo Baselines (Appendix M)
- Qwen3-8B 3-shot per-test: 71.61%, variant: 45.83% ← exp-e-qwen3-3shot-baseline ✓
- DeepSeek 3-shot per-test: 46.28%, variant: 45.83% ← repo-level-3shot-baseline ✓

### Block Correlation (§4.3)
- ICC=0.191, DEFF=3.97, all-correct ratio=2.81 ← block-corr-empirical ✓

### Inline Text Numbers
- "25.59pp at 4B": 83.63−58.04=25.59 ✓
- "18.35pp at 8B": 84.83−66.48=18.35 ✓
- "16.82pp below fine-tuned CLS at 8B": 89.94−73.12=16.82 ✓ (best 3-shot 14B vs fine-tuned CLS 8B mean)
- "CLS-CWM gap of 0.02pp" (DeepSeek func): 86.85−86.83=0.02 ✓
- "CLS-CWM gap 1.24pp" (Qwen3 func): 88.43−87.19=1.24 ✓
- "$>$50% unparseable" CWM format collapse: 53.7% (4B), 73.8% (8B) ✓
- "parseable-only 38-43%": parseable accuracy 38.52% (8B) to 42.88% (4B) ← cwm4b-s42-mutation-breakdown, §4.4 text ✓

### Checkpoint Ablation (Appendix N)
- CLS 8B s42: ckpt-2200=85.34, ckpt-3600=84.48, ckpt-6633=85.29, <1pp range ← cls8b-s42-ckpt-ablation ✓

### LoRA Rank Ablation (Appendix B)
- r=16 α=32: 87.51; r=32 α=32: 87.00 (−0.51); r=32 α=64: 87.04 (−0.47) ← cwm-rank32-ablation-v2, cwm-rank32-alpha64-ablation ✓

### CWM Convergence (Appendix N)
- Eval loss minimum at step 300-400 across 3 seeds ← confirmed by paper table data ✓

---

## ⚠️ 不一致 / 需修正

### 1. §4.1 "CLS-TRAJ gap <1pp on Qwen3" — 比较层级不一致
**位置**: experiments.tex line 62
**问题**: 论文声称 "the CLS-TRAJ gap is model-dependent: <1pp on Qwen3 but 2.69pp on DeepSeek"。但 Table 1 per-test 数据显示 Qwen3 CLS-TRAJ gap = 88.43−86.30 = 2.13pp，不是 <1pp。

"<1pp" 来自 variant-level matched TOST 分析 (pooled gap = −0.45pp，|0.45| < 1)，而 "2.69pp" 来自 DeepSeek per-test 数据 (86.85−84.16)。同一句话混用了两个不同层级的比较。

**建议修复**: 明确比较层级。例如：
> "The CLS-TRAJ per-test gap varies by model family: 2.13pp on Qwen3-4B and 2.69pp on DeepSeek-6.7B. At variant level, the Qwen3 gap narrows to $<$1pp ($-$0.45pp matched TOST), while the DeepSeek gap (2.69pp) exceeds the $\pm$2pp equivalence margin."

或者统一使用 per-test level：
> "The CLS-TRAJ gap is ${\sim}$2pp on Qwen3 but 2.69pp on DeepSeek, the latter exceeding the $\pm$2pp equivalence margin."

### 2. Table 1 DeepSeek 0-shot: 63.00 vs 63.02 — 微小四舍五入差异
**位置**: experiments.tex line 49
**问题**: Registry deepseek-0shot-func-baseline: accuracy=0.6302 → 63.02%，论文写 63.00%。差距仅 0.02pp。
**来源**: deepseek-0shot-func-baseline, unparseable_count=20, total_samples=1890
**建议**: 改为 63.02 以与 registry 一致，或确认 63.00 的计算方式（如不同 unparseable 处理）。

### 3. "35-36pp" 0-shot gains — 下限略低于 35
**位置**: experiments.tex line 62, 151; introduction.tex line 8; conclusion.tex line 4
**问题**: Qwen3 gain = 84.83−49.90 = 34.93pp (严格来说不到 35pp)。DeepSeek = 84.38−48.54 = 35.84pp。
**建议**: 改为 "35-36pp" → "~35-36pp" 或 "34-36pp"，或保留但接受 34.93 约等于 35 的四舍五入。这属于边界情况。

### 4. CLS 8B s123 两个不同评估值: 89.40 vs 89.37
**位置**: scaling table (experiments.tex line 81)
**问题**: Registry 有两个不同实验 — cls8b-seed123: 89.40, cls8b-eval-seed123: 89.37。论文 scaling table 使用 89.40。差异 0.03pp，可能是不同 eval 脚本或 precision 导致。
**影响**: 对 8B CLS mean 影响 <0.02pp (89.94 → 89.93 if using 89.37)。实际影响可忽略。
**建议**: 确认哪个评估结果是 canonical，保持一致使用。

---

## ❌ 无法追溯

### 1. z=−23.7 (LPM formulation×complexity interaction)
**位置**: experiments.tex line 182
**问题**: Mixed-effects LPM 分析的 z-statistic。未找到独立的 JSON artifact 存储这个值。该值出现在 paper text 和 review artifacts 中但没有可直接核查的分析输出文件。
**建议**: 将 LPM 分析脚本输出保存为 `artifacts/lpm_interaction_results.json`。

### 2. p=0.0066 (8B CLS-CWM scaling gap clustered bootstrap)
**位置**: experiments.tex line 102
**问题**: "clustered bootstrap on the 3-seed superset (42, 123, 456 for CLS/CWM) yields p=0.0066 (95% CI [1.80, 2.71])"。未找到对应的 artifact JSON。
**建议**: 将结果保存为 `artifacts/8b_cls_cwm_scaling_bootstrap.json`。

### 3. DeepSeek LLM-as-judge 56.56%
**位置**: experiments.tex line 51
**问题**: Table 1 "ZS LLM-as-judge | 6.7B (DeepSeek) | 1 | 56.56"。在 registry 的 success 实验中未找到对应条目。可能在未列出的实验中或使用不同的 experiment_id。
**建议**: 确认 experiment_id 并验证。

### 4. DeepSeek 3-shot ICL function-level 59.95%
**位置**: experiments.tex line 55
**问题**: Table 1 "3-shot ICL | 6.7B (DeepSeek) | 1 | 59.95"。在 registry excerpt 中未找到。
**建议**: 确认 experiment_id 并验证。

### 5. Table 3 failure mode taxonomy 具体数值
**位置**: experiments.tex line 170-175
**问题**: Format collapse "48-52%", Decision collapse "~14% fail recall, 56% variant acc", Aggregation penalty "51-57% fail recall, 73-81% variant acc" — 这些值需要从 prediction-level 分析文件追溯（非 registry 级别 metrics）。值在 variant-level accuracy 表 (Appendix D) 中部分可交叉验证：
  - Decision collapse (DeepSeek s123): variant acc=56.25, fail recall=~13.72 ← deepseek-cls-repo-s123: recall_fail_seq8192=13.72 ✓ (paper says ~14% ✓)
  - Aggr penalty (Qwen3-8B): variant acc=72.92/81.25 ← appendix variant table ✓
  
**建议**: 其余值从 Appendix D variant-level table 交叉验证。

### 6. "477 tokens" 具体来源
**位置**: introduction.tex line 8, experiments.tex line 189
**问题**: inference_benchmark_results.json 确认 avg_output_tokens=477.1。✓ 
**状态**: 已确认。（从 ❌ 移到 ✅）

### 7. Appendix O "386 variant-level instances, ~8K per-test equivalents"
**位置**: appendix.tex line 76
**问题**: Repo-level TRAJ training data量。需从训练数据文件直接验证 variant count=386 和 per-test equivalents ~8K。
**建议**: 从训练数据文件 count 验证。

---

## 交叉一致性总结

| 检查项 | 结果 |
|--------|------|
| Table 1 ↔ Registry (function-level) | ✅ 所有 mean±std 一致 |
| Table 2 ↔ Registry (repo-level) | ✅ 所有 mean±std 一致 |
| Scaling Table ↔ Registry (14B) | ✅ 个别 seed 值、mean、std 均一致 |
| Scaling Table ↔ 14b_seed_level_stats.json | ✅ 完全一致 |
| Abstract 数字 ↔ Tables | ✅ 一致（均可从 Tables 计算得出） |
| Holm Table ↔ holm_bonferroni_results.json | ✅ 完全一致 |
| Bayesian ROPE ↔ bayesian_rope_results_reproduced.json | ✅ 完全一致 |
| 14B stats ↔ 14b_seed_level_stats.json | ✅ 完全一致 |
| Routing claim ↔ routing_analysis_report.md | ✅ <0.4pp 一致 |
| Oracle ↔ exp-a-routing + compute_oracle_3seed.py | ✅ 一致 |
| Inference ↔ inference_benchmark_results.json | ✅ 一致 |
| Introduction ↔ Experiments | ✅ 数字一致 |
| Conclusion ↔ Experiments | ✅ 数字一致 |
| Appendix ↔ Main text | ✅ 一致（使用相同 source） |
| §4.1 CLS-TRAJ "<1pp" claim | ⚠️ 比较层级不一致 |
| Table 1 DeepSeek 0-shot | ⚠️ 63.00 vs 63.02 |
