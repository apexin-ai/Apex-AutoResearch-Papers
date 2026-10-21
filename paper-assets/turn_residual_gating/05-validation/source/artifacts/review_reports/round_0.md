---
round: 0
review_mode: 
overall_score: weak reject
timestamp: 2026-05-19T15:48:40.194550+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 圆桌审稿报告（Round 1）

**论文**: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**Venue**: EMNLP 2026 via ACL Rolling Review
**审稿人**: Reviewer 1（方法/实验）、Reviewer 2（Novelty/Related Work）
**日期**: 2026-05-19

---

## Summary

本文提出 ThreadGate——一种基于标量残差门控的轻量方法，试图通过辅助 GAR（Goal Attention Ratio）损失修复多轮对话中的注意力退化问题。在 Qwen-2.5-7B 和 Llama-3.1-8B 上的实验表明，尽管训练时 GAR 显著提升（0.48），推理时 GAR 仅为 0.016，产生约 30× 的训练-推理鸿沟。论文将此失败归因于两个机制：NTP-GAR 梯度竞争（NTP 梯度幅度 7-15× 主导 GAR）和 teacher-forcing 分布偏移（exposure bias）。Scheduled sampling 将 gap 从 30× 缩小至 12.3×（p≈0.07），提供了 exposure bias 作为主因的间接因果证据。

---

## Strengths

**S1. 有价值的负面结果**：社区需要知道"训练时优化 GAR 不等于推理时 GAR 提升"。两个失败机制的归因（梯度竞争 + exposure bias）为后续工作提供了明确的避坑方向。[R1, R2 共识]

**S2. 实验设计方法论规范**：Qwen 上的 4-way 消融（Base/LoRA-only/ThreadGate/Uniform Gate）有效隔离了各组件贡献。Uniform Gate 对照组证明 per-layer specialization 无额外增益，是消融设计亮点。Bootstrap CI（10K resamples）提供了统计保障的框架。[R1 主导发现]

**S3. 跨模型方向一致性**：Qwen（30× gap, 67-79% conflict rate）和 Llama（26× gap, 65-56% conflict rate）的结果方向一致，增强了核心发现的可信度。[R1, R2 共识]

**S4. 梯度冲突量化分析**：Table 6 的逐层、逐 epoch 梯度统计（conflict fraction、magnitude ratio）提供了比总体数字更丰富的机制证据，是论文最有说服力的分析。[R1, R2 共识]

**S5. 诚实的学术 hedging**：§7 Discussion 坦承结果的范围限制，Contribution 4 用"suggestive evidence"而非断言，Limitations 部分明确了适用条件。[R2 主导发现]

**S6. 清晰的叙事结构**：从问题定义（§1-3）→ 方法设计（§4）→ 负面结果（§5）→ 机制分析（§6）→ 缓解探索（§7）的逻辑链条连贯。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [format/critical] 所有引用渲染为 "?"——bibliography 编译失败** [R1-N1, R2 同意]
PDF 中 37 处 \citep/\citet 均显示为 "?"。引用审计发现：3 条 bib 在 OpenAlex 未找到（含核心依赖 dongre2026）、5 条 author/year 不匹配、4 条 orphan entries。这是投稿级 disqualifying issue，审稿人无法验证任何基于先行工作的 claim。

**MF2. [framing/critical] 标题 "Cannot" 过度声称** [R2-N2, R1 确认]
标题使用绝对否定"Cannot"，但：(a) 仅测试标量 per-layer gate 一种变体；(b) scheduled sampling 将 gap 从 30× 降至 12.3×，说明训练策略变化即可部分修复；(c) §7 自己承认"our findings are specific to lightweight residual gating with auxiliary GAR losses"。标题的绝对性与证据范围严重不匹配。

**MF3. [framing/critical] Novelty 声称过高——两个核心机制均为已知现象** [R2-N1, R1 同意]
梯度竞争 = multi-task gradient conflict（GradNorm 2018, PCGrad 2020 已有成熟方案）；distribution shift = exposure bias（Bengio et al. 2015）。论文在 Abstract 声称"first quantitative measurement"，但量化一个预期现象的具体数值不构成方法论贡献。两位 Reviewer 共识：这是 confirmatory quantification，novelty 有限。

**MF4. [framing/critical] Related Work 缺失 multi-task gradient conflict 关键文献** [R2-N4, R1 同意]
§6.1 核心机制正是 multi-task gradient conflict，但 §2 完全未讨论 GradNorm/PCGrad/CAGrad/Nash-MTL。更关键的是，如果 PCGrad 能解决梯度竞争，论文的"失败"可能仅因未使用正确优化策略而非 gating 固有局限——缺少 gradient surgery baseline 使核心结论悬空。

**MF5. [experiment/critical] 单种子 (seed=42) 支撑绝对否定 claim** [R1-N2, R2 同意]
所有实验仅一次训练。Bootstrap CI 覆盖 eval variance 但不覆盖 training variance（权重初始化、batch shuffling、dropout）。对于声称"不可能 work"的论文，无法排除"seed=7 下 gap 仅 5×"的可能性。负面结果论文的证据标准应高于正面结果论文。

**MF6. [experiment/critical] 评估样本量过小（50 conversations），统计功效不足** [R1-N3]
Cohen's d ≈ 0.22（小效应量）在 n=50 下 power 不足以区分"真零效应"与"underpowered 假阴性"。Scheduled sampling p≈0.07 在 α=0.05 下不显著但被列为正式 Contribution。

**MF7. [method/critical] 损失函数超参数和 v1-v6 配置定义缺失** [R1-N4, R2 同意]
λ_GAR、λ_div 具体数值从未报告；L_div 无数学定义；v1-v6 共 6 个 loss 变体完全无细节。读者无法判断 v7 是 principled selection 还是 cherry-picking，无法复现任何实验。

**MF8. [format/critical] 核心先行工作 Dongre et al. (2026) 不可查证** [R2-N3, R1 同意]
论文整个动机链（GAR 定义、probe AUC baseline、"27-48% drop"数据）依赖此引用，但 OpenAlex 查证 similarity score 仅 0.336，无法确认该文是否存在或已发表。如不可验证，实验框架基础悬空。

### Should-Fix（影响评分但不一票否决）

**SF1. [writing/critical] 全文零 figure——"Mechanistic Analysis" 论文无可视化** [R1-W4, R2 同意升级]
9 个 table 的纯数值呈现无法替代 attention heatmap、training curve、gate distribution 等标准机制分析视觉证据。§6.3 声称"attention heatmaps are visually indistinguishable"但不展示让读者判断。R1 首先发现，R2 在交叉回应中承认遗漏并升级为 major weakness。

**SF2. [experiment/warning] Llama 上未测试 Uniform Gate——跨模型消融不对称** [R1-W1, R2 同意]
Qwen 4-way vs Llama 3-way。Uniform Gate 是排除 per-layer specialization 价值的关键对照，Llama 缺失使跨模型声称不完整。

**SF3. [method/warning] 范围过窄——仅标量门控不足以支撑 "lightweight gating" 一般性结论** [R2-W1, R1 同意]
未测试 vector gate、head-specific gate、low-rank gate 等变体。论文仅覆盖约 20% 的 lightweight gating 假设空间。标题用泛称"Lightweight Gating"但证据仅针对最简单的标量变体。

**SF4. [experiment/warning] 无 λ_GAR 敏感性消融** [R1-W2]
梯度冲突严重程度直接取决于 λ_GAR 大小。仅一个 λ 值不能支撑"本质上不行"的结论。

**SF5. [experiment/warning] Scheduled sampling 因果推断局限** [R1-W5, R2 同意]
仅测试 50% ratio、仅 Qwen、p≈0.07 不显著、SS 对 PPL 影响未报告。Contribution 4 的支撑不足。

**SF6. [experiment/warning] 训练数据量（1,000 conversations）可能是混淆变量** [R1-W3]
对 7B 模型 LoRA 微调偏少，gate 可能未学到 robust 模式。Limitations 未讨论。

**SF7. [method/warning] GAR 单指标依赖的局限性未充分讨论** [R2-W3, R1 同意]
所有机制分析建立在 GAR 上。下游验证 r=0.82 通过 sanity check 但不足以建立 gold-standard proxy 地位。未讨论 GAR 的 construct validity 局限或替代指标。

**SF8. [experiment/warning] Reverse turn conditioning 证据间接** [R1-W6]
Gate attenuation 仅 2-7%（mean 93-98%），无显著性检验，差异可能是数值噪声。

**SF9. [format/warning] 无代码/数据发布** [R1, R2 共识]
负面结果论文的可复现性尤为重要——读者需要验证负面结果非实现 bug。

### Minor Issues

- §1 "probe AUC up to 0.98" 基线和计算方法应在正文简述
- §4.2 v1-v7 loss 选择过程仅一句带过
- Table 1 "Relative drop" 行未明确标注基线
- §5.5 Table 5 bootstrap CI 包含零，应更明确说明 ThreadGate 增量效果可能完全不存在
- Abstract "30× training-inference gap" 表述有歧义（比值还是相对退化幅度）
- 正文约 6 页，远低于 EMNLP long paper 8 页上限，有空间补充缺失内容
- liu2016attention 引用可能错配（语音识别 vs 注意力引导）
- 4 条 orphan bib 条目（vaswani2017, elhage2021, olsson2022, efron1994）
- 无独立 Limitations section 标题（嵌入 §7 Discussion 内）
- Appendix 表格编号可能与正文冲突

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：

1. **引用全部失效是 disqualifying issue**——投稿级硬伤，必须修复
2. **标题 "Cannot" overclaims**——证据仅支持 "fails to" under tested conditions
3. **零 figure 是重大弱点**——"Mechanistic Analysis" 论文无可视化不可接受
4. **单种子不足以支撑负面结论**——bootstrap CI 不覆盖 training variance
5. **Novelty 有限**——两个核心机制是已知现象（gradient conflict + exposure bias）的组合应用
6. **范围过窄**——仅标量门控不能代表 "lightweight gating" 类别
7. **Overall 评分一致**：Weak Reject / Borderline Findings

## Reviewer Divergence [REBUT]

仅一处分歧（已在交叉回应中澄清）：

- **标题版本问题**：R1 确认 PDF 标题为 "Cannot Fix"，R2 初审中提到 Director 描述的标题为 "Struggles to Fix"。经核实 PDF 原文使用 "Cannot"。分歧已消解——双方一致认为 "Cannot" 过强。

---

## Questions（需要作者澄清）

1. Dongre et al. (2026) 是否已公开发表？请提供 arXiv 链接或会议接收确认。
2. λ_GAR 和 λ_div 的具体数值是什么？v1-v6 的 loss 配置和关键结果？
3. Goal token 的标注方式（手动/自动，position matching/语义匹配）？
4. 是否考虑过 PCGrad 或 GradNorm 来缓解梯度竞争？如果是，结果如何？
5. 在不同 seed 下 30× gap 是否稳定复现？
6. Instruction compliance 的具体测量方式是什么（格式遵守 vs 语义遵循）？
7. 引用编译失败是提交版本问题还是编译环境问题？

---

## Missing References

以下文献与论文核心机制直接相关但完全未被引用：

| 文献 | 相关性 |
|------|--------|
| GradNorm (Chen et al., ICML 2018) | 动态调整 loss 权重以平衡梯度幅度——直接对应 §6.1 梯度竞争 |
| PCGrad (Yu et al., NeurIPS 2020) | 投影消除梯度方向冲突——§6.1 核心机制的已知解决方案 |
| CAGrad (Liu et al., NeurIPS 2021) | 冲突感知梯度下降——multi-task gradient conflict 方向 |
| Nash-MTL (Navon et al., ICML 2022) | 纳什博弈框架下的多任务优化 |
| Ranzato et al. (2016), Wiseman & Rush (2016) | Exposure bias 在 sequence generation 中的量化先例 |

已引用但讨论不足：
- Li et al. (ITI, 2024) 和 Zou et al. (RepE, 2023)：推理时干预方法，绕过 exposure bias，是更有希望的替代方向，论文仅一句列举

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。项目配置中未启用外部审稿（`external_review.paperreview_ai.enabled` 未配置）。

---

## Visual Layout Check（非评分项）

**状态**：未启动。视觉审查 Agent 因 `review_paper_pdf_path` 未配置而派发失败。

基于 Reviewer 观察的排版问题摘要：
- 全文 0 figure（9 tables only）
- 正文约 6 页，低于 EMNLP long paper 8 页上限
- 引用全部显示为 "?"
- Appendix 表格编号可能与正文冲突
- 无独立 Limitations section 标题

---

## Overall Assessment

### 评分汇总

| 维度 | R1 最终 | R2 最终 | 综合 |
|------|---------|---------|------|
| **Soundness** (ARR 5-pt) | 3/5 | 2.5/5 | **2.5/5** |
| **Excitement** (ARR 5-pt) | 2.5/5 | 2/5 | **2/5** |
| **Reproducibility** (ARR 5-pt) | 2/5 | 3.5/5 | **2.5/5** |
| **Soundness** (6-pt) | 3.5/6 | — | **3/6** |
| **Novelty** (6-pt) | — | 2.5/6 | **2.5/6** |
| **Significance** (6-pt) | 3/6 | 2.5/6 | **2.5/6** |
| **Clarity** (6-pt) | 3/6 | 3/6 | **3/6** |
| **Overall** (ARR 5-pt) | 2.5-3.0 | 2.5 | **2.5/5 — Borderline Findings** |
| **Overall** (6-pt) | 3/6 | 3/6 | **3/6 — Weak Reject** |

### 综合判断

**ARR Overall Assessment: 2.5 / 5 — Borderline Findings**

论文提出了一个合理的研究问题（轻量门控能否修复多轮注意力退化），实验设计框架（4-way 消融 + 跨模型验证 + scheduled sampling 因果测试）方法论思路正确，梯度冲突量化分析有信息价值。

但论文有 8 个 critical 级别问题和 9 个 warning 级别问题。核心障碍：

1. **格式硬伤**：引用全部失效 + 零 figure——即使内容过关，这两个 presentation 问题在 ARR 审稿中可能直接拉低 1-2 个 notch
2. **Novelty 不足**：两个核心机制（gradient conflict + exposure bias）是已知现象的组合应用，缺少 multi-task gradient conflict 领域的关键文献和 baseline
3. **证据不足以支撑 claim 强度**：标题"Cannot"与单种子、标量门控唯一变体、50 样本的证据范围严重不匹配
4. **可复现性低**：关键超参未报告、核心引用不可查证、无代码发布

**当前状态不满足 EMNLP 2026 Main Conference 接收标准（需 ≥4.0）。** Findings 接收（≥3.0）需要至少修复：引用编译、增加图表、多种子训练、报告全部超参。Borderline Conference（≥3.5）还需补充 gradient surgery baseline 和更多门控变体。

### 修改路径

**达到 Findings (3.0) 的最低要求**：
1. 修复 bibtex 编译，清理引用
2. 增加 2-3 张关键 figure（training curve、attention heatmap、gate distribution）
3. 至少 3 个 seed 的 mean±std
4. 报告所有 λ 值和 loss component 定义
5. 修正标题："Cannot" → "Fails to"

**达到 Borderline Conference (3.5) 的路径**：
- 以上全部 + gradient surgery baseline（PCGrad）+ 至少一种非标量门控变体 + Llama Uniform Gate + λ_GAR sensitivity sweep + 更大评估集

### Reviewer 信心

- R1 Confidence: 4/5（实验方法论在专业领域内）
- R2 Confidence: 4/5（熟悉 exposure bias、multi-task optimization 和 transformer 机制分析文献）

---

## Detailed Comments

### §1 Introduction
- "first quantitative measurement" 声称需降级为 "first empirical demonstration in the attention-steering context"
- "probe AUC up to 0.98" 需在正文简述计算方法
- "30× training-inference gap" 表述有歧义，需精确定义

### §2 Related Work
- 完全缺失 multi-task gradient conflict 子节（GradNorm/PCGrad/CAGrad/Nash-MTL）
- ITI 和 RepE 仅一句列举，应深入讨论为什么推理时方法可能更适合
- liu2016attention 可能错配（语音识别 vs 注意力引导）

### §3 Background
- GAR 定义依赖 Dongre et al. (2026)，如该引用不可验证需自包含重新定义
- Goal token 标注方式未说明

### §4 Method
- §4.1: 仅标量门控（ReZero 风格），未讨论为何不测试 vector gate 等变体
- §4.2: λ_GAR、λ_div 数值缺失；L_div 无数学定义；v1-v6 无任何细节
- §4.3: 1,000 conversations 是否足够未讨论

### §5 Experiments
- 单种子（seed=42）是核心限制
- n=50 评估样本统计功效不足
- Table 2 Qwen 4-way 设计好，Table 3 Llama 缺 Uniform Gate
- Table 5 bootstrap CI 包含零——应更明确说明增量效果可能完全不存在

### §6 Mechanistic Analysis
- §6.1: 梯度竞争分析有价值（Table 6），但本质是 multi-task gradient conflict 的 re-discovery
- §6.2: Reverse turn conditioning 证据间接（2-7% attenuation 无显著性检验）
- §6.3: 声称 heatmaps "visually indistinguishable" 但不展示——需要图表
- §6.4: Exposure bias 归因概念上预期；scheduled sampling p≈0.07 不显著
- §6.5: 下游验证 r=0.82 通过 sanity check 但不充分

### §7 Discussion
- Hedging 诚实，但与标题/Abstract 的 overclaiming 不一致
- Scheduled sampling 仅 Qwen、仅 50% ratio、PPL 影响未报告
- Future directions 过于模糊，缺乏具体实验路径

### 格式/呈现
- 全文 0 figure，9 tables——机制分析论文不可接受
- 引用全部失效（"?"）
- 正文 ~6 页 vs EMNLP 8 页上限——有空间补充内容
- 4 条 orphan bib entries
- 无独立 Limitations section 标题
