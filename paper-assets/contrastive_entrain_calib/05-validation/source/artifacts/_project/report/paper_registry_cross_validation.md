# 数据自查报告：论文数字 vs Registry 交叉验证

**日期**: 2026-05-23  
**范围**: 论文全部 .tex 文件 vs registry.yaml 全量实验数据  

---

## ⚠️ 不一致 / 需修复

### 1. Abstract/Conclusion vs Discussion: "4/31 (12.9%)" vs "4/28 (14.3%)"

| 位置 | 写法 | 计算 |
|------|------|------|
| Abstract | "4 of 31 checkpoints (12.9%)" | 12(s1) + 16(s2) + 3(gs=8) = 31, 4/31=12.9% |
| Conclusion | "4/31 checkpoints > vanilla" | 同上 |
| Discussion body | "4 of 28 checkpoints (14.3%)" | 12(s1) + 16(s2) = 28, 4/28=14.3% |
| Discussion body | "3/12 for seed 1 (25%), 1/16 for seed 2 (6.3%)" | 3+1=4, 12+16=28 |

**问题**: Abstract/Conclusion 的 31 包含 gs=8 的 3 个 checkpoint，Discussion 的 28 只算 gs=2。两个数字各自正确，但读者会以为指同一件事。Abstract 未说明包含 gs=8。

**建议**: 统一为 4/28 (14.3%) 只计 gs=2，或在 Abstract 明确 "across all group sizes"。

**Registry 验证**:
- Seed 1 (gs=2): 3/12 > vanilla ✅ (ckpt-4500: 0.1337, ckpt-6500: 0.1529, ckpt-8000: 0.1433)
- Seed 2 (gs=2): 1/16 > vanilla ✅ (ckpt-4000: 0.1430)
- gs=8: 0/3 > vanilla ✅

### 2. gs=8 轨迹描述为 "monotonically declining" 但实际先升

**论文 (discussion.tex)**: "monotonically declining trajectory ($0.084 \to 0.085 \to 0.054$)"

**Registry**: ckpt-500=0.0844, ckpt-1000=0.0845, ckpt-1500=0.0538

0.0844 → 0.0845 先微升再降，严格来说不是 monotonically declining。差异极小 (0.0001) 但用词不精确。

### 3. R3 饱和步数: 论文 "by step 300" vs Registry step 100

**论文 (cosine_failure.tex)**: "$\rthree$ saturates at 0.9998 by step 300"

**Registry (exp-002v3)**: r3_saturation_step: 100, r3_saturated_value: 0.9998

数值正确 (0.9998)，但步数不匹配。"by step 300" 技术上包含 step 100，但读者会理解为 "在 step 300 左右饱和"，实际在 step 100 就饱和了。

---

## ✅ 已核对一致

### Direction Quality (Claim 1)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| Qwen3-8B AUROC | 0.827 ± 0.028 | 0.8269 ± 0.0278 | exp-001 |
| Qwen3-8B best layer | L19 | 19 | exp-001 |
| Llama-3-8B AUROC | 0.779 ± 0.019 | 0.7793 ± 0.0189 | exp-012 |
| Llama-3-8B best layer | L16 | 16 | exp-012 |
| Qwen weak AUROC | 0.675 | 0.675 | exp-001 |
| Qwen medium AUROC | 0.883 | 0.883 | exp-001 |
| Qwen strong AUROC | 0.929 | 0.929 | exp-001 |
| Llama weak AUROC | 0.711 | 0.7106 | exp-012 |
| Llama medium AUROC | 0.864 | 0.8635 | exp-012 |
| Llama strong AUROC | 0.911 | 0.9109 | exp-012 |
| Llama geography AUROC | 0.751 | 0.7507 | exp-012 |
| Llama commonsense AUROC | 0.844 | 0.8444 | exp-012 |
| Surface confound AUROC | 0.923 | 0.9227 | exp-012 |
| Probe on learned direction | 0.835 | 0.835 | exp-012 (qwen_d_syc) |
| Probe on random direction | 0.727 | 0.727 | exp-012 (qwen_random) |
| Probe gap | +0.108 | 0.108 | exp-012 (qwen_gap) |
| Num pairs | 181 | 181 | exp-001 |

### Vanilla Baseline

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| SYCONScore | 0.134 | 0.1335 | vanilla-d027-reeval |
| ToF | 0.072 | 0.0718 | vanilla-d027-reeval |
| NoF | 0.945 | 0.9448 | vanilla-d027-reeval |

### R3-only GRPO (Table 1 + Discussion)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| Best SYCONScore | 0.153 | 0.1529 | exp-003-eval-ckpt6500 |
| Best ToF | 0.083 | 0.0829 | exp-003-eval-ckpt6500 |
| Best NoF | 0.983 | 0.9834 | exp-003-eval-ckpt6500 |
| Best step | 6500 | ckpt-6500 | exp-003-eval-ckpt6500 |
| S1 final (ckpt-8000) | 0.143 | 0.1433 | exp-003-eval-ckpt8000 |
| S2 peak | 0.143 (step 4000) | 0.1430 | exp-003-eval-s2-ckpt4000-v2 |
| S2 final (ckpt-8000) | 0.124 | 0.1240 | exp-003-eval-s2-ckpt8000 |
| 3/12 seed 1 > vanilla | 3/12 (25%) | 3/12 ✅ | 见上方验证 |
| 1/16 seed 2 > vanilla | 1/16 (6.3%) | 1/16 ✅ | 见上方验证 |
| gs=8 best | 0.085 | 0.0845 | exp-003-gs8-eval-ckpt1000 |
| gs=8 trajectory | 0.084→0.085→0.054 | 0.0844→0.0845→0.0538 | exp-003-gs8-eval-ckpt{500,1000,1500} |
| gs=8 >vanilla | 0/3 | 0/3 ✅ | exp-003-gs8 |

### ACT (Table 1 + Discussion)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| S1 best SYCONScore | 0.301 | 0.3013 | exp-004-eval-ckpt8000-v2 |
| S1 best ToF | 0.182 | 0.1823 | exp-004-eval-ckpt8000-v2 |
| S1 best NoF | 0.867 | 0.8674 | exp-004-eval-ckpt8000-v2 |
| S1 best step | 8000 | ckpt-8000 | exp-004-eval-ckpt8000-v2 |
| S2 best SYCONScore | 0.286 | 0.2858 | exp-004-s2-eval-ckpt7000 |
| S2 best step | 7000 | ckpt-7000 | exp-004-s2-eval-ckpt7000 |
| S1 dip at step 4000 | 0.214 | 0.214 (0.2140) | exp-004-eval-ckpt4000 |
| S1 worst checkpoint | 0.170 | 0.1699 | exp-004-eval-ckpt500 |
| Reduced-LoRA peak | 0.326 (step 7000) | 0.3257 | exp-004-reduced-lora-eval-ckpt7000 |
| Reduced-LoRA final | 0.267 | 0.2673 | exp-004-reduced-lora-eval-ckpt8000 |
| 47/47 all ACT > vanilla | 47/47 | 47/47 ✅ | 16(s1)+15(s2)+16(rl)=47 |
| 31/31 two full seeds | 31/31 | 31/31 ✅ | 16(s1)+15(s2)=31 |
| 16/16 reduced-LoRA | 16/16 | 16/16 ✅ | exp-004-reduced-lora |
| S2 checkpoints count | 15 | 15 ✅ (missing ckpt-3000) | exp-004-s2 |
| 1.7× SFT/GRPO ratio | 1.7× | 0.2673/0.1529=1.748 | reduced-LoRA vs R3-only |

### Cosine Failure (F1a–F1d)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| F1a gradient zeroing step | 955 | 955 | exp-002 notes |
| F1d R3 saturation value | 0.9998 | 0.9998 | exp-002v3 |
| F1d terminal collapse step | 2160 | 2160 | exp-002v3 |
| F1d entropy at kill | 0.006 | 0.006 | exp-002v3 |
| Norms ratio | 100–1,200× | confirmed in exp-002 hypothesis | exp-002/002v2 |
| Cosine gap | 0.098 | avg across layers | exp-002v2 |

### Probe Trap (exp-008v3)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| ckpt-500: ToF | 0.000 | 0.0 | exp-008v3 preset_eval_ckpt500 |
| ckpt-500: NoF | 0.995 | 0.9945 | exp-008v3 |
| ckpt-500: SYCONScore | 0.000 | 0.0 | exp-008v3 |
| ckpt-1000: ToF | 0.006 | 0.0055 | exp-008v3 |
| ckpt-1000: NoF | 0.995 | 0.9945 | exp-008v3 |
| ckpt-1000: SYCONScore | 0.011 | 0.011 | exp-008v3 |
| ckpt-1500: ToF/NoF/SYCONScore | 0/1.000/0 | 0/1.0/0 | exp-008v3 |
| ckpt-2000: ToF/NoF/SYCONScore | 0/1.000/0 | 0/1.0/0 | exp-008v3 |

### Continuous Probe (exp-009)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| ckpt-500: SYCONScore | 0.124 | 0.1238 | exp-009 eval_ckpt500 |
| ckpt-500: ToF | 0.066 | 0.0663 | exp-009 |
| ckpt-500: NoF | 0.934 | 0.9337 | exp-009 |

### ActAdd (exp-016)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| alpha=5 SYCONScore | 0.054 | 0.0537 | exp-016 D027 re-eval |
| alpha=5 ToF | 0.028 | 0.0276 | exp-016 |
| alpha=5 NoF | 0.961 | 0.9613 | exp-016 |

### Held-out Generalization (Limitations)

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| Held-out peak | ~0.20 | 0.2045 | exp-004-heldout-eval-ckpt500 |
| Vanilla held-out | (implicit) | 0.0556 | exp-004-heldout-vanilla-baseline |
| 3.7× vanilla | 3.7× | 0.2045/0.0556=3.68 | 计算验证 ✅ |
| 72% ceiling | 72% | 0.2045/0.2841=71.98% | 计算验证 ✅ |
| ckpt-2000 SYCONScore | 0.157 | 0.1567 | exp-004-heldout-eval-ckpt2000 |
| 2.8× vanilla | 2.8× | 0.1567/0.0556=2.82 | 计算验证 ✅ |
| 146/35 split | 146/35 | n_total=70 (35 pairs) | exp-004-heldout |

### Differentiable Probe Gaming

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| ToF (gamed probe) | 0.978 | 0.978 | exp-014 ckpt-3000 |
| NoF (gamed probe) | 0.006 | 0.006 | exp-014 |
| Gaming onset | ~30 steps | ~30 steps | exp-008 notes |

### Miscellaneous

| 数字 | 论文值 | Registry 值 | 来源 |
|------|--------|-------------|------|
| 1,300-step lag | 1,300 | ~1840-500=1340 | exp-008v3 probe_trap trajectory |
| Llama AUROC (limitations) | 0.779 | 0.7793 | exp-012 |
| 19/200 pairs discarded | 19/200 → 181 | num_pairs=181 | exp-001 |
| ~1.75× ACT LoRA params | ~1.75× | 7/4=1.75 | config |

---

## ❌ 待确认（Registry 无法追溯）

### 1. Direction 稳定性 cosine ≈ 0.96 (direction_quality.tex, framework.tex)

**论文**: "cosine similarity between initial d_syc and re-extracted direction at step 500 is approximately 0.96"

**Registry**: exp-002v2 (GRPO training) 在 step 500 的 mean cosine = 0.2828 (SIGNIFICANT_DRIFT)。这是 GRPO 的数据，与 0.96 完全矛盾。

**推测**: 0.96 可能来自 ACT 训练的 direction 稳定性分析，ACT 是 SFT 方式、模型变化更小。但 Registry 中无 ACT direction stability 数据。

**需要**: 检查 exp-004 训练日志或对应分析脚本的输出确认。

### 2. Post-recalibration AUROC 0.910 (cosine_failure.tex)

**论文**: "offline AUROC from 0.827 to 0.910"

**Registry**: exp002v2-recalib 存在但无 metrics 记录（conclusion: negative）。

**需要**: 检查 recalibration 分析输出文件确认 0.910。

### 3. AUROC 0.76 (full response) → 0.60 (truncated) 

**论文 (cosine_failure.tex, limitations.tex)**: 分析 256-token truncation 对 d_syc AUROC 的影响

**Registry**: 无对应实验。来自独立分析脚本。

**需要**: 检查 truncation analysis 输出确认。

### 4. R3 ~0.98 + p=0.703 (discussion.tex)

**论文**: R3-only GRPO 中 "$\rthree$ saturates at ~0.98 (p=0.703)"

**Registry**: exp-003 无 R3 saturation 数据（仅 exp-002v3 有 R3=0.9998 at step 100）

**需要**: 检查 exp-003 训练日志中的 R3 值和统计检验结果。

### 5. Probe trap entropy/reward 值

| 数字 | 来源需求 |
|------|----------|
| Entropy 0.702 at step 500 | exp-008v3 训练日志 |
| Entropy 0.800 at step 1000 | exp-008v3 训练日志 |
| Entropy 0.608 at step 1500 | exp-008v3 训练日志 |
| Entropy 0.304 at step 2000 | exp-008v3 训练日志 |
| Reward +0.72 at step 500 | exp-008v3 训练日志 |
| Entropy collapse at step ~1840 | exp-008v3 训练日志 |

### 6. AUROC <0.01 variation across GRPO checkpoints

来自 per-checkpoint AUROC 分析，Registry 中 eval 只记录 ToF/NoF/SYCONScore，不记录 AUROC。

### 7. Failure mode taxonomy 百分比

| 数字 | 论文值 | 内部一致性 |
|------|--------|-----------|
| Deliberation traps | 28.7% | |
| Sycophantic stubbornness | 24.3% | |
| Acknowledge-but-maintain | 23.8% | |
| Genuine-accept-missed | 18.8% | |
| Refute/ignore/other | 4.5% | |
| 总和 | 100.1% (rounding OK) | ✅ |
| Top 3 合计 | 76.8% = 28.7+24.3+23.8 | ✅ |

来自手工标注，Registry 无数据。内部算术一致。

### 8. F1c entropy collapse to 0.069 within 300 steps

F1c 是一个 cosine variant 配置，无独立 registry entry。可能来自 exp-002 系列的某个变体训练日志。

### 9. 80–84% truncation rate

来自 GRPO max_completion_length=256 分析，Registry 无数据。

---

## 总结

| 类别 | 数量 |
|------|------|
| ✅ 核对一致 | ~65 个数字 |
| ⚠️ 需修复 | 3 个问题（4/31 vs 4/28 scope 不一致、gs=8 "monotonically" 用词、R3 saturation step 300 vs 100） |
| ❌ 待确认 | 9 个数字/组需检查训练日志或分析脚本 |

**最高优先修复**: Abstract/Conclusion 的 "4/31 (12.9%)" 与 Discussion 的 "4/28 (14.3%)" scope 不一致，审稿人很可能注意到。

**所有可由 Registry 追溯的核心指标（AUROC、SYCONScore、ToF、NoF、checkpoint counts）均与论文一致**，差异仅为四舍五入。
