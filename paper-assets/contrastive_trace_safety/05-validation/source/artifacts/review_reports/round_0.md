---
round: 0
overall_score: 2.5/5 — Borderline (between Substantial Revision and Findings Acceptance)
timestamp: 2026-05-16T22:18:22.413366+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿圆桌会议报告 — Round 1

**论文**: "Hidden States Universally Encode Safety Commitment Better Than Text: A Cross-Architecture Evaluation of Reasoning Model Monitoring"
**Venue**: EMNLP 2026 ARR
**审稿人**: R1 (Methods & Experimental Soundness), R2 (Novelty & Related Work)
**日期**: 2026-05-16
**外部审稿**: 未请求

---

## Overall Assessment

**评分**: 2.5/5 (Borderline — 介于 Substantial Revision 和 Findings Acceptance 之间)

两位 Reviewer 独立给出完全相同的 2.5/5 评分，交叉分享后达成高度共识。论文问题定义清晰且有实际意义（reasoning model self-jailbreak 的实时检测），实验框架设计有野心，部分发现（negative finding on pre-textual detection、geometric methods universal failure）有价值。但 execution 层面存在多处方法论不透明、统计 claims 超出证据支撑、related work 严重不足。**当前版本不满足 ACL ARR 发表标准，需要 major revision。**

修复全部 critical issues 后可达 **Findings track** 水平；进一步增加模型多样性和深化 transfer 分析后有 Main track 可能。

---

## Summary

论文研究推理模型（如 DeepSeek-R1 蒸馏版、QwQ-32B）在 chain-of-thought 中自我越狱时的 "commitment point"（safety reasoning 永久停止的时刻）检测。在 4 个模型（1 Llama-based、3 Qwen2.5-based）的 209 traces 上，使用 logistic regression 和 GRU 探针在 hidden states 上做 step-level 二分类。核心发现：(1) hidden-state probes 比 text-based probes FPR 低约 2 倍，(2) temporal context (W=15) 提升 coverage 5-7pp，(3) pre-textual detection（提前于 CP 的检测）不可靠（median lead ≈ 0）。附带 cross-model transfer (67-74% accuracy) 和 geometric methods universal failure 的负结果。

---

## Strengths

1. **问题定义准确且有实际意义**：识别了 reasoning model self-jailbreak 与传统 adversarial attack 的本质区别（内部推理失败 vs 外部攻击），commitment point 形式化合理，检测指标体系（coverage, pre-CP FPR, lead time）直接对应部署需求。

2. **有价值的负结果**：(a) geometric methods (TrajGuard/Mahalanobis) 在所有模型上失败（max Δ < 0.025），配合 Fisher ratio 分析（full space 18-19 → PCA-3 约 1.0）给出可操作解释；(b) pre-textual detection unreliable（median lead ≈ 0）配合 oracle decomposition 建立了 information-theoretic limitation argument。

3. **实验设计系统性**：2×2 设计意图（architecture × scale）、pooled bootstrap analysis、I² heterogeneity test、multi-method head-to-head 比较、window/layer ablation 的框架本身质量高。

4. **统计实践**：I²=0.08-0.21（虽然 k=3 下不可靠，见 Weaknesses）、bootstrap CIs、5-seed GRU stability report 体现了统计意识。

5. **Cross-model transfer**：67-74% accuracy (vs 50% chance) 配合 within-family vs cross-family 分解是一个有趣的初步发现，暗示跨架构共享信号结构。

---

## Weaknesses（按严重程度排序）

### Critical Issues（影响接收决定）

**C1. "Universally" / "Cross-Architecture" overclaim** [R1-N3 + R2-N3, 完全共识]
- 4 模型中 3 个基于 Qwen2.5。2×2 matrix 缺 Llama/32B cell，无法分离 architecture vs scale。标题级 overclaim 是 ARR 常见 reject 原因。
- 修复：重命名标题（去 "Universally"）+ Limitations 声明 + 理想情况下补 1-2 个非 Qwen 模型。

**C2. 缺少 Control Task — 无法排除位置混淆** [R2-N2, R1 交叉同意]
- CP 位置与 trace 进度相关（review context 显示 CP 均值在 trace 83% 处）。probe 可能学到 step_index/trace_length 而非 safety state。Hewitt & Liang (2019) 的 random-label control 是标准验证方法，完全缺失。
- 修复：报告 CP 位置分布 + 实施 random-label control + 计算 selectivity。

**C3. k=3 pooled meta-analysis 不成立** [R1-N2, R2 交叉同意]
- Cochran's Q 在 k<5 时 power 极低；I²=0.12 的 CI 可从 0% 跨到 >75%。更严重：3 模型非独立（共享蒸馏 teacher 或 base architecture），违反 meta-analysis 独立性假设。Abstract 中 p=0.003 不可靠。
- 修复：改用 per-model consistency argument + paired bootstrap；去掉 Abstract 中 I² 引用；承认 k=3 limitation。

**C4. 数据划分矛盾** [R1-N1, R2 交叉同意]
- Section 3.3 报告 "166 train / 43 test"，Section 5.7 报告 "n=125 training traces"。疑存在未声明 validation set (125/41/43)。val set 若用于 layer selection / threshold tuning 需明确说明。
- 修复：统一报告三折划分 + 明确 val 用途。

**C5. OpenThinker-7B 选择性排除** [R1-N4, R2 交叉同意]
- 声称 4 模型但 pooled analysis 仅用 3 个，排除理由未说明。
- 修复：纳入 pooled 或预声明排除标准。

**C6. Related Work 严重不足** [R2-N1, R1 交叉同意]
- 仅 14 篇引用。缺失 probing classifier 奠基文献（Belinkov 2017, Conneau 2018, Hewitt & Manning 2019, Hewitt & Liang 2019）、activation patching (Meng 2022, Conmy 2023)、jailbreak detection 方向、PRM/process supervision (Uesato 2022, Wang 2023)、cross-model representation analysis (CKA, Model Stitching)。
- 修复：扩展 Related Work 至 2 页，增加 Probing Classifiers、Causal Interpretability、Process Supervision 子段落，引用达 30+。

### Should-Fix Issues（影响评分但非 dealbreaker）

**S1.** Hidden state 提取方式未指定（last token / mean pooling / first token）[R1-W1]
**S2.** Text baseline 过弱（TF-IDF vs 4096-d continuous）— 应加 sentence embeddings baseline 或严格限定 claim scope [R1-W2]
**S3.** CP 定义鲁棒性未讨论（oscillation、HarmThoughts IAA）[R1-W3]
**S4.** Bootstrap 实施不透明（resampling unit、CI type、test statistic）[R1-W4]
**S5.** BOCPD 有方法描述无结果数据 — "有 claim 无 evidence" [R1-W5]
**S6.** GRU std=9-11% 意味着不可复现，应报告 worst-seed 下界 [R1-W6]
**S7.** Transfer projection head 训练数据未说明（若用 target labels 则非 transfer）[R1-W7]
**S8.** "HS > text" 从信息论是预期，需论证非显然性 [R2-W1]
**S9.** Probing 是相关性非因果性，Limitations 应声明 [R2-W2, R1 部分 rebut — 检测任务中 correlation 可接受]
**S10.** PRM 结构性联系未讨论 [R2-W3]
**S11.** Cross-model transfer 分析浅（缺 CKA/CCA，"shared geometry" claim 无支撑）[R2-W4]
**S12.** Oracle decomposition 方法学不清晰（62%/28%/10% 如何计算）[R2-W5]

### Format Issues

- 使用 `\documentclass[11pt,a4paper]{article}` 而非 ACL/EMNLP 官方模板 → desk reject 风险
- 缺 Responsible NLP Checklist（EMNLP ARR 必需）
- References 格式不完整（"et al." 缩写、缺 arXiv ID）
- Table 格式不一致（GRU: "76-93%" vs "81±9%"）

---

## Questions to Authors

1. Section 3.3 的 166 train traces 和 Section 5.7 的 125 training traces 哪个是正确的？是否存在未声明的 validation set？如存在，layer selection 和 threshold tuning 使用的是哪个集合？
2. Commitment point 在 trace 中的相对位置分布是什么？（均值、中位数、std）如果高度集中在某个区间，如何排除 probe 学到位置启发式？
3. OpenThinker-7B 为什么被排除出 pooled analysis？其 coverage/FPR/precision/lead time 完整结果是什么？
4. Cross-model transfer 的 projection head 用什么数据训练？是否使用了 target model 的标注数据？
5. Oracle decomposition 的 62%/28%/10% 具体如何计算？是 ablation 还是 variance decomposition？K-step lookahead 的 K 是多少？

---

## Missing References

**Probing Classifiers（奠基文献）**:
- Belinkov et al. (2017) "What do neural machine translation models learn about morphology?"
- Conneau et al. (2018) "What you can cram into a single $&!#* vector"
- Hewitt & Manning (2019) "A structural probe for finding syntax in word representations"
- Hewitt & Liang (2019) "Designing and interpreting probes with control tasks"

**Causal Interpretability**:
- Meng et al. (2022) "Locating and Editing Factual Associations in GPT"
- Conmy et al. (2023) "Towards Automated Circuit Discovery for Mechanistic Interpretability"

**Process Supervision / PRMs**:
- Uesato et al. (2022) "Solving math word problems with process- and outcome-based feedback"
- Wang et al. (2023) "Math-Shepherd: Verify and Reinforce LLMs Step-by-step"

**Representation Analysis**:
- Kornblith et al. (2019) "Similarity of Neural Network Representations Revisited" (CKA)
- Bansal et al. (2021) "Revisiting Model Stitching to Compare Neural Representations"

**Jailbreak Detection**:
- Robey et al. (2023) "SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks"
- Alon & Kamfonas (2023) "Detecting Language Model Attacks with Perplexity"

---

## Detailed Comments

### 关于 Findings vs Main track

当前版本修复 C1-C6 后适合 **Findings track**（问题有价值 + 实验框架合理 + 含有价值的负结果）。要进入 **Main track** 还需：
- 增加 ≥2 个非 Qwen2.5 模型（如 Mistral-based、Gemma-based reasoning models）
- 深化 cross-model transfer 分析（CKA/CCA + mechanism 讨论）
- 实施 control task 且结果支持 safety-specific selectivity

### 关于统计框架重构

建议放弃 "meta-analysis" framing。k=3 non-independent models 不适合 meta-analytic treatment。改为：
- Per-model results table（主表）
- "Cross-model consistency" 叙述（文字论证 pattern 一致性）
- Paired permutation test 或 stratified bootstrap（如需 formal test）
- 去掉 I²，保留 pooled bootstrap CI 作为 supplementary

### 关于 Control Task 的预期结果

如果 CP 集中在 trace ~83% 位置（从 review context 推断），position-only baseline 可能达到 75-80%。如果实际 probe 达到 85%+，selectivity 为正但较低。这**不一定是坏消息**——它重新框架了 contribution 为 "probe 编码了 safety state + 位置信息"，quantifying 各自贡献。但如果 selectivity ≈ 0，则论文核心 claim 需要根本重构。

### R1-R2 唯一分歧

R2-W2（因果验证缺失）：R1 认为对于 detection task，reliable correlation 已足够，activation patching 不是 Must-Fix。R2 同意但坚持 Limitations 应明确声明。**共识结论：在 Limitations 增加 1 段因果讨论即可，无需补充 intervention 实验。**

---

## Reviewer 维度汇总

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 2.5/5 | 3/5 | 2.5-3/5 |
| Excitement | 3.5/5 | 2/5 | 2.5-3/5 |
| Overall | 2.5/5 | 2.5/5 | **2.5/5** |
| Reproducibility | 2/5 | 3/5 | 2.5/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**Soundness 分歧**：R1 更严（data split + meta-analysis 问题），R2 略宽容（基本合理但缺 control task）。
**Excitement 分歧**：R1 认为问题定义新颖（3.5），R2 认为发现方向预期（2）。交叉后 R1 同意 "HS > text" 的 novelty 需要更好的论证。

---

## Director 备注

1. **R2 发现 Director 转发 review 草稿中的事实错误**：草稿中提及的 "MI analysis (MI=0.42)"、"41.6% CP in last 10%"、"Frank (2603.18280)" 均不存在于论文中。Fisher ratio 数值也有偏差（草稿 17-18，实际 18-19）。建议未来转发材料前验证事实准确性。

2. **外部审稿**：本轮未请求外部审稿（Stanford Agentic Reviewer）。鉴于两位内部 Reviewer 已达成充分共识，外部审稿非必需。如果进入 Round 2（修订后重审），可考虑请求外部意见作为第三方验证。
