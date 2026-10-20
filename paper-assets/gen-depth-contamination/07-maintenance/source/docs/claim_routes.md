# 双路线 Claim 框架

> 根据 MVP 结果 K* 的取值，准备两条论文叙事路线。

---

## 路线 A：K* ≥ 3（MVP Pass）

### Core Claim
**Generational depth estimation is feasible and enables graduated filtering that outperforms binary detection for quality-aware data curation.**

### Supporting Claims 拆解

**C1: Depth signals exist and are ordinal-structured**
- 递归生成文本的统计特征（surprisal、vocabulary diversity、tail metrics）随 depth 呈系统性单调变化
- Ordinal regression（CORAL/CORN）显著优于 multinomial classification，证明 depth 的有序结构可被利用
- 证据：pairwise AUC matrix、ordinal vs. multinomial ablation、calibration curves

**C2: K* characterization reveals linguistic degradation ordering**
- K* 是首次被系统量化的判别饱和边界
- Feature group ablation 揭示"降解序"：不同语言维度（vocabulary diversity → surprisal dynamics → tail metrics）在不同 depth 饱和
- Heatmap：feature group × depth → discriminative power
- 证据：per-feature saturation curves、cross-model K* comparison、decoding strategy 对 K* 的调控效应

**C3: Graduated filtering > binary filtering**
- Depth-aware weighted filtering（weight ∝ quality(k)/quality(0)）在 MMLU/HellaSwag 等 data-quality-sensitive tasks 上显著优于 binary filtering 和 no filtering
- 理论动机：binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting
- 证据：downstream benchmark results with bootstrap CIs + paired significance tests、contamination severity ablation（10%/30%/50%）

**C4: Cross-model generalization**
- 在 model A 上训练的 depth classifier 可迁移到 model B 的生成文本
- Cross-scale probe（7B/14B）验证小模型训练的特征在更大模型生成文本上的迁移性
- 证据：cross-model transfer accuracy matrix、feature distribution MMD analysis

### Story Arc

```
Problem:  Web data 被未知深度的递归合成文本污染，binary detection 丢失 graded quality signal
Insight:  递归生成是 iterated lossy channel，depth-discriminative signals 系统性存在且可量化
          → 类比 JPEG 重压缩检测
Method:   (1) 15维特征 + ordinal regression → depth estimation
          (2) Depth-graduated curation: weight ∝ estimated quality decay
Results:  K*≥3 → fine-grained depth discrimination feasible
          Graduated filtering 显著优于 binary 和 no filtering
          Cross-model/cross-scale 泛化
Takeaway: Depth is the missing dimension in synthetic data curation
```

### 评审攻击面预演

**Q1: "方法论贡献不足——feature engineering + off-the-shelf ordinal regression"**
- Rebuttal：(a) 贡献不在分类器本身，而在 problem formulation + empirical characterization + practical paradigm shift；(b) 信道级联 + DPI 理论框架提供了 beyond-empirical 的科学理解；(c) 类比 DetectGPT——方法简单但 problem formulation 有影响力；(d) learned representation baseline（frozen LM embeddings + MLP）作为对比，证明 hand-crafted features 在此任务上的优势（可解释性 + 泛化性）

**Q2: "Prompt-chain ≠ 真实递归污染路径，ecological validity 存疑"**
- Rebuttal：(a) Prompt-chain 是 upper bound estimate——如果 prompt-chain 下特征已饱和，retrain-chain 只会更快饱和；(b) 我们用 retrain-chain validation（1 config, LoRA fine-tuning）验证两种 chain 的 feature distribution 对比和 cross-setting transfer accuracy；(c) Clean chains 定位为 theoretical bound，实际 depth estimates 定位为 ordinal quality proxies

**Q3: "Cross-scale 证据不足——真实世界合成文本主要来自 frontier models（GPT-4, Claude）"**
- Rebuttal：(a) 我们明确定位 practical scope 为开源模型生态（7B-14B）；(b) frontier model limitation 是 principled limitation（RLHF/instruction-tuning 改变分布、API-only 限制特征计算），非简单的"没做"；(c) 7B-14B probe 已覆盖开源社区主流生成规模；(d) WildChat feature trend analysis 提供 naturalistic 证据

---

## 路线 B：K* = 2（Conditional Pass）

### Core Claim
**The saturation boundary K* is a novel, measurable fundamental quantity of recursive text generation: even coarse ordinal depth signals (human / gen-1 / gen-2+) provide calibration advantages over binary detection, and K*'s dependence on model family and decoding strategy yields actionable guidance for data curation.**

### Supporting Claims 拆解

**C1: K* 是首次被系统测量的 fundamental resolution limit**
- 这不是分类器的能力上限，而是 information-theoretic impossibility boundary（DPI 约束）
- K*=2 意味着 depth ≥2 的文本在信息论意义上已不可区分——这本身是重要的科学发现
- 证据：信道级联 + DPI 理论推导、empirical K* measurement across models/decoding strategies

**C2: Linguistic degradation ordering 揭示递归生成的结构性规律**
- 即使 K*=2，per-feature saturation analysis 仍揭示哪些语言维度先坍缩
- Feature group × depth heatmap 展示 degradation ordering
- 证据：vocabulary diversity 先于 semantic coherence 坍缩（假设）、cross-model 对比 heatmap

**C3: Decoding strategy 调控 K***
- 假设检验：greedy → 指数衰减（K* 更小），high-temperature → 多项式衰减（K* 可能更大）
- AIC/BIC model comparison 验证 exponential vs. polynomial MI 衰减
- 实际意义：指导数据生成策略选择——如果特定 decoding 延长 discriminability，可指导 synthetic data generation best practices
- 证据：K*(decoding strategy) 的系统性变化、MI 衰减曲线拟合

**C4: 即使 coarse ordinal signal（3-class）仍有 calibration advantage**
- 3-class（human / gen-1 / gen-2+）vs. binary 在 downstream tasks 上的对比
- Depth=1（单代合成，质量较高）vs. depth≥2（多代合成，质量显著下降）的区分对 curation 有实际价值
- 证据：3-class graduated filtering vs. binary filtering benchmark results

### 如何把 K*=2 包装为 Contribution 而非 Limitation

关键 framing 转换：

| 避免的措辞 | 改用的措辞 |
|---|---|
| "Unfortunately, depth discrimination saturates at K*=2" | "We establish K*=2 as the fundamental resolution limit for prompt-chain recursive generation" |
| "Only 3 classes are distinguishable" | "The human/first-gen/multi-gen trichotomy captures the critical quality boundary" |
| "The classifier cannot distinguish depth 3 from depth 4" | "Beyond depth 2, texts converge to a stationary distribution — a novel empirical finding consistent with our DPI analysis" |
| "If K*≤2, the contribution is limited" | "K* itself is the contribution: its measurement, model-dependence, and decoding-strategy modulation are all first-of-kind results" |

### Saturation Characterization 路线的卖点

1. **首次量化测量**：之前只有定性讨论（Shumailov "early collapse"），我们给出精确的 K* 数值和置信区间
2. **可操作指导**：K*=2 告诉 practitioners "对于 model X + decoding Y，depth≥2 的文本无需细分——binary vs. first-gen vs. rest 即可"
3. **理论-实验闭环**：DPI 预测 MI 单调衰减 → 实验测量 K* 位置 → 衰减曲线拟合验证理论
4. **跨模型/跨策略 K* 地图**：不同 model family 和 decoding strategy 的 K* 对比，形成 actionable lookup table
5. **Model collapse early-warning 应用**：即使 K*=2，depth distribution（human / gen-1 / gen-2+ 占比）作为 corpus quality indicator

### Story Arc

```
Problem:  同路线 A
Insight:  递归生成的 depth-discriminability 有 fundamental limit K*
          K* 不是分类器能力问题，而是 information-theoretic boundary
Method:   DPI 理论框架 + systematic empirical measurement of K*
Results:  K*=2 across most configurations → human/gen-1/gen-2+ trichotomy
          K* varies with decoding strategy → actionable guidance
          Even 3-class graduated filtering > binary filtering
Takeaway: K* is the right quantity to measure; its value tells you exactly
          how much depth granularity your curation can exploit
```

### 评审攻击面预演

**Q1: "K*=2 means the depth classifier is not very useful — just use binary detection"**
- Rebuttal：(a) 3-class > binary 在 downstream benchmarks 上有统计显著差异——first-gen text 和 multi-gen text 质量差异显著；(b) K* 本身是一个比分类器更重要的科学贡献——它量化了 recursive generation 的 information-theoretic resolution limit；(c) K* 随 decoding strategy 变化的发现直接指导 synthetic data generation 最佳实践

**Q2: "如果 K*=2 是 fundamental limit，后续工作空间在哪？"**
- Rebuttal：(a) Scale effect——更大模型的 K* 可能更大（7B probe 数据）；(b) Retrain-chain vs. prompt-chain 可能有不同 K*；(c) Domain-specific K*（code vs. natural language vs. scientific text）；(d) 信息注入策略（external verifier）对 K* 的调控

**Q3: "理论框架（DPI）过于简化，unigram 近似不 justified"**
- Rebuttal：(a) 我们明确标注 JSD 作为 MI proxy 的 unigram 层面局限性；(b) DPI bound 是 model-free 的——即使 proxy 不精确，monotone decay 的定性结论仍成立；(c) 这是 first attempt，更精确的 MI estimation（如 neural MI estimators）留作 future work

---

## 路线选择决策树

```
MVP 结果出来后：
├── AUC(0 vs 1) < 0.70 → FAIL，重新评估项目
├── K* ≥ 3 → 路线 A（depth estimation + graduated filtering 为主线）
├── K* = 2 且 feature trends 清晰 → 路线 B（K* characterization 为主线）
└── K* = 2 且 feature trends 不清晰 → 评估是否有 decoding strategy 调控空间
    ├── 有 → 路线 B + decoding strategy modulation 加强
    └── 无 → 考虑 scope narrowing 或 target 降级
```
