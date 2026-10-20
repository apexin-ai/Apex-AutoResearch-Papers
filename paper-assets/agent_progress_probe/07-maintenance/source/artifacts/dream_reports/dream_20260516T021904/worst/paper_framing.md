# Paper Framing — agent_progress_probe

## Target Venue
- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
- Format: Long paper (8 pages + appendix)
- Track: LLM Agents / Main Conference
- Paper type: **Framework paper**（D073 revision: anti-circularity centered + detection-to-intervention）

## Core Claims (4 条) — D072 Upgrade

1. **Structural Features Dominate Zero-Shot Cross-Agent Transfer (primary contribution)**: 系统性对比发现结构特征在跨 agent 零样本迁移上具有压倒性优势——30 个结构特征在 in-domain (RF 0.9951) 和 cross-agent zero-shot (GB 0.967) 近完美预测停滞，零样本迁移上大幅领先 probe（zero-shot 0.598 vs 0.967, +36.9pp）和 best LLM judge（+16.8pp, cross-agent structural 0.967 vs best LLM 0.799）。然而 probe 在少量目标域数据微调后迅速缩小差距：10% FT 0.918（-5pp），20% FT 0.948（-2pp），50% FT 0.968（追平）。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)。这揭示：(a) 结构特征天然跨 agent 迁移——不需要任何目标域数据即可部署；(b) probe 的语义信号在 domain adaptation 后能匹配结构特征——stagnation 信息在 embedding 中存在但需要适配提取；(c) 实际部署中，目标 agent 数据不可用时结构特征是明确首选；有少量标注数据时两种方法收敛。**改变社区对 agent monitoring 方法选型的认知：结构特征是零数据部署的默认选择，不需要昂贵的表示学习和域适配。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。

2. **LF Temporal Dynamics and Label Quality as Transfer Bottleneck (analytical contribution)**: 两层发现。**时序动态**：LFs 在 trajectory 上展现系统性但 agent-specific 的时序角色。SWE-Agent 上 cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)；OH 上 cmd_rep 角色从 leading 变 lagging (+3.32步)，而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。不同 agent 架构产生不同的 LF 行为模式，但部分 LF（file_diff, OB）展现跨域稳定性。**标签质量瓶颈 + cmd_rep coverage 贡献**：通过标签审计发现，label quality 是 cross-agent transfer 的主导因素。修复 OH 标签版本偏差（stag_rate 6.56%→21.45%）后：(a) probe 5% FT 从 0.570 跃升到 0.850（+28pp），新 5% 超过旧 50%（0.688）；(b) cmd_rep 实际是高精度低召回检测器（precision 97.91%, FP 0.15%），旧 "71% FP 噪声源" 完全是标签 bug 产物。**Prevalence-matched ablation**（同一测试集 N=6122, stag=19.3%）揭示 cmd_rep 真实贡献是 **-29.4pp**（p≈0, McNemar chi²=1551）：移除 cmd_rep 不改变高置信标签质量（2-LF 与 3-LF 在交集上 100% 一致），但将可用训练数据从 43K 缩减到 4K——cmd_rep 的核心价值是 coverage（让足够多窗口进入 conf≥2），而非标签质量。**实证指导**：WS pipeline 中 LF 的主要贡献可能是 coverage 而非精度，移除看似冗余的 LF 可能导致训练数据崩塌。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。

3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) **TWV（时序加权投票）**：绝大多数 σ 下有害（twv-ablation）；唯一微弱正向的 σ=2 训练的下游分类器全面劣化（in-domain -4.9pp, cross-agent -21.7pp, conf≥2 -1.8pp）(structural-on-twv)；(b) **HMM-TLM**：stagnation class overpredict；(c) **Lag-aware HMM**：仅追平 MV（0.8936）。**结论**：在当前 3-LF、低冲突（conf≥2 一致率 95.1%）的 regime 下，temporal alignment 的收益被噪声引入抵消。TWV 改变的主要是低置信标签，但改变方向是错的。这是对 "i.i.d. violation → temporal model must help" 这一直觉的重要否定，为未来 temporal label model 研究提供了关键约束条件。

4. **Detection-to-Intervention: Compute-Efficient Early Termination (D072 upgrade, actionable contribution)**: 将停滞检测从 passive monitoring 升级为 actionable intervention。基于检测器输出设计 early termination policy：当连续 k 个窗口被预测为 stagnation 时终止 agent 执行。**三层实证**：(a) **Compute waste audit**：回溯分析 SWE-Agent + OpenHands 全量轨迹，量化 "stagnation tail"——从首次真正停滞到轨迹结束浪费的 token/step/时间占比；(b) **Early termination simulation**：在测试集上模拟不同 threshold 的 early stopping policy，量化 precision-recall trade-off（误杀正常执行 vs 漏放停滞）和计算节省（saved tokens / steps）；(c) **Cost-effectiveness Pareto curve**：横轴 compute saved (%)，纵轴 task success preserved (%)，展示 structural detector 在不同 operating point 的 Pareto 前沿，与 oracle / random baseline 对比。**核心论点**：轻量级 structural features (<5ms per window) 不仅能准确检测停滞，还能在 deployment 中直接作为 early termination trigger，节省 X% 计算资源且仅损失 Y% 任务成功率——将 detection 研究连接到实际部署价值。**2-LF deployable config**：移除使用 privileged task outcome 的 λ₃ (outcome_backpropagation)，仅用 cmd_rep + file_diff 的 2-LF 配置在 conf≥2 上性能仅降 1.8pp (0.978)，且与 3-LF 标签 100% 一致——证明 early termination 可在无 outcome 信息的 real-time 场景下部署。

## Story Spine

- **Problem**: LLM agents 在长期任务中频繁"语义停滞"——执行看似合理但集体无效的动作序列。每个动作可能非重复、局部合理，但整个窗口缺乏 goal-directed progress。现有方法要么检测结构性循环（漏掉语义多样的停滞），要么做 step-level scoring（丢失窗口内的时序动态），要么依赖 LLM 自我评估（高开销 + 受困模型的判断力受限）。

- **Existing approaches & gaps**: (a) Cycle detectors（CDCS+CDSA, SpecRA, TrajAD）捕获重复/异常但漏掉语义多样的停滞；(b) Process Reward Models — **AgentPRM (Xi et al., ACM Web 2026, arxiv 2511.08325)** 是最直接的竞争者：用 TD/GAE 训练 step-level PRM 评估 "promise and progress"，但需要 outcome labels + RL pipeline，是 training signal 而非 monitoring tool。另有 PRM framework (arxiv 2502.10325)、ToolPRMBench (arxiv 2601.12294)、trajectory-level reward modeling (arxiv 2604.08178)。PRM 方向在 2025-2026 非常拥挤，我们的差异：**不需要 outcome labels**、**window-level 捕获 temporal dynamics**、**monitoring 而非 training**；(c) Self-reflection（Reflexion, LATS, Tree of Thoughts）依赖被困模型的自我评估，且是 intervention 而非 monitoring；(d) RL value functions (CodeRL) 需要 reward shaping；(e) **Agent monitoring 新方向**："Monitoring LLM Agents for Sequentially Contextual Harm" (ICLR 2025 Workshop) 论证了 sequence-level monitoring 的必要性（单步分析不够）；"Reliable Weak-to-Strong Monitoring" (arxiv 2508.19461) 研究了弱模型监控强 agent，但关注 safety 而非 progress；(f) **Agent degradation benchmark**：SlopCodeBench (arxiv 2603.24755, 2026) 量化了 coding agent 在长期任务中的退化——structural erosion 在 77% 轨迹上升、verbosity 在 75.5% 上升——为我们的 problem motivation 提供了最新实证。

- **Our framing (D072 Upgrade)**: 从 stagnation detection 到 compute-efficient intervention 的完整框架。**四层贡献**：(1) **Zero-Shot Transfer Dominance (primary)** — 结构特征在零样本跨 agent 迁移上大幅领先 probe（+39.4pp matched-scope）和 best LLM judge（+16.8pp），且仅需 2-LF deployable config（无 privileged outcome 信息）即可在 conf≥2 上达到 0.978 F1——结构特征是零数据部署的默认选择；(2) **Detection-to-Intervention (D072 新增)** — 将检测器输出转化为 early termination policy，回溯量化 compute waste 并模拟不同 threshold 下的 precision-recall-savings trade-off——建立从 detection research 到 deployment value 的直接桥梁；(3) **LF Temporal Dynamics Analysis** — 量化 LFs 在 agent trajectory 上的时序角色 + label quality as transfer bottleneck + circular evaluation 方法论贡献；(4) **TLM Negative Finding** — 三种 temporal label model 均未超越 MV，提供 failure analysis 约束未来研究。

- **Headline result template**: "We present a framework for real-time LLM agent stagnation monitoring, validated on human-annotated gold and bridging detection with compute-efficient intervention. Lightweight structural features (<5ms per window) achieve 0.967 cross-agent F1 with zero target-domain data. Human gold validation (505 windows, 3 annotators, Fleiss κ=0.39) confirms structural classifiers outperform majority-vote silver labels (GB 0.839 vs MV 0.798, p<0.001). Critically, on windows where labeling functions disagree (conf=1, N=282), the classifier maintains F1=0.784 vs MV 73.8% agreement — demonstrating learned soft decision boundaries that generalize beyond binary LF heuristics. In matched cross-agent evaluation, structural features outperform the best LLM judge by Xpp (structural Y vs LLM Z, both on OpenHands) and a zero-shot neural probe by 39.4pp. A deployable 2-LF configuration (without privileged task outcomes) maintains 0.978 F1. Retrospective compute-waste analysis shows X% of agent steps occur after stagnation onset; early termination simulation at k=K saves Y% compute while preserving Z% task success. Three temporal label model implementations fail to improve over majority vote, providing a well-characterized negative result constraining future research directions."

## Venue Fit Risks

- **EMNLP vs ICSE**: 核心 LFs 和数据 100% 来自 SE 领域。贴合 NLP venue 的策略：(a) weak supervision on sequential data 是通用方法论，适用于任何有时序结构的标注场景——data programming / Snorkel 出自 NLP 社区；(b) structural vs semantic signal 的发现对任何 agent monitoring 系统有指导意义；(c) circular evaluation 问题是 weak supervision 评估的通用挑战；(d) TLM negative finding 对 sequential label model 研究有方法论价值。
- **Reviewer lottery**: 遇到 SE-skeptical 的 NLP reviewer 可能被判 "more suitable for ICSE/FSE"——通过强化方法论洞见的跨域普适性和 LLM agent 社区的 NLP 属性来降低风险。
- **"Negative finding paper 不够 novel"**: 论文不是纯 negative finding——structural signal discovery (Claim 1) 是强正面结果；TLM negative finding (Claim 3) 附带详细 failure analysis 和对未来研究的约束条件。EMNLP 接受 analysis paper 和 well-motivated negative results。
- **vs PRMs（2025-2026 最拥挤的方向）**: Related Work 加专门小节。核心定位差异：PRM 需要 outcome labels + RL pipeline（昂贵），我们是 monitoring tool + weak supervision pipeline（轻量）；PRM 是 step-level training signal，我们是 window-level detection。
- **"Why not LLM-as-judge?"**: 已有 baseline 对比——structural approach <5ms inference vs LLM 高开销，且 structural +16.8pp vs best LLM。

## Anticipated Reviewer Concerns & Countermeasures

| Concern | 应对 |
|---------|------|
| Circular evaluation（训练和评估都在自动标签上） | **6 层防御（D073 强化）**：(1) 明确声明 F1 = LF consensus fidelity；(2) structural baseline 0.9951 量化 circularity 上界；(3) Cross-agent OH 评估（cmd_rep 从 65.5%→5.4%，LF 分布剧变但 model 稳定）；(4) Gold set GB 0.839 > MV 0.798 (p<0.001)——model 优于 LF vote on human labels；(5) **Conf=1 gold stratified analysis（新增核心证据）**：在 LFs 意见分歧的 282 个 gold 窗口上，GB F1=0.784 vs MV agreement 73.8%——模型在 LFs 失效的地方仍然有效，证明学到了 beyond-LF 的软决策边界；(6) **LLM-on-OH matched comparison（新增）**：相同 OH 轨迹上 structural vs LLM 直接对比，消除评估范围混淆 |
| Structural features outperform everything — so what's the point of the probe? | 论文已更新：probe 在 50% FT 后追平 structural（0.968 ≈ 0.967）。Probe 的价值：(1) 有目标域数据时性能收敛且支持 real-time inference + end-to-end deployment；(2) data scaling 曲线（0.598→0.968）展示真实学习过程，对比 structural 的 circular eval；(3) Gold set 上的对比是最终裁判 |
| Probe catches up with fine-tuning — is structural advantage real? | 零样本优势 +36.9pp 是真实且巨大的实用价值——部署时目标 agent 数据通常不可用。收敛现象本身是重要发现：stagnation 信号同时存在于结构和语义表示中，差异在于提取成本（structural = 零适配，probe = 需要域适配数据）。论文定位为 data efficiency advantage for deployment，不是 fundamental signal type difference |
| TLM negative finding 不够有 contribution | Failure analysis 详细到足以约束未来研究：(1) 3-LF 低冲突 regime（conf≥2 一致率 95.1%）限制了 temporal alignment 的改进空间；(2) TWV 在低置信区改变标签方向错误；(3) 三种不同实现排除了实现偏差。论文同时有强正面结果（Claim 1, 2） |
| 跨 agent 迁移只测了两个 SE agent | Two-agent scope 在 Limitations 讨论 + structural features 跨域 0.967 的强迁移证据。Future work 包含 non-SE agents |
| 为什么不直接用 LLM | LLM-as-judge baseline 已对比：cross-agent structural +16.8pp vs best LLM (0.967 vs 0.799)、<5ms vs LLM 高开销 |
| outcome_backpropagation 信息泄露 | 3-seed holdout：移除 OB 后 f1_stag=0.641±0.034（-22pp），7.1pp 为纯信号贡献。OB 作为 "Privileged Distant Supervision"，在 3-LF 框架中不可替代 |
| Probe 只学了 LF 启发式 | LF oracle baseline（All-Agreement 0.854, probe +5.1pp）+ 错误分析（FP 65% = LF 未覆盖的语义多样停滞）+ gold set 最终验证 |
| Early termination 只是 simulation 不是真实部署 | Simulation 在真实轨迹上回溯执行，等价于 offline policy evaluation——online deployment 需要 agent framework 集成（future work），但 savings estimate 是 conservative lower bound（真实场景中 freed compute 可重新分配给新 attempt） |
| Compute savings 数字依赖 stagnation 标签质量 | Gold set 验证 + bootstrap CI 确保 savings 估计有置信区间；2-LF config 不依赖 privileged outcome info，savings 数字完全基于 deployable 配置 |
| Architecture novelty 不足 | 论文升级为 framework paper——novelty 在于从 detection 到 intervention 的完整链路 + matched-scope evaluation 方法论 + 2-LF deployable 配置设计，不在架构 |
| Gold set underpowered (N=505, κ=0.39) | Power analysis 诚实报告能力边界 + human ceiling estimate（如果 annotators 自身 agree 80%，GB 84% 接近 ceiling）+ conf-stratified 证据（conf≥2 agreement 96.7%）+ 多角度 defense: N=505 sufficient to detect 4pp at α=0.05 (power=X)；κ=0.39 是 stagnation 本身 definitional ambiguity 反映（见 related task comparisons）|
| +39.4pp gap 可能是 encoder 太弱 | 报告 BGE-M3 和 E5-large probe zero-shot cross-agent transfer。如果 gap 缩小到 <20pp 则调整 headline；如果仍 >30pp 则 encoder 无关论证成立 |
| "Semantic stagnation" rebrands existing concepts | 明确映射到现有 agent failure mode taxonomy + window-level formulation 的特殊性论证 |
| Related work incomplete | 扩展到 30+ references：PRMs / agent self-reflection / weak supervision / agent degradation benchmarks |
| Embedding model unspecified | 具名 Qwen3-Embedding-0.6B + encoder ablation（BGE/E5/GTE，三者均 >0.90） |
| LF hold-one-out ablation 解读 | **禁止 "去掉 X 后 F1 更高" 的 claim**（test set 偏移假象）。正确框架：覆盖率贡献 + 跨集泛化 + 标签一致性 |
| Structural data scaling 不能表述为 "robustness to data scarcity" | Circular eval 框架下正确解读：结构特征 ≈ LF 输入，10% 数据即可学会 LF→label 映射（RF 0.991）。这是 LF 重建的简单性证据，不是检测鲁棒性。论文呈现时标注 $^\dagger$ circular caveat，与 probe 的 data scaling（0.805→0.906，真正的学习曲线）对比呈现 |
| OB 移除后 f1_stag 数字来源 | ✅ **已闭环**：outcome-bp-3seed 3-seed mean f1_stag=0.641±0.034（seeds 42/123/456: 0.600/0.640/0.683）。"0.000" 来源已溯清：woob 模型在 OB-only 窗口子集（687w）上全预测 progress 导致子集 f1_stag=0.000，非完整测试集结果。D025/D026 已正确撤回。 |

## D039 Pivot 变更记录
- D034 → D039: Claim 1 TLM（原"论文最强 claim"）降级为 Claim 3 negative finding
- D034 → D039: Claim 2 structural signal 升级为 Claim 1 primary contribution
- D034 → D039: Claim 3 LF temporal → Claim 2，加入 circular eval methodology
- D039 新增: TLM 三种实现全败的 failure analysis 作为独立贡献
- D039 触发实验: structural-on-twv (TWV labels degrade downstream -4.9pp ~ -21.7pp) + twv-ablation (TWV harmful for most σ) + temporal-label-model (HMM/lag-aware HMM failed)
- oh-fewshot-retrain (标签修复后): Claim 1 从 "fundamentally structural" 修正为 "zero-shot transfer dominance"——probe 50% FT 追平 structural（0.968≈0.967），但零样本差距 +36.9pp 仍是核心实用优势
- oh-label-retrain (标签修复后): Claim 2 ablation 结论反转——去掉 cmd_rep 从 +17.6pp 变为 -6.5pp，cmd_rep FP 从 71%→2.3%。"cmd_rep 在 OH 是噪声源" 完全是标签 bug 产物。Claim 2 重构为 "temporal dynamics + label quality as transfer bottleneck"（Option A, D051）
- [2026-05-15] Headline result template 已更新：移除旧 +17.6pp claim，改为 label quality audit + prevalence-matched ablation 叙事
- [2026-05-15] SlopCodeBench 数字修正：90%/80% → 77%/75.5%（与原文 arXiv:2603.24755 一致）
- [2026-05-15] Registry swe_agent_stag_ratio 修正：0.36 → 0.2846（整体 28.46%，非 conf≥2 的 37.96%）
- [2026-05-15] **D072 Upgrade**: 从 3-claim empirical study 升级为 4-claim framework paper。新增 Claim 4 (Detection-to-Intervention)：early termination simulation + compute waste audit + cost-effectiveness Pareto curve。Narrative 从 "systematic empirical study" 升级为 "real-time monitoring framework: from structural detection to compute-efficient intervention"。2-LF deployable config (0.978, -1.8pp) 同时支撑 Claim 1 和 Claim 4。Matched-scope eval (+39.4pp) 修正 headline comparison
- [2026-05-16] **D073 Anti-Circularity Revision**: Dream 三档均 3/6 (Weak Reject)，核心问题是循环性证据不足。修订策略：(1) 以 conf=1 gold analysis 为反循环性核心证据（LFs 分歧时 GB 仍优于 MV）；(2) headline 以 gold-validated 结果为主（silver 为辅）；(3) LLM-on-OH 必须执行消除评估范围混淆；(4) cross-agent probe BGE/E5 确认 gap 是否 encoder-independent；(5) calibration + power analysis 加强 deployment 可信度；(6) references 扩到 30+。新增 11 个实验覆盖 anti-circularity + fair comparison + statistical robustness + figures