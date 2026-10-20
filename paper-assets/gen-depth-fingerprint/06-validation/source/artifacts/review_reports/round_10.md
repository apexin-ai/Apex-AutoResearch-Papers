---
round: 10
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T16:48:04.361628+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计声明; R2: 新颖性/完整性/Related Work/写作质量）
**轮次**: Round 1（独立审稿 + 交叉分享，1 轮收敛）

---

## Summary

本文提出 ordinal generation depth estimation 任务，将 AI 文本检测从二分类扩展为三分类（gen-0/gen-1/gen-2+）。核心发现是 differential depth response (DDR)：在递归生成链中，central-tendency features 随深度单调漂移，而 shape features 近似平稳。基于 7 个手工特征 + XGBoost 的分类器在 8 个 base model 生成器的 LOGO 评估下达到 3-class macro F1=0.762，leak-free binary F1=0.694。

---

## Strengths

1. **任务定义新颖且及时**：从 binary detection 扩展到 ordinal depth estimation 是有价值的研究方向，与两篇 concurrent work 的定位区分准确。
2. **评估协议严谨**：LOGO cross-validation + 14 个附录消融（cross-domain, cross-temperature, perturbation robustness, LOFO, QLoRA, 5-class 等），覆盖面远超同类投稿。
3. **统计方法规范**：Bonferroni 校正、percentile bootstrap CI、TOST 等价性检验、KS 检验使用得当。
4. **DDR 框架提供可解释洞察**：drifting vs. stationary 的分离是有启发性的实证观察。
5. **透明诚实**：明确承认已知缺陷（gen-0 泄漏、base-model-only、instruction-tuning failure）。
6. **轻量且可复现**：仅需 410M 参考模型 + 7 特征 + XGBoost（1.48M 参数），计算成本极低。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**MF1** [critical, consensus R1+R2] **Abstract framing 误导 + Gen-0 数据泄漏膨胀 headline metric**

所有 generators 共享相同的 gen-0 Wikipedia seeds。在 LOGO 中，held-out generator 的 gen-0 测试样本与训练集 gen-0 完全相同，构成数据泄漏。Confusion matrix 显示 gen-0 recall=99.4%（几乎完美）vs gen-1=75.0%/gen-2+=73.7%。3-class LOGO F1=0.762 因 gen-0 的 trivially 高分类而膨胀。

更严重的是，Abstract 以 cross-model chains 的 0.809 领衔（该设定甚至不使用 LOGO），LOGO 0.762 次要，而 leak-free binary F1=0.694（唯一不受泄漏影响的指标）完全未出现在 Abstract 中。真实的跨生成器无泄漏性能（0.694）与 Abstract 主打数字（0.809）相差 11.5pp。

**Required action**: (a) Abstract 以 leak-free binary F1=0.694 为主指标；(b) 3-class F1 标注 gen-0 泄漏 caveat；(c) 理想方案：为每个 generator 使用独立 seed set 消除泄漏。

---

**MF2** [critical, consensus R1+R2] **仅限 base model，实际适用性与 Introduction 动机根本性脱节**

全部 8 个 generator 为 base (pretrained) model。唯一的 instruction-tuned 实验：OLMo-Instruct LOGO F1=0.338，Qwen3-0.6B-chat length-matched binary F1≈0.50（近随机）。现实中网络 LLM 文本几乎全部来自 instruction-tuned/RLHF 模型。

Introduction 以 "web-crawled pretraining corpora increasingly contain LLM-generated text" 和 "provenance tracking" 为动机，但方法在实际应用场景中完全失效。且仅有单一 instruct model 数据点，无法判断这是系统性限制还是 model-specific。

**Required action**: (a) Reframe Introduction 动机——从 "解决 web contamination" 转为 "理解 recursive generation 分布特性"，定位为 analytical/scientific contribution；(b) Abstract 明确 "base model" scope；(c) 减少 practical applicability 暗示。

---

**MF3** [critical, consensus R1+R2] **标题 "Ordinal" framing 与实际方法存在根本性矛盾**

论文自身证据表明 ordinal structure 不提供任何增益：
- Appendix D：CORAL ordinal regression, Frank-Hall reduction 均与 multiclass XGBoost 表现相当（overlapping CIs）
- 5-class 尝试 F1 仅 0.50，gen-2/gen-3 F1=0.268/0.259
- Gen-1/gen-2+ binary error rate 48%

标题 "Ordinal Generation Depth Estimation" 创造了序数回归方法论贡献的预期，但实际是 3-class multiclass classification。序数性质在方法论和特征层面均未被有效利用。

**Required action**: (a) 去掉标题中 "Ordinal"，改为 "Generation Depth Classification"；或 (b) 提供证据证明 ordinal structure 有帮助。

---

### Should-Fix（影响评分但非一票否决）

**SF1** [warning, consensus] **DDR "机制解释" 超越实证证据**

"Location shift preserving distributional shape" 的断言仅基于 7 个 summary statistics 的 Spearman ρ 和 KS 统计量，而非对完整 NLL 分布的直接分析。Discussion 中 "softmax architecture constrains shape" 是未经验证的直觉。

→ 弱化措辞为 "empirical pattern" 而非 "mechanism"，或补充完整 NLL 分布直方图对比验证。

**SF2** [warning, consensus] **Multi-detector ensemble 在 3-class（核心任务）上优于所提方法**

Table 4：4-det+surface 3-cl F1=0.795 > 7-feature 0.774（2.1pp gap）。Introduction "competitive performance" 措辞模糊了这一事实。方法的核心竞争力仅在 cost-efficiency，而非 detection quality。

→ Introduction 明确表述 cost-accuracy trade-off。

**SF3** [warning, consensus] **6-gen/5-gen/8-gen 子集混用，数字难以横向比较**

Table 1 (8-gen, F1=0.762) vs Table 4 (6-gen, F1=0.774)——同为 LOGO 但不可比。Llama/Mistral 更难分类导致 8-gen 下降 1.2pp，但从未解释。Appendix 大量使用 6-gen，无统一说明。

→ 添加 generator-subset summary table；主实验统一 8-gen；解释差异来源。

**SF4** [warning, consensus] **Downstream utility (Contribution 3) 本质是 null result**

TOST 表明 depth-aware curation = random subsampling（±2% margin, p<0.001）。仅 n=3 seeds、单一 metric (perplexity)、小 scale (3,951 samples)。论文 frames 为 "decoupling detectability from harm"，但同样读作 "depth info has no curation utility"——与 data quality 动机矛盾。

→ 在 Discussion 中诚实承认 null result；减少 Abstract/Introduction 中的 prominence。

**SF5** [warning, consensus] **温度敏感性讨论不足**

t=1.0 时 6pp degradation；cross-temperature transfer（t=0.7 训练 / t=1.0 测试）Qwen3-1.7B 从 0.789 骤降至 0.418。Cross-domain (t=1.0) 与 Wikipedia (t=0.7) 方向矛盾。论文对 unknown-temperature 部署场景的影响讨论不充分。

→ 主文讨论 cross-temperature failure 及 unknown-temperature 限制。

**SF6** [warning, consensus] **Reference model family bias 未分析**

Pythia-410M 作为 reference model，对 Pythia 家族 generators 可能产生 same-family 优势。Table 2 cross-reference 实验无法隔离此效应。

→ 报告 same-family vs cross-family per-generator F1。

---

### Minor

1. Discussion 过度使用 `\paragraph{}`（7+ 标题），典型 AI 写作风格——应合并为 3-4 个自然段。
2. "Entropy" 实为 token-level NLL/surprisal，仅 footnote 1 说明，易混淆——应在正文中更明确。
3. Tail decay rank 范围 100-1000 缺乏理论支撑（LOFO 显示影响极小，低优先级）。
4. Appendix G confusion matrix 使用 6-gen 而非 8-gen，与 Table 1 不对齐。
5. |ρ| < 0.10 定义 "near-stationary" 阈值缺乏理论依据。
6. Cross-domain 使用 t=1.0 而非主实验 t=0.7，结果不可直接比较。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全独立发现并达成 [AGREE]：
- Gen-0 数据泄漏 + Abstract framing 误导 (MF1)
- Base-model-only 与 Introduction 动机脱节 (MF2)
- Ordinal framing overclaim (MF3)
- DDR 机制解释超越证据 (SF1)
- Multi-detector ensemble 更优 (SF2)
- Generator subset 混用 (SF3)
- Downstream null result (SF4)
- Temperature sensitivity (SF5)
- 全部 Minor issues

## Reviewer Divergence

**Gen-1/gen-2+ 区分能力弱的严重程度**：
- R1 视为 Must-Fix (critical)——认为 48% error rate 使 "ordinal depth estimation" 名不副实，方法主要成功在于 gen-0 识别
- R2 视为 Should-Fix (warning)——认为 binary F1=0.694 排除了 gen-0，是纯 depth discrimination 且优于所有单一 baseline；3-class ceiling 是 recursive generation 的固有特性（两篇 concurrent work 独立收敛于相同结论）

**Director 裁决**：采纳 R2 的论证——binary F1=0.694 确实是排除 gen-0 后的真实 depth discrimination，且论文已透明报告此局限。但此问题与 MF3（Ordinal framing）互相加重：如果 gen-1/gen-2+ boundary 仅 52% 正确率，"Ordinal Depth Estimation" 的标题更难以自圆其说。因此将 gen-1/gen-2+ 区分弱作为 MF3 的 supporting evidence 而非独立 Must-Fix。

---

## Questions for Authors

1. 如果为每个 LOGO fold 使用独立 gen-0 seeds（消除泄漏），3-class F1 下降多少？
2. DDR 的 "location shift preserving shape" 能否用完整 NLL 分布的 location-scale family 检验直接验证？
3. 是否测试过 Llama-3-chat / Mistral-Instruct 等其他 instruction-tuned 模型？OLMo-Instruct 的失败是系统性的还是 model-specific？
4. Cross-model chains + LOGO（held-out generator 不出现在任何链的任何深度）的 F1？
5. 多个参考模型特征的 concat/ensemble 能否改善 gen-1/gen-2+ 区分？

---

## Missing References

引用总体充分（58 条，验证通过），以下可补充：
1. M4/SemEval 2024 shared task 的 top-performing systems（具体方法，非仅 overview）
2. Data provenance/lineage tracking 领域文献（与 §2.4 provenance 讨论相关）
3. LLM output distribution 的信息论分析工作

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**（两位 Reviewer 均仔细阅读全文 + 全部附录，熟悉 AI text detection 方法论）

**评分理由**：

本文最大的贡献是 task formulation（ordinal depth estimation）和 empirical finding（DDR drifting vs. stationary features 的分离）。实验执行质量高，统计方法规范，写作诚实。

但三个根本性问题联合限制了 main conference 级别的影响力：

1. **Scope 太窄**：仅限 base model（0.6B-8B）continuation chains，instruction-tuned 模型完全失效。Introduction 的 practical motivation 与实际贡献之间存在严重 gap。
2. **Framing 不匹配**：标题强调 "Ordinal Estimation" 但 ordinal methods 无增益、gen-1/gen-2+ 边界 48% 错误率；Abstract 以泄漏膨胀的 0.809 领衔而非真实能力 0.694。
3. **贡献增量有限**：方法不优于 multi-detector ensemble（3-class -2.1pp）；downstream utility 为 null result。核心竞争力仅在于 cost-efficiency（60% 成本减少）。

如果重新 frame 为 "an empirical study of distributional drift in recursive base-model generation chains"，以 binary F1=0.694 为主指标，去掉 ordinal overclaim，诚实定位为 analytical contribution，这是一个扎实的 Findings paper。

**EMNLP 2026 评分标准映射**：3.0 = Findings（可被 Findings 接收）。距 3.5 (Borderline Conference) 需解决 MF1-MF3 中至少两个（重新 frame + 消除泄漏）。

---

## Detailed Comments（逐节）

### Abstract
- 以 3-class F1=0.809 (cross-model) 开头，这是最乐观的设定（非 LOGO、含 gen-0 泄漏）。应以 leak-free binary LOGO F1=0.694 为主。
- "Ordinal" 在 Abstract 中设定了后文无法兑现的期待。
- Contribution 3 (downstream) 可降低 prominence 或重新表述为 negative finding。

### Introduction
- Web contamination / data quality 动机与 base-model-only scope 脱节。应重新定位为 analytical/scientific contribution。
- "outperforming all individual detection baselines" 准确但暗示整体最优——multi-det ensemble 在 3-class 上更强。

### Related Work
- 覆盖充分，positioning 准确。与 concurrent work 的区分诚实。
- 可补充 data provenance 和 SemEval top systems。

### Method
- 特征设计合理但 standard（NLL statistics + lexical diversity）。
- Tail decay rank 100-1000 未 justify。
- "Entropy" misnomer 应在正文（非仅 footnote）中解决。

### Results
- LOGO 设计恰当，但 gen-0 泄漏问题需从根本上修复或在 framing 中充分承认。
- DDR 分析有洞察价值，但机制解释应弱化为 empirical pattern。
- Generator subset 不一致影响可读性和可比性。

### Discussion
- 过度碎片化（7+ \paragraph{}）。
- Instruction-tuning limitation 讨论充分但应反映在 Introduction 动机中。
- Temperature robustness 的 cross-temperature transfer failure 应更显著讨论。

### Limitations
- 诚实且全面，值得肯定。