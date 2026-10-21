---
round: 1
overall_score: weak reject
timestamp: 2026-05-18T06:41:05.607306+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 2

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**审稿编排**: 2 Reviewers, 1 round + cross-sharing
**收敛状态**: 13/15 条意见达成共识，2 条轻微分歧（ESS 证明必要性、novelty 程度），无需额外轮次

---

## Summary

本文提出双约束自适应指数选择框架，用于 detect-and-reweight 预训练中自动确定下权指数 $b^*$。给定 per-sample 检测器分数 $q(x)$，对每个 batch 求解满足 effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ 且 ESS$(b) \geq n_{\min}$ 的最小 $b$（minimum intervention principle）。在 Qwen3-0.6B continued pretraining（132M tokens FineWeb, 40% 合成污染）上，方法与 grid-searched best 的 PPL 差距为 0.031（17.651 vs 17.620），消融层级（Adaptive < Uniform < ESS-only < Random）证实 detector 信号和 minimum intervention 两个因素均必要。

---

## Strengths

**S1. 问题定义清晰且实际。** Web 数据合成污染是真实且日益严重的问题，无需验证集/已知 $\rho$ 的自适应方法有实际需求。

**S2. 框架设计简洁优雅。** $\alpha_{\mathrm{eff}}$ 和 ESS 的对立单调性自然定义 feasible region，bisection 求解高效（~44 FLOPs/batch），minimum intervention 直觉合理。

**S3. 消融设计有层次且诚实。** 四级消融（Random > ESS-only > Uniform > Adaptive）有效分解因素贡献。固定 $\bar{b}^*$ 实验（PPL ≈ uniform）进一步证明 per-batch adaptation 的必要性。Hard filtering 优势被坦诚报告。

**S4. 超参敏感性分析全面。** $\tau$ sweep（0.50-0.95）、$n_{\min}$ sweep、batch size sweep ($B \in \{4,8,16\}$) 均有覆盖。$\tau \in [0.5, 0.8]$ 宽 safe range 是实用性证据。

**S5. 写作质量高。** 无 AI 写作痕迹（无 em-dash、无黑名单用词、无过度分段），叙事主线基本连贯，Limitations 诚实全面。

**S6. 历史问题已修复。** RR-W1（"from random initialization" → "continued pretraining"）和 RR-W2（"balanced test set" → "human-only"）均已正确修正。

---

## Weaknesses

### Critical（影响接收决定）

**C1. "Statistically indistinguishable" claim 基于错误的统计范式** [R1-N1, R2 AGREE]
- 论文核心 claim（Abstract, Introduction, Conclusion）依据 bootstrap $p = 0.30$, $N = 3$。$p = 0.30$ 仅表示未能拒绝差异为零的零假设，不等于证明等价。$N = 3$ 统计功效极低——即使真实差异 0.5 PPL 也可能得到 $p > 0.05$。声称 "indistinguishable" 需要 equivalence test（如 TOST），预设实际等价边界 $\delta$ 并证明差异落在 $[-\delta, +\delta]$ 内。当前表述是 absence of evidence ≠ evidence of absence 的统计推断错误。
- **两位 Reviewer 完全一致。**

**C2. $\alpha_{\mathrm{eff}}$ 理论动机与实际计算存在逻辑断层** [R1-N2, R2 AGREE]
- 理论动机来自 Wang et al. (2026) 基于真实 $\alpha$ 的收敛速率定理，但 $\alpha_{\mathrm{eff}}$ 用 $r_i = \mathbf{1}[q_i \leq 0.5]$ 估计——检测器不完美时（AUC = 0.939, 46.3% 样本在不确定区间 $[0.2, 0.8]$）会系统性偏离真实 $\alpha$，论文未给出误差界。
- Proposition 1 的 covariance 正性是 tautological：$r_i$ 是 $q_i$ 的阈值函数，$\alpha_{\mathrm{eff}}$ 增加是因为"权重转移到检测器认为是真实的样本"而非"权重转移到真实样本"。
- **两位 Reviewer 完全一致。**

**C3. 实验外部效度严重不足** [R1-N3, R2-N1, R2-W2, 全部 AGREE]
- 单一模型规模（0.6B）、单一 detector（TF-IDF+LR）、单一数据源（FineWeb）、自污染设计（最容易检测的场景）。
- Drayson et al. (2025) 在 160M/360M/1.7B 三个规模实验，本文声称改进其方法却实验覆盖远不如。
- Llama-3.2-3B 单 seed 显示 PPL parity（无改善），暗示方法可能不 scale。
- $\rho = 0.2$ 失效（+0.046 PPL）无深入分析。$\rho > 0.6$ 未测试。
- Abstract 声称 "score calibration may matter as much as raw classification accuracy" 但未用任何其他检测器验证。
- **两位 Reviewer 独立指出，全部一致。这是最严重的问题。**

**C4. Hard filtering 碾压所有 reweighting 方法，削弱核心动机** [R2-N2, R1 AGREE with nuance]
- Detect & Remove（17.290）比 Adaptive（17.651）低 0.36 PPL，差距远大于 Adaptive vs Uniform（0.043）。
- 即使 suboptimal threshold（$q > 0.3$: 17.253, $q > 0.5$: 17.290）也全面优于所有 reweighting，threshold 敏感度（0.037 PPL）远小于 filtering vs reweighting 差距（0.36）。
- R1 补充：threshold 方向不可知是 reweighting 的一个 defense，但论文未测试极端阈值，full robustness picture 缺失。
- **基本一致，R1 同意核心论点但补充了 nuance。**

**C5. 效果量极小且 downstream 无改善，framing 不匹配** [R1-W1, R1-W6, R2-N3, 全部 AGREE]
- PPL 改善 0.043（0.24% relative）。Appendix Table 5 的 5 个 downstream benchmarks 中 4/5 adaptive 略低于 uniform（ARC-C -0.5pp, ARC-E -0.7pp, HellaSwag -0.5pp, WinoGrande -0.8pp），方向一致性令人担忧。
- PPL 改善可能来自对 human-only evaluation set 的隐式 distribution matching，非真正的训练质量提升。
- 论文标题和 Abstract 的 "contamination-aware pretraining" framing 暗示性能提升，但实际贡献更接近 "消除 grid search 成本"。
- **两位 Reviewer 完全一致。**

### Warning（影响评分但不一票否决）

**W1. Proposition 1 证明 gap** [R1-W2, R2 AGREE]
- 命题声称 strictly increasing，证明只建立 non-decreasing（covariance non-negative ≠ strictly positive）。可修复。

**W2. ESS 单调性未正式证明** [R1-W3, R2 REBUT]
- R1：对 bisection 算法正确性至关重要，应提供证明。
- R2：标准 IS 结果，只需提供具体 lemma/theorem 引用。
- **轻微分歧**：严重程度不一致，但都同意当前引用过于笼统。

**W3. Grid-$b$ baseline 的 post-hoc oracle 问题** [R1-W4, R2 AGREE]
- Grid-best 在 test set 上 post-hoc 选择，给了 oracle 优势。实践中 grid search 用 val set 选 $b$，test set 表现通常更差。
- R2 补充：这反而有利于论文——realistic grid search 可能不如 adaptive。但论文应双向讨论。

**W4. 重要 baselines 仅 single seed** [R1-W5, R2-W5, 全部 AGREE]
- Detect & Remove（最强 baseline）和 Golden Ratio 仅 seed 42。至少 D&R 需要 3-seed。

**W5. Novelty 相对 Drayson et al. 有限** [R2-W1, R1 REBUT]
- R2：核心公式直接来自 Drayson, dual constraint 是标准 IS 技术在新场景的组合，数学上 trivial。
- R1 反驳：ESS-only 失败是反直觉的（17.737 > uniform 17.694），regime analysis（4.9× over-intervention ratio）提供非平凡洞察。Novelty 属于 "useful engineering insight backed by careful ablation"。
- **分歧**：novelty 程度判断不同，但都同意足以支撑 Findings。

**W6. $\tau$ 依赖 $\rho$ 与 "zero validation cost" 矛盾** [R2-W3, R1 AGREE with nuance]
- optimal $\tau$ 从 0.8（$\rho=0.4$）变为 0.7（$\rho=0.6$），$\rho=0.2$ 方法退化。
- Discussion 的 $\tau \approx 1 - \rho/2$ heuristic 与 $\rho$-unknown 假设直接矛盾。
- R1 补充：$\tau \in [0.5, 0.8]$ safe range 宽 0.3，default $\tau = 0.8$ 在 $\rho \in [0.4, 0.6]$ 足够好。部分缓解但不消除矛盾。

**W7. 引用密度不足** [R2-W4, R1 AGREE]
- 23 篇引用，EMNLP 长文通常 40-60+。高优先级缺失：Sagawa et al. (2020) Group DRO, Hans et al. (2024) Binoculars, Bao et al. (2024) Fast-DetectGPT, Gadre et al. (2024) DataComp-LM, Guo et al. (2017) temperature scaling。

### Minor

- M1: "five approaches" 实际列 6 个方法（experiments.tex line 20）
- M2: Grid-$b$ 值列表不一致（正文 7 个 vs Appendix 9 个 vs "nine runs"）
- M3: `guo2025escaping` 缺 arXiv ID，可能为 phantom reference；`vehtari2024psis` 年份待核实
- M4: Hybrid $\rho=0.6$ 行数据可比性说明不足

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全一致：
1. **统计 claim 错误**（C1）：必须修正 "indistinguishable" 表述
2. **实验覆盖不足**（C3）：至少需要多模型/多 detector 实验才能支撑 general claims
3. **效果量小 + downstream 无改善**（C5）：需要重新 framing
4. **Hard filtering 优势明显**（C4）：需要更有力的 reweighting positioning
5. **历史 issue 已修复**：RR-W1 和 RR-W2 均已正确修正
6. **写作质量高**：无 AI 痕迹，Limitations 诚实

## Reviewer Divergence [REBUT]

1. **Novelty 程度**（W5）：R2 认为 mathematically trivial，R1 认为 ESS-only 失败的反直觉性和 regime analysis 有非平凡价值。不影响整体评估（都同意 Findings 水平）。
2. **ESS 证明必要性**（W2）：R1 要求 formal proof，R2 认为标准结果只需精确引用。

---

## Questions for Authors

1. 如果执行 TOST 等价检验（预设 $\delta = 0.1$ PPL），当前 $N = 3$ 的数据是否能通过？如不能，需要多少 seeds？
2. 在已知 ground truth 的合成实验中，$\alpha_{\mathrm{eff}}$ 与 true $\alpha$ 的 correlation/误差是多少？
3. 训练 loss 几乎不变但 PPL 改善——如果 evaluation set 包含合成样本，差异是否消失？（评估 human-only eval 的隐式 distribution matching 效应）
4. $\rho = 0.2$ 时用 $\tau = 0.5$ 或 $\tau = 0.6$ 是否恢复有效性？
5. 将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$ 对性能和理论保证的影响？
6. micro-batch $B = 4$ 时 $\alpha_{\mathrm{eff}}$ 仅有 5 个离散值 $\{0, 0.25, 0.5, 0.75, 1.0\}$，per-batch $b^*$ 的噪声对训练稳定性有何影响？
7. 什么具体场景下 practitioner 应该选择 reweighting 而非 hard filtering？请给出量化论据。

---

## Missing References

**高优先级**（实质性遗漏）：
- Guo et al. (2017) "On Calibration of Modern Neural Networks" — 论文用了 temperature scaling 但未引用
- Sagawa et al. (2020) Group DRO — DoReMi 的理论基础，已引 DoReMi 但缺上游
- Hans et al. (2024) "Spotting LLMs with Binoculars" — 直接相关的检测器
- Bao et al. (2024) Fast-DetectGPT — 已引 DetectGPT 但缺后续改进
- Gadre et al. (2024) DataComp-LM — 数据质量/选择基准

**中优先级**：
- Bengio et al. (2009) Curriculum Learning
- Lin et al. (2017) Focal Loss
- Kirchenbauer et al. (2023) Watermarking for LLMs
- Abbas et al. (2023) SemDeDup
- Equivalence testing 文献（如 Lakens 2017），若论文要保留 "indistinguishable" claim

**引用验证问题**：
- `guo2025escaping` 无 arXiv ID，在线搜索无匹配，疑似 phantom reference
- `vehtari2024psis` 年份需核实（2024 JMLR 发表 vs 2015 原始预印本）

---

## External Review (Stanford Agentic Reviewer)

未配置，未请求。

---

## Overall Assessment

**Score: weak reject (Findings borderline)**
**Confidence: 4/5**

两位 Reviewer 独立给出 3.0/5（Findings 水平），交叉分享后在所有 critical 问题上达成共识。

**核心判断**：方法 formulation 干净、消融设计好、写作诚实，具备 Findings 论文的基本素质。但五个 critical 问题制约当前版本：(1) 核心统计 claim 基于错误范式，(2) 理论动机与实际计算脱节，(3) 实验仅覆盖单一极窄 setting，(4) hard filtering 全面碾压使 reweighting 动机不清，(5) 效果量极小且 downstream 无改善。

**如果仅修正表述**（降级 claim、加入讨论、补引用），可作为 borderline Findings 投稿，但缺乏竞争力。

**如果扩展实验**（至少 1-3B 规模 3-seed + 一个 neural detector + D&R 3-seed + $\rho = 0.2$ 分析 + reposition framing），可望稳定在 Findings accept，有可能冲击主会议 borderline。

---

## Detailed Comments（逐节）

### Abstract
- "statistically indistinguishable" 必须替换（C1）
- "score calibration may matter as much as raw classification accuracy" 无实验支撑，需降级或删除

### Introduction
- 从 contamination 问题切入、到 dual constraint、到实验证据，叙事线基本连贯
- Contribution 列表中 "statistically indistinguishable" 需同步修改
- 第三贡献（lightweight detector）更像实验观察而非方法贡献

### Related Work
- Positioning 准确，与 Drayson et al. 的三点差异表述清楚
- 引用密度不足（W7），缺 Group DRO、更多检测器、calibration 文献
- 需补充 curriculum learning / instance reweighting 经典文献

### Method
- Proposition 1：strictly increasing → non-decreasing 或加强证明（W1）
- ESS 单调性需精确引用（W2）
- $r_i = \mathbf{1}[q_i \leq 0.5]$ 与理论动机的 gap 需讨论（C2）
- Algorithm 1 清晰可实现

### Experimental Setup
- "five approaches" → 6 个方法（M1）
- Grid 值列表与 Appendix 不一致（M2）
- 自污染设计局限需在正文（非仅 Limitations）讨论

### Results
- Table 1 的 "indistinguishable" claim 需修正（C1）
- D&R 优势需更充分讨论（C4）
- Grid-$b$ post-hoc oracle 需双向讨论（W3）

### Discussion
- $\tau \approx 1 - \rho/2$ 与 $\rho$-unknown 矛盾需解决（W6）
- "where the advantage manifests" 段落暗示 PPL 改善来自 human-only eval 的 distribution matching——如果如此，应明确讨论

### Limitations
- 已覆盖大部分局限，诚实度高
- $\rho = 0.2$ 失效需更深入分析

### References
- 总量不足（23 → 建议 40+）
- `guo2025escaping` 可疑，需核实或删除
- `vehtari2024psis` 年份需核实