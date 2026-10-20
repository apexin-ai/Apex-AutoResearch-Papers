# 正文数据审计报告

**审计日期**: 2026-05-25
**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, related_work.tex (含 Table 1)
**数据源**: experiment registry (60 experiments), included tables (tab_*.tex)

## 统计
- 总定量声明数：~160
- 已验证（与 Registry 一致）：~135
- 问题数：6（含 2 个 major、4 个 minor）
- 暂无出处/需独立验证：~19

---

## 逐章节审计

### Abstract

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| "order of magnitude" TF-AR gap | d048_final_ar_eval: 8–17× | ✓ | 8–17× ≈ 1 order of magnitude |
| "collapses by an order of magnitude" | 同上 | ✓ | |
| "near parity on Qwen" (SS) | d048_final_ar_eval + d048_eval_ss_s123/s456: gap 1.24× | ⚠️ minor | 1.24× 称为 "near parity" 可接受 |
| "no perplexity cost" (SS) | d048_final_ar_eval: TG PPL 1.432, SS PPL 1.442 (Δ=0.7%) | ✓ | |
| Two architectures (Qwen-2.5-7B, Llama-3.1-8B) | 多个 Llama 实验确认 | ✓ | |

### Introduction

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| "goal attention drops by over 70% within just five turns" | phase1_gar_diag: relative_drop=0.708=70.8% | ✓ | |
| AUC = 0.98 | N/A | 文献引用 | 来自 Dongre et al. (2026) |
| Fig 1 caption: "85–90% decay" | phase1_gar_diag: turn1→turn10 = 84.7%; analysis_attention_heatmap: base=87.5% | ⚠️ minor | 对 base 模型大致正确 (85–87.5%), 但 fine-tuned 仅 77–81%。Caption 未区分 |
| Fig 1 caption: "8–17×" | d048_final_ar_eval: 7.81–16.7× | ✓ | 7.81→8, 16.7→17 |
| Fig 1 caption: "7.8× to 1.3× (Qwen)" | d048_final_ar_eval + SS multi-seed | ⚠️ minor | 7.8× ✓; ~1.3× 实际为 1.24×（多种子均值） |
| Fig 1 caption: "~27× to 2.9× (Llama)" | eval_llama_ar_n20 + p1_llama_ss_eval | ✓ | 27.0× ✓; 2.87× ≈ 2.9× ✓ |
| Contribution 2: "p = 0.002, effect reverses" | 无 registry entry | ❓ | p=0.002 在正文引用但 registry 无统计检验记录 |
| Contribution 4: "~1.3× on Qwen and ~2.9× on Llama" | 同上 | ⚠️ | ~1.3× 偏高，同 Fig 1 caption |

### Method

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| GAR-Dongre ~0.01–0.02 in multi-turn | phase2_4way_eval_heldout: 0.0124–0.0152 | ✓ | |
| GAR-ours range 0.019–0.50 | d048_final_ar_eval (AR Base=0.019) + table (TF=0.50) | ✓ | |
| r = 0.200, p = 0.007 (GAR–compliance) | instruction_retention_test: r=0.2003, p=0.007 | ✓ | |
| ~57K parameters | 架构设计值 | ✓ | 28 layers × ~2K params/layer ≈ 57K |
| <0.001% of 7B | 57K/7B = 0.00081% < 0.001% | ✓ | |
| σ(1.5) ≈ 0.82 | 数学计算 | ✓ | sigmoid(1.5)=0.8176≈0.82 |
| proj to 16; emb 16-dim; 32→64→1 | 架构设计值 | — | 设计选择 |
| σ_min = 0.05; λ_GAR = λ_div = 1.0 | 超参设计值 | — | |
| 10× learning rate multiplier | 超参设计值 | — | |
| UG: L3=0.777, L27=1.000 | phase2_ug_s42 notes | ✓ | |
| Seven iterations, four loss families | 项目历史 (v1–v7) | — | |

### Experiments

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| lr = 2×10⁻⁴, batch 1, accum 8, seed 42 | phase2_tg_s42_v8_schedsampling spec | ✓ | |
| 8K conversations from UltraChat | tab_dataset_stats: Training=8,000 | ✓ | |
| 3 epochs, ~6 hours | phase2_tg_s42_v7: 3 epoch, 21352s=5.9h | ✓ | |
| RTX PRO 6000 Blackwell, 96 GB | llama_tg_s42 GPU; 96GB = nominal spec | ✓ | |
| **Table 1 IID TG: GAR-O=0.50** | phase2_4way_eval: TG=0.4866 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |
| Table 1 IID UG: GAR-O=0.49 | phase2_4way_eval: UG=0.4923 → 0.49 | ✓ | |
| **Table 1 IID LO: GAR-O=0.50** | phase2_4way_eval: LO=0.4860 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |
| Table 1 IID PCGrad: GAR-O=0.50 | phase2_tg_s42_v9_pcgrad: 0.5002 → 0.50 | ✓ | |
| **Table 1 IID PPL: all fine-tuned = 2.78** | phase2_4way_eval: TG/UG/LO PPL=2.62–2.63 | ⚠️ MAJOR | 见 ISSUE-1 |
| Table 1 Held-out: all values | phase2_4way_eval_heldout | ✓ | 全部匹配 |
| Table 1 AR: all values | d048_final_ar_eval | ✓ | Base=0.019, TG=0.064, UG=0.033, LO=0.037, PC=0.030 |
| Table 1 CI values | d048_final_ar_eval bootstrap | ✓ | |
| Table 1 gate: TG .93±.05, UG .96±.05 | phase2_tg_s42_v7/phase2_ug_s42 | ✓ | |
| "GAR-ours spans 0.49–0.51 (≤2 pp)" | Table 1 values | ✓ | |
| "PPL is 2.78 for all" | Table 1 | ✓ | 表中如此，但 IID 数据来源存疑 |
| **"held-out GAR-ours differs by ≤1 pp"** | 各变体 IID→held-out diff 最大 1.7pp | ⚠️ MAJOR | 见 ISSUE-2 |
| "GAR-Dongre remains low (0.01–0.02)" | Table 1 | ✓ | |
| "8–17× gap" | d048_final_ar_eval | ✓ | 7.81–16.7× → 8–17× |
| "TG 0.064 > LO 0.037 > UG 0.033 > PC 0.030 > Base 0.019" | d048_final_ar_eval | ✓ | |
| "TG vs LO significant (p=0.004)" | 无 registry entry | ❓ | 来自统计检验脚本 |
| "gap remains 7.8×" | 0.50/0.064=7.81 | ✓ | |
| "second seed: 0.504±0.001" | eval_v7_tg_s123: 0.5052; heldout s42: 0.5035 | ✓ | mean=0.504, ±0.001 |
| "MMLU within 0.8 pp" | mmlu_eval_all: max Δ=0.77pp | ✓ | |
| §4.3: "β=3 → GAR=0.556 (9% PPL cost)" | attention_steering_gen_n50: 0.5558, (1.56-1.43)/1.43=8.9% | ✓ | |
| "β=5: GAR 0.727±0.061 (PPL 1.77)" | attention_steering_gen_n50: 0.7271±0.0605, PPL 1.7723 | ✓ | |
| "PPL below 1.8 in [3,5]" | β=3: 1.56, β=5: 1.77 | ✓ | |
| "+11.1 pp late-turn compliance" | instruction_retention_test: delta=0.111 | ✓ | |
| "p=0.077" (McNemar) | instruction_retention_test: 0.0771 | ✓ | |
| "+23.8 pp content-constrained" | instruction_retention_test: 0.238 | ✓ | |
| §4.4: "AR GAR 0.401±0.047" (SS 3-seed) | mean(0.347,0.4231,0.4325)=0.4009, std=0.0469 | ✓ | |
| **"gap from 7.8× to ~1.3×"** | 0.4992/0.4009=1.245 | ⚠️ minor | 见 ISSUE-3 |
| **"TF GAR 0.498±0.004"** | mean(0.4983,0.503,0.4964)=0.4992, std=0.0034 | ⚠️ minor | 见 ISSUE-4 |
| "PPL 1.441±0.001" | mean(1.442,1.4408,1.4394)=1.4407, std=0.0013 | ✓ | |
| "β=5: 0.717±0.001, std 0.047→0.001" | mean(0.717,0.7174,0.7157)=0.7167, std=0.0009 | ✓ | |
| "Llama SS: ~27× to 2.9×" | p1_llama_ss_eval: gap=2.87 | ✓ | |
| "fewer epochs (2 vs 3)" | p1_llama_ss_training spec: epochs=3 | ⚠️ minor | 见 ISSUE-6 |

### Analysis

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| Fig 4: "77–81% decay" | analysis_attention_heatmap: TG=77.7%, LO=81.0% | ✓ | |
| "Δ=3.3 pp TG vs LO" | 81.0−77.7=3.3 | ✓ | |
| "Base decays 87.5%" | analysis_attention_heatmap: 0.875 | ✓ | |
| §5.1: "27/28 layers" gate inversion | 无 registry entry | ❓ | gate 分析脚本 |
| "Wilcoxon p=3.73×10⁻⁸, r=0.975" | 无 registry entry | ❓ | 同上 |
| "layer 23: 0.769→0.979" | 无 registry entry | ❓ | 同上 |
| "0.93–0.98 (2–7% attenuation)" | phase2_tg_s42_v7: mean=0.93 | ✓ | 1−0.93=7%, 1−0.98=2% |
| "L3=0.777, L27=1.000" (UG) | phase2_ug_s42 | ✓ | |
| §5.2: "68–79% of layers" | analysis_gradient_conflict: 67.9–78.6% | ✓ | |
| "cos_sim −0.089→−0.042" | analysis_gradient_conflict | ✓ | |
| "NTP mag 7.5× to 14.7×" | analysis_gradient_conflict | ✓ | |
| "AR GAR worsens: 0.064→0.030" | d048_final_ar_eval: TG=0.064, PC=0.030 | ✓ | |
| "(p=0.002)" | 无 registry entry | ❓ | |
| "Llama cos=+0.005" | p2_llama_gradient_conflict: 0.0045→0.005 | ✓ | |
| "25.7× NTP dominance" (Llama) | p2_llama_gradient_conflict: 25.7 | ✓ | |
| §5.3: "77–87% per-turn decay" | analysis_attention_heatmap | ✓ | |
| §5.4: TRC 0.334/0.332 (TG, gap +0.002) | trc_baseline_v7_tg: 0.3339/0.3323/+0.0016 | ✓ | |
| TRC 0.349/0.411 (LO, gap −0.062) | trc_baseline_v7_tg: 0.349/0.4106/−0.0617 | ✓ | |
| "GAR-Dongre: Llama 1.002×" | llama_ar_matched_eval: 0.018/0.018=1.0 | ✓ | |
| "GAR-Dongre: Qwen 1.28×" | 无明确 registry 来源 | ⚠️ | |
| §5.5: Llama TF 0.484(TG)/0.481(LO) | llama_eval_s42: 0.4836; eval_llama_lora_only_s42: 0.4807 | ✓ | |
| "medians: 0.018(TG,LO), 0.009(Base)" | eval_llama_ar_n20: 0.0179/0.0184/0.0093 | ✓ | |
| "gaps of 27× and 26×" | 0.484/0.018=26.9≈27; 0.481/0.018=26.7≈27 | ✓ | |
| "CoV > 100%" | eval_llama_ar_n20: CoV=231% | ✓ | |
| "Llama SS TF 0.477, AR 0.166" | p1_llama_ss_eval: 0.477, 0.1662 | ✓ | |
| "β=3: Qwen SS 0.593" | d048_final_ar_eval: beta3.ss=0.593 | ✓ | |
| "β=3: Llama SS 0.173" | 无 registry entry | ❓ | |
| "Llama β=5: 0.791" | p1_llama_ss_eval: 0.7905→0.791 | ✓ | |
| "Qwen L1=0.793" | v7_tg_s123 gate profile: L1=0.793 | ✓ | 来自 s123 非 s42 |
| "Llama L25=0.719" | llama_tg_s42 gate profile: L25=0.719 | ✓ | |
| "79.8% GAR decay" (1.5B) | tab_qwen15b: (0.0336−0.0068)/0.0336=79.8% | ✓ | |
| "β-steering to 0.715" (1.5B) | tab_qwen15b: AR β=5 TG=0.7150 | ✓ | |

### Discussion

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| "≤1.3×" (GAR-Dongre shift) | analysis §5.4: Qwen 1.28× | ✓ | |
| "r=0.743" (per-head analysis) | 无直接 registry match | ❓ | p1_tf_ar_kl_divergence gate_kl_correlation=0.11 不匹配 |
| "r=0.200" (GAR–compliance) | instruction_retention_test: 0.2003 | ✓ | |
| "7.5–25.7× NTP dominance" | analysis_gradient_conflict + p2_llama_gradient_conflict | ✓ | |
| "SS=0.717 vs TG=0.727" (β=5) | d048_final_ar_eval | ✓ | |

### Conclusion

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| "GAR=0.50" (TF) | 多处 | ✓ | |
| "order of magnitude" | 同 Abstract | ✓ | |
| "~1.3× (Qwen)" | 同 §4.4 | ⚠️ | 实际 1.24× |
| "~2.9× (Llama)" | p1_llama_ss_eval: 2.87× | ✓ | |

### Related Work

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| "27–48% across 12 models" | N/A | 文献引用 | Dongre et al. |
| "70.8% decline on Qwen-2.5-7B" | phase1_gar_diag: 0.708 | ✓ | |
| "MMLU +2.03 at 15B" | N/A | 文献引用 | Qiu et al. |

### Limitations

| 数字/声明 | Registry 来源 | 状态 | 备注 |
|-----------|-------------|------|------|
| "8K conversations" | tab_dataset_stats | ✓ | |
| "three seeds" (SS) | d048_ss_s42/s123/s456 | ✓ | |
| "τ=0.5" | method 定义 | ✓ | |

---

## 跨章节一致性检查

| 关键数字 | Abstract | Intro | Experiments | Analysis | Discussion | Conclusion | 一致? |
|----------|----------|-------|-------------|----------|------------|------------|------|
| TF GAR ≈ 0.50 | ✓ (implied) | — | 0.49–0.51 | — | — | 0.50 | ✓ |
| AR collapse "order of magnitude" | ✓ | 8–17× | 8–17× | — | ✓ | ✓ | ✓ |
| Gap 7.8× (TG) | — | 7.8× | 7.8× | — | — | — | ✓ |
| ~1.3× SS gap (Qwen) | "near parity" | ~1.3× | ~1.3× | ~1.3× | — | ~1.3× | ✓ (各处一致，但均偏高) |
| ~2.9× SS gap (Llama) | — | — | 2.9× | 2.9× | — | ~2.9× | ✓ |
| p=0.002 (PCGrad) | — | 0.002 | — | 0.002 | — | — | ✓ |
| 0.064 (TG AR) | — | — | 0.064 | 0.064 | — | — | ✓ |
| 0.727 (TG β=5) | — | — | 0.727 | — | 0.727 | — | ✓ |
| 0.717 (SS β=5) | — | — | 0.717 | — | 0.717 | — | ✓ |
| 70%/70.8% decline | — | "over 70%" | — | — | — | — | ✓ vs RW 70.8% |
| r=0.200 | — | — | — | — | 0.200 | — | ✓ vs Method 0.200 |

**所有跨章节数字内部一致，无矛盾。**

---

## 问题清单

### ISSUE-1 [MAJOR]: Table 1 IID 列数据与 Registry 不匹配
- **位置**: related_work.tex Table 1, IID (TF) 列
- **描述**: Table 1 IID 列显示 TG GAR-O=0.50, LO GAR-O=0.50, PPL=2.78。Registry `phase2_4way_eval`（IID eval）记录 TG=0.4866（→0.49）, LO=0.4860（→0.49）, PPL=2.63。Held-out eval (`phase2_4way_eval_heldout`) 则为 TG=0.5035→0.50, PPL=2.78，与表中 IID 值匹配。
- **影响**: 若 IID 列误用了 held-out 数据，则 IID/held-out 对比的有效性被削弱。注意 Base IID PPL=4.23 与 registry 匹配，仅 fine-tuned 模型有差异。PCGrad IID 值来自独立实验 (0.5002, 2.78) 且匹配。
- **可能原因**: (a) IID eval 已用新协议重跑但 registry 未更新；(b) Table 误用 held-out 数据
- **建议**: 确认 IID 列数据来源。若为旧 eval 数据，更新 registry；若为 held-out 误用，需修正。

### ISSUE-2 [MAJOR]: "≤1 pp" 声明应为 "≤2 pp"
- **位置**: experiments.tex §4.2
- **原文**: "IID and held-out protocols produce identical rankings (held-out GAR-ours differs by ≤1 pp)"
- **实际**: IID→held-out 差异: TG 1.7pp, UG 1.3pp, LO 1.2pp, PCGrad 0pp (基于 registry 精确值)。即使在 Table 1 精度下，UG 从 0.49(IID) 变为 0.51(held-out)=2pp。
- **建议**: 改为 "≤2 pp"。或若指 held-out 内部 variants spread (0.75pp)，需重措辞明确。

### ISSUE-3 [minor]: ~1.3× SS gap 偏高于多种子均值
- **位置**: Intro fig caption, Experiments §4.4, Analysis §5.5, Conclusion
- **描述**: 多种子 gap = TF_mean/AR_mean = 0.499/0.401 = 1.245 ≈ 1.2×。s42 单种子 gap = 1.29×（d048_eval_ss_s42）。Paper 称 "~1.3×" 更接近单种子值。
- **建议**: 若引用多种子均值，改为 "~1.2×"；若引用 s42，标注为单种子。

### ISSUE-4 [minor]: SS TF GAR 0.498±0.004 精度偏差
- **位置**: experiments.tex §4.4
- **描述**: 三种子 TF GAR: 0.4983, 0.503, 0.4964 → mean=0.4992≈0.499, std=0.0034≈0.003。Paper 称 0.498±0.004。差异小但精度不匹配。
- **建议**: 修正为 "0.499±0.003"。

### ISSUE-5 [minor]: Fig 1(a) "85–90%" 未区分 base vs fine-tuned
- **位置**: introduction.tex Fig 1 caption
- **描述**: Caption 称 "Goal attention decays 85–90% across turns"。Base model: 84.7–87.5% 符合。Fine-tuned: 77–81%（Fig 4 已正确标注）。Caption 涵盖范围模糊。
- **建议**: 明确为 base model 数据或调整为 "77–87%"。

### ISSUE-6 [minor]: Llama SS "2 vs 3 epochs" 需确认
- **位置**: experiments.tex §4.4, analysis.tex §5.5
- **描述**: Paper 称 Llama SS 训练 "fewer training epochs (2 vs 3)"，但 `p1_llama_ss_training` spec 显示 epochs=3。可能实际只完成 2 epoch 或因 checkpoint 选择使用 epoch_1。
- **建议**: 确认实际 epoch 数并更新 registry 或论文。

---

## 暂无出处的数字

| 数字 | 位置 | 原因 |
|------|------|------|
| p=0.002 (TG vs PCGrad Wilcoxon) | Intro contribution 2, Analysis §5.2 | 无 registry entry；来自统计检验脚本 |
| p=0.004 (TG vs LO Wilcoxon) | Experiments §4.2 | 同上 |
| r=0.743 (per-head TF GAR vs AR shift) | Discussion | p1_tf_ar_kl_divergence 中 gate_kl_correlation=0.11 不匹配 |
| 27/28 layers gate inversion | Analysis §5.1 | gate 分析脚本，非 registry |
| Wilcoxon p=3.73×10⁻⁸, r=0.975 | Analysis §5.1 | 同上 |
| Layer 23: 0.769→0.979 | Analysis §5.1 | 同上 |
| Llama SS β=3 GAR=0.173 | Analysis §5.5 | p1_llama_ss_eval 仅有 β=0 和 β=5 |
| Qwen GAR-Dongre 1.28× | Analysis §5.4 | 无直接 registry 来源 |
| "mean 3.6 user turns" | Table 1 caption | eval 数据统计 |
| 95% CI 边界值 | Table 1 | bootstrap 输出 |
| Pilot gaps "20–34×" | Fig 3(b) caption | N=5 pilot eval |
| "mid-turn GAR above 0.36" | §4.4 | tab_gar_robustness 可交叉验证 |
| AUC=0.98 | Intro | 文献引用 (Dongre 2026) |
| "27–48% across 12 models" | Related Work | 文献引用 (Dongre 2026) |
| "MMLU +2.03 at 15B" | Related Work | 文献引用 (Qiu 2025) |

**建议**: 为 p 值 (0.002, 0.004) 和相关系数 (r=0.743) 补充 registry entry `tab_statistical_tests`，提高可追溯性。

---

## MMLU 详细验证 (tab_mmlu_detail.tex)

| 指标 | 表中值 | Registry (mmlu_eval_all) | 匹配? |
|------|--------|-------------------------|------|
| Base Overall | 74.23% | 0.7423 | ✓ |
| TG Overall | 73.47% | 0.7347 | ✓ |
| PCGrad Overall | 73.86% | 0.7386 | ✓ |
| SS Overall | 73.75% | 0.7375 | ✓ |
| LoRA-only Overall | 73.57% | 0.7357 | ✓ |
| UG Overall | 73.46% | 0.7346 | ✓ |
| Max Δ | −0.77pp | 74.23−73.46=0.77 | ✓ |
| "within 0.8 pp" | 0.77 ≤ 0.8 | | ✓ |

## GAR Robustness 验证 (tab_gar_robustness.tex)

- SS mid-turn GAR >0.36 for all strategies ✓ (Last: 0.458, All: 0.366, First: 0.412, Goal: 0.444)
- §4.4 "mid-turn GAR above 0.36 for all token-position variants" 与表一致 ✓

## Qwen-1.5B 验证 (tab_qwen15b_results.tex)

| 指标 | 表中值 | 验算 | 匹配? |
|------|--------|------|------|
| Turn-1 GAR | 0.0336 | — | ✓ |
| Mid-turn GAR | 0.0068 | — | ✓ |
| Relative drop | 79.8% | (0.0336−0.0068)/0.0336=79.76% | ✓ |
| AR β=5 TG | 0.7150 | — | ✓ |
| p=0.005 (β=0), p<0.001 (β=5) | — | 来自 Wilcoxon 脚本 | ❓ |
