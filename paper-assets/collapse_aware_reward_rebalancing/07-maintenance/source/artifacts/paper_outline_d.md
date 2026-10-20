# Direction D: Negative Result Paper Outline

## 1. Title Candidates

**T1**: Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training

**T2**: The Diversity Collapse That Didn't Happen: An Empirical Study of Reward-Based Curation in Iterative Self-Training

**T3**: Reward Curation Without Collapse: Why Iterative Self-Training Resists Diversity Loss Under Standard Conditions

推荐 T1: 问句形式吸引注意力，"Surprising Resilience" 同时传达 negative result 和 positive framing。

---

## 2. Abstract 核心 Message (3 sentences)

**S1 (问题 + 假设来源)**: A growing body of work warns that reward-based optimization reduces output diversity in language models, raising concerns that iterative self-training with reward curation could trigger compounding diversity collapse across generations.

**S2 (核心 finding)**: Through a systematic study spanning 7 training configurations over 3 iterative generations, we find that the answer depends on what you measure: semantic diversity (embedding-based Vendi Score) remains resilient across all conditions, while format diversity (opening patterns, template repetition) collapses significantly under curation, with near-duplicate opening rates rising from 50% to 84%.

**S3 (为什么重要)**: This reveals that diversity collapse under reward curation is real but mischaracterized by standard metrics, and we propose complementary measurements (opening entropy, near-duplicate start rate) that capture the overlooked format homogenization mode.

---

## 3. Sections Outline

### 3.1 Introduction

**动机 (P1-P2)**:
- Iterative self-training (self-consuming loops) 越来越普遍: 模型生成数据 → 筛选 → 重新训练
- Reward-based curation (用 reward model 选择高质量样本) 是标准做法
- 直觉担忧: 每一代选择高 reward 样本 → 训练分布窄化 → 下一代更窄 → compounding collapse
- Kirk et al. (2024) 发现单轮 RLHF 降低 diversity; 延伸到 iterative 设置，collapse 风险应更严重

**问题定义 (P3)**:
- 核心问题: 在多代 iterative self-training 中，reward-based curation 是否真的导致 measurable diversity collapse?
- 这个问题重要因为: 如果 collapse 是 real risk，需要 diversity-preserving 机制 (DIVE, DARLING, GEM 等); 如果不是，这些机制的 motivation 需要重新审视

**我们的发现 (P4)**:
- 7 条件 × 3 代系统实验: 变化 adaptation method (LoRA vs Full-FT), selection pressure (K=4, 8, 16), learning rate (5e-6, 2e-5)
- 核心结果: 所有 curated 条件 Vendi Score 变化 < 1%，无 collapse 信号
- Baseline 对比: no-curation 条件 diversity 自然增长 +1.4% 到 +3.1%
- LoRA 条件下观察到的 3pp 相对 gap 是 capacity artifact; Full-FT 下 gap 消失甚至反转为正 (+0.63pp), 表明 curation 在充分学习条件下微促进 diversity

**Contributions (list)**:
1. [CONFIRMED] 首个系统性实证：reward curation 不导致 semantic diversity collapse (7 configs × 3 gens)，即使 loss 下降 80% 的激进学习条件下 Vendi Score 仍稳定
2. [CONFIRMED] **发现 metric-dependent collapse**: format/template 维度有显著 collapse（opening unique ratio 70%→37%, near-dup start 50%→84%），而 Vendi Score 完全盲区——collapse is real but mischaracterized
3. [CONFIRMED] LoRA capacity artifact + direction reversal: curation effect 从 LoRA 下的抑制 (-3.4pp) 反转为 aggressive Full-FT 下的促进 (+0.63pp)
4. [CONFIRMED] Measurement contribution: 推荐 opening_entropy + near_duplicate_start_rate 作为 iterative training diversity 的补充指标，捕捉标准 embedding metrics 遗漏的 format homogenization
5. [DEPENDS ON K=16] Boundary condition: extreme selection pressure (K=16, 6.25% retention) 下的边界行为

### 3.2 Related Work

**分组**:

**(a) Diversity in RLHF and Reward Optimization**
- Kirk et al. (2024, ICLR): RLHF reduces lexical/semantic diversity (foundational observation, 单轮)
- CD-RLHF (ACL 2025): curiosity-driven reward 维持 diversity in online RL
- 我们的定位: Kirk et al. 的发现在单轮成立，但我们的 iterative 设置显示 curation 单独并不导致 compounding 效应

**(b) Iterative Self-Training and Self-Consuming Loops**
- Self-play / self-improvement literature (STaR, ReST, etc.)
- Model collapse in generative models (Shumailov et al., 2024): 训练在自己的输出上导致 distribution collapse
- DIVE (2501.00747): 专门解决 iterative self-improvement 中的 diversity loss
- 我们的定位: model collapse literature 关注 unfiltered self-training; 我们关注 reward-filtered self-training，发现 curation filter 并不加剧 collapse

**(c) Diversity-Preserving Training Methods**
- DARLING (Facebook, 2509.02534): online RL 中 quality+diversity 联合优化
- GEM (ICLR 2025): game-theoretic 方法维持 SFT diversity
- 我们的定位: 这些方法假设 collapse 是 default outcome，但我们的证据显示在 standard iterative SFT 中 collapse 并未自然发生

**(d) Diversity Measurement**
- Vendi Score, Self-BLEU, embedding-based metrics
- 简要说明 metric 选择的 rationale

### 3.3 Experimental Setup

**Pipeline 描述**:
- Base model: Qwen3-0.6B (选择理由: 小模型允许完整 iterative loop 在合理时间内完成; 0.6B 是最小的 "capable" 模型，能生成 coherent responses)
- Dataset: UltraFeedback 2200 prompts (通用指令 following)
- 每代: 对每个 prompt 生成 K 个候选 → reward model (ArmoRM) 评分 → 选择 top-1 → 训练下一代模型
- 3 generations (Gen 0 → Gen 1 → Gen 2)

**条件设计 (6 conditions)**:
| Condition | Adaptation | K | LR | Curation | Rationale |
|-----------|-----------|---|-----|----------|-----------|
| C1 | LoRA (r=16) | 4 | 2e-4 | ArmoRM top-1 | Standard LoRA setup |
| C2 | LoRA (r=16) | 8 | 2e-4 | ArmoRM top-1 | Doubled selection pressure |
| C3 | Full-FT | 4 | 5e-6 | ArmoRM top-1 | Full capacity, conservative LR |
| C4 | Full-FT | 4 | 2e-5 | ArmoRM top-1 | Full capacity, aggressive LR |
| C5 | LoRA (r=16) | 4 | 2e-4 | Random 1-of-K | No-curation baseline (LoRA) |
| C6 | Full-FT | 4 | 5e-6 | Random 1-of-K | No-curation baseline (Full-FT, conservative LR) |
| C7 | Full-FT | 4 | 2e-5 | Random 1-of-K | No-curation baseline (Full-FT, aggressive LR) |

(+ C8: Full-FT K=16 LR=2e-5, if available)

**变量设计逻辑**:
- LoRA vs Full-FT: 隔离参数容量的影响
- K=4 vs K=8 (vs K=16): 隔离 selection pressure 的影响
- LR=5e-6 vs 2e-5: 隔离学习强度的影响 (underfitting vs aggressive fitting)
- Curated vs Random: 隔离 curation 本身的因果效应

**Metrics**:
- Vendi Score (primary): kernel-based diversity, 捕捉 semantic diversity
- Self-BLEU: lexical overlap
- NN Distance: embedding space 中 nearest-neighbor 距离
- Training loss: 学习动态
- ArmoRM quality score: 质量保持

### 3.4 Results

**Main Finding: No Diversity Collapse (Section 4.1)**
- 核心表格: 所有 6 条件的 Vendi Score 轨迹
- Claim: 所有 curated 条件 Vendi 变化 < 1% (range: -0.27% to +0.91%)
- 即使 K=8 (12.5% 保留率)，collapse 仍不出现
- 即使 loss 下降 80% (Full-FT lr=2e-5)，模型 aggressively 拟合 curated 分布，diversity 仍微增 (+0.68%)

**Sub-finding 1: Relative Suppression, Not Absolute Collapse (Section 4.2)**
- No-curation baselines 显示 diversity 自然增长 (+1.4% to +3.1%)
- Curated 条件增长被抑制但不逆转
- Distinction 很重要: "slower growth" ≠ "collapse"

**Sub-finding 2: Curation Effect Direction Reversal (Section 4.3)** ⭐ CORE FINDING
- Curation-vs-baseline gap 随训练容量增加从**抑制→促进**方向性反转:
  - LoRA (low capacity): curation 抑制 diversity **-3.40pp**
  - Full-FT lr=5e-6 (medium): 抑制收窄 **-0.46pp**
  - Full-FT lr=2e-5 (high): curation **促进** diversity **+0.63pp**
- 诊断: LoRA 的 1.67% 可训练参数对 diversity 施加 implicit regularization; 充分学习后，curation 选出的高质量样本反而提供了更丰富的学习信号
- Figure 4 bar chart 展示这个从负到正的梯度（**关键可视化**）
- 这意味着: "curation hurts diversity" 的结论是 capacity-confounded; 在充分训练条件下 curation 甚至微促进 diversity

**Sub-finding 3: Quality-Diversity Non-Tradeoff (Section 4.4)**
- ArmoRM 质量评分在所有条件下保持稳定 (变化 < 1.2%)
- 无 quality-diversity tradeoff: curation 不提升质量也不降低 diversity
- 可能原因: reward model 区分度不足 (候选间 reward gap 仅 ~0.04)

**(Conditional) Sub-finding 4: K=16 Boundary Condition (Section 4.5)**
- If K=16 shows collapse: 发现 boundary (K=8 safe, K=16 collapses)
- If K=16 also stable: further strengthens the negative result

### 3.5 Analysis

**Metric-Dependent Collapse: Format vs Semantic (Section 5.1)** ⭐ CORE ANALYSIS
- **核心发现**: Collapse is real but mischaracterized — semantic diversity resilient, format/template diversity collapses
- 数据 (K=8 curation, Gen0→Gen2):
  - Opening unique ratio: 70.1% → **36.7%** (vs baseline 79.4% → 51.3%)
  - Near-dup start rate: 50% → **84%** (vs baseline 38% → 75%)
  - Opening entropy: -1.13 bits (vs baseline -0.75 bits)
  - 但 per-response TTR: curation -0.008 vs baseline -0.023 (curation 更好)
- 机制: ArmoRM 隐性偏好特定 opening patterns → 迭代选择放大为模板
- Vendi Score 盲区: embedding models 对 surface formatting 不敏感
- **推荐补充指标**: opening_entropy, near_duplicate_start_rate, structural_template_frequency

**Why doesn't SEMANTIC collapse happen? (Section 5.2)**
- 假说 1: Prompt diversity as anchor — 2200 不同 prompts 维持 corpus-level semantic diversity
- 假说 2: Reward model saturation — ArmoRM 区分度低 (reward range ~0.04)
- 假说 3: Generation stochasticity — Temperature > 0 注入足够随机性
- 数据支持: per-prompt candidate variance 表格

**CARR Proxy Covariance (Section 5.3, supplementary)**
- Adaptive reweighting 99.3% selection overlap (proxy scores r=0.63-0.77)
- 解释: text heuristic proxies 天然与 reward 共变，multi-objective rebalancing 无增量
- 与 format collapse 的联系: proxy-based 方法无法修复 format homogenization

**When MIGHT semantic collapse occur? (Section 5.4)**
- Much higher K (K=64), longer iteration (T >> 3), narrower prompts, stronger RM
- 每个条件有实验/文献证据支撑

### 3.6 Discussion

**Implications for the field (Section 6.1)**:
- Diversity collapse under curation is real but mischaracterized: 发生在 format 层而非 semantic 层
- 现有 diversity-preserving 方法 (DIVE, DARLING, GEM) 可能在解决错误的层面: 它们优化 embedding diversity，但真正的 collapse 在 surface patterns
- 实践指导: (1) 标准 Vendi/embedding metrics 不足以监控 iterative training diversity; (2) 需要加入 format-level 指标; (3) semantic collapse 在标准条件下不是首要担忧

**Relation to Kirk et al. (Section 6.2)**:
- Kirk et al. 的 observation (RLHF reduces diversity) 在单轮中成立
- 但在 iterative SFT 中，curation 的效应没有 compound: 每一代的 diversity loss 不累积
- 可能原因: SFT ≠ RLHF; iterative generation 注入了足够的 stochasticity

**Limitations (Section 6.3)**:
- 模型规模: 仅测试 0.6B, 更大模型可能行为不同
- 代数: 仅 3 代, 长期 (10+ 代) 效应未知
- 数据: UltraFeedback 2200 prompts, 更窄的 domain-specific 数据可能不同
- Reward model: 仅用 ArmoRM, 更强/更对齐的 reward model 可能产生更大 selection pressure
- Diversity metrics: format collapse 发现基于 n-gram/pattern 分析，更细粒度的 style/reasoning diversity 未覆盖

### 3.7 Conclusion

- 核心发现: Diversity collapse under reward curation is metric-dependent — semantic diversity (embedding-based) is resilient, while format diversity (opening patterns, templates) collapses significantly
- 贡献: metric-dependent collapse 发现 + 补充指标推荐 + direction reversal + boundary taxonomy
- Call to action: (1) 监控 iterative training 时加入 format-level 指标, (2) 未来 diversity-preserving 方法应区分 semantic vs format 层面, (3) 在更极端条件下验证 semantic collapse 是否最终也会发生

---

## 4. Tables/Figures 清单

### Main Paper

| ID | 类型 | 标题 | 内容 | Section | 用途 |
|----|------|------|------|---------|------|
| **Table 1** | Table | Vendi Score Trajectory Across Conditions and Generations | 6 条件 × 3 代 Vendi Score (Gen0, Gen1, Gen2) + 绝对变化 + 相对变化%, 加粗 baseline | 4.1 Results | **Main result table** |
| **Figure 1** | Figure | Experimental Pipeline Overview | Iterative self-training loop 示意图: Generate K → Reward Score → Select Top-1 → Train → Next Gen. 标注各 condition 的变量 | 3 Setup | Pipeline 说明 |
| **Figure 2** | Figure | Vendi Score Trajectories: Curated vs Uncurated | 折线图, x=generation, y=Vendi Score, 6 条线 (4 curated + 2 baseline), baseline 用虚线. 直观展示: curated 平坦, baseline 微升, 无 collapse | 4.1 Results | **Core visualization** |
| **Table 2** | Table | Full Metrics by Generation | 6 条件 × 3 代的完整指标 (Quality, Vendi, Self-BLEU, NN Distance, PPL) | 4.1 Results | 完整数据 |
| **Figure 3** | Figure | LoRA Capacity Artifact: K=4 vs K=8 Convergence | 并排对比: LoRA K=4 和 K=8 的 Vendi 轨迹几乎重合 (Gen2 都是 107.25); 加注 Full-FT 消除 gap | 4.3 Analysis | LoRA artifact 可视化 |
| **Table 3** | Table | Training Loss Dynamics Across Conditions | 6 条件 × 3 代 average training loss, 显示 learning dynamics 差异 | 4.1 Results | 训练动态 |
| **Figure 4** | Figure | Curation Effect Direction Reversal | Bar chart: x=训练容量递增 (LoRA → Full-FT lr=5e-6 → Full-FT lr=2e-5), y=curated-vs-baseline Vendi gap (pp). 展示从 -3.4pp → -0.46pp → **+0.63pp** 的方向反转梯度 | 4.3 Results | **核心可视化: direction reversal** |

### Supplementary / Appendix

| ID | 类型 | 标题 | 内容 | Section | 用途 |
|----|------|------|------|---------|------|
| **Table A1** | Table | Per-Generation Training Loss (Detailed) | 每个条件的 per-step loss 曲线数据 | Appendix | 训练细节 |
| **Table A2** | Table | CARR Dry-Run: Weight Evolution and Selection Overlap | CARR adaptive weights 变化 + 与 fixed-weight 的 overlap % | 5.3 Analysis | CARR negative finding |
| **Table A3** | Table | Proxy Score Correlation Matrix | Quality/Diversity/Complexity 三维度间 Pearson r | 5.3 Analysis | 解释 CARR 失效原因 |
| **Figure A1** | Figure | Per-Prompt Candidate Variance Across Generations | 3 代的 within-prompt score variance 下降趋势 | 5.1 Analysis | 解释 reward signal 弱化 |
| **Table A4** | Table | Quality Retention Across Conditions | ArmoRM 质量评分的 gen0 vs gen2 对比 | 4.4 Results | Quality 稳定性 |
| **(Conditional) Table 4 / Figure 5** | Table/Figure | K=16 Boundary Condition Results | K=16 的 Vendi 轨迹, 与 K=4/K=8 对比 | 4.5 Results | Boundary finding (if available) |

### 图表总计
- Main paper: 4 Figures + 3 Tables (约 2.5-3 页空间)
- Appendix: 1 Figure + 3-4 Tables
- Conditional: 1 Table/Figure (K=16 data)

---

## 5. 页数预估与优先级

EMNLP 2026 长文限额 8 页正文 + unlimited references/appendix:

| Section | 预估页数 | 优先级 |
|---------|----------|--------|
| Abstract | 0.3 | P0 |
| Introduction | 1.2 | P0 |
| Related Work | 1.0 | P1 |
| Experimental Setup | 1.0 | P0 |
| Results | 2.0 | P0 |
| Analysis | 1.5 | P0 |
| Discussion + Limitations | 0.7 | P1 |
| Conclusion | 0.3 | P2 |
| **Total** | **8.0** | |

---

## 6. 论文 Framing 关键策略

### 6.1 Narrative Arc
```
Intuitive fear (curation → narrowing → collapse)
    → Systematic test (7 conditions × 3 generations)
        → Surprising nuance: semantic diversity resilient, BUT format collapses
            → Key insight: collapse is real but mischaracterized by standard metrics
                → Measurement contribution: what to measure and when to worry
```

### 6.2 避免的陷阱
- **不要写成 "我们失败了"**: 写成 "contrary to widespread expectation, we find..."
- **不要贬低 diversity-preserving 方法**: 写成 "our results refine the conditions under which these methods are most needed"
- **不要过度泛化**: 明确 boundary conditions (model size, K range, generation count, prompt diversity)
- **不要忽视 relative suppression**: 承认 curation 确实抑制了自然增长，只是不导致 absolute collapse

### 6.3 Selling Points for Reviewers
1. **Timeliness**: iterative self-training 是当前热点，diversity concern 是 open question
2. **Rigor**: 6 条件系统对照，隔离了 adaptation method / selection pressure / learning rate 三个变量
3. **Actionable**: 不只是说 "没有 collapse"，还分析了 why 和 when might
4. **Honest**: 明确 limitations 和 boundary conditions，不过度宣传
