# Paper Framing — agent_progress_probe

## Target Venue
- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
- Format: Long paper (8 pages + appendix)
- Track: LLM Agents
- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)

## Core Claims (3 条)

1. **Temporal Label Model for Sequential Agent Data**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态（leading/concurrent/lagging），导致 majority vote 在 LF 分歧区域（conf=1, 占 72%）标签质量低。我们提出 temporal label model，利用 LF 时序角色（command_repetition 领先 ~1.8 steps, outcome_backpropagation 滞后 ~2.1 steps）进行时序感知的标签聚合，在人工 gold set 上标签质量显著优于 majority vote。**这是对 data programming 在序列数据上的方法论贡献**，不是简单应用。

2. **Window-level Progress Estimation**: GRU probe 在 temporal label model 生成的标签上训练，在 LF 不可用/分歧的推理场景下有效估计 window-level progress。在人工 gold set 上 probe 超过 LF oracle（"student exceeds teacher"），且在 cost-accuracy Pareto 前沿优于 LLM-as-judge（含 CoT variant），<5ms inference vs LLM 高开销。

3. **Cross-implementation Transferability**: Progress signals 在不同 agent 实现间可迁移（SWE-agent → OpenHands），probe 在 cross-agent 评估中保持有效，而 LF oracle 严重退化，表明 probe 学到的是通用 goal-directed progress 信号。

## Story Spine

- **Problem**: LLM agents 在长期任务中频繁"语义停滞"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态），要么依赖 LLM 自我评估（高开销 + 受困模型的判断力受限）。

- **Existing approaches & gaps**: (a) Cycle detectors（CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；(b) Process Reward Models (PRMs, Lightman et al. 2023, Math-Shepherd) 在 step 粒度打分，需要 outcome labels per step（昂贵），window 内均匀聚合丢失 stagnation onset 的时序签名；(c) Self-reflection（Reflexion, LATS, Tree of Thoughts）依赖被困模型的自我评估，且是 intervention 而非 monitoring；(d) RL value functions (CodeRL) 需要 reward shaping。

- **Our framing**: 将 progress stagnation 重新定义为 window-level progress estimation 问题。**三层贡献**：(1) **Temporal label model** — 发现 LFs 在 agent trajectory 上产生系统性时序动态（leading/concurrent/lagging indicators），提出时序感知的标签聚合方法，解决标准 data programming 的 i.i.d. 假设违反问题（方法论贡献）；(2) **ProgressProbe** — 轻量 GRU probe 在弱监督标签上学到超越 LF 的 progress 信号（"student exceeds teacher"），且在 cost-accuracy 维度优于 LLM-as-judge；(3) **系统性实证研究** — 跨实现迁移 + LF 时序动态分析 + stagnation taxonomy。

- **Headline result template**: "Our temporal label model improves label quality by X% over majority vote on human gold set; ProgressProbe trained on these labels achieves 0.86 macro-F1, outperforming the best heuristic baseline by +Ypp and LLM-as-Judge (with CoT) while being 600× faster and 30× cheaper."

## Venue Fit Risks

- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。通过以下方式 frame 贴合 NLP venue：(a) temporal label model 对 data programming on sequential data 的方法论贡献是通用的，适用于任何有时序结构的标注场景；(b) 建立与 NLI/paraphrase detection 的结构类比（trajectory-level semantic equivalence under surface diversity）；(c) non-NLP baseline 对比证明 NL embedding 的必要性；(d) data programming / weak supervision 本身是 NLP 社区熟悉的范式（Snorkel 出自 NLP）。
- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 "more suitable for ICSE/FSE"——通过强化 temporal label model 的方法论普适性和跨 domain 方法论洞见来降低风险。
- **vs PRMs**: 必须明确定位 — PRMs 需要 step-level outcome labels（昂贵），我们用自动 LFs + temporal label model 实现类似效果，是 "weak supervision alternative to PRMs for progress estimation"。
- **"Why not LLM-as-judge?"**: 必须有 LLM-as-judge baseline 对比（含 CoT variant）——ProgressProbe 的优势是 <5ms inference vs LLM 的高开销。

## Anticipated Reviewer Concerns & Countermeasures

| Concern | 应对实验 |
|---------|----------|
| Circular evaluation（训练和评估都在自动标签上） | 400+ 窗口人工标注 gold set + 在人工标签上重新评估所有方法 |
| Why not use a label model (FlyingSquid)? | FlyingSquid baseline 对比 + temporal label model ablation |
| Probe 只学了 LF 启发式（0.95 F1 太高） | LF ensemble oracle baseline + conf=1 全量数据泛化 + 错误分析 |
| 为什么不直接用 LLM | LLM-as-judge baseline（含 CoT variant）+ cost-accuracy Pareto 图 |
| 跨 agent 迁移只测了两个 SE agent | Limitations 中明确 scope，讨论 cross-domain 预期 failure mode |
| Architecture novelty 不足 | 架构降权为 technical choice，novelty 锚在 temporal label model（方法论贡献） |
| outcome_backpropagation 信息泄露 | exit_context 占比统计 + hold-out 灵敏度分析 + 仅 last-N windows variant |
| Repeat-3 baseline 已经很强 | 强调 probe 在 stagnation 检测上的增量 + 错误分析展示 Repeat-3 漏掉的模式 |
| Related work incomplete (PRMs, Reflexion) | 扩展到 30+ references，显式定位 vs PRMs / agent self-reflection / weak supervision advances |
| Code-paper architecture alignment | 确保论文描述与实现精确匹配（有 attention 就写 attention，没有就不写） |
| Embedding model unspecified | 具名 Qwen3-Embedding-0.6B + encoder ablation（BGE/E5/GTE） |
| "Semantic stagnation" rebrands existing concepts | 明确映射到现有 agent failure mode taxonomy，论证 window-level formulation 的特殊性 |
