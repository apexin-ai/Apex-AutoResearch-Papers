---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T13:08:16.990855+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 3 审稿报告 — turn_residual_gating

**论文**: "Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)
**截止日期**: 2026-08-03
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）

---

## Summary

本文提出 ThreadGate，一种 per-layer content-and-turn-conditioned MLP gate，通过调制 residual stream 并结合 GAR auxiliary loss 来解决多轮对话中的注意力衰减问题。五路对比实验（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示所有训练时干预在 teacher-forced 下成功（GAR=0.50），但在 autoregressive 生成下 GAR 跌至 0.015–0.025（20–33× gap），gating 无增量贡献。论文将此归因于 exposure bias，并通过 inference-time attention steering 和 scheduled sampling 提供 mitigation 证据。跨模型在 Llama-3.1-8B 上确认了该 gap（27×）。

---

## Strengths

1. **五路对比实验设计精良**：系统性隔离 turn conditioning、gating mechanism、gradient direction conflict、fine-tuning 四个因素，每对对比有明确实验支撑。PCGrad 作为因果排除工具（modus tollens）的使用超出标准消融范式。[AGREE: R1, R2]
2. **诚实且有深度的 negative result**：不伪装成正面结果，直接呈现 gating 失败并追溯到 exposure bias 机制。TRC 指标作为正交验证增强了论证。[AGREE: R1, R2]
3. **Hedging 措辞适度**："a proximal cause consistent with our evidence" 比 "the root cause" 更准确；Discussion 明确列出了 alternative hypotheses（attention drift, KV cache effects, implicit label smoothing）。[AGREE: R1, R2]
4. **Loss formulation 搜索透明**：Table 2 (Appendix B) 记录 7 次迭代中 6 次失败的完整历程，为后续工作节省探索成本。[AGREE: R1, R2]
5. **跨模型验证**（Llama-3.1-8B）增强结论泛化性，尽管覆盖有限（2 model families, 3/5 conditions）。[AGREE: R1, R2]

---

## Weaknesses — Must-Fix (影响接收决定)

### MF-1 [Critical] GAR 全称引用错误 [AGREE: R1, R2]

Dongre et al. (2026, arXiv:2605.12922) 原文定义为 **"Goal Accessibility Ratio"**，本文在 Abstract、§1、§3.1 等所有位置误写为 "Goal Attention Ratio"。已通过 arXiv 原文验证。这是论文最核心度量指标的定义错误，直接损害学术严谨性。"Accessibility" 强调信息可达性（与论文引用的 AUC=0.98 linear probe 结果一致），"Attention" 缩窄到注意力权重。

**修复**: 全文替换为正确全称。可保留说明 GAR-ours 变体聚焦 attention weight。

### MF-2 [Critical] 正文超过 EMNLP 2026 的 8 页限制 [AGREE: R1, R2]

§6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。正文约 8.4 页，超出约 0.4 页。ARR 格式检查可能 desk-reject。

**修复**: 将 §6 instruction retention 段落移入 Appendix（~0.3 页）+ 压缩写作冗余（见 SF-3）。

### MF-3 [Critical] AR 评估样本量过小（N=5），核心 claim 缺乏统计检验 [AGREE: R1, R2]

Table 1 的 AR GAR 列仅基于 N=5 条 10-turn 对话。五个配置的 AR GAR (0.012–0.025) 差异在 N=5 下无法做统计区分。论文未报告 AR GAR 的 confidence interval 或条件间显著性检验。"all variants collapse equally" 这一核心 claim 缺乏统计支撑。

注：TF-AR gap 本身（0.50 vs 0.015–0.025，跨越一个数量级）即使 N=5 也不太可能是随机波动，且 seed 42/123 双种子结果一致。问题在于五个条件之间的 AR GAR 差异无法判断是否有意义。

**修复**: AR 评估扩大至 N≥30（与 steering 实验 N=50 对齐），报告 bootstrap 95% CI，做条件间成对检验。

### MF-4 [Critical] Scheduled sampling 单种子结果作为 contribution 可靠性不足 [AGREE: R1, R2]

两个种子结果差异大（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×，差异 31%），且训练策略不同（resume vs from scratch），无法分离 seed variance 和 strategy effect。Abstract 仅引用 seed 1 数据（gap 1.57×），给读者过高确定性印象。

**修复**: 从 contribution 列表降级为 Discussion 中的 preliminary observation，或补充 ≥3 个同策略种子。

---

## Weaknesses — Should-Fix (影响评分但不一票否决)

### SF-1 [Warning] Exposure bias 归因未完全排除替代假说 [R1: Critical, R2: Should-Fix → Director 裁定: Should-Fix]

KV cache drift（10-turn 中 KV cache 长度远超 TF 片段）、model-generated text 统计差异、GAR-ours 在 AR 下的有效性等替代假说在 Discussion 中仅一句带过。Steering 论证存在循环性风险（加 goal bias 当然增加 goal attention，无论原因是什么）。

但论文的 hedging 适度（"a proximal cause consistent with our evidence"），TRC+steering 组合提供了 non-trivial evidence：如果 root cause 是 representation degradation 而非 attention routing，β-steering 应无法恢复 meaningful GAR，但实际恢复了 11×。Negative result paper 不应被要求达到 causal inference 标准。

**修复**: 在 §5.3 或 §6 加一段明确讨论 KV cache drift 作为 confound（当前仅一句带过），承认 steering 论证的局限。不要求额外排除实验。

### SF-2 [Warning] Cross-model 验证不完整 [AGREE: R1, R2]

仅 3/5 条件（缺 +PCGrad, Uniform Gate），使用 median 而非 mean（未报告 mean 对照），N=20 偏小且与 TF N=50 不匹配。Attention spikes（5–8%）成因未解释。

**修复**: 报告 mean+median 双指标，展示 AR GAR 完整分布，在正文标注覆盖局限。

### SF-3 [Warning] "20–33× gap" 等数字在六个章节重复 8+ 次 [AGREE: R1, R2]

同一数字在 Abstract/§1/§4.2/§5.3/§5.5/§6/§7 反复出现，信息密度低，浪费页面空间（加剧 MF-2 超页问题）。

**修复**: Abstract 和 §4.2 各保留一次完整数字，后续章节改用 "the TF-AR gap (Table 1)" 等简洁回指。

### SF-4 [Warning] PCGrad modus tollens scope 过度概括 [AGREE: R1, R2]

§5.2 排除了 gradient direction conflict，但 magnitude imbalance (GradNorm) 和 Nash equilibrium violations 未测试。§1 contribution (1) 中 "gradient conflict" 未加 "directional" 限定词。

**修复**: "gradient conflict" → "gradient direction conflict"；结论处提及 magnitude imbalance 未排除。

### SF-5 [Warning] Contribution 声称需调整 [AGREE: R1, R2 (部分)]

- Contribution (1): "systematic diagnostic framework" + "in principle applicable to other auxiliary objective analyses" 未验证泛化性。R2 认为等同消融，R1 反驳认为 PCGrad exclusion + TRC 正交验证超出标准消融。**共识**: 删除 "in principle applicable"，保留 framework 表述。
- Contribution (2): "first empirical characterization" 风险高。**共识**: 改为 "to our knowledge, the first" 或 "a detailed"。
- 标题: R2 认为 "Per-Layer Residual Gating" 过宽（仅两种变体），R1 反驳标题准确描述所测试方法。**Director 裁定: 当前标题可接受**。

### SF-6 [Warning] 缺少 Rhea (arXiv:2512.06869, 2025) 引用 [AGREE: R1, R2]

Role-aware Heuristic Episodic Attention，inference-time multi-turn attention 方案，与 §4.3 steering 和 §6 Discussion 直接相关。

**修复**: 在 §2 "Attention manipulation" 段落引用，§6 与 β-steering 对比（Rhea 不需要 oracle access to goal tokens）。

### SF-7 [Warning] Instruction retention 分析不显著但占 Discussion 过多篇幅 [AGREE: R1, R2]

McNemar p=0.077 不显著，r=0.200 极弱。在超页压力下应优先压缩。

**修复**: 移入 Appendix 或压缩至一句（同时帮助解决 MF-2 超页问题）。

---

## Reviewer Consensus [AGREE]

1. GAR 全称引用错误必须修正（Critical）
2. 页数超限必须解决（Critical）
3. AR 评估 N=5 不足以支撑核心 claim "all collapse equally"（Critical）
4. Scheduled sampling 不应作为 contribution-level 声称——单种子 + 不同策略（Critical）
5. 写作冗余需压缩，关键数字回引简化
6. 论文是有价值的 negative result，五路对比设计超出标准消融
7. **两位 Reviewer 均给出 3.0/5 (Findings)**

---

## Reviewer Divergence

### 分歧 1: Exposure bias 归因严重性 [R1: Critical → R2: Should-Fix]

- **R1**: 替代假说（KV cache drift, text statistics）未排除，steering 论证存在循环性，"mechanistic analysis" 标题要求超越相关性的因果理解
- **R2**: 论文 hedging 适度，TRC+steering 组合提供 non-trivial evidence，negative result paper 不应等同 causal inference 标准
- **Director 裁定**: **Should-Fix**。论文已做合理 hedging，但 KV cache drift 讨论确实过于简略。不要求额外排除实验。

### 分歧 2: LoRA capacity saturation [R1: Should-Fix → R2: Minor]

- **R1**: LoRA 可能已饱和 TF GAR target，"gating 无用"结论可能是 capacity ceiling artifact
- **R2**: 此问题不影响核心 TF-AR gap claim——即使 LoRA 在 TF 饱和，也不解释 AR 崩溃
- **Director 裁定**: **Minor**。R2 反驳有理——LoRA saturation 仅影响 "gating vs LoRA-only" 对比解读，不影响论文核心结论。在 §4.2 加一句 acknowledge 即可。

---

## Questions

1. 如果 AR 评估扩大到 N=50，五个条件的 AR GAR 排序和 gap 大小是否保持不变？
2. Scheduled sampling 两个种子采用不同策略（resume vs from scratch），相同策略下 3+ 种子是否可行？
3. GAR 在 Dongre et al. 中的原始全称是 "Goal Accessibility Ratio"。使用 "Goal Attention Ratio" 是有意修改还是引用错误？
4. β-steering 需要 oracle access to goal token positions，在实际部署中如何确定 goal tokens？
5. "token-level self-recovery does not extend to auxiliary objectives" 是否是 trivially expected？论文贡献在于定量证据还是概念发现？
6. Cross-model 评估中 "5–8% sporadic attention spikes" 的成因是什么？systematic behavior 还是 noise？

---

## Missing References

1. **Rhea** (arXiv:2512.06869, Dec 2025): Role-aware Heuristic Episodic Attention，inference-time 多轮对话注意力方案 [AGREE: R1, R2]
2. **"Beyond Single-Turn: A Survey on Multi-Turn Interactions with LLMs"** (arXiv:2504.04717, 2025): 多轮对话综述 [R2 提出，R1 认为可选]
3. **Zhang et al., 2019** ("Bridging the Gap between Training and Inference for NMT"): exposure bias 在 NMT 中的经典分析 [R1 提出]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 4 warning, 12 info）。

**Warnings**:
- p3–4: Related Work + Method 连续 2 页无 figure/table，形成文字墙
- p7: Figure 4+5 同页，Figure 5 子面板 axis label 字号过小（~55–60% 正文字号），建议放大或改为全宽 figure*
- p8: Discussion 纯文本页，无 display item，建议加总结性表格
- p11: Appendix 最后页 ~70% 空白，建议合并 Appendix A 内容

**Info（选摘）**:
- Figure 1 全宽概念图信息清晰，颜色区分度好
- Table 1 booktabs 风格规范，float 位置良好
- 全文 5 figures + 2 tables = 7 个 display items，合理
- 无 margin 溢出、未解析引用或 LaTeX 错误残留

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings（可被 Findings 接收）**

**Reviewer Confidence: 4/5**

**Findings 而非 Conference 的核心原因**：4 个 critical must-fix 中，GAR 命名错误和超页属于格式/准确性问题可快速修复；但 AR 评估样本量不足（N=5）和 scheduled sampling 统计可靠性不足是实质性问题，需要额外实验才能解决。在补充多种子 AR 评估和 SS 实验之前，论文的统计基础不足以支撑 conference-level 接收。

**达到 Findings 标准的原因**：五路对比设计精良且超出标准消融（PCGrad exclusion + TRC 正交验证），negative result 对 multi-task LLM 训练社区有实际参考价值，exposure bias 对 auxiliary loss 的选择性破坏是有意义的发现，hedging 适度。论文的实验框架和分析深度超出一般 workshop paper。

**距 Conference (4.0) 的差距**：(1) AR 评估样本量和多种子覆盖需大幅加强；(2) scheduled sampling 需统计验证或从 contribution 降级；(3) 写作冗余需压缩以满足 8 页限制；(4) exposure bias 归因需更充分讨论替代假说。

---

## Detailed Comments

### Abstract
- "Goal Attention Ratio" → "Goal Accessibility Ratio"
- "Scheduled sampling compresses the gap to 1.57×" → 加强 "preliminary, single-seed" 标注或移除

### §1 Introduction
- Contribution (1): 删除 "in principle applicable to other auxiliary objective analyses"
- Contribution (2): "first empirical characterization" → "to our knowledge, the first" 或 "a detailed"
- Contribution (2): scheduled sampling 从 contribution 降级或加强 preliminary 标注

### §3.1 Preliminaries
- "Goal Attention Ratio" → "Goal Accessibility Ratio"（全文替换）
- 可保留说明 GAR-ours 变体聚焦 attention weight

### §4.1 Setup
- 确认 GPU 型号 "RTX PRO 6000 Blackwell Server Edition" 准确性

### §4.2 Main Results
- Table 1 AR 列: 扩大评估至 N≥30 + bootstrap 95% CI
- Table 1 caption: "GAR-O" 缩写在首句解释
- 加一句 acknowledge LoRA capacity saturation 替代解释

### §4.3 Inference-Time Steering
- 承认 β-steering 论证的循环性风险
- 明确 steering 证据 + TRC 组合的 inferential scope

### §5.2 PCGrad
- "gradient conflict" → "gradient direction conflict"
- 结论处提及 magnitude imbalance 未排除

### §5.5 Cross-Model
- 报告 mean + median 双指标
- 展示 AR GAR 完整分布
- 说明排除前两 turn 的理由
- 在正文标注 3/5 条件覆盖的局限

### §6 Discussion
- Instruction retention 段落移入 Appendix（解决超页问题）
- 加强 KV cache drift 讨论（不能仅一句带过）
- Scheduled sampling: 标注 "preliminary, single-seed, high-variance (GAR 0.318 vs 0.418 across two seeds)"

### §7 Conclusion
- 数字回引简化，不重复 "20–33×"

### Figure 4 caption
- 删除重复句："the gap persists across all five variants..., the gap persists across all five tested configurations"

### Bib
- grattafiori2024llama3: 统一作者列表格式
- 全文 "Goal Attention Ratio" → "Goal Accessibility Ratio"