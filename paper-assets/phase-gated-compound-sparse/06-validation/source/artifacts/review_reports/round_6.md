---
round: 6
overall_score: borderline
timestamp: 2026-05-15T11:29:06.703535+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Phase-Modulated Compound Sparsity
## Round 6 — EMNLP 2026 Main Conference

**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Deadline**: 2026-06-15
**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)
**External Review**: 未配置，不适用

---

## Summary

本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）对数学推理模型的影响，发现 compound severity 具有 phase-strategy interaction：importance-based eviction 在 low-sparsity reasoning phase 产生远大于 high-sparsity phase 的 super-additive degradation（amplification ratio G=30-148×, n=496），而 random eviction 保持近平坦（G≈1）。在 s=0.25 处出现 strategy ranking crossover。结果在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上复现，LLaMA 上有初步证据。提出 discrimination collapse 作为 correlational 机制解释。

---

## Strengths

**S1. 研究问题定义精准且有部署价值** [R1-S1, 共识]
Compound sparsity 的 phase-dependent interaction 是先前工作忽略的维度。Phase × strategy 的分析框架对推理模型部署有直接指导意义。

**S2. 统计方法论达到高水准** [R1-S2, R2-S1, 共识]
非参数检验 + bootstrap CI (B=10,000) + Bonferroni + BH-FDR 双重校正 + JT dose-response + permutation test + multiplicative null robustness check。在 NLP 实证研究中属于顶级标准。

**S3. Random eviction 作为 falsification control 设计精妙** [R1-S5, R2-S2, 共识]
利用 random eviction 的 score-independence 特性隔离 strategy-specific 效应，G≈1 的 baseline 有效确认 severity gradient 是 importance-based eviction 的特有现象。

**S4. 负面结果和局限性诚实报告** [R1-S3, R2-S3, 共识]
LLaMA 弱证据（仅 s=0.30 显著）、mitigation pilot 未通过 30% gate（oracle 18%）、entropy redistribution Qwen 不一致（s=0.25 反转）、Qwen mid-phase 45.2% null rate——全部坦承，不掩盖。

**S5. n=50→n=500 精度提升验证有说服力** [R1-S4, R2-S4, 共识]
CI 收窄 2.5-5.9×，直接展示统计功效提升。32/32 引用全部真实，无 hallucinated citations。

---

## Weaknesses

### Must-Fix（3 个，影响接收决定）

**N1. [CRITICAL, 共识] Crossover 证据基础不足——n=50 数据未在 n=496 验证**

- 位置：Table 2 (results.tex:31-53), §5.3 (results.tex:63-66), Appendix D
- Table 2 报告 n=50 profiling subset 的 per-phase II 值（G=69-274×），n=496 数据给出 G=30-148×（仅在正文 inline 和 Figure 1 caption 以 bootstrap CI 形式出现），过高估计 42-85%
- §5.3 crossover 的核心数字（importance: 0.032 vs 0.818, random: 7.196 vs 1.363, 5.3× reversal）完全来自 n=50
- Crossover 是三大 contribution 之一（Introduction: "no single strategy dominates uniformly"），证据基础必须匹配 claim 强度
- **R1-R2 交叉回应**：完全共识。两位 Reviewer 独立将此列为 #1 critical issue
- **修改要求**：在 n=496 数据上重新计算 per-phase per-strategy II 中位数和 crossover magnitude with bootstrap CI。替换 Table 2 或新建 n=496 per-phase table 为主体；如保留 n=50 数据移至 Appendix

**N2. [CRITICAL, 共识] Discrimination collapse effect size 与 severity gradient magnitude 之间的 gap**

- 位置：§6.1 (analysis.tex:1-9), Appendix Table 8
- Gini coefficient 下降 0.030-0.081 (DeepSeek), 0.010-0.020 (Qwen)——绝对变化微小（Gini 范围 0-1），未报告 baseline Gini 值，无法评估相对变化
- 0.01-0.02 的 score distribution 变化如何驱动 G=30-148× 的 severity amplification？论文未讨论 threshold amplification 等放大机制
- §6 标注了 "correlational"（好），但 Introduction 和 Conclusion 仍将 "entropy-discrimination collapse" 作为完整机制叙事
- **R1-R2 交叉回应**：共识此 gap 需弥合。R2 认为降级 mechanism claim 即可；R1 认为需要更充分的讨论
- **修改要求**：(a) 报告 baseline Gini 和 ΔGini/Gini_baseline 的相对变化；(b) 讨论 threshold amplification 机制（小的 score 变化如何通过 eviction threshold 产生大效应差异），或将 §6 明确降级为 "preliminary correlational observation"

**N3. [CRITICAL→SHOULD-FIX, 分歧] "following ThinKV" 对 phase segmentation 的错误归因**

- 位置：background.tex:33
- ThinKV 使用 explicit reasoning delimiters（`<think>` tokens），本文使用 quantile-based attention sparsity segmentation——方法不同，"following" 措辞误导方法 provenance
- **R1-R2 交叉回应**：R1 列为 must-fix（方法归因准确性），R2 同意需修改但认为 should-fix 级别。两者均同意措辞必须改变
- **修改要求**：改为 "inspired by ThinKV's phase-aware perspective" 或 "analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters"

### Should-Fix（8 个，影响评分）

**W1. [WARNING, 共识] Spearman ρ=1.0 on n=4 过度报告**
- methodology.tex:22, results.tex:71
- n=4 的 ρ=1.0 统计意义极弱（p=0.042 不能存活 multiple testing）。JT test (z=6.2-33.7, per-problem values) 才是 substantive evidence
- 修改：将 JT test 作为 primary dose-response evidence，Spearman 降为脚注或 Appendix

**W2. [WARNING, 分歧] Novelty 增量不足**
- **R2 观点 (2.5/5)**：核心发现可由 HIES (discrimination collapse) + ThinKV (phase segmentation) + Sparse Frontier (strategy non-dominance) 的组合预期；pure characterization paper 对 EMNLP main conference 偏弱
- **R1 观点 (3.5/5)**：compound interaction 是 emergent coupling（head pruning 改变 importance score → 改变 KV eviction 有效性），不可从单轴工作线性推导；crossover 是单轴框架无法生成的预测
- R1 conditional：如 crossover 在 n=496 验证通过且 mechanism gap 弥合，达 Conference level
- 修改建议：强化 novelty 论述——在 Introduction 或 Discussion 中明确阐述为什么 compound interaction 产生单轴框架无法预测的现象

**W3. [WARNING, 共识] 缺乏下游任务评估**
- PPL-based II 未映射到 accuracy。G=148× 在 MATH-500 accuracy 上对应多少损失？"motivate phase-aware compression budgets" 缺乏 grounding
- 修改：在 Discussion/Limitations 讨论 PPL→accuracy 关系

**W4. [WARNING, 共识] Mitigation pilot 失败的影响 under-discussed**
- Oracle 18% < 30% gate, heuristic 32% but CI spans zero。Phase-aware budget reallocation alone insufficient
- 修改：增加一段讨论为什么 characterization 本身有价值（diagnostic signal），即使当前 mitigation 不成功

**W5. [WARNING, 共识] Entropy redistribution 跨模型不一致**
- Qwen s=0.25 反转（ΔH=+0.045, 22/30 problems positive）。§6.2 正确标注 "model-dependent" 但仍占 ~15% Analysis 篇幅
- 修改：精简或在 Discussion 明确承认非 robust mechanism

**W6. [WARNING, 部分共识] LLaMA CI/Wilcoxon 不一致**
- s=0.15: CI excludes zero but Wilcoxon p_Bonf=0.219 (ns); s=0.30: CI includes zero but Wilcoxon p_Bonf=0.029 (sig)
- R1 要求解释；R2 认为论文已 hedge 为 "mixed evidence" 但同意加技术解释
- 修改：加脚注说明 bootstrap CI vs Wilcoxon signed-rank 在 small n + heavy tails 下的行为差异

**W7. [WARNING, 条件共识] 遗漏引用 "Hold Onto That Thought" (NeurIPS 2025, arXiv:2512.12008)**
- 直接评估 KV cache compression 对 reasoning 的影响——与本文主题直接相关
- 修改：验证相关性后补引

**W8. [WARNING, 共识] h2o-neurips2023 bib entry title 字段为空**
- 跨 3 轮审稿仍未修复
- 修改：补全 title 字段

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
1. **N1 (crossover n=50)** — 最关键缺陷，决定 Contribution 1 存废
2. **N2 (mechanism gap)** — effect size 与 claim 强度不匹配
3. **W1 (Spearman n=4)** — JT test 应为 primary
4. **W3 (无 accuracy 评估)** — PPL→accuracy gap 是盲区
5. **W4 (pilot 失败)** — 需更坦诚讨论
6. **W5 (entropy redistribution)** — 跨模型不一致
7. **所有 minor issues** — bib 问题、\placeholder 残留、orphaned file

## Reviewer Divergence

| 问题 | R1 | R2 | 分析 |
|------|----|----|------|
| **Novelty (W2)** | 3.5/5, compound interaction 超越单轴叠加 | 2.5/5, HIES+ThinKV+Sparse Frontier 已基本预示 | 根本分歧在于 characterization paper 的价值判断。R1 认为 compound coupling 的量化超越已知定性方向；R2 认为 quantitative magnitude alone 不构成 EMNLP main conference 的 novelty threshold |
| **N3 severity** | Must-fix (方法归因准确性) | Should-fix (attribution 修正) | 实质共识（必须改措辞），仅 severity 分级不同 |
| **R1-W2 (Bonferroni k=4)** | Should-fix | Rebutted (rationale exists + BH-FDR confirms) | 偏向 R2：rationale 已给出，BH-FDR 覆盖全量；但同意 main text 应更突出 BH-FDR |
| **R2-W6 (Qwen mid-phase null)** | Rebutted (不影响 primary Δ) | Should-fix | 偏向 R1：Δ 仅需 low/high phase，sensitivity analysis 已验证 robustness |

---

## Questions to Authors

1. Table 2 per-phase II 为何未在 n=496 上重新计算？是否有技术障碍？
2. Discrimination collapse 的 baseline Gini 值？ΔGini/Gini_baseline 的相对幅度？
3. Phase boundary 在不同 problem 间的稳定性？是否存在 boundary-sensitive cases？
4. 是否考虑过 accuracy-based（非 PPL-based）的 Interaction Index？
5. Frobenius norm head pruning 是否是核心假设？gradient-based metric 下结果是否一致？
6. float16→bfloat16 切换的时间点？n=50 profiling 是否在 float16 下进行？

---

## Missing References

1. **"Hold Onto That Thought"** (NeurIPS 2025, arXiv:2512.12008) — 直接评估 KV cache compression 对 reasoning 的影响 [R2-W7, R1 conditional agree]
2. SnapKV bib first author 可能有误（Li vs Cai）[R2 minor]

---

## External Review (Stanford Agentic Reviewer)

未配置，不适用。

---

## Overall Assessment

**评分：Borderline (weak reject → borderline accept)**
- R1: 3.5/5 → 交叉后 3.0-3.5（取决于 crossover 验证和 mechanism 补充）
- R2: 2.5/5 → 维持 2.5
- 综合：**3.0/5 — Borderline**

**置信度：High (4/5)**

**理由：**

论文在实验执行和统计分析上达到高水准（S2），研究问题有实际部署价值（S1），负面结果诚实报告（S4）。然而存在三个层面的问题：

1. **证据完整性 (N1)**：最具区分度的 crossover 发现仅有 n=50 证据，而 n=50→n=496 scaling 已证明 G 值下降 42-85%。这是 fixable 的——n=496 数据已存在，重新计算 per-phase 分解即可。

2. **机制分析 (N2)**：discrimination collapse 的 effect size 与 severity gradient 之间存在 orders-of-magnitude 的 gap，削弱了论文的解释力。Fixable——通过 threshold amplification 讨论或降级 mechanism claim。

3. **Novelty (W2)**：这是不可通过修改弥合的根本分歧。论文本质是 characterization study（无新方法、无新系统），且 pilot mitigation 失败。R1 和 R2 对 characterization 的价值判断不同。如果 crossover 在 n=496 验证通过，novelty 论证加强（"单轴框架无法预测"）；如果 crossover 不成立或 magnitude 大幅缩水，novelty 进一步削弱。

**建议：**
- 如果 crossover 在 n=496 上 direction 保持 + magnitude 仍然 substantial + mechanism gap 被弥合/降级 → **Findings track acceptable, main conference borderline**
- 如果 crossover 在 n=496 上不成立或 magnitude trivial → **需要重新评估核心 contribution，可能 weak reject**

**前轮遗留 open issues 状态：**
- R5-W1 (Table 2 n=50): 升级为 N1 critical — 仍 open
- R5-W2 (crossover n=50): 升级为 N1 critical — 仍 open
- R5-1 (following ThinKV): 仍 open — 本轮再次确认
- R5-2 (LongFlow bib): 仍 open
- R5-3 (\placeholder): 仍 open
- R1-W1 (ThinKV wording): 仍 in_progress

**本轮新增 open issues**: 9 个 (R6-N2, R6-W1 through R6-W6, R6-M1 through R6-M5)

---

## Detailed Comments

### §1 Introduction
- Contribution 列表第 1 条 crossover 的证据在 §5.3 来自 n=50——需 n=496 数据支撑
- "entropy-discrimination collapse" 作为 Contribution 3 的 mechanism framing 与 §6 的 correlational evidence 有张力

### §3 Background
- background.tex:33 "following ThinKV" 必须修改——方法不同，不能用 "following"

### §4 Experimental Setup
- Bonferroni k=4 的 family definition 需更 prominent 地 reference BH-FDR
- Spearman ρ 应降为脚注，JT test 为 primary

### §5 Results
- Table 2 (n=50) 应替换为 n=496 per-phase table 或移至 Appendix
- §5.3 crossover 数字需在 n=496 上验证并报告 bootstrap CI
- §5.5 LLaMA CI/Wilcoxon 不一致需技术解释

### §6 Analysis
- §6.1 需报告 baseline Gini 和相对变化
- §6.1 需讨论 threshold amplification 或降级 mechanism claim
- §6.2 entropy redistribution 应精简（Qwen 不一致削弱叙事）

### §7 Discussion
- Pilot 失败的 implications 需更坦诚讨论
- 添加 PPL→accuracy gap 讨论
- "within a single generation (n=496)" 改为 "within individual generations, across n=496 problems"

### References
- h2o-neurips2023: title 为空
- LongFlow: 删除 "Withdrawn" 标注，改为 arXiv preprint
- 补引 "Hold Onto That Thought" (NeurIPS 2025)
- 验证 SnapKV first author

### Formatting
- main.tex:21: 删除 \placeholder 命令定义
- appendix_results.tex: orphaned file + duplicate label
- Abstract "over an order of magnitude" 应明确指 amplification ratio G