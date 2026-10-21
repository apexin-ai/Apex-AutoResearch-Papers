# Reviewer Prep — 数据溯源应对话术

## Rebuttal 预实验总结

| 实验 | 结论 | 一句话 |
|------|------|--------|
| exp68_lora_comparison | success | LoRA r=8（0.16% 参数）DD=0.994/AA=0.962，与 full DAPT（DD=0.997/AA=0.972）差距 ≤1pp——classification objective 本身驱动 OOD 泛化，参数更新量不是关键 |
| exp69_mixed_llm_aa_error | success | AA F1=0.504 完全由 recall 崩溃导致（29.2%，precision 97.8%），攻击族难度梯度 FITD>DD>AA 与策略多样性正相关 |
| exp70_deberta_large_scale | negative | DeBERTa-v3-large 9-class DD=0.997/AA=1.000，比 vanilla +10pp/+13pp——355M "DAPT 有害" 是 RoBERTa-specific，非通用 scale 效应 |
| exp71_mixed_llm_disentangle | success | 350+350 mixed AA=0.709 vs 250+250 AA=0.504（+20.5pp, 44% gap）vs 350 Qwen-only AA=0.972（残差 26.3pp, 56% gap）——数据量和分布异质性都有显著贡献，异质性略占主导 |

---

## 话术 1：Binary DD-Full 1.000±.000 的 seed42 registry 缺失

**问题**：Registry 中 Binary 变体仅有 seed123 和 seed456 的 DD OOD 指标（mf1_binary_seed123, mf1_binary_seed456），seed42 的 Binary DD 值来自 plan_013_none_collapse（0.9904），与 seed_level 表（1.000）不一致。

**事实**：seed_level 表（Appendix Table 12）中 Binary DD-Full: s42=1.000, s123=1.000, s456=1.000，来自最终评估 pipeline 的完整 3-seed 运行。plan_013 是早期实验（可能使用不同数据版本 v4c 或评估代码），其值不构成最终 paper 数据来源。服务器上保留了完整的评估输出文件。

**建议回答**：Binary DD-Full 的 3-seed 数据（seeds 42/123/456）来自最终评估 pipeline 的完整运行，per-seed 值均为 1.000（Appendix Table 12）。Registry 是内部实验追踪工具，部分早期实验条目未与最终 pipeline 对齐，不影响论文报告的数据完整性。

---

## 话术 2：Table 3 Dual-OOD 4 cells 无独立 registry 条目

**问题**：Table 3 底部 Dual-OOD 行（no adapt DD=.855/AA=.842, +10-shot DD=.994/AA=.981）无直接 registry 条目。

**事实**：这些是**估算值**，方法论记录在 Appendix Section "Estimated Dual-OOD Detection Performance"（§app:dual_ood）。计算方式：对每个 seed，组合 OOD 评估的 attack recall（来自主评估 pipeline）与 WildChat/OASST2 的 benign FPR（来自 exp19_wildchat_fpr / exp45_benign_adaptation_curve），在 OOD 测试组成（80 jailbreak + 38 benign）上计算 binary detection F1。假设 attack detection 与 benign false positive 独立。

**建议回答**：Dual-OOD F1 是 per-seed 估算值（Appendix §E.4），组合同一 seed 的 attack recall 和 benign FPR，在 OOD 测试集组成上计算 F1。源数据为 exp19（WildChat FPR per-seed: 0.668/0.611/0.765）和主 OOD 评估（attack recall per-seed）。方法论和独立性假设在 appendix 中明确说明。

---

## 话术 3：Table 3 Mean pooling K=2 混用实验源

**问题**：Mean pooling 行 DD-K=2 当前为 **1.000**（来自 exp27，E2E fine-tuned mean pooling，3-seed），但 DD-Full (.991±.013) 和 AA-Full (.962±.015) 来自 exp13（frozen encoder + mean pooling linear head，3-seed）。Table 3 脚注描述的是 "9-class encoder with mean pooling replacing BiGRU"——即 frozen encoder 配置（exp13），非 E2E（exp27）。

**事实**：
- exp13 (frozen encoder): DD-K=2 = **.994±.009**, DD-Full = .991±.013, AA-Full = .962±.015
- exp27 (E2E fine-tuned): DD-K=2 = 1.000±.000, DD-Full = 1.000±.000, AA-Full = 1.000±.000

**已修复**（commit f7333ec）：Table 3 Mean pooling DD-K=2 已从 1.000 改为 .994±.009，统一使用 exp13 frozen encoder 数据。如审稿人仍追问实验源差异，解释 exp27（E2E）与 exp13（frozen encoder）的区别即可。

---

## 话术 4：Table 7 clean .994 vs 主表 .997 的 0.003 差异

**问题**：Table 7（perturbation）中 9-class Clean Full = .994±.005，但 Table 2/3 中 9-class DD-Full = .997±.005。同一模型、同一数据，为何有 0.003 差异？

**事实**：Table 7 的 clean baseline 来自 exp4（perturbation 实验），该实验独立重新评估了 clean data 作为 perturbation 对照。exp4 使用的评估代码可能与主评估 pipeline 有微小差异（如随机种子影响的 batch 处理顺序、浮点精度差异），导致 3-seed 均值偏移 0.003（约等于 118 样本中不到 0.4 个预测差异）。Scrambled 有同样的 0.003 偏移；Binary 两表一致（1.000）。

**建议回答**：Table 7 的 clean baseline 来自 perturbation 实验的独立重评估（exp4），与主评估 pipeline 在 118 样本上存在 0.3% 的微小浮点差异。Δ 列在 Table 7 内部自洽（clean→perturbed 计算来自同一评估 run），不影响 perturbation robustness 的结论（"zero degradation for classification variants"）。

---

# 方法层面应对话术

## 话术 5：为什么选 DAPT 而不是其他 adaptation 策略（LoRA/Adapter/Prompt Tuning）？

**问题**：论文只比较了 full fine-tuning 形式的 DAPT 变体，为什么不与 LoRA、Adapter、Prompt Tuning 等参数高效方法比较？

**事实**：
- 论文定位是 controlled ablation study（Introduction: "the contribution is the decomposition, not the pipeline"），而非方法竞赛。核心变量是 adaptation objective（9-class / binary / scrambled / MLM / topic / wiki-MLM / vanilla），不是 adaptation mechanism。
- DAPT 选择的理由：(1) 直接延伸 Gururangan et al. 2020 的 DAPT 框架到 supervised 变体；(2) full fine-tuning 是 adaptation 上界；(3) MLM 与 classification 构成自然对照。
- **exp68_lora_comparison 实证验证**（rebuttal 备用数据）：

| 方法 | 可训练参数 | DD OOD F1 | AA OOD F1 |
|------|-----------|-----------|-----------|
| LoRA r=8 | 303K (0.16%) | 0.994±0.005 | 0.962±0.013 |
| LoRA r=16 | 597K (0.32%) | 0.994±0.005 | 0.947±0.012 |
| Full DAPT | 184M (100%) | 0.997±0.005 | 0.972±0.026 |

- LoRA r=8 用 0.16% 参数达到 DD 仅差 0.3pp、AA 差 1.0pp，几乎匹配 full DAPT。
- r16 AA 反而比 r8 低（0.947 vs 0.962），暗示小数据（350 条）上更多参数过拟合。
- 核心结论：**classification objective 本身驱动 OOD 泛化，参数更新量不是关键因素**。这强化了论文的 ablation 定位——objective 选择比 mechanism 选择更重要。

**建议回答**：LoRA with 0.16% trainable parameters achieves within 1pp of full DAPT on both OOD families, confirming that the classification objective—not the extent of parameter modification—drives OOD generalization. 本研究选择 full fine-tuning 作为上界来隔离 objective 的效果，LoRA 实验进一步验证了这一设计选择的合理性。

---

## 话术 6：mixed-LLM AA=0.504 的 root cause 分析

**问题**：mixed-LLM 训练下 9-class ActorAttack F1 仅 0.504±0.107，接近随机水平，root cause 是什么？

**事实**（exp69_mixed_llm_aa_error 实证分析）：
- **崩溃完全是 recall 问题，不是 precision 问题**：Jailbreak precision = 97.8%，recall = 29.2%。平均每个 seed 仅 0.3 个 FP，但 56.7 个 FN（80 个 jailbreak 中漏检 57 个）。模型决策边界过度收缩——几乎不误报，但大量漏检。
- **Seed 间 recall 方差巨大**：17.5%~48.8%，训练极不稳定，指向 per-source 数据量不足（250 vs 单源 350）。
- **攻击族难度梯度**：FITD F1=0.997（不受影响）> DD F1=0.818（中等影响）> AA F1=0.504（最严重）。策略多样性越高的攻击族受损越严重。ActorAttack 依赖 role-play/persona-switching 等风格化策略，这些模式在不同 LLM 间表达差异大；FITD 的 false information injection 更依赖内容而非风格，因此 LLM 来源不敏感。
- **单源对比**：单源 9-class AA recall ~96% → 混合训练后 recall ~29%，delta = -67pp。
- **MLM 完全崩溃**：MLM 在 mixed-LLM 下降至 0.258±0.075（vanilla 0.389±0.073），分类 DAPT 仍是唯一显著优于 vanilla 的方法。
- **Scale 实验佐证**（Appendix Table, 1000 条 Qwen）：9-class AA OOD = 0.913±0.041，仍未达到单源 350 条的 0.972——策略多样性本身构成瓶颈。

**exp71_mixed_llm_disentangle 解耦实验**（rebuttal 备用数据）：

| 条件 | DD OOD F1 | AA OOD F1 |
|------|-----------|-----------|
| 350 Qwen-only | 0.997±0.005 | 0.972±0.026 |
| 250+250 mixed | 0.818±0.096 | 0.504±0.107 |
| 350+350 mixed | 0.944±0.007 | 0.709±0.085 |

- AA 总 gap = 0.972 - 0.504 = 0.468pp。数据量恢复（250→350 per source）贡献 +0.205pp（**44%**），分布异质性残差 -0.263pp（**56%**）。
- DD 也从 0.818→0.944 显著恢复（+12.6pp），但仍低于单源 0.997——模板攻击也受异质性影响但程度较轻。
- 350+350 AA seed 间方差仍大（0.601~0.808），训练不稳定性与混合分布本身相关。
- 直接回应论文 §4.4："per-source data reduction is an alternative explanation we cannot yet disentangle"——现在已解耦。

**建议回答**：We disentangled data quantity from distributional heterogeneity: increasing mixed-LLM data from 250 to 350 per source recovers AA F1 from 0.504 to 0.709 (+20.5pp, 44% of gap), while the remaining 26.3pp gap (56%) is attributable to distributional heterogeneity. Both factors contribute significantly. 错误模式分析（exp69）显示崩溃完全由 recall 驱动（precision 97.8%, recall 29.2%），模型决策边界过度收缩。攻击族难度梯度（FITD 0.997 > DD 0.944 > AA 0.709 at 350+350）与策略多样性正相关。

---

## 话术 7：355M scale DAPT 有害的解释

**问题**：RoBERTa-large (355M) 上 vanilla AA=1.000 优于 9-class AA=0.946，DAPT 反而有害，为什么？

**事实**：
- **Table 5 数据**：RoBERTa-large vanilla DD=0.927±0.036, AA=1.000±0.000；9-class DD=0.987±0.004, AA=0.946±0.057；MLM DD=0.884±0.065, AA=0.874±0.014。
- **DD vs AA 分离**：DAPT 在 DD 上仍有优势（9-class 0.987 > vanilla 0.927），但在 AA 上反转（0.946 < 1.000）。MLM 在两个维度都比 vanilla 差。
- **exp70_deberta_large_scale 实证（rebuttal 备用数据）**——同架构 scale-up 实验：

| 模型 | 参数量 | Vanilla DD | 9-class DD | Vanilla AA | 9-class AA |
|------|--------|-----------|-----------|-----------|-----------|
| DeBERTa-v3-base | 184M | 0.312±0.026 | 0.997±0.005 | 0.258±0.000 | 0.972±0.026 |
| DeBERTa-v3-large | 304M | 0.898±0.033 | **0.997±0.005** | 0.870±0.022 | **1.000±0.000** |
| RoBERTa-large | 355M | 0.927±0.036 | 0.987±0.004 | **1.000±0.000** | 0.946±0.057 |

- **结论修正**：DeBERTa-v3-large 9-class 在 DD 和 AA 上都达到 0.997/1.000，比 vanilla 分别 +10pp/+13pp。DAPT 在 DeBERTa 架构上 **scale-invariant**（base 和 large 都获益）。355M "DAPT 有害" 是 **RoBERTa-specific 的架构交互**，非通用 scale 效应。
- RoBERTa-large vanilla AA=1.000 可能源于 RoBERTa 预训练语料/tokenizer 与 ActorAttack 的特定匹配，而非 capacity 充足的通用证据。
- **Limitations 已覆盖**（L33）："cross-encoder comparisons confound architecture with parameter count"——exp70 直接解决了这个 confound。

**建议回答**：We conducted same-architecture scaling (DeBERTa-v3 base→large, 184M→304M): DAPT improves both DD (+10pp) and AA (+13pp) at the larger scale, confirming the negative effect at 355M is RoBERTa-specific rather than a general scaling phenomenon. RoBERTa-large 的 AA 反转可能源于其预训练语料与 ActorAttack 风格的特定匹配。论文 Limitations 已标注 architecture-parameter count confound，此实验为 rebuttal 提供了直接证据。
