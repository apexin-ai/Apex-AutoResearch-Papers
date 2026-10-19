---
round: 1
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T10:10:53.246897+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: "Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards"
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewers**: 2 人（R1: 方法严谨性 + 实验设计 + 统计分析；R2: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规）
**圆桌轮次**: 1 轮（交叉回应后高度收敛，无需 Round 2）
**收敛度**: R1 对 R2 的 8 条意见 7 [AGREE] 1 [REBUT]；R2 对 R1 全部 [AGREE]

---

## Summary

论文从 Qwen3-8B 和 Llama-3-8B 上提取对比式 sycophancy 方向 $d_{syc}$（AUROC 0.827 / 0.779），然后测试三种将 $d_{syc}$ 转化为 GRPO 奖励信号的方案（cosine projection、binary probe、continuous probe），以及移除 $d_{syc}$ 后的纯行为奖励（R3-only GRPO）。所有 GRPO 方案均失败：cosine reward 因 gap 过窄或 mode collapse 而无效；binary probe 产生 stubbornness trap（ToF=0 at step 500，entropy 1300 步后才崩溃）；R3-only GRPO 仅 4/25 checkpoints 超过 vanilla。唯一成功的方法是 ACT（SFT + L2 activation consistency loss），seed 1 在 16/16 checkpoints 均超过 vanilla（SYCONScore 0.301）。论文提出根因是 $d_{syc}$ 编码 belief change 方向但不编码 evidential warrant，valid revision 和 sycophantic capitulation 在该方向上产生重叠激活。

---

## Strengths

**S1. 系统性诊断链设计优秀（§4）** [R1, R2 共识]
F1a→F1b→F1c→F1d 的递进式消除结构清晰有力：每个 variant 解决前一个的失败模式但暴露更深层问题。这是 negative result 论文的典范写法。

**S2. Probe trap 发现有独立实用价值（§5）** [R1, R2 共识]
Behavioral death (ToF=0 at step 500) 先于 distributional collapse (entropy 到 step ~1840 才下降) 1,300 步的发现，对 RL alignment 社区有直接警示：entropy-based early stopping 无法检测这类失败。此发现不受 ACT vs GRPO confound 影响。

**S3. Cross-model validation 增强可信度（Table 1）** [R1, R2 共识]
$d_{syc}$ 在 Qwen3-8B 和 Llama-3-8B 两个架构上均展示 discriminability，且 evidence-strength gradient 定性一致，表明 contrastive sycophancy 方向反映了共享的表征现象。

**S4. 清晰的写作和可视化** [R2]
论文结构紧凑，Figure 2（probe trap trajectory）和 Figure 3（SYCONScore trajectories）直观展示失败模式，Table 4 全方法对比一目了然。

**S5. Stubbornness Taxonomy（Appendix A）有参考价值** [R1, R2 共识]
对 probe-trained responses 的 100-sample 定性分析（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging）提供了有价值的 failure mode 分类。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] Fisher exact test 独立性假设违反** [R1 首提, R2 AGREE]
§1 和 §6 报告 Fisher exact test 比较 GRPO (4/25 checkpoints > vanilla) vs ACT seed 1 (16/16)，p<0.0001。但同一训练 run 的 checkpoints 具有强时序自相关（Figure 3 清楚展示连续振荡），严重违反独立性假设。Run-level 比较仅有 2 GRPO runs vs 1 ACT run（n=3），无法支撑统计检验。两位 Reviewer 共识：定性结论从轨迹图可直接观察，但 p 值赋予了虚假的统计权威性。
- **修复方向**：移除 checkpoint-level Fisher test；改为 run-level 描述性统计 + effect size；增加 seed 数量；或使用 block bootstrap。

**MF2. [critical] 遗漏直接相关成功案例 Papadatos & Freedman (2024)** [R2 首提, R1 AGREE]
arXiv 2412.00967 "Linear Probe Penalties Reduce LLM Sycophancy" 使用 linear probe 在 reward model 内部惩罚 sycophancy 标记并报告成功。这与论文 "representation-level detection 不能转化为有效 reward signal" 的核心 thesis 存在直接张力。论文未讨论为何同类信号在不同框架下（RM 内部 penalty vs GRPO scalar reward）效果截然不同。R1 指出合理区分可能存在（probe penalty 保留 RM per-token richness vs 本文压缩为 per-completion scalar），但论文必须做这一分析。
- **修复方向**：§7 Related Work 增加专段讨论；§6 root cause 分析中解释两种方法差异；提出 testable hypothesis。

**MF3. [critical] references.bib 多条引用严重不完整** [R2 首提, R1 AGREE 且认为比 R2 描述更严重]
至少 7 条 bib entry 存在严重问题：
- `consistency2025bctact`（ACT，唯一成功 baseline）：author = "Unknown"，论文标题也不准确
- `zhang2026latentgrpo`, `wang2025internal`, `sinii2025smallvectors`, `obrien2025fewbadneurons`：仅 "et al."
- `wei2024synthetic`：将 "Anthropic" 列为作者名
- `ackermann2026gradreg`："Ackermann, Johannes and others"

ACT 引用的 "Unknown" 尤其严重——唯一正面 baseline 的方法来源不可追溯，可能触发 ARR desk-rejection checklist 的 hallucinated references 检查。R1 补充：如果 "Unknown" 是匿名化自己的工作，存在 baseline 公平性问题。
- **修复方向**：补全所有 bib entries 的完整作者列表、正确标题、准确 venue。

**MF4. [critical] ACT 正面结果仅基于单 seed 完整评估** [R1, R2 独立提出]
ACT seed 2 仅评估 3/16 checkpoints（标注 "ongoing"）。论文核心对比（GRPO 4/25 vs ACT 16/16）仅基于 seed 1。考虑到 GRPO 本身已展示跨 seed 高方差，n=1 的正面 baseline 不足以建立方法有效性。R2 补充：ACT seed 1 在 checkpoint 4000 曾出现回落（0.255→0.214），seed 2 若有更严重回落将影响结论。
- **修复方向**：提交前完成 seed 2 全部 16 checkpoints；或在 Limitations 中将 ACT 成功定性为 preliminary evidence 并调整 claims 强度。

**MF5. [critical] ACT vs GRPO 对比存在 supervision granularity confound** [R1 首提, R2 AGREE 并深度分析]
ACT 使用 dense per-token supervision（SFT + L2 activation consistency loss），GRPO 使用 single scalar per completion。论文 §6 自身写到 "The critical difference is supervision density"，但 framing（标题、Abstract、C1、C3、Conclusion）强调 "d_syc fails as RL reward"，暗示问题出在方向本身。实际证据仅支持更窄结论："sparse scalar d_syc reward fails for sycophancy calibration"。缺少关键控制实验——per-token d_syc projection 作为 dense reward 给 GRPO。R3-only GRPO 的失败也无法区分 "GRPO 框架问题" 和 "sparse reward 问题"，因为同样是 sparse scalar。
- **修复方向**：(1) 调整 framing 为 "d_syc fails as sparse scalar reward"；(2) 增加 dense d_syc reward 控制实验；(3) 或在 Limitations 中显式承认此 confound。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] 标题 "RL Rewards" 过于宽泛，未讨论 DPO/KTO** [R1-W2, R2-W1 独立提出, 交叉互 AGREE]
仅测试 GRPO 一种 RL 算法。DPO 基于 preference pair 而非 scalar reward，天然适合 $d_{syc}$ 构造的 sycophantic vs non-sycophantic pair，可能绕过 "单一标量无法区分 warranted vs unwarranted" 的核心问题。标题应限定为 "GRPO Rewards" 或 "Scalar RL Rewards"。

**SF2. [warning] Process Reward Models 讨论不足** [R2 首提, R1 降级为 minor-to-warning]
SMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。论文仅 1 句 future directions 提及。per-step reward 是 sparse scalar 和 dense SFT 之间的自然中间方案，对 supervision density 论点至关重要。

**SF3. [warning] Conclusion 的 broader lesson overclaiming** [R2 首提, R1 AGREE]
§8 "any alignment effort that converts a detection probe into a reward signal must verify..." 仅基于 sycophancy/GRPO/Qwen3-8B。论文 §7 自己承认 reasoning/safety 的 probe-based RL 存在成功案例。应改为条件化表述，明确标注这是从 sycophancy case 推广的 hypothesis。

**SF4. [warning] 超参数 w1 仅测试 0.25/0.40 两个值** [R1 首提, R2 部分同意]
GRPO 失败可能是调参不充分的 artifact。F1a 中 d_syc/20 的 scaling factor 未解释来源。需报告选择过程或 sensitivity analysis。R2 指出 F1b cosine gap 0.098 与 w1 无关，但 F1d 的设计空间未被充分探索。

**SF5. [warning] AUROC ±值不是正式 CI** [R1 首提, R2 同意但认为不 critical]
5-fold CV 的 5 个值的标准差不等于 confidence interval，每个 fold 仅约 36 pairs。建议改用 bootstrap 95% CI。

**SF6. [warning] Contrastive pairs 构建方法细节严重缺失** [R1 首提, R2 AGREE]
§2.1 仅称 "style-controlled to match hedging, politeness, and length"，但未说明生成方法（人工/LLM/模板）、quality control、inter-annotator agreement、evidence strength 三级划分标准。直接影响 reproducibility。

**SF7. [warning] 所有 RL/SFT 训练仅在 Qwen3-8B 上进行** [R1-W5, R2-W4 独立提出]
Llama-3-8B 仅验证 direction discriminability。GRPO 失败和 ACT 成功的模型无关性未验证。C1 的 "Every tested GRPO formulation fails" 严格意义上仅适用于 Qwen3-8B。

**SF8. [warning] Cross-seed 分析仅 2 个 seed** [R1 首提, R2 AGREE]
n=2 不足以建立统计意义上的可复现性。两个 seed 的 crash 时间已有显著分歧（seed 1 at ckpt 6000, seed 2 at ckpt 3500）。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：
1. **Overall 3.0 (Findings)**——核心 insight 有价值但证据/framing 不足以支撑 main conference
2. **Probe trap (C2) 是论文最强贡献**——独立于 ACT 对比，不受 supervision granularity confound 影响
3. **标题和结论 overclaim**——从 sycophancy/GRPO/Qwen3-8B 推广到 general "RL Rewards" 证据不足
4. **ACT 单 seed 是最薄弱环节之一**——论文核心正面 baseline 的可靠性存疑
5. **Fisher test 误用和引用不完整同等严重但影响路径不同**——前者攻击 soundness，后者攻击 scholarly credibility

## Reviewer Divergence [REBUT]

唯一分歧：**181 对训练数据规模是否偏小**
- R2 认为更大训练集可能产生更鲁棒 direction，缓解 cosine gap 0.098 的问题
- R1 [REBUT]：cosine gap 0.098 反映 valid/invalid activations 在 activation space 中的结构性接近（两者都沿 $d_{syc}$ 方向移动），不会因更多数据消失。问题是 pair 构建的质量控制不透明（R1-W4），而非数量不足。
- **Director 判断**：采纳 R1 的分析——数据量不是核心问题，质量控制透明度是（已列为 SF6）。

---

## Questions for Authors

1. 如何解释 Papadatos & Freedman (2024) 用 probe penalty 在 RM 上成功降低 sycophancy，而本文 probe-based GRPO reward 全部失败？关键差异是 intervention 位置、optimization 框架，还是 supervision granularity？
2. ACT seed 2 完整评估何时完成？若 seed 2 表现不稳定（如仅 50% checkpoints 超过 vanilla），论文结论是否需要修改？
3. 是否尝试过 DPO/KTO？如果 $d_{syc}$ 用于构造 preference pair 而非 scalar reward，"discriminability ≠ utility" 论点是否成立？
4. 论文是否做过 per-token $d_{syc}$ projection 作为 dense GRPO reward 的实验？这是区分 "direction 本身问题" 和 "reward granularity 问题" 的关键控制。
5. Fisher exact test 如果改为 run-level 比较（每 run 取 peak SYCONScore），结论是否仍然成立？
6. w1=0.25 如何选定？是否做过 sensitivity analysis？
7. Contrastive pairs 的构建流程是什么（人工/LLM/模板）？是否有 quality control？

---

## Missing References

1. **Papadatos, H. & Freedman, R. (2024).** Linear Probe Penalties Reduce LLM Sycophancy. arXiv:2412.00967. [最关键遗漏——probe-based reward 成功案例]
2. **SMART (2025).** Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories. arXiv:2509.16742. [per-step process rewards 用于 sycophancy mitigation]
3. **Rafailov et al. (2023).** DPO: Direct Preference Optimization. [preference-based RL 替代方案]
4. **Ethayarajh et al. (2024).** KTO: Model Alignment as Prospect Theoretic Optimization. [preference-based RL 替代方案]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical / 2 warning / 3 info）。

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | p1-3 | 连续 3 页无任何 display item，第一个视觉锚点推迟到 p4。实证论文建议前 2 页内放置概念图或核心结果 teaser |
| ⚠️ warning | p10 | Appendix A 仅占页面约 1/4，剩余 3/4 空白。建议扩充或合并 |
| ℹ️ info | p5 | 单页含 3 个 display items（Table 2 + Table 3 + Figure 2），密度较高但可读 |
| ℹ️ info | p7 | Figure 3 legend 字号偏小，打印时可能需要辨认 |
| ℹ️ info | p4-7 | 全部 7 个 display items 集中在 4 页内，前后页面无视觉元素，节奏不均匀 |

---

## Overall Assessment

**评分：3.0 — Findings**（两位 Reviewer 一致）

**置信度：4/5**（两位 Reviewer 均熟悉 representation engineering、RLHF、sycophancy 相关文献）

论文揭示了一个重要的结构性现象：表征空间中的 sycophancy 方向虽然具有良好的判别能力，但不能直接转化为有效的 GRPO 奖励信号。Probe trap 的发现（behavioral death 先于 distributional collapse 1300 步）对 RL alignment 社区有直接实用价值。

但论文存在 5 个 critical 问题：(1) Fisher exact test 将非独立 checkpoints 当独立样本导致 p 值不可信；(2) 遗漏了 Papadatos & Freedman (2024) 的 probe penalty 成功案例；(3) 引用质量严重不足（ACT 作者为 "Unknown"）；(4) ACT 正面结果仅基于单 seed；(5) ACT vs GRPO 对比存在 supervision granularity confound。此外，标题从 sycophancy/GRPO/Qwen3-8B 推广到 general "RL Rewards" 证据不足，缺少 DPO/KTO 讨论和 process reward models 分析。

核心贡献（特别是 C2: probe trap）有 Findings 接收的价值，但需要：修复统计分析、补全引用、完成 ACT seed 2、调整 framing 精确化 claims scope、补充关键相关工作讨论。

---

## Detailed Comments

### §1 Introduction
- "p < 0.0001" (Fisher exact test) 需移除或替换为 run-level 统计（MF1）
- 三个 contributions 的 scope 需与实际证据对齐——C1 和 C3 应限定为 "GRPO scalar rewards" 而非 "RL rewards"（MF5, SF1）

### §2 Experimental Framework
- §2.1: Contrastive pairs 构建方法需详细说明（SF6）
- §2.2: w1=0.25 的选择过程需说明（SF4）；应讨论为何未测试 DPO/KTO（SF1）
- §2.4: ACT 引用需修复——author="Unknown" 不可接受（MF3）
- §2.5: NLI flip classifier 的准确率需报告

### §3 Direction Discriminability
- AUROC ±0.028 应改为 bootstrap 95% CI（SF5）
- Table 1 和 Figure 1 的呈现清晰，是论文的优势部分

### §4 Cosine R1: Structural Failure
- Table 2 的诊断链设计是论文最强的方法论贡献（S1）
- F1a-F1d 的分析有说服力，但 w1 sensitivity analysis 缺失（SF4）

### §5 The Probe Reward Trap
- 最强独立贡献（S2）——behavioral-before-distributional collapse 的 1300-step lag 发现有独立价值
- 不受 ACT confound 影响

### §6 Analysis
- "The critical difference is supervision density" 与标题/abstract 的 framing 矛盾（MF5）
- Fisher test p 值需移除（MF1）
- 应增加对 Papadatos & Freedman (2024) 和 SMART (2025) 的讨论（MF2, SF2）
- ACT seed 2 数据需补完或将 claims 降级为 preliminary（MF4）

### §7 Related Work
- 缺少 Papadatos & Freedman (2024)——最关键遗漏（MF2）
- 缺少 DPO/KTO 和 process reward models 的讨论（SF1, SF2）
- 整体偏薄（约 1 页），对于做出广泛方法论声明的论文不够

### §8 Conclusion
- "any alignment effort" 的一般性声明需条件化（SF3）
- broader lesson 应明确标注为从 sycophancy case 推广的 hypothesis

### Limitations
- 已覆盖 3 个点（单模型训练、ACT seed 2 未完成、binary evaluation），但应追加：supervision granularity confound（MF5）、引用问题（MF3）、Fisher test 局限（MF1）

### References
- 7 条 bib entry 需补全完整作者和正确 venue（MF3）

### Appendix
- Stubbornness Taxonomy 有参考价值但样本量偏小（100）
- 大面积空白（visual check warning）建议扩充内容