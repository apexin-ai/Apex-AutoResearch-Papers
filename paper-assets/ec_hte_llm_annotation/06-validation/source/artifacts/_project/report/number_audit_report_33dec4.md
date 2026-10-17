# 数字核查报告 (2026-05-24)

## A. 追溯性检查

### Abstract 数字

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| R²≥0.97 | abstract.tex:5 | exp-002 (K2=0.994, K4=0.974), exp-019 (≥0.976), exp-024 (0.975) | ✅ | K4=0.974 四舍五入到0.97 |
| 14.9% at τ(0)=0.03 | abstract.tex:5 | exp-038 reversal_pct_tau003=14.9 | ✅ | 精确匹配 |
| 5× across subgroups | abstract.tex:3 | N/A（文献引用 Ashwin et al.） | ✅ | 非本文实验数据 |
| 7.4× bias reduction | abstract.tex:7 | 由 Table 1 推导: 0.059/0.008=7.375≈7.4× | ✅ | exp-039 K2_bias=0.008 |
| AUC=1.0 | abstract.tex:6 | exp-028 K4 perfect combos (Llama/Qwen/Mistral/gpt-4o) | ✅ | Δτ>0 子集 |
| AUC=0.86 | abstract.tex:6 | exp-005 subgroup AUC=0.833; ROC figure caption=0.86 | ⚠️ | registry 0.833 vs paper 0.86，见问题 W1 |
| AUC=0.63 | abstract.tex:6 | exp-028 overall symmetric AUC=0.626 | ✅ | 0.626≈0.63 |
| 11 empirical CMs | abstract.tex:5 | exp-024 n_llm_dataset_combos=11 | ✅ | 精确匹配 |

### Experiments.tex 数字

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| 0.059 (global bias K=2) | experiments.tex:25 | Table 1 行47 | ✅ | 内部一致 |
| 0.008 (HB bias K=2) | experiments.tex:27 | exp-039 K2_echte_bias=0.008 | ✅ | 精确匹配 |
| 7.4× | experiments.tex:27 | 0.059/0.008=7.375 | ✅ | 四舍五入 |
| 4.7× (K=4 DIM) | experiments.tex:27 | 0.056/0.012=4.667 | ✅ | 四舍五入到4.7 |
| 4.9× (CF) | experiments.tex:33 | 0.191/0.039=4.897 | ✅ | 四舍五入到4.9 |
| 5.9× (CF amplification) | experiments.tex:33 | exp-011 debiasing_hurts_max_ratio=5.9 | ✅ | 精确匹配 |
| 93.8% (CF coverage) | experiments.tex:65 | exp-036 plugin_coverage=0.9375 | ✅ | 0.9375→93.8% |
| 260/520 configs | experiments.tex:18 | exp-002 "260/520 (excluding dc=0)" | ✅ | 精确匹配 |
| 2.86× (K=2) | experiments.tex:18 | exp-002 max_bias_ratio_k2=2.86 | ✅ | 精确匹配 |
| 2.41× (K=4) | experiments.tex:18 | exp-002 max_bias_ratio_k4=2.41 | ✅ | 精确匹配 |
| 89% R-learner | experiments.tex:34 | exp-017 "89% reduction" (0.121→0.013) | ✅ | 1-0.013/0.121=89.3% |
| 14.9% sign reversal | experiments.tex:19 | exp-038 | ✅ | 同 abstract |
| 31% at τ(0)=0.01 | experiments.tex:19 | exp-038 reversal_pct_tau001=31 | ✅ | 精确匹配 |
| 0.94–0.96 coverage | experiments.tex:27 | exp-039 K2=0.938, K4=0.956 | ✅ | 0.938≈0.94, 0.956≈0.96 |

### Table 1 完整核查 (experiments.tex:40-66)

| Config | Method | |Bias| | RMSE | Cov | 来源 | 匹配? |
|--------|--------|-------|------|------|------|-------|
| DIM K=2 | Naive | 0.058 | 0.090 | 0.82 | exp-001/exp-039 | ✅ |
| DIM K=2 | Global | 0.059 | 0.099 | 0.87 | exp-001/exp-039 | ✅ |
| DIM K=2 | F-L Scalar | 0.122 | 0.159 | 0.68 | exp-034 | ✅ |
| DIM K=2 | F-L Per-sub | 0.168 | 0.220 | 0.65 | exp-034 | ✅ |
| DIM K=2 | Strat MLE | 0.012 | 0.094 | 0.95 | exp-001 | ✅ |
| DIM K=2 | HB EC-HTE | 0.008 | 0.089 | 0.94 | exp-039 K2_bias=0.008, RMSE=0.089, cov=0.938 | ✅ |
| DIM K=4 | Naive | 0.062 | 0.113 | 0.88 | exp-001/exp-039 | ✅ |
| DIM K=4 | Global | 0.056 | 0.125 | 0.91 | exp-001/exp-039 | ✅ |
| DIM K=4 | Strat MLE | 0.010 | 0.127† | 0.95 | exp-001 | ✅ |
| DIM K=4 | HB EC-HTE | 0.012 | 0.120 | 0.96 | exp-039 K4_bias=0.012, RMSE=0.120, cov=0.956 | ✅ |
| CF K=4 | Naive | 0.208 | 0.231 | 0.44 | exp-011 specific config | ✅ |
| CF K=4 | Global | 0.191 | 0.244 | 0.58 | exp-011 specific config | ✅ |
| CF K=4 | EC-HTE Forest | 0.039 | 0.180 | 0.90 | exp-011 specific config | ✅ |

### Theory.tex 数字

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| R²=0.994 (K=2) | theory.tex:93 | exp-002 R²_K2=0.9939 | ✅ | 0.994 |
| R²=0.97 (K=4) | theory.tex:93 | exp-002 R²_K4=0.9738 | ✅ | 四舍五入 |
| R²≥0.976 at P(Z=1)=0.1 | theory.tex:92 | exp-019 K2/P0.1=0.998, K4/P0.1=0.984 | ✅ | min=0.976 |
| RMSE ratio 1.06–1.68 | theory.tex:92 | exp-019 K4 ratios: 1.54,1.68,1.12,1.08,1.06 | ✅ | 精确匹配 |
| γ_T=0.10 → 75% coverage | theory.tex:98 | exp-040 gamma010_cov=0.750 | ✅ | 精确匹配 |
| F-L 0.058→0.122 (2.1×) | theory.tex:54 | Table 1: naive=0.058, F-L=0.122 | ✅ | 0.122/0.058=2.10 |
| F-L per-sub 0.168 (2.9×) | theory.tex:54 | Table 1: F-L Per-sub=0.168 | ✅ | 0.168/0.058=2.90 |
| R²=0.991 (asymmetric) | theory.tex:67 | exp-014 R²=0.992 | ⚠️ | 0.991 vs 0.992，差0.001 |
| AUC 0.86→0.66 (asymmetric) | theory.tex:64 | appendix.tex:176 AUC=0.66 | ✅ | 合成数据非对称实验 |
| ≥93% coverage | theory.tex:87 | exp-039/多个实验 | ✅ | A5 violation 下 ≥93% |
| 50% of K=2 configs (260/520) | theory.tex:120 | exp-002 | ✅ | 同 experiments.tex |
| 2.86× / 2.41× | theory.tex:120 | exp-002 | ✅ | 同上 |

### Method.tex 数字

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| RMSE change ≤4% | method.tex:12 | exp-022: K2<1%, K4≈4-5% | ⚠️ | K4超过4%，见问题 W2 |
| <5% RMSE variation | method.tex:21 | exp-022: K4≈4-5% | ✅ | <5% 准确 |
| 2× perturbation | method.tex:12 | exp-022 scale range 0.5-2.0 | ✅ | |
| 87.5% (21/24) HB>MLE | method.tex:18 | exp-006 "87.5%" | ✅ | 21/24=87.5% |
| ≥93% coverage (κ range) | method.tex:33 | appendix kappa analysis: ≥93.2% | ✅ | |
| AUC=0.86 (diagnostic) | method.tex:53 | exp-005 subgroup AUC=0.833 | ⚠️ | 见问题 W1 |
| |bias| 0.179→0.007 | method.tex:60 | PPCI table DGP C z=0 | ✅ | 精确匹配 |
| 27% RMSE advantage | method.tex:61 | PPCI table DGP A | ❌ | 见问题 C1 |
| |bias|=0.003–0.004 (DGP C) | method.tex:61 | PPCI table | ❌ | 见问题 C2 |
| "outcome-side error alone (DGP C)" | method.tex:61 | appendix DGP定义 | ❌ | 见问题 C2 |
| ≥93% coverage A5 | method.tex:87 | A5 violation table: EC-HTE≥0.94 | ✅ | |

### Introduction.tex 数字

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| 5× (literature) | intro.tex:10 | N/A (Ashwin et al.) | ✅ | |
| Δπ>0.20 | intro.tex:10 | Ashwin et al. 文献引用 | ✅ | |
| 0.15 threshold | intro.tex:10 | 论文 operating conditions | ✅ | |
| GPT-4.1 85.8% accuracy | intro.tex:10 | exp-012 accuracy_binary=0.858 | ✅ | |
| 10.2%–20.0% error range | intro.tex:10 | exp-008/exp-012 pilot data | ✅ | 20.0-10.2=0.098=Δπ |
| Δπ=0.098 | intro.tex:10 | exp-008 GPT-4.1 Δπ=0.098 | ✅ | |
| 14.9% | intro.tex:13 | exp-038 | ✅ | |
| 31% at τ(0)=0.01 | intro.tex:13 | exp-038 | ✅ | |
| τ̂=−0.059 | intro.tex:13 | policy_reversal table τ(0)=0.03 extreme | ✅ | appendix.tex:1501 |
| 5.9× (K=4 CF) | intro.tex:14 | exp-011 | ✅ | |
| 2.9× (F-L) | intro.tex:14 | 0.168/0.058=2.897 | ✅ | |
| 0.059→0.008 | intro.tex:20 | Table 1 | ✅ | |
| R²≥0.97 | intro.tex:17,34 | exp-002 | ✅ | |
| AUC=1.0 | intro.tex:18,35 | exp-028 | ✅ | |
| 7.5% subgroup estimates | intro.tex:28 (Fig caption) | 具体配置数据 | ⚠️ | 非 registry 顶层指标，需从原始CSV验证 |

### Appendix 数字（代表性抽查）

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| K=8 coverage≥95.6% | appendix.tex:381 | exp-030/exp-039 K8 cov=0.956 | ✅ | |
| R²=0.975 (11 real CMs) | appendix.tex:979 | exp-024 R²=0.975 | ✅ | |
| R²=0.991 (asymmetric) | appendix.tex:437 | exp-014 R²=0.992 | ⚠️ | 差0.001 |
| 4× bias reduction (asym) | appendix.tex:439 | exp-014 bias_reduction=4.2× | ⚠️ | 论文4×, registry 4.2× |
| 93.8% plugin coverage | appendix.tex:1101 | exp-036 0.9375 | ✅ | |
| 95.0% bootstrap coverage | appendix.tex:1107 | exp-036 boot_cov=0.950 | ✅ | |
| 89% R-learner reduction | appendix.tex:835 | exp-017 | ✅ | 1-0.013/0.121=89.3% |
| 13.3% stance sign rev (Global) | appendix_stance.tex:10 | 4/30=0.133 | ✅ | 内部算术 |
| 3.3% stance sign rev (EC-HTE) | appendix_stance.tex:10 | 1/30=0.033 | ✅ | |
| ≥94.5% confounded coverage | appendix.tex:1386 | exp-032 all HB cov≥0.945 | ✅ | |

### Limitations.tex 数字

| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |
|------|--------------|-----------------|-------|------|
| K=8 coverage≥95.6% | limitations.tex:5 | exp-030 cov=0.956 | ✅ | |
| AUC=0.86 synthetic | limitations.tex:6 | ROC figure, exp-005 | ⚠️ | 同问题 W1 |
| AUC=0.63 real LLM | limitations.tex:6 | exp-028 AUC=0.626 | ✅ | |
| ≥93.5% outcome-dep | limitations.tex:9 | exp-029 全γ范围≥93.5% | ✅ | |
| ≥89.7% treatment-dep | limitations.tex:9 | exp-040 γ=0.05 cov=0.897 | ✅ | |

---

## B. 跨位置一致性

| 数字 | 出现位置 | 值是否一致 | 备注 |
|------|---------|-----------|------|
| R²≥0.97 | abstract:5, intro:17, intro:34, theory:93, experiments:17 | ✅ 一致 | 所有位置均为 ≥0.97 |
| 14.9% sign reversal | abstract:5, intro:13, experiments:19, Fig1 caption | ✅ 一致 | |
| 11 empirical CMs | abstract:5, intro:17, experiments:11, conclusion:4 | ✅ 一致 | |
| AUC 1.0/0.86/0.63 | abstract:6, intro:18,35, method:53, experiments:72, limitations:6 | ✅ 一致 | 各位置引用一致（但registry值存疑，见W1） |
| 7.4× bias reduction | abstract:7, experiments:27 | ✅ 一致 | intro:20 用 0.059→0.008 表述 |
| 0.059 / 0.008 | intro:20, experiments:25,27, Table 1 | ✅ 一致 | |
| 5.9× CF amplification | intro:14, experiments:33 | ✅ 一致 | |
| 260/520 (50%) | theory:120, experiments:18 | ✅ 一致 | |
| 2.86× / 2.41× | theory:120, experiments:18 | ✅ 一致 | |
| 93.8% CF coverage | experiments:65, appendix:1101 | ✅ 一致 | |
| 89% R-learner | experiments:34, appendix:488,835 | ✅ 一致 | |
| 0.179→0.007 (PPCI) | method:60, appendix:488,518 | ✅ 一致 | |
| γ_T=0.10 → 75% | theory:98 | ✅ | 仅出现一次（正文），appendix table确认 |
| F-L 0.122 / 0.168 | theory:54, experiments:26, Table 1 | ✅ 一致 | |
| F-L 2.1× / 2.9× | theory:54, intro:14(仅2.9×) | ✅ 一致 | |
| RMSE change ≤4% vs <5% | method:12 vs method:21 | ❌ 不一致 | 见问题 W2 |

---

## C. 四舍五入一致性

| 类型 | 小数位数 | 示例 | 一致? |
|------|---------|------|-------|
| |Bias| | 3位 | 0.058, 0.059, 0.008, 0.012 | ✅ |
| RMSE | 3位 | 0.090, 0.099, 0.089, 0.120 | ✅ |
| Coverage | 2位 | 0.82, 0.87, 0.94, 0.96 | ✅ |
| R² | 2-3位 | 0.97, 0.994, 0.976 | ✅ 可接受（≥0.97用2位，具体值用3位） |
| AUC | 2位 | 0.86, 0.63, 1.0 | ✅ |
| 百分比 | 1位或整数 | 14.9%, 31%, 93.8%, 89% | ✅ |
| 倍数 | 1-2位 | 7.4×, 4.7×, 2.86×, 2.41× | ⚠️ 不完全一致 |

倍数的小数位数不统一：7.4×/4.7×/4.9×/5.9× 用1位，2.86×/2.41× 用2位。但 2.86 和 2.41 是精确的 max 值（registry 直接存储），而 7.4/4.7/4.9 是从 table 值推导的四舍五入。逻辑上合理但格式不完全统一。**建议统一为1位或注明 max 值保留2位。**

---

## 问题汇总

### [CRITICAL] C1: method.tex:61 DGP 标签错误

**位置**: method.tex:61
**内容**: "under outcome-side error alone (DGP~C)"
**问题**: DGP C 在 appendix PPCI table 中定义为 "both errors"（covariate + outcome），而 "outcome-side error alone" 对应 DGP B。DGP 标签写反。

**修复**: 将 "(DGP~C)" 改为 "(DGP~B)"。

### [CRITICAL] C2: method.tex:61 PPCI |bias| 值不匹配

**位置**: method.tex:61
**内容**: "PPCI achieves $|\text{bias}| = 0.003$--$0.004$"
**问题**: 无论对应哪个 DGP，PPCI table 中都没有 0.003–0.004 这个范围：
- DGP B (outcome only) PPCI: |bias| z=0=0.015, z=1=0.020
- DGP C (both) PPCI: |bias| z=0=0.017, z=1=0.007
- DGP D (no error) PPCI: z=0=0.007, z=1=0.003

0.003–0.004 不匹配任何 DGP 的 PPCI 结果。最接近的是 DGP D z=1=0.003，但 DGP D 是 "no error" 场景，语境不对。

**修复**: 需要确认正确的 DGP 标签和对应的 bias 值。如果指 DGP B，bias 应为 0.015–0.020。

### [CRITICAL] C3: method.tex:61 "27% RMSE advantage" 无法复现

**位置**: method.tex:61
**内容**: "under covariate-side error alone (DGP~A), EC-HTE provides a 27\% RMSE advantage over PPCI"
**问题**: 从 PPCI table DGP A 计算：
- EC-HTE avg RMSE = (0.097+0.108)/2 = 0.1025
- PPCI avg RMSE = (0.162+0.168)/2 = 0.165
- Advantage = 1 - 0.1025/0.165 = **37.9%**，非 27%

尝试了多种聚合方式（单z-level, 几何均值等），均无法得到27%。

**修复**: 需要确认计算方式。如果是从 table 直接推导，应改为约38%，或注明计算口径。

### [WARNING] W1: AUC=0.86 与 registry 不完全匹配

**位置**: abstract:6, intro:18,35, method:53, experiments:72, limitations:6
**Registry**: exp-005 subgroup AUC=0.833
**Paper**: 0.86

**分析**: ROC figure caption 标注 "Δπ-only condition (AUC = 0.86)"。exp-005 registry 中 "Subgroup correlation: 0.86" 与 "Subgroup AUC: 0.833" 是两个不同指标。论文中统一称为 "AUC=0.86"，但 registry 的实际 AUC 是 0.833。可能是不同评分规则（Proposition 2 score vs Δπ-only score）给出的不同 AUC 值。

**建议**: 确认论文中的 0.86 对应 ROC 曲线中哪条具体曲线的 AUC，确保描述准确。

### [WARNING] W2: method.tex 内部 hyperprior sensitivity 不一致

**位置**: method.tex:12 说 "RMSE change ≤4%"，method.tex:21 说 "<5% RMSE variation"
**Registry**: exp-022 报告 K2 <1%, K4 ≈4-5%
**Appendix**: appendix.tex:278 说 "<1% RMSE variation for K=2 and ~4-5% for K=4"

**问题**: K=4 的 RMSE 变化为 4-5%，超过 method.tex:12 的 "≤4%" 声明，但符合 method.tex:21 的 "<5%"。同一篇论文中两处描述不一致。

**修复**: 将 method.tex:12 的 "≤4%" 改为 "≤5%" 或 "<5%"，与 method.tex:21 和 appendix 保持一致。

### [WARNING] W3: theory.tex R² 与 registry 差 0.001

**位置**: theory.tex:67 说 R²=0.991（asymmetric），appendix.tex:437 同
**Registry**: exp-014 R²=0.992

**分析**: 差 0.001，可能是四舍五入差异（0.9915 四舍五入到 0.991 或 0.992）。影响极小。

### [WARNING] W4: appendix asymmetric bias reduction 4× vs registry 4.2×

**位置**: appendix.tex:439 "4× improvement"
**Registry**: exp-014 bias_reduction_vs_global=4.2×
**Table**: 0.025/0.006=4.17

**分析**: 论文约为 4×（0.025→0.006），精确计算为 4.17×。Registry 存 4.2×。论文用 4× 是粗略近似，差异不大但略不精确。

### [WARNING] W5: Figure 1 caption "7.5% of subgroup estimates"

**位置**: intro.tex:28
**问题**: 7.5% 是 subgroup-estimate level 的 sign reversal rate（vs 14.9% 是 configuration level）。该数字未作为 registry 顶层指标存储，需从原始实验 CSV 验证。

**建议**: 确认 7.5% 的具体计算口径（哪些 subgroup × z-level estimates 中有 7.5% 出现符号翻转）。

---

## 其他检查

### 8 LLMs 计数验证
- 论文声称 "8 LLMs" (experiments.tex:11)
- appendix realcm_bias (appendix.tex:951) 列出 8 个模型: GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B
- 另有 GPT-5.4（exp-008 multi-LLM）和 Llama-3.1-8B（appendix open-source）未纳入 "8 LLMs" 主体分析
- ✅ 计数正确

### 16 model–dataset–K combinations 验证
- appendix screening table (appendix.tex:996-1016): 正好 16 行
- 4 open-source × TweetEval × K=2 + 4 open-source × TweetEval × K=4 + 5 proprietary × TweetEval × K=4 + 3 proprietary × CivilComments × K=4 = 4+4+5+3 = 16
- ✅ 正确

### Policy reversal table 内部一致性
- τ(0)=0.03, extreme: τ̂=-0.059 (appendix.tex:1501)
- intro.tex:13,28: "true τ=+0.03, estimated τ̂=-0.059"
- ✅ 一致

---

## 结论

**共检查 ~80 个关键数字。**

- **3 个 CRITICAL 问题** (method.tex:61): DGP 标签错误(C→B)、PPCI |bias| 值不匹配(0.003-0.004 无出处)、27% RMSE advantage 无法复现(实际≈38%)。三个问题出现在同一句话中，需要整体修改。
- **5 个 WARNING** (W1-W5): AUC 0.86 vs registry 0.833 需澄清、hyperprior sensitivity ≤4% vs <5% 内部不一致、两处 ≤0.001 的四舍五入差异、一处未验证的 Figure 数字。
- **其余所有数字均与 registry 精确匹配或在合理四舍五入范围内。**

**优先修复**: method.tex:61 的三个 CRITICAL 问题（同一句话），以及 method.tex:12 的 ≤4%→<5%。
