---
round: 5
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T08:48:24.457712+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 5 (Fresh Re-Review) [修正版]

**论文**: Turn-Residual Gating for Multi-Turn LLMs
**目标 Venue**: EMNLP 2026 (via ARR)
**审稿日期**: 2026-05-25
**Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性)
**模式**: 圆桌审稿 Round 1，交叉回应后收敛
**修正说明**: R1 交叉回应纠正了 R2 三处事实错误（代码链接已存在、Figure 1(b) 已标注 log scale、论文有三层评估非仅 PPL），影响 MF3→SF 降级及代码发布 issue 解决

---

## Summary

本文研究 per-layer residual gating (ThreadGate) 能否缓解多轮 LLM 在自回归解码中的 per-turn grounding 损失。通过 Qwen2.5-7B + ShareGPT 上五种训练条件（Base, ThreadGate, TG+PCGrad, Uniform Gate, LoRA-only）的系统对比，论文报告所有 gating 变体均无法弥合 teacher-forcing 与 autoregressive 模式下 20-33× 的 GAR 差距，将此归因于 exposure bias 而非 gradient conflict。Llama-3.1-8B 上仅 3/5 条件的跨模型复制部分支持该发现。诊断性 β-steering 干预可部分恢复 GAR 但下游改善微弱（p=0.077）。

---

## Strengths

**S1. 系统的五路条件对比**
Base / ThreadGate / TG+PCGrad / Uniform Gate / LoRA-only 覆盖从无干预到 gradient conflict 缓解的合理消融范围。逐对因素隔离设计精良（R1 肯定），实验逻辑清晰。

**S2. 有价值的负面结果**
证明 lightweight per-layer gating 无法解决 TF-AR grounding gap，对社区有实际意义——避免后续研究重复尝试类似方案。

**S3. Exposure bias 假说具启发性**
将 multi-turn grounding 失败从架构层面转向训练范式层面（exposure bias），为社区提供新研究方向。SS 条件下 GAR 改善约 8.5× 间接支持这一假说。

**S4. β-steering 诊断工具**
推理时注意力操控作为诊断手段具有方法论创新性，为理解 LLM 内部 attention dynamics 提供可复用工具。

**S5. 多层评估 + 丰富附录**
主文包含 instruction retention（N=200, 18 constraint categories, McNemar 检验）+ MMLU 5-shot + PPL 三层评估。35 页附录覆盖 v1-v7 loss iterations、gate value distributions、per-turn breakdowns、bootstrap CIs 等。代码和数据已通过匿名链接提供。

---

## Weaknesses

### Must-Fix (阻碍接收的关键问题)

**MF1. 因果排除链不完整——exposure bias 声称过强** [R1-N2 + R2-N1, 强共识]

论文将 exposure bias 定位为 TF-AR gap 的根因，但因果排除链存在关键缺口：
- **KV cache drift 未排除**：TF 使用 ground-truth prefix，AR 使用模型生成 prefix，两者 KV cache 内容本质不同。§7 Limitations 自己承认未排除这一混淆变量。
- **NTP magnitude imbalance**：§5.2 显示 NTP loss magnitude 碾压 GAR loss 7.5-14.7×。PCGrad 仅消除方向冲突（cosine < 0），不处理量级碾压——PCGrad 失败可能反映投影副作用而非 gradient direction conflict 不存在。
- **Appendix L 非独立验证**：gradient cosine 数据在 PCGrad 条件下获得，不能作为 exposure bias 假说的独立证据。
- R1 建议将 "causal exclusion" 重新定位为 "systematic diagnostic comparison"——肯定设计精良但排除集不完备。

**MF2. GAR 指标与下游任务弱相关——核心叙事基础不稳** [R1-N1 Must-Fix, R2 同意数据但建议降级]

Table 4 / §6 显示 GAR 与 instruction retention rate：r ≈ 0.200, r² = 0.04（N=54 paired samples, 95% CI ≈ [0.05, 0.35]）。
- 标题 "Destroys" 暗示 catastrophic downstream impact，但 GAR 仅解释 4% 下游方差
- CI 跨越近零，统计说服力不足
- R2 建议重新定位 GAR 为 diagnostic probe 可部分缓解，但即使作为 diagnostic probe，4% 解释方差仍质疑其诊断价值
- 建议补充至少一个 established 下游评估（如 MT-Bench multi-turn subset）建立 GAR 与实际性能的桥梁

### Should-Fix (影响论文质量但不直接阻碍接收)

**SF1. β-steering 部分循环论证** [R1-W1, R2 同意]
β-steering boost attention → GAR（attention metric）recovers 是同义反复。非循环部分（下游 instruction retention +11.1pp）的 McNemar p=0.077 未达 α=0.05 显著水平。论文应解耦 GAR 恢复（自明）与下游改善（需独立统计支撑）两个声称。

**SF2. 单数据集 + 单模型为主** [R1-W2 + R2-W2, 一致]
核心实验仅在 ShareGPT（8K conversations）+ Qwen2.5-7B 上完成。Llama 跨模型复制仅覆盖 3/5 条件。对 "general phenomenon" 的泛化声称缺乏数据集多样性支撑。

**SF3. 单种子伪重复** [R1-N3 Must-Fix, R2 建议降级, Director 裁定 Should-Fix]
Table 1 中 Base/PCGrad/UG 为单种子。ThreadGate 有 2-3 种子（Appendix T），SS 有 2 种子但协议不同不可比。
- R2 反驳降级理由：效应量 8-17× 远超种子间方差（AR GAR seed 42: 0.064 vs seed 123: 0.055），Bootstrap CI 部分缓解
- R1 反驳 R2-W4：N=50 下 paired Wilcoxon 对 8-17× 效应量足够（r=0.802），真正问题是 training variance 而非 eval 样本量
- Director 裁定 Should-Fix：效应量大，但 training variance 完全未覆盖仍是方法论遗憾

**SF4. Llama 跨模型验证不完整** [R2-N3 Must-Fix, R1 部分同意, Director 裁定 Should-Fix]
仅 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 Uniform Gate。
- R1 部分反驳 R2：核心发现（gap + SS 有效）已完整复现；Llama 重尾分布（CoV>100%）使用 median 统计合理；Table 7 同时报告 mean 和 median（R2 关于 metric inconsistency 的批评不成立）
- R1 建议措辞："cross-architecture replication of the main finding, with partial replication of the exclusion chain"
- Director 裁定 Should-Fix：3/5 条件削弱完整排除，但核心发现复制成功

**SF5. 标题 overclaim** [R2-W1, R1 同意]
"Destroys" 暗示 catastrophic downstream failure，但 GAR collapse 仅解释 4% 下游方差。当前标题与证据强度不匹配。

**SF6. GAR-Dongre 全条件接近零——度量选择讨论不充分** [R1-W4, R2 同意]
Table 1 所有条件 GAR-D ≈ 0.00-0.02（包括 TF 下 ThreadGate 也仅 0.02）。§3.1 对选择 GAR-ours 而非 Dongre 原始定义的讨论不充分。

**SF7. SS+LoRA-only 消融缺失** [R1-W1 + R2 交叉共识]
SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× 提升 vs ThreadGate ~2.6×。如果 SS+LoRA-only（无 gating 架构）达到相似水平，ThreadGate 的架构贡献将大幅降低。关键缺失消融。

**SF8. 缺少推理时方案对比** [R2-N2 Must-Fix, R1 Should-Fix, Director 裁定 Should-Fix — divergence]
β-steering 已证明推理时注意力干预可恢复 GAR，但论文未与已发表的推理时方案做实验对比（Li et al. 2024 split-softmax, Rhea）。
- R2 认为 Must-Fix：诊断论文不与最直接替代方案对比是完整性缺陷
- R1 明确反对升级：论文定位为诊断性贡献，split-softmax 是推理时解决方案，不在同一层面竞争。建议 Discussion 中定性讨论适用场景差异即可。
- Director 裁定 Should-Fix：R1 的 scope 论证有理——诊断论文不必做方案对比实验，但 Discussion 中应有定性讨论

---

## Reviewer Consensus

| 问题 | R1 定级 | R2 定级 | Director 裁定 |
|------|---------|---------|---------------|
| 因果排除链不完整 | N2 Must-Fix | N1 Must-Fix | **Must-Fix** (强共识) |
| GAR 弱下游相关 r²=0.04 | N1 Must-Fix | Should-Fix | **Must-Fix** (4% 不足以支撑核心叙事) |
| 缺 split-softmax/Rhea 对比 | W3 Should-Fix | N2 Must-Fix | **Should-Fix** (见 Divergence) |
| β-steering 循环论证 | W1 Should-Fix | 同意 | **Should-Fix** |
| 单数据集 | W2 Should-Fix | W2 Should-Fix | **Should-Fix** |
| 单种子伪重复 | N3 Must-Fix | Should-Fix | **Should-Fix** (效应量大) |
| Llama 不完整 | 部分同意 | N3 Must-Fix | **Should-Fix** (核心发现已复制) |
| 标题 overclaim | 同意 | W1 Should-Fix | **Should-Fix** |
| GAR-D 近零 artifact | W4 Should-Fix | 同意 | **Should-Fix** |
| SS+LoRA-only 消融缺失 | W1 | 同意 | **Should-Fix** |

---

## Reviewer Divergence

**1. GAR 弱相关的严重性**
- R1 视为 Must-Fix：核心指标不可靠，论文基础动摇
- R2 视为 Should-Fix：若重定位 GAR 为 diagnostic probe，弱下游相关可接受
- **Director 裁定 Must-Fix**：即使作为 diagnostic probe，4% 解释方差也严重削弱论文叙事说服力

**2. 单种子的严重性**
- R1 视为 Must-Fix：training variance 完全未覆盖
- R2 认为效应量 8-17× 足以缓解；R1 确认 eval 样本量（N=50, r=0.802）足够
- **Director 裁定 Should-Fix**：效应量确实远超 seed noise，但 training variance 仍是遗憾

**3. Split-softmax 对比的严重性**
- R2 视为 Must-Fix：β-steering 已开推理时干预先河，不对比不合理
- R1 明确反对升级：论文定位为诊断，split-softmax 为推理时方案不在同层面竞争，Discussion 定性讨论即可
- **Director 裁定 Should-Fix**：R1 的 scope 论证成立——诊断论文核心贡献是发现问题而非提出解决方案，但 Discussion 应讨论

**4. Llama median vs mean**
- R2 批评 median 使用有 metric selection 之嫌
- R1 反驳：Llama 重尾分布 CoV>100%，median 是统计合理选择；Table 7 已双报
- **Director 裁定**：R1 反驳有理，R2 此项批评不成立

---

## R2 事实错误（由 R1 交叉回应纠正）

| R2 声称 | R1 纠正 | 影响 |
|---------|---------|------|
| R2-W6: 无代码/数据链接 | Abstract p.1 有 anonymous.4open.science/r/turn-residual-gating | 该 weakness 撤销 |
| R2-M3: Figure 1(b) 缺 log scale 标注 | Caption 已明确标注 "(log scale)" | 该 minor 撤销 |
| R2-W3: 仅用 PPL 评估 | 论文有 instruction retention (N=200, 18 categories, McNemar) + MMLU 5-shot + PPL 三层评估 | 评估完整性无问题，但 r²=0.04 弱相关问题仍在 |

---

## Questions

Q1. 如果 GAR 与下游 instruction retention 仅 r²=0.04，为什么 GAR 是论文的核心指标？有没有更好的 grounding proxy metric？

Q2. SS 贡献 ~8.5× vs ThreadGate ~2.6×，如果进一步做 SS+LoRA-only 消融，ThreadGate 的独立架构价值还有多少？

Q3. KV cache drift 是否是 TF-AR gap 的另一个 confound？可以设计什么实验排除？（如 AR decoding with oracle-prefix injection）

Q4. LoRA rank 16 是否可能限制了 gate 效用上界？在更高 rank（32/64）下是否会有不同结论？

Q5. GAR-ours 与 GAR-Dongre 的巨大差异（~0.5 vs ~0.01）的根因是什么？这是否意味着 Dongre 原始定义在 multi-turn 场景下更鲁棒？

---

## Missing References

- **Li et al. 2024** — split-softmax：推理时 multi-turn attention 解决方案，需 §2/Discussion 讨论 [R1, R2 共识]
- **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention [R1, R2 共识]
- **Zhang et al. 2024** "Tell Your Model Where to Attend" — 推理时注意力操控方法 [R2]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求**

---

## Visual Layout Check (非评分项)

**状态：已完成** (耗时 ~4 分钟，0 critical / 0 warning / 8 info)

主要发现：
- **Page 1**：首页无 display item，Figure 1 在 page 2（可接受但非最优）
- **Page 4**：Figure 2 偏小，legend 文字在打印尺寸下可能偏小
- **Page 6**：Figure 4 五种柱状颜色灰度打印可区分度下降，建议添加 hatching pattern
- **Page 8**：Figure 6(a) 标签密集，图内数值标注字号偏小（建议 ≥8pt）
- **Pages 19-20**：附录图表密集排列，单图尺寸偏小
- **全文配色**：红/蓝双色主调，饱和度适中，色盲友好，语义连贯性好

整体排版质量可接受，无影响审稿印象的严重问题。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | Director |
|------|-----|-----|----------|
| Overall | 3.5 | 3.5 | **3.0** |

**Director 综合评分：3.0 / 5 (Findings)**

**置信度：4/5 (High)**

### 评分理由

本文呈现了一个有价值的负面结果——lightweight per-layer gating 无法弥合多轮 LLM 的 TF-AR grounding gap——并提出 exposure bias 作为解释假说。系统的五路条件对比（R1 肯定设计精良）和 β-steering 诊断工具是亮点。评估体系完善（instruction retention + MMLU + PPL 三层），代码/数据已匿名发布。

**2 个 Must-Fix 问题限制接收前景：**
1. **因果声称过强**（强共识）：exposure bias 归因缺少对 KV cache drift 和 NTP magnitude imbalance 的排除，"root cause" 声称站不住——R1 建议重新定位为 "systematic diagnostic comparison"
2. **核心指标薄弱**：GAR 与下游仅 r²=0.04，"Destroys" 叙事的基础不稳

这两个问题分别涉及方法论（因果推断）和指标有效性，需要实验补充（排除实验 + 下游评估），非纯写作修改可解决。

**8 个 Should-Fix 问题**可在一个 resubmission cycle 内完成修改（R1 明确确认）。

**Director 评分低于两位 Reviewer 0.5 分的理由：**
因果排除链（Round 2 首次提出）和 GAR 有效性（Round 1 首次提出）跨 5 轮审稿从未被真正解决——每轮只是措辞微调而非补充排除实验。持续未解决的核心问题降低论文在审稿周期内可修复的信心。

**升级路径（→ 3.5 Borderline Conference）：**
(a) 将 GAR 明确重定位为 diagnostic probe + 补充至少一个 established 下游评估
(b) 将 exposure bias 降级为 "a proximal cause consistent with evidence" 并充分讨论替代假说（KV cache drift, magnitude imbalance）
(c) 补充 SS+LoRA-only 消融以明确 ThreadGate 独立贡献
(d) Discussion 中定性讨论 split-softmax/Rhea 适用场景差异

---

## Detailed Comments

### §1 Introduction
- "Destroys" 标题词与 r²=0.04 不匹配，需降调
- Contribution (1) "to our knowledge, the first" 仍被 R2 质疑

### §3 Method / GAR Definition
- r_min 数值在正文中未报告（仅 Appendix），影响可复现性 [R1-M1]
- GAR-ours vs GAR-Dongre 选择理由不充分——GAR-D 全条件 ≈ 0.00-0.02，论文未解释为何弃用原始定义
- UG 描述需明确仍为可学习 MLP

### §4 Results
- Table 1 AR 列仍仅 N=5，需扩容至 N≥50 + CI + GAR-D + PPL
- 数字精度不一致：§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp
- "20-33× gap" 重复 8+ 次——Abstract/§4.2 保留完整数字，其余用回指

### §5 Analysis
- PCGrad 失败分析需限定 scope："gradient direction conflict" 而非泛化的 "gradient conflict"。NTP magnitude imbalance 7.5-14.7× 是替代解释，必须讨论
- β-steering GAR 恢复是同义反复，需与下游效果解耦报告
- §5.5 Llama：R1 确认 median 使用合理（CoV>100%），Table 7 已双报——建议正文明确说明选择理由。标题改为 "Cross-Model Replication"

### §6 Discussion
- Exposure bias 归因需降级措辞
- Instruction retention McNemar p=0.077 未达显著
- 需定性讨论 split-softmax / Rhea 适用场景差异（R1 建议）

### §7 Limitations
- KV cache drift 已提及但未设计排除实验
- LoRA rank capacity saturation 未讨论

### Appendix
- Appendix C per-category McNemar's test（18 categories）未做 FDR/Bonferroni 校正——主实验已有 Holm-Bonferroni（Appendix E p30），但 Appendix C 漏掉了
- Bib 格式仍有不一致：Raposo et al. 缺 ICML 2024 venue、Gromov et al. 年份问题
- liu2016attention 引用可能错配（语音识别 vs 注意力引导），需确认