# Paper Framing — distrib_canary_collapse

## Target Venue
- Primary: AAAI 2027 (expected deadline ~August 2026)
- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)
- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间

## Core Claims (3 条)

1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。
2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% self-consuming 下 perplexity 与 canary 同步崩溃（不可预测），低 α 条件下 collapse 更渐进、canary lead time 有望扩展到 quality 指标。Predictability phase diagram 划定可预测/不可预测边界。
3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。

## Story Spine

- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。

- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。

- **Our framing**: 我们不是提出"通用 canary"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。

- **Headline result template**: "ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning."

## Anticipated Reviewer Concerns & Responses

| Concern | Response Strategy | Required Experiment |
|---------|-------------------|---------------------|
| "Canary 不预测 perplexity，实用价值有限" | Framing 为 regime-dependent：100% SC 是极端 regime；α-sweep 展示低 α 下 canary→perplexity 是否恢复 | α-sweep (P0) |
| "只在 Pythia-410M 上验证，scale 泛化？" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |
| "WikiText-103 单一数据集" | C4 cross-domain validation | domain-transfer (P1) |
| "为什么不用简单相关分析？" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |
| "4 个 canary 中 2 个失败，选择偏差？" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |
| "Intervention 实验缺失" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |

## Venue Fit

AAAI 2027 优势：
- ML 方法论 track 接受 empirical analysis + 统计方法论贡献
- 不要求 SOTA，接受 systematic study with novel methodology
- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力

风险：
- 如果被认为"只是 empirical study 没有算法贡献"→ 补 CRS + intervention 提升 method 贡献
- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend

## Key Narrative Constraints (from MVP)

1. **不能 claim "canary predicts model collapse"** — 只能 claim "canary predicts diversity collapse"，perplexity 通道在 100% SC 下断裂
2. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果
3. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — 主文聚焦 distinct_1/2，distinct_3 放 supplementary
4. **max_lag=5 可能截断真实 lead** — α-sweep 中增大 max_lag≥7
