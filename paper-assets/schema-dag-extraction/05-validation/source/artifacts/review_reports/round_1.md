---
round: 1
overall_score: borderline
timestamp: 2026-05-16T01:18:14.481430+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 1

**论文**: "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**目标 Venue**: EMNLP 2026 (ARR May 2025 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）
**轮次**: Round 1（独立初审 + 交叉分享，1 轮收敛）

---

## Summary

本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER (Few-NERD) / RE (FewRel) / ED (MAVEN) 三个任务，辅以跨模型验证 (Qwen3-32B + LLaMA-3.1-8B)，并通过 SDGD 实验报告 decompose-then-merge 的负面结果。研究问题定义清晰、实验设计严谨，但核心定量 claim 的统计基础薄弱，论文呈现存在严重缺陷。

---

## Strengths

**S1. 实验设计精良，因果推断层次清晰 [R1, R2 一致]。** Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，从观察到干预逐步升级。这在 LLM IE 文献中属首次。

**S2. Error taxonomy 分析质量高 [R1]。** IntraSub 随 BCS 单调递增（RE: ρ=0.954），RE 中 100% confusion 为 intra-batch，为 Channel 2 提供机制层面证据。

**S3. Centrality confound 发现有方法论价值 [R1, R2 一致]。** §4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，对后续 metric 设计有直接指导。

**S4. 跨模型验证设计合理 [R1, R2 一致]。** 不同模型家族 (Qwen vs Llama) + 不同规模 (32B vs 8B)，high-BCS accuracy 在两模型上收敛到 ≈51% 的 model-invariant floor。

**S5. 负面结果 (SDGD) 报告诚实且有信息量 [R2]。** 系统测试多种 decomposition mode，明确定位 merge amplification 为瓶颈。

**S6. 写作透明度高 [R1]。** Limitations section 主动披露 factorial 检验不显著、3.4× 为两点比较等问题。

---

## Weaknesses

### Must-Fix（4 项，两位 Reviewer 达成共识）

**MW1. 3.4× amplification 统计基础薄弱 [R1-W1, R2-W3 — 完全一致]**

3.4×（31.2pp / 9.1pp）是论文最突出的定量 claim，在 abstract/introduction/contributions/results 中至少出现 4 次，但：
- 16-rel 条件下 low/high BCS 各仅 1 个 batch，9.1pp 基线是单次观测，无 CI
- 16-rel 来自 validation split，80-rel 来自 train+val 合并 pool，跨 pool 比较引入混淆
- CI 传播后 1.9–4.7× 范围仍基于分母无 CI 的前提

**建议**: 在 80-rel pool 内构造 16-type 子集 BCS-controlled 实验（多 batch + CI），获取可比 baseline。否则 3.4× 必须降格为描述性观察，大幅降低修辞突出度。

**MW2. Pairwise SCS framing 与效应量不匹配 [R1-W2, R2-W2 — 共识+微调]**

r = 0.112, r² = 1.3%。Contribution 2 使用 "robust predictor" 措辞容易误导。R2 指出论文正文已三次承认解释力有限，"robust" 可能指可复现性而非效应量大——但 contribution list 的简短表述有误导性。

两位 Reviewer 完全一致的是：nonzero-confusion 子集分析 (ρ = 0.27–0.31) 存在 **conditioning-on-outcome bias**——剔除 confusion=0 pair 人为抬高相关性。

**建议**: 将 "robust predictor" 改为 "statistically significant but modest predictor"；保留 nonzero 分析但添加 conditioning bias 讨论；讨论剩余 98% variance 来源。

**MW3. NER count×confusability 交互证据不足 [R1-W3, R2 AGREE]**

§5.4 声称两个 channel "interact"，但唯一的直接检验（2×2 factorial, z=−0.67, p=0.50）不显著。正文措辞未反映这一结果。

**建议**: 将 "interact" 改为 "suggestive evidence of interaction"；在正文（非仅 Limitations）中提及 factorial 检验不显著。

**MW4. 正文零 figure [R2-W1, R1 AGREE]**

所有 `\includegraphics` 仅出现在 `\appendix` 后。Count curves、BCS scaling、error taxonomy 三张核心图全在附录。对于实证发现驱动的论文，reviewer 评估正文 8 页时无法看到最核心证据，不可接受。

**建议**: 将 Fig 1（count curves）和 Fig 2（BCS scaling）移入正文。

---

### Should-Fix（6 项）

**SW1. 无 Discussion section [R2-W4, R1 AGREE]**

discussion.tex 仅含 4 行 Conclusion。对于发现复杂且部分矛盾的论文（MAVEN 反转、centrality confound、SDGD 失败、NER 交互），缺少 Discussion 是严重缺陷。需讨论：两通道框架边界条件、SCS/BCS 差异化使用指南、merge amplification 方向、schema 设计操作性建议。

**SW2. SDGD "structural bottleneck" overclaim [R1-W4, R2 部分 REBUT]**

R2 认为理论论证有合理性（k pass 累积不校准预测是结构性质），confidence-gated 已覆盖校准思路。但仅两种 merge 策略 + 单数据集 (Few-NERD) 不足以支撑 "structural" 修饰语。

**共识建议**: 弱化为 "structural challenge for union-based merge pipelines"；补做 FewRel SDGD 实验；测试 majority voting。

**SW3. v1/v2 prompt 切换引入实验内混淆 [R1-W5, R2 AGREE]**

v1 (fabricate offset 96.5%) 用于 NER count curves 和 BCS-controlled；v2 用于后续实验。Table 6 证实 v1 vs v2 recall 差 8pp。虽然 within-experiment 相对结论仍有效，但跨实验绝对数值不可比。

**建议**: 统一用 v2 重跑 NER count curves，或提供 v1/v2 对照消融。

**SW4. MAVEN 结果限制 generalizability [R2-W5, R1 PARTIALLY AGREE]**

MAVEN 上 count channel 反转、mean BCS 聚合失效，SCS/BCS 适用范围被限制在 cross-domain schema。R1 指出论文对此的处理比 R2 给的 credit 更充分（§4.5 有完整因果解释），但 same-domain schema 在实际应用中常见（医疗 NER、法律 RE），generalizability 确实缩小。

**建议**: Abstract/introduction 添加适用范围限定；Discussion 充分讨论 same-domain 局限。

**SW5. Limitations section 结构差 [R2-W7, R1 AGREE]**

单段 ~20 行涵盖 6+ 个议题，难以评估各 limitation 严重程度。

**建议**: 结构化为分点列表并标注严重程度。

**SW6. Prompt 模板未在 appendix 中提供 [R1-W8, R2 AGREE]**

对于 zero-shot IE 研究，prompt 本身就是方法的核心部分，必须完整公开。

---

### Minor（6 项）

- **m1.** MiniLM 引用错误：`\cite{minilm-2019}` 指向 Sentence-BERT，应引 Wang et al. 2020 (NeurIPS) [R2-W8, R1 AGREE]
- **m2.** MAVEN 反转未在 abstract 中限定：abstract 写 "count channel suppresses recall" 无限定词 [R1-W9, R2 AGREE]
- **m3.** 缺少 Responsible NLP Research Checklist [R2-W9, R1 AGREE]
- **m4.** FewRel train+val 合并为非标准设置，抽样方式未说明 [R2-W10, R1 AGREE]
- **m5.** "Multi-channel degradation model" 应改为 "framework" 或 "taxonomy" [R2-W11, R1 AGREE]
- **m6.** FewRel 1,000 balanced instances 抽样方式未说明 [R1-W7, R2 AGREE]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下核心判断上完全一致：

1. **3.4× amplification 是最严重的方法论问题**——需要实验补充或大幅降级 claim
2. **NER 交互效应缺乏统计支撑**——正文措辞必须降级
3. **正文无 figure 不可接受**——核心 evidence 必须在正文呈现
4. **论文整体达到 Findings track 接收水平**——实验设计是主要优势，但 effect size 弱 + 呈现缺陷限制了主会议竞争力
5. **Pairwise SCS conditioning bias 需要修复**——nonzero-confusion 子集分析存在方法论问题

## Reviewer Divergence [REBUT]

分歧集中在严重程度评估而非方向：

1. **SCS "robust predictor" framing (R1-W2)**：R1 认为论文 "掩盖" 了 r²=1.3%；R2 反驳认为论文正文已三次承认解释力有限，"robust" 指可复现性。**Director 判断**：R2 的 rebut 有道理——论文的 framing 比 R1 描述的更审慎，但 Contribution 2 的措辞确实需要修改。

2. **SDGD "structural bottleneck" (R1-W4)**：R1 认为仅两种策略不足以声称 "structural"；R2 反驳理论论证有合理性。**Director 判断**：R2 的理论论点成立（union-based merge 的结构性质），但需弱化表述 + 补实验。

3. **Embedding 不一致 (R1-W6)**：R1 认为是 should-fix；R2 反驳这实际是 robustness check，within-dataset 分析不受影响。**Director 判断**：R2 的 rebut 成功——两种 embedding 结果一致 (ρ=0.168 vs 0.144)，这是优势而非劣势。**从 weakness 列表中移除**。

4. **Supervised baseline (R1-W10)**：R1 认为需要参照；R2 反驳本文是诊断性研究，supervised baseline 不在 scope 内。**Director 判断**：R2 的 rebut 成功。**从 weakness 列表中移除**。

---

## Questions（需作者澄清）

1. **16-rel 为何仅一个 extreme batch？** C(16,8)=12,870 种组合，技术障碍是什么？[R1-Q1, R2-Q1 一致]
2. **是否探索过多变量模型**（加入 type frequency、prompt position）提升解释力？[R1-Q2, R2 支持]
3. **SDGD single_pass baseline 用的是 v1 还是 v2？** Table 5 未标注。[R1-Q3, R2 AGREE 认为关键遗漏]
4. **Residualized BCS**：对 MAVEN mean BCS 去除 centrality component 后，是否恢复预期相关方向？[R2-Q2, R1 强烈支持]
5. **High-BCS ≈51% floor 的来源？** 远高于随机猜测 (1/8=12.5%)，需解释机制。[R1-Q5, R2 提出 "混淆子组" 假设]
6. **Non-zero temperature 对 type confusion 的影响？** [R2-Q5, R1 认为次要]

---

## Missing References

1. **"Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion" (AAAI 2026)** — confusion-aware prompting for IE，高度相关 [R2 提出, R1 AGREE]
2. **MiniLM 原始论文 (Wang et al., 2020, NeurIPS)** — 当前引用 Sentence-BERT 不准确 [R2 提出, R1 AGREE]
3. **Sclar et al. 2024 (TACL) — prompt sensitivity** — 与 v1/v2 差异讨论直接相关 [R2 提出, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | **3/5** |
| Excitement | 3.5/5 | 3/5 | **3/5** |
| Overall | 3/5 | 3/5 | **3/5 (Borderline → Findings track)** |
| Confidence | 4/5 | 4/5 | **4/5** |

**总评: Borderline (3/5) — 推荐 Findings track 接收，主会议需实质修改。**

实验设计是 LLM IE 文献中最严谨的之一（从 correlational 到 interventional 的层次化推理），centrality confound 和 merge amplification 发现有实际指导价值。但：

1. 核心定量 claim (3.4×) 统计基础薄弱
2. 主要 predictor 解释力极弱 (r² < 2%) 且存在 conditioning bias
3. NER 交互效应缺乏统计支撑
4. 呈现问题严重（零 figure + 无 Discussion）
5. MAVEN 结果限制 generalizability 至 cross-domain schema

修复 MW1–MW4 + SW1 后可上升至 weak accept (Findings)。若补充 80-rel pool 内 16-type 实验、v2 count curves 重跑、FewRel SDGD，可具备主会议竞争力。

---

## Detailed Comments

### §1 Introduction
- Contribution 1 中 "interact" 需降级为 "suggestive" [MW3]
- Contribution 2 中 "robust predictor" 需改为 "statistically significant but modest predictor" [MW2]
- Contribution 3 中 3.4× 应附 CI 或降格 [MW1]
- "Multi-channel degradation model" → "framework" [m5]

### §3 Methodology / §4 Experiments
- v1/v2 prompt 切换需在方法论部分显式说明适用范围 [SW3]
- FewRel 数据构造需补充抽样细节 [m4, m6]
- MiniLM 引用需更正 [m1]

### §5 Results
- §5.2 nonzero-confusion 子集分析需添加 conditioning bias 讨论 [MW2]
- §5.3 amplification 部分需降低修辞突出度或补充实验 [MW1]
- §5.4 NER 交互措辞需降级 [MW3]
- MAVEN count channel 反转需在正文更显著地限定 [m2]
- 核心 figures 必须从 Appendix 移入正文 [MW4]

### §6 SDGD
- "structural bottleneck" → "structural challenge for union-based merge pipelines" [SW2]
- 补做 FewRel SDGD + majority voting [SW2]
- 明确 single_pass baseline 的 prompt 版本 [Q3]

### §7 Discussion（需新建）
- 两通道框架的理论边界条件 [SW1]
- SCS/BCS 在 same-domain vs cross-domain 的差异化指南 [SW4]
- Merge amplification 的可能解决方向 [SW2]
- 对实际 schema 设计的操作性建议 [SW1]

### Appendix
- 补充完整 v1/v2 prompt 模板 [SW6]
- 添加 Responsible NLP Research Checklist [m3]

### References
- 添加 3 条遗漏引用 [见 Missing References]