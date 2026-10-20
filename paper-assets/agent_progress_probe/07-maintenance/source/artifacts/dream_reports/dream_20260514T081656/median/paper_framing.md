# Paper Framing — agent_progress_probe

## Target Venue
- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
- Format: Long paper (8 pages + appendix)
- Track: LLM Agents
- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)

## Core Claims (3 条)

1. **弱监督标注框架有效性**: Domain-specific labeling functions（file_diff_delta, command_repetition, outcome_backpropagation）通过 data programming 范式为 agent 轨迹提供足够的训练信号，尽管 LF 间一致率仅 40.3%，majority vote 标签在人工校验中达到 81.5% 准确率（conf≥2 子集）。这是 Snorkel 范式到 agent trajectory 的非平凡迁移——LFs 产生时序信号而非 i.i.d. 标签。

2. **Window-level 时序建模优于启发式和静态聚合**: 学习的 GRU probe 在 progress stagnation 检测上显著优于所有 baseline——包括最强启发式 Repeat-3（+6.24pp macro-F1）、embedding cosine similarity、static mean-pooling、LF ensemble oracle。时序建模捕获了 stagnation onset 的位置依赖动态，这是 uniform aggregation 无法表达的。

3. **跨实现迁移性**: Progress signals 在不同 agent 实现间可迁移（SWE-agent → OpenHands），probe 在 cross-agent 评估中保持有效，表明学到的是通用的 goal-directed progress 信号而非特定 agent 的行为模式。

## Story Spine

- **Problem**: LLM agents 在长期任务中频繁"语义停滞"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态）。

- **Existing approaches & gaps**: Cycle detectors（IBM CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；step-level value estimators（AgentPRM, SWE-TRACE）在 step 粒度打分，window 内均匀聚合丢失 stagnation onset 的时序签名；self-reflection（AgentCollab）依赖被困模型的自我评估。

- **Our framing**: 将 progress stagnation 重新定义为 window-level progress estimation 问题。双贡献：(1) 基于 data programming 的弱监督标注框架——将 Snorkel 范式迁移到 agent trajectory，解决标注数据缺失问题；(2) 系统性实证研究——证明轻量 GRU probe 在弱监督标签上能学到有效的 progress 信号，并在跨实现场景下保持迁移性。架构（GRU + attention）是 deliberately simple 的技术选择，不是核心贡献。

- **Headline result template**: "On SWE-bench agent trajectories, ProgressProbe achieves 0.91 macro-F1 for window-level progress estimation while the best heuristic baseline (Repeat-3) achieves only 0.84, demonstrating that learned temporal modeling on weakly-supervised labels captures stagnation patterns beyond structural repetition."

## Venue Fit Risks

- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。通过以下方式 frame 贴合 NLP venue：(a) 建立与 NLI/paraphrase detection 的结构类比（trajectory-level semantic equivalence under surface diversity）；(b) non-NLP baseline 对比证明 NL embedding 的必要性；(c) data programming / weak supervision 本身是 NLP 社区熟悉的范式（Snorkel 出自 NLP）。
- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 "more suitable for ICSE/FSE"——通过强化弱监督方法论贡献和跨 domain 方法论洞见来降低风险。
- **"Why not LLM-as-judge?"**: 必须有 LLM-as-judge baseline 对比——ProgressProbe 的优势是 <5ms inference vs LLM 的高开销（The Verifier Tax 2.0-2.8x token inflation）。

## Anticipated Reviewer Concerns & Countermeasures

| Concern | 应对实验 |
|---------|----------|
| Circular evaluation（训练和评估都在自动标签上） | 400 窗口人工标注 gold set + 在人工标签上重新评估所有方法 |
| Probe 只学了 LF 启发式（0.95 F1 太高） | LF ensemble oracle baseline 对比 + conf=1 全量数据泛化测试 + 错误分析 |
| 为什么不直接用 LLM | LLM-as-judge baseline + cost-accuracy Pareto 图 |
| 跨 agent 迁移只测了两个 SE agent | Limitations 中明确 scope，讨论 cross-domain 预期 failure mode |
| Architecture novelty 不足 | 架构降权为 technical choice，novelty 锚在方法论（弱监督框架 + 实证研究） |
| Repeat-3 baseline 已经很强（0.84） | 强调 probe 在 stagnation 检测上 +10.6pp（0.86 vs 0.75），错误分析展示 Repeat-3 漏掉的模式 |
