---
round: 13
overall_score: 3.0 - Findings
timestamp: 2026-05-17T19:42:07.139491+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 14 (Fresh Review)

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
**目标**: EMNLP 2026 via ARR May 2026 cycle (截止 2026-05-25)
**类别**: Long Paper
**Reviewer**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+Related Work+写作质量+格式)

---

## Summary

本文提出 generation depth classification 任务，将文本按递归 LLM 生成次数分为 gen-0/gen-1/gen-2+ 三类，并识别出 differential depth response (DDR)：central-tendency 特征（mean entropy, lexical diversity）随深度单调漂移，而 shape 特征（entropy max, tail slope）保持近似平稳。7 特征 XGBoost 在 8 个 base model 生成器（5 家族, 0.6B-8B）的 LOGO 评估下达到 leak-free binary F1=0.694, cross-model F1=0.764。研究限定于 base model，instruct model 下信号大幅衰减（F1=0.338）。

---

## Strengths

**S1. 新颖的任务定义 [R1,R2 共识]**
将 AI 文本检测从二分类拓展到递归深度分类（gen-0/gen-1/gen-2+），在现有文献中未被明确提出。与 SemEval-2024 Task 8（生成器识别）和 Beyond Binary（角色识别）正交。

**S2. DDR 分解具有分析价值 [R1,R2 共识]**
Drifting vs. stationary 特征分解（|ρ|>0.60 vs. <0.10，六倍量级差距）为理解递归生成分布动力学提供有用框架。KS 统计量差异 ~10×，Bonferroni 校正后显著。

**S3. 评估协议设计严谨 [R1,R2 共识]**
LOGO 确保跨模型泛化真实性；binary F1 排除 gen-0 避免种子共享泄漏；LOFO 验证特征互补性。

**S4. 消融分析全面 [R1,R2 共识]**
14 个附录覆盖长度混淆、温度敏感性、跨域泛化、跨温度迁移、prompt 类型等消融。

**S5. 对局限性坦诚 [R1,R2 共识]**
明确报告 instruct model 退化和温度限制，无过度宣传。

**S6. 引用覆盖总体充分 [R2]**
58 篇引用覆盖 AI 文本检测、model collapse、迭代生成、stylometry 等主要领域。

---

## Weaknesses

### Must-Fix

**MF1. 3-class F1 中 gen-0 数据泄漏处理不够干净 [R1-W1, R2 AGREE]**
- LOGO 中 gen-0 文本在所有生成器间完全共享，gen-0 per-class F1≈0.94 是人为膨胀
- Abstract 以 3-class F1=0.764 为 headline；Table 1 标题栏、Table 4 baseline 对比仍显著展示 3-class
- 论文采用 binary F1 为 primary metric 值得肯定，但 3-class F1 报告方式需更透明
- **建议**: 3-class F1 出现处附加 gen-0 leakage caveat；考虑提供排除 gen-0 的修正宏平均

**MF2. Binary F1 未超过多检测器基线 [R1-W2, R2 AGREE]**
- Table 4: 7-feature binary F1=0.705 vs. 4-det+surface=0.708，本方法在 leak-free binary 上未优于已有方法组合
- Table 1 全集 binary F1=0.694 vs. Table 4 子集 0.705，样本差异（37,058 vs 34,131）引入对比偏差
- **建议**: 贡献声明调整为单模型效率和可解释性优势；解释 Table 1 vs Table 4 子集差异

**MF3. Base-model-only 限制严重削弱实际意义 [R1-W3, R2-W4, 共识]**
- OLMo-Instruct LOGO F1 从 0.763 降至 0.338，信号几乎消失
- 当前部署 LLM 绝大多数是 instruct/RLHF 模型
- 标题 "LLM Text Chains" 暗示更广适用性
- **建议**: 标题或 Abstract 明确限定 base model；讨论为什么 instruct 退化不否定整体 framework

**MF4. DDR 与 model collapse 区分薄弱 [R2-W1, R1 部分同意]**
- DDR 核心观测（词汇多样性下降、分布压缩、tail collapse）与 model collapse 文献高度重合
- "固定参数 vs. 训练" 是机制差异，非现象层面新发现
- R1 部分反驳：drifting/stationary decomposition 是 model collapse 文献没有的分解
- **共识**: 区分有基础但论文未充分论证；需更清晰说明 DDR 提供的独特 insight

**MF5. 下游实用价值未能证实 [R2-W3, R1-W6, 共识]**
- Appendix K/L: depth-aware curation 与随机子采样统计等价（TOST ±2% margin）
- 直接削弱 Introduction 中数据质量控制的核心动机
- n=3 seeds 统计效力严重不足
- **建议**: 在正文中诚实讨论负面结果；将论文重新定位为分析性贡献

### Should-Fix

**SF1. DDR "location shift" 假说缺乏充分验证 [R1-W4, R2 AGREE]**
- Levene test 对 shape features 也拒绝等方差（p<1e-10），与 "preserves shape" 矛盾
- CV shift <3% 作为 "近似保持" 的阈值是事后定义
- **建议**: 弱化 causal 暗示；提供 location-scale 拟合检验或明确 CV 阈值依据

**SF2. 方法缺乏算法新颖性 [R2-W2, R1 同意降级为 Should-Fix]**
- XGBoost + 7 NLL/表面特征均为标准工具
- 近期文献（Alikhanov et al. 2025; AAAI 2025 shared task）已有高度类似 pipeline
- **共识**: 对 EMNLP 主会议不够，Findings 可接受

**SF3. 温度敏感性构成根本限制 [R1-W7, R2 AGREE]**
- t=1.0 时 entropy_mean ρ=-0.002，方法基本失效
- 实际部署中用户不知道目标文本解码温度
- 跨温度迁移退化严重（Qwen3-1.7B: 0.789→0.418）
- 与 MF3 共同构成双重实用性限制

**SF4. 特征选择理论依据不足 [R1-W5, R2 AGREE]**
- §3.3 声称 "not post-hoc" 但假说从同一数据得出，构成循环论证
- entropy_min LOFO Δ=+0.01pp 仍保留缺乏实证依据
- 未报告特征间相关矩阵

**SF5. Baseline 比较 framing 不够准确 [R2-W5, R1 部分反驳]**
- DetectGPT/Binoculars 等未设计用于 ordinal classification
- R1 反驳：QLoRA (App E) 提供 embedding 上界；LOGO+同一 XGBoost 确保公平
- **共识**: 应明确标注为 "repurposed baselines"

### Minor

**M1. 跨域评估温度混淆 [R1-W8]**
跨域实验用 t=1.0 而主实验用 t=0.7，domain × temperature interaction 使跨域泛化结论不可靠。

**M2. Seed-sharing 混淆 [R2-W6, R1 反驳]**
R1 认为 LOGO + cross-domain 已基本排除。R2 认为独立 seeds 实验更理想。共识：现有证据基本充分。

**M3. AI 写作痕迹 [R2-W8]**
-ing 短语结尾（"approximately preserving distributional shape"）、部分段落过短、Conclusion "70B+" 过度暗示。

**M4. Entropy 术语不精确 [R1-W9]**
Token-level NLL 称为 "entropy" 与信息论概念有歧义。

**M5. Missing references [R1, R2]**
Alikhanov et al. 2025, AAAI 2025 shared task systems, CORN loss (Shi et al. 2021), data contamination detection 文献。

---

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)** — 两位 Reviewer 完全一致
2. **Excitement 2.5** — 完全一致
3. **任务定义是主要贡献** — 共识
4. **gen-0 泄漏处理需更透明** — 共识 Must-Fix
5. **binary F1 未超过多检测器基线** — 共识 Must-Fix
6. **base-model-only + 温度限制 = 双重实用性限制** — 共识
7. **DDR 假说验证需弱化 causal 暗示** — 共识
8. **下游实验为负面结果且效力不足** — 共识
9. **方法无算法新颖性，Findings 可接受** — 共识
10. **实验消融全面、写作整体坦诚** — 共识正面评价

## Reviewer Divergence [REBUT]

1. **DDR vs model collapse 区分度**
   - R2: 核心观测与 model collapse 高度重合，"固定参数" 区分不足
   - R1: drifting/stationary decomposition 是独特贡献，model collapse 文献无此分解
   - **Resolution**: 区分有基础但论文需更强论证；不影响 Overall 评分

2. **Baseline 比较公平性**
   - R2: 二分类检测器作为 ordinal baseline 不公平，需 n-gram/embedding baseline
   - R1: QLoRA 提供上界，LOGO+同一 XGBoost 确保公平
   - **Resolution**: 明确标注 "repurposed baselines" 即可；不升级为 Must-Fix

3. **Seed-sharing 混淆严重程度**
   - R2: 分类器可能学到 topic fingerprint
   - R1: LOGO + cross-domain 已基本排除
   - **Resolution**: R1 论据更有说服力；降为 Minor

---

## Questions（需作者澄清）

**Q1.** LOGO 中 gen-1 测试与训练共享种子，是否存在种子内容相关性导致的隐性泄漏？ [R1]

**Q2.** Reference-only binary F1 (0.833) 远高于 Full 7-feature (0.695)。surface features 是否为 noise source？这对特征互补性声明构成直接挑战。 [R1, R2 强烈同意]

**Q3.** Cross-model chain 使用 5-fold CV 而非 LOGO，F1 差异可能来自协议差异而非 generator heterogeneity。两者是否可比？ [R1, R2 同意]

**Q4.** Instruction-tuned 模型 DDR 信号消失（F1=0.338）是否意味着 DDR 是 pretrained model 特有的 artifact？ [R2]

**Q5.** gen-2+ 合并是实用考量还是信号饱和？Appendix D 5-class F1=0.484 是否说明深度信号在 gen-2 后已饱和？ [R2]

**Q6.** DDR 两分法是否过于简化？entropy_std (|ρ|=0.17) 和 entropy_min (|ρ|=0.41) 不属于任何一端。应重新表述为连续光谱。 [R1提出, R2部分同意]

---

## Missing References

1. Alikhanov et al., 2025. "AI-generated Text Detection: A Multifaceted Approach" (arXiv:2505.11550) — 近期 stylometric+XGBoost 检测 pipeline
2. AAAI 2025 AI-Generated Text Detection Shared Task 系统论文 — 多个使用 XGBoost/LightGBM + NLL 特征
3. CORN loss (Shi et al. 2021) — 现代 ordinal classification 方法
4. Data contamination detection 文献

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。

---

## Overall Assessment

| 维度 | R1 | R2 | 合并 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.5 | **3.0** |
| Excitement | 2.5 | 2.5 | **2.5** |
| Overall | 3.0 | 3.0 | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |

**Overall: 3.0 — Findings 级别**

论文提出了新颖的 generation depth classification 任务和有分析价值的 DDR 发现，实验消融全面（14 个附录），对局限性坦诚。但存在以下结构性限制：

1. **实用性双重限制**: base-model-only (instruct 退化至 F1=0.338) + 温度敏感性 (t=1.0 失效) 使当前方法无实际部署价值
2. **性能无优势**: binary F1 未超过多检测器组合基线
3. **核心新颖性受挑战**: DDR 与 model collapse 的区分、方法无算法贡献
4. **下游价值未证实**: depth-aware curation 等价于随机采样

适合 EMNLP 2026 Findings track 发表。主会议接收需要：(a) 在 instruct model 上验证 DDR 信号或提供理论解释, (b) 方法性能超越现有基线, (c) 证实下游实用价值。

---

## Detailed Comments

### Abstract
- 当前版本以 LOGO binary F1=0.694 为主且提及 instruct 退化，结构合理
- 3-class F1 仍在 headline 附近，需标注 gen-0 leakage caveat
- "approximately preserving distributional shape" 是 -ing 短语结尾，建议改写

### Introduction
- 叙事结构清晰但第 2 段 DDR 描述过于技术化（Spearman ρ 具体值不适合 Intro）
- Contribution 第 2 条 "We identify DDR" 应弱化为 "We characterize..."
- 数据质量控制动机与 Appendix K/L 负面结果存在张力

### Related Work
- §2.2 DDR vs model collapse 论证需加强：drifting/stationary decomposition 作为独特贡献应在此展开
- 缺少近期 feature-based detection systems 讨论（Alikhanov et al. 2025）

### Method
- §3.2 chain attrition (2,746 chains) 可能引入 selection bias
- §3.3 "not post-hoc" 声明需修订或删除
- 特征间相关矩阵缺失

### Results
- Table 1 leak-free binary 为主值得肯定
- §4.2 DDR "location shift" 需弱化表述
- §4.3 baseline 比较应明确标注 "repurposed baselines"

### Discussion
- instruct 模型退化讨论诚实
- 温度限制讨论可更深入（t=1.0 是否意味着 DDR 是解码参数 artifact）

### Conclusion
- "frontier-scale (70B+)" 给读者过高期望（实际最大 8B），建议修改

### 格式合规
- 正文 8 页 ✓
- Double-blind ✓
- Limitations section ✓ (有实质内容)
- Ethics Statement ✓
- 引用格式 ✓ (ACL 规范)
- 附录在正文中均有引用 ✓