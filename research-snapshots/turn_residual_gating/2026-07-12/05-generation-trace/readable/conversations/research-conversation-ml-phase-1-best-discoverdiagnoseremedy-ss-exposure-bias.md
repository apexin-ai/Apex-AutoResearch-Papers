# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画 核心假

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/642a24ab-9637-448d-be97-8ff6319b4917.jsonl`
- **Structured JSON:** [`e3a65ae82bd1316b039f.json`](../../sessions/e3/e3a65ae82bd1316b039f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T08:13:19.711Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T08:13:19.711Z",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画\n核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general mitigation', \"Exposure bias 对 auxiliary attention loss 的 8×–27× gap 被审稿人接受为该场景下的 novel 实证贡献（非 'exposure bias is already known' 驳回）\", 'PCGrad 因果排除链（观察→假设→排除→指向真因）被认为方法论严谨，非 trivial ablation', \"SS + β-steering 双路径 mitigation 被视为 substantive constructive contribution（非 'just applied known technique'）\", '3-seed 统计 + bootstrap CI + 跨模型 + alternative GAR definitions 充分回应 W7/W1/W3', '论文写作成功执行 gromov/sun/xiao 对标模式，56 references 解决 W6']\n关键指标范围：{'llama_ss_ar_gar_beta0': [0.3, 0.5], 'llama_ss_tf_ar_gap_ratio': [1.0, 2.0], 'qwen_ss_ar_gar_beta0_3seed': [0.38, 0.45], 'qwen_ss_tf_ar_gap_ratio': [1.1, 1.5], 'dream_review_score': [3.5, 4.0], 'fatal_severe_concerns_remaining': [0, 1], 'reviewer_novelty_objection_probability': [0.0, 0.3], 'alternative_gar_defs_ss_improves': [3, 4]}\n叙事方向：原始 framing 完全成立。Title 用 T2（'From Collapse to Recovery'）强调完整弧。5 个 contributions 均可 full-strength claim。SS 跨模型通用性升级 C5 为 'cross-model validated mitigation'。Paper 定位 solid EMNLP main conference，不需要 Findings fallback。核心叙事：首次定量刻画 exposure bias 如何摧毁 auxiliary attention loss（8×–27×），因果排除梯度冲突后精确定位 distribution shift 为根因，SS 提供通用初步修复（gap 8×→~1.3×），构成完整的诊断-修复循环。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: turn_residual_gating\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**\n> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + \"观察→假设→排除→指向真因\" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result\n> **⚠️ Dream review D024: \"Cannot\" overclaims, novelty \"first measurement\" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 \"Fails to\", novelty 降级 \"first empirical characterization\"**\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 \"发现→定位→修复\" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。\n\n---\n\n## 1. Title Candidates\n\n- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating\n- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）\n- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）\n- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）\n\n推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 \"selectively destroys\"，去掉冗长副标题。T2 强调 \"发现→定位→修复\" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete \"discover → diagnose → initial remedy\" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |\n| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**\n\n**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 \"PPL -46%\" 和 \"selective dissociation\" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**\n7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication\n8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**\n9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) \"Parallel Attention Forcing\" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期（2026-05-23 Framing 升级后）\n- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。\n- **Best case**: 3.5 (Borderline Conference / Accept)。完整 \"发现→定位→修复\" 弧匹配 gromov/sun/xiao 模式。\n- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。\n- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复\"（强）。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: C1\n  description: Phase 1 GAR degradation diagnosis on Qwen-2.5-7B (70.8% raw drop)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: phase1_gar_diag\n  status: DONE\n  conclusion: success\n  metrics:\n    turn1_avg_gar: 0.0418\n    mid_turns_avg_gar: 0.0122\n    relative_drop: 0.708\n    num_conversations: 5\n    num_turns: 10\n    per_turn_avg_gar:\n    - 0.0418\n    - 0.0241\n    - 0.0224\n    - 0.013\n    - 0.0133\n    - 0.0086\n    - 0.0078\n    - 0.008\n    - 0.0157\n    - 0.0064\n- id: plan_002\n  claim: C2\n  description: ThreadGate v7 training (MSE+gate_div) - training GAR 0.48, inference\n    GAR 0.016\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_tg_s42_v7\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5035\n    eval_iid_dongre_mid_gar: 0.0152\n    eval_iid_ppl: 2.784\n    eval_heldout_ours_mid_gar: 0.5035\n    eval_heldout_dongre_mid_gar: 0.0152\n    eval_heldout_ppl: 2.78\n    eval_modelgen_ours_mid_gar: 0.0157\n    eval_modelgen_dongre_mid_gar: 0.0194\n    eval_modelgen_ppl: 1.36\n    gate_mean_final: 0.9336\n    gate_std_final: 0.0492\n- id: plan_003\n  claim: C4\n  description: Uniform Gate ablation - isolate turn conditioning contribution\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_ug_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_avg_loss: 1.0019\n    epoch0_avg_ntp: 0.9755\n    epoch0_avg_gar: 0.0259\n    epoch0_avg_div: 0.0005\n    epoch1_avg_loss: 0.9447\n    epoch1_avg_ntp: 0.9435\n    epoch1_avg_gar: 0.0013\n    epoch1_avg_div: 0\n    epoch2_avg_loss: 0.9319\n    epoch2_avg_ntp: 0.9309\n    epoch2_avg_gar: 0.001\n    epoch2_avg_div: 0\n    final_gate_mean: 0.9598\n    final_gate_std: 0.0518\n    final_gate_min: 0.7773\n    final_gate_max: 1\n    final_profile_L3: 0.777\n    final_profile_L5: 0.812\n    final_profile_L0: 0.875\n    final_profile_L27: 1\n    training_time_seconds: 21994.5\n    training_time_hours: 6.1\n    global_steps: 7950\n    unexpected_per_layer_variation: true\n    eval_modelgen_ours_mid_gar: 0.0149\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.396\n- id: plan_004\n  claim: C4\n  description: LoRA-only ablation - isolate gating mechanism contribution\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_lora_only_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    global_steps: 3000\n    training_time_seconds: 20588.6\n    training_time_hours: 5.7\n    gate_fixed: 1\n    gate_type_actual: none\n    final_lora_size_mb: 20\n    eval_modelgen_ours_mid_gar: 0.0245\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.371\n- id: plan_005\n  claim: C4\n  description: Four-way eval (Base/TG/UG/LoRA-only x GAR-ours/Dongre + PPL)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_002\n  - plan_003\n  - plan_004\n  registry_id: phase2_4way_eval\n  status: DONE\n  conclusion: negative\n  metrics:\n    base_ours_mid_gar: 0.0107\n    base_ours_recovery_pp: -0.15\n    base_dongre_mid_gar: 0.003\n    base_dongre_recovery_pp: -0.92\n    base_ppl: 4.23\n    base_ntp: 1.4162\n    tg_ours_mid_gar: 0.4866\n    tg_ours_recovery_pp: 47.44\n    tg_dongre_mid_gar: 0.0157\n    tg_dongre_recovery_pp: 0.35\n    tg_ppl: 2.63\n    tg_ntp: 0.9484\n    ug_ours_mid_gar: 0.4923\n    ug_ours_recovery_pp: 48.01\n    ug_dongre_mid_gar: 0.013\n    ug_dongre_recovery_pp: 0.08\n    ug_ppl: 2.62\n    ug_ntp: 0.9433\n    lora_ours_mid_gar: 0.486\n    lora_ours_recovery_pp: 47.39\n    lora_dongre_mid_gar: 0.0137\n    lora_dongre_recovery_pp: 0.15\n    lora_ppl: 2.63\n    lora_ntp: 0.9482\n    route_b_confirmed: true\n    gating_incremental_benefit: none\n- id: plan_006\n  claim: C3\n  description: Gradient conflict analysis on v7 (3 epoch checkpoints) - NTP vs GAR\n    gradient cos_sim + magnitude ratio\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  registry_id: analysis_gradient_conflict\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_cos_sim: -0.089\n    epoch1_cos_sim: -0.054\n    epoch2_cos_sim: -0.042\n    epoch0_neg_layers_pct: 78.6\n    epoch1_neg_layers_pct: 71.4\n    epoch2_neg_layers_pct: 67.9\n    epoch0_mag_ratio: 7.5\n    epoch1_mag_ratio: 13.7\n    epoch2_mag_ratio: 14.7\n- id: plan_007\n  claim: C3\n  description: Attention heatmap visualization (4 models x 3 conversations x 28 layers)\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  - plan_003\n  - plan_004\n  registry_id: analysis_attention_heatmap\n  status: DONE\n  conclusion: success\n  metrics:\n    base_mean_goal_attn: 0.0136\n    base_decay: 0.875\n    tg_mean_goal_attn: 0.0232\n    tg_decay: 0.777\n    ug_mean_goal_attn: 0.0216\n    ug_decay: 0.803\n    lora_mean_goal_attn: 0.0216\n    lora_decay: 0.81\n    gating_incremental_benefit: none\n- id: plan_008\n  claim: C2, C4\n  description: 'Held-out eval: create truly held-out eval set (50 convs, idx>=8000\n    from UltraChat full) and re-run 4-way eval to validate conclusions on unseen data'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  status: DONE\n  registry_id: phase2_4way_eval_heldout\n  conclusion: success\n  metrics:\n    base_ours_mid_gar: 0.0128\n    base_ours_recovery_pp: 0.06\n    base_dongre_mid_gar: 0.0031\n    base_dongre_recovery_pp: -0.91\n    base_ppl: 4.34\n    base_ntp: 1.4045\n    tg_ours_mid_gar: 0.5035\n    tg_ours_recovery_pp: 49.13\n    tg_dongre_mid_gar: 0.0152\n    tg_dongre_recovery_pp: 0.3\n    tg_ppl: 2.78\n    tg_ntp: 0.9771\n    ug_ours_mid_gar: 0.5053\n    ug_ours_recovery_pp: 49.31\n    ug_dongre_mid_gar: 0.0124\n    ug_dongre_recovery_pp: 0.02\n    ug_ppl: 2.78\n    ug_ntp: 0.9752\n    lora_ours_mid_gar: 0.4978\n    lora_ours_recovery_pp: 48.56\n    lora_dongre_mid_gar: 0.0132\n    lora_dongre_recovery_pp: 0.1\n    lora_ppl: 2.78\n    lora_ntp: 0.9771\n    three_way_convergence_confirmed: true\n    gar_ours_spread_pp: 0.75\n    ppl_spread: 0\n    data_overlap: false\n- id: plan_009\n  claim: C5\n  description: Llama-3.1-8B Phase 1 GAR degradation diagnosis - confirm GAR decay\n    exists on different architecture\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps: []\n  status: DONE\n  registry_id: llama_phase1_gar_diag\n  conclusion: success\n  metrics:\n    per_turn_gar:\n      turn_1: 0.0263\n      turn_2: 0.0183\n      turn_3: 0.0087\n      turn_4: 0.0055\n      turn_5: 0.006\n      turn_6: 0.0035\n      turn_7: 0.0038\n      turn_8: 0.0037\n      turn_9: 0.005\n      turn_10: 0.0026\n    t1_t10_decay_pct: 90.1\n    t1_mid38_drop_pct: 80.2\n    n_topics: 5\n    model: Meta-Llama-3.1-8B-Instruct\n    mode: gen\n    n_conversations: 5\n    n_turns: 10\n- id: plan_010\n  claim: C5\n  description: Llama-3.1-8B ThreadGate v7 training - replicate Qwen setup on Llama\n  priority: P0\n  gpu_budget_hours: 7\n  deps:\n  - plan_009\n  status: DONE\n  registry_id: llama_tg_s42\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    total_steps: 3000\n    wall_clock_seconds: 26212\n    wall_clock_hours: 7.28\n    final_avg_loss: 0.9233\n    final_avg_ntp: 0.9224\n    final_avg_gar: 0.0009\n    final_avg_div: 0\n    final_gate_mean: 0.9099\n    final_gate_std: 0.0701\n    final_gate_min: 0.7188\n    final_gate_max: 0.9922\n    gate_profile_step3000:\n      L0: 0.957\n      L1: 0.973\n      L2: 0.977\n      L3: 0.965\n      L4: 0.992\n      L5: 0.969\n      L6: 0.957\n      L7: 0.957\n      L8: 0.961\n      L9: 0.949\n      L10: 0.938\n      L11: 0.934\n      L12: 0.969\n      L13: 0.953\n      L14: 0.957\n      L15: 0.965\n      L16: 0.953\n      L17: 0.961\n      L18: 0.922\n      L19: 0.902\n      L20: 0.883\n      L21: 0.863\n      L22: 0.836\n      L23: 0.844\n      L24: 0.809\n      L25: 0.719\n      L26: 0.762\n      L27: 0.805\n      L28: 0.801\n      L29: 0.855\n      L30: 0.898\n      L31: 0.934\n    checkpoint_size_gate_mb: 4.2\n    checkpoint_size_lora_mb: 26\n    gpu: NVIDIA RTX PRO 6000 Blackwell\n    vram_gb: 102\n    mem_used_gb: 63.4\n- id: plan_011\n  claim: C5\n  description: Llama-3.1-8B LoRA-only training - cross-model gating redundancy validation\n    (D020)\n  priority: P0\n  gpu_budget_hours: 7\n  deps:\n  - plan_009\n  status: DONE\n  registry_id: llama_lora_only_s42\n  conclusion: success\n  metrics:\n    final_avg_loss: 0.9288\n    final_avg_ntp: 0.9279\n    final_avg_gar: 0.0009\n    gate_fixed: 1\n    gate_type: none\n    wall_clock_s: 25317\n    wall_clock_h: 7.03\n    epochs_completed: 3\n- id: plan_012\n  claim: C5\n  description: Llama-3.1-8B 3-way eval (Base/TG/LoRA-only x GAR + PPL) on held-out\n    data\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_010\n  - plan_011\n  status: DONE\n  registry_id: llama_eval_s42\n  conclusion: success\n  metrics:\n    tf_base:\n      gar_ours: 0.0166\n      ngar_ours: 0.3882\n      gar_dongre: 0.0038\n      ngar_dongre: 0.163\n      ppl: 3.45\n      N: 50\n      T: 4\n    tf_tg:\n      gar_ours: 0.4836\n      ngar_ours: 11.8818\n      gar_dongre: 0.018\n      ngar_dongre: 0.7922\n      ppl: 2.57\n      N: 50\n      T: 4\n    ar_base:\n      gar_ours: 0.0086\n      ngar_ours: 0.0798\n      gar_dongre: 0.0118\n      ngar_dongre: 0.1265\n      ppl: 1.24\n      N: 5\n      T: 10\n    ar_tg:\n      gar_ours: 0.0304\n      ngar_ours: 0.2632\n      gar_dongre: 0.0217\n      ngar_dongre: 0.2459\n      ppl: 1.32\n      N: 5\n      T: 10\n    gap_ratio_tg_ours: 15.9\n    gap_ratio_base_ours: 1.93\n    gap_ratio_tg_dongre: 0.83\n    vs_qwen_v7_gap_ratio: 32.1\n    baseline_mid_gar: 0.0122\n- id: plan_013\n  claim: C3\n  description: Llama-3.1-8B gradient conflict analysis - verify NTP-GAR competition\n    is model-agnostic\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_010\n  status: planned\n  result: 'cos_sim=0.0045 (near-orthogonal, not conflict), neg_layers=53.1% (near\n    random), mag_ratio_median=25.7×. Cross-model confirms: gradients not conflicting,\n    NTP magnitude dominates. Consistent with Qwen. D054.'\n- id: plan_014\n  claim: W3\n  description: Downstream task sanity check - simple instruction retention test across\n    turns to link GAR to task performance\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_005\n  status: DONE\n  registry_id: instruction_retention_test\n  result: β=3 late-turn retention 87.0% vs β=0 75.9%, delta=+11.1pp. GAR-compliance\n    correlation r=0.200, p=0.007. Written to Appendix C. D046.\n  conclusion: success\n  metrics:\n    late_turn_rate_beta0: 0.759\n    late_turn_rate_beta3: 0.87\n    late_turn_delta: 0.111\n    mcnemar_chi2: 3.125\n    mcnemar_p: 0.0771\n    gar_compliance_r: 0.2003\n    gar_compliance_p: 0.007\n    category_content_constraint:\n      beta0: 0.619\n      beta3: 0.857\n      delta: 0.238\n    category_count_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_format_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_position_constraint:\n      beta0: 0.667\n      beta3: 0.733\n      delta: 0.067\n- id: plan_015\n  claim: C4, W7\n  description: Statistical significance analysis - paired bootstrap CI from held-out\n    eval (50 convs) for TG-LoRA-only comparison. If CI includes 0 → statistically\n    supports 'zero benefit'. Addresses Dream W3 (single seed).\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_008\n  status: orphaned\n  registry_id: worker_analysis_bootstrap_ci_tg_vs_lora_20260519T144212\n  result: 'PASS: All GAR-ours and PPL 95% CIs include 0 (TG-LO GAR: [-0.0018,+0.0036],\n    UG-LO: [-0.0006,+0.0045], TG-UG: [-0.0030,+0.0006]). Statistically confirms zero\n    benefit. W7 addressed.'\n- id: plan_016\n  claim: W8\n  description: Exposure-bias mitigation test - train ThreadGate v7 with scheduled\n    sampling applied to GAR loss (mix teacher-forced + model-generated contexts).\n    Test whether closing exposure bias gap narrows the 30x training-inference GAR\n    gap. Constructive direction that upgrades paper from pure negative result.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_008\n  status: DONE\n  registry_id: phase2_tg_s42_v8_schedsampling\n  conclusion: failed\n  metrics:\n    killed_at_microstep: 1950\n    total_microsteps: 24000\n    completion_pct: 8.1\n    global_step_approx: 244\n    total_global_steps: 3000\n    ss_steps_observed: 1\n    tf_lgar_mean_step850_1400: 0.0062\n    tf_lgar_std: 0.0082\n    tf_lgar_collapse_step: 800\n    gate_mean_final: 0.93\n    ss_ratio_at_kill: 0.081\n    crash_reason: 'killed by director: SS path code bug (D026) makes experiment invalid,\n      GPU needed for PCGrad'\n    design_flaw_ss_ramp_too_slow: true\n    design_flaw_no_ss_tf_separate_logging: true\n- id: plan_017\n  claim: R4\n  description: Code-paper architecture verification - confirm ThreadGate implementation\n    matches paper Eq.3 (gate on residual vs gate on sub-layer output). Quick code\n    audit, no GPU.\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: orphaned\n  registry_id: worker_analysis_code_paper_arch_verify_20260519T144058\n  result: 'CRITICAL: code implements x+g·f(x) (ReZero-style), dream paper.tex wrote\n    g·x+f(x). Semantically opposite when g→0. Data unaffected. D023.'\n- id: plan_018\n  claim: C3, W8\n  description: PCGrad baseline - project NTP gradient onto GAR-orthogonal plane for\n    gate params only. If 30x gap persists after removing gradient conflict → causal\n    evidence that exposure bias (not gradient competition) is the root cause.\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_006\n  registry_id: phase2_tg_s42_v9_pcgrad\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5002\n    eval_iid_dongre_mid_gar: 0.0123\n    eval_iid_ppl: 2.78\n    eval_iid_ntp: 0.9752\n    eval_heldout_ours_mid_gar: 0.5002\n    eval_heldout_dongre_mid_gar: 0.0123\n    eval_heldout_ppl: 2.78\n    eval_heldout_ntp: 0.9752\n    eval_modelgen_ours_mid_gar: 0.0151\n    eval_modelgen_dongre_mid_gar: 0.0173\n    eval_modelgen_ppl: 1.5\n    vs_v7_iid_ppl_diff: 0.004\n    vs_v7_iid_gar_diff: -0.0033\n- id: plan_019\n  claim: C2, MF5\n  description: Multi-seed validation — train TG v7 + LoRA-only with seed=123 on Qwen.\n    Provide mean±std for 30x gap. 1 extra seed sufficient given extreme effect size.\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_002\n  status: DONE\n  registry_id: v7_tg_s123\n  conclusion: success\n  metrics:\n    epoch_1:\n      avg_loss: 0.9447\n      avg_ntp_loss: 0.9434\n      avg_gar_loss: 0.0013\n      avg_div_loss: 0\n    epoch_2:\n      avg_loss: 0.9315\n      avg_ntp_loss: 0.9305\n      avg_gar_loss: 0.001\n      avg_div_loss: 0\n    final_gate:\n      mean: 0.9467\n      std: 0.051\n      min: 0.793\n      max: 1\n    final_gate_profile:\n      L0: 0.883\n      L1: 0.793\n      L2: 0.996\n      L3: 0.988\n      L4: 0.984\n      L5: 0.797\n      L6: 0.961\n      L7: 0.918\n      L8: 0.965\n      L9: 0.934\n      L10: 0.969\n      L11: 0.918\n      L12: 0.926\n      L13: 0.941\n      L14: 0.93\n      L15: 0.965\n      L16: 0.941\n      L17: 0.91\n      L18: 0.961\n      L19: 0.965\n      L20: 0.973\n      L21: 0.988\n      L22: 0.969\n      L23: 0.98\n      L24: 0.98\n      L25: 0.984\n      L26: 0.988\n      L27: 1\n    training_time_s: 21425.2\n- id: plan_020\n  claim: C4, MF6\n  description: Expanded eval set — increase from 50 to 200 conversations (idx>=7000\n    from UltraChat). Boost bootstrap CI statistical power.\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  status: planned\n  result: 'Partially done: TF eval uses eval_200 (N=200), AR eval uses d048_final_ar\n    (N=50). AR N=200 not planned — N=50 sufficient given extreme effect sizes. No\n    additional GPU needed.'\n- id: plan_022\n  claim: C3, SF4\n  description: λ_GAR sensitivity — train v7 with λ_GAR=10 (1 epoch only). Show gradient\n    competition trend under higher GAR weight. If budget allows, add λ=0.1.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_002\n  status: planned\n- id: plan_023\n  claim: W8, C3\n  description: 'v8b: Fixed Scheduled Sampling — fix compute_gar_loss len==1 bug (Option\n    A: handle single-turn mse_target), fix OOM (reduce batch/gen_length), use lambda_gar=1.0\n    (match v7). Tests whether training on model-generated text closes the 30x distribution\n    shift gap. If successful, paper upgrades from pure negative to ''diagnosis + initial\n    remedy''. D026.'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  status: DONE\n  registry_id: phase2_tg_s42_v8b_resume\n  conclusion: success\n  metrics:\n    training:\n      total_steps: 3000\n      epochs_completed: 3\n      wall_clock_hours: 8.1\n      final_loss: 0.933\n      final_ntp_loss: 0.9322\n      final_gar_loss: 0.0008\n      final_gate_mean: 0.9586\n      final_gate_std: 0.0582\n      ss_ratio: 0.5\n    eval_iid:\n      gar_ours: 0.4983\n      gar_dongre: 0.3855\n      ppl: 2.78\n    eval_modelgen:\n      gar_ours: 0.3177\n      gar_dongre: 0.3533\n      ppl: 1.38\n    vs_v7:\n      iid_gar_ours_delta: -0.005\n      modelgen_gar_ours_delta: 0.302\n      gap_ratio_v7: 32\n      gap_ratio_v8b: 1.57\n- id: plan_024\n  claim: C4\n  description: 'SS + β-steering combined eval — CANCELLED. Data already exists in\n    ss_s42_ar_n50.json (β=0,3,5). SS and steering are substitutes not complements\n    (β=5: SS 0.717 ≈ TG 0.727). No need to re-run.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_023\n  status: PREPARING\n  registry_id: p0_ss_steering_eval\n  result: 'Cancelled — existing data shows SS+steering do not stack. β=0: SS 0.347\n    (independent value). β=3: SS +0.037 marginal. β=5: SS ≈ TG (converge). Discussion\n    added to paper.'\n  conclusion: killed\n- id: plan_025\n  claim: C1\n  description: TF vs AR attention KL divergence — compute per-head KL(P_TF||P_AR)\n    on 50 conversations to quantify attention distribution shift. If GAR-relevant\n    heads show larger KL → mechanistic evidence for why GAR collapses. Pure CPU analysis.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_026\n  claim: C5, C4\n  description: Llama-3.1-8B Scheduled Sampling — replicate SS training on Llama to\n    verify cross-model gap compression. If Llama gap also compresses → SS is a general\n    mitigation, not model-specific.\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_010\n  status: planned\n- id: plan_027\n  claim: C4, W7\n  description: 'SS 3-seed validation — s42 (gap 1.45×), s123 (TF NaN, AR 0.423), s456\n    (gap 1.15×). 3-seed AR GAR β=0: 0.401±0.047. β=3/5 extremely stable (std<0.01).\n    Addresses single-seed reviewer concern.'\n  priority: P0\n  gpu_budget_hours: 16\n  deps:\n  - plan_023\n  status: planned\n  result: '3-seed complete. TF GAR 0.498±0.004 (s42=0.503, s123=0.495, s456=0.496).\n    AR GAR β=0: 0.401±0.047 (s42=0.347, s123=0.423, s456=0.433). Gap 1.26±0.17 (range\n    1.15–1.45×, 3 valid seeds). β=3: 0.596±0.008. β=5: 0.717±0.001. PPL β=0: 1.441±0.001.\n    W7 addressed.'\n- id: plan_028\n  claim: C2, W5\n  description: Alternative GAR definition robustness — 4 token selections (last/all/first/goal-only)\n    × 3 checkpoints (Base/TG/SS). Needed GPU re-eval (raw attention not saved).\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_027\n  status: planned\n  result: TG only improves last-token GAR (0.325), all/first-token near-zero (0.025/0.039).\n    SS improves ALL 4 definitions >0.36. SS builds broader goal-attention pattern,\n    not position-specific overfitting. Base consistently <0.022. D054.\n- id: plan_029\n  claim: C2, W7\n  description: SS 4th seed (s789) — additional seed to strengthen mean±std. Training\n    ~6.5h + eval ~1h. ROI lower than Llama SS (cross-model > extra seed given extreme\n    effect size). Run if time permits after plan_026.\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_027\n  status: planned\n- id: plan_030\n  claim: C1, C2\n  description: Long conversation eval (>10 turns) — test whether exposure bias gap\n    worsens with conversation length. Need to identify suitable long conversations\n    from UltraChat. Eval ~1-2h.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_027\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: phase1_gar_diag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    turn1_avg_gar: 0.0418\n    mid_turns_avg_gar: 0.0122\n    relative_drop: 0.708\n    num_conversations: 5\n    num_turns: 10\n    per_turn_avg_gar:\n    - 0.0418\n    - 0.0241\n    - 0.0224\n    - 0.013\n    - 0.0133\n    - 0.0086\n    - 0.0078\n    - 0.008\n    - 0.0157\n    - 0.0064\n- exp_id: phase2_tg_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_ntp_loss: 0.94\n    final_gar_loss: 0\n    gate_mean: 0.988\n    gar_loss_zero_pct: 87.6\n    epochs_completed: 1.67\n    killed_reason: SIGTERM by diagnose worker (unauthorized)\n- exp_id: phase2_ug_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_avg_loss: 1.0019\n    epoch0_avg_ntp: 0.9755\n    epoch0_avg_gar: 0.0259\n    epoch0_avg_div: 0.0005\n    epoch1_avg_loss: 0.9447\n    epoch1_avg_ntp: 0.9435\n    epoch1_avg_gar: 0.0013\n    epoch1_avg_div: 0\n    epoch2_avg_loss: 0.9319\n    epoch2_avg_ntp: 0.9309\n    epoch2_avg_gar: 0.001\n    epoch2_avg_div: 0\n    final_gate_mean: 0.9598\n    final_gate_std: 0.0518\n    final_gate_min: 0.7773\n    final_gate_max: 1\n    final_profile_L3: 0.777\n    final_profile_L5: 0.812\n    final_profile_L0: 0.875\n    final_profile_L27: 1\n    training_time_seconds: 21994.5\n    training_time_hours: 6.1\n    global_steps: 7950\n    unexpected_per_layer_variation: true\n    eval_modelgen_ours_mid_gar: 0.0149\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.396\n- exp_id: phase2_tg_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_tg_s42_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    gate_mean_step0: 0.8743\n    gate_mean_step500: 0.8761\n    gate_delta: 0.004\n    gate_std: 0.001\n    final_ntp_loss: 0.94\n    final_gar_loss: -0.019\n    gar_contribution_pct: 2-4%\n    diagnosis: gate frozen, GAR indirect gradient too weak\n- exp_id: phase2_tg_s42_v3b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gate_std_final: 0.087\n    gate_mean_final: 0.9388\n    gate_min_final: 0.5352\n    gate_max_final: 0.9922\n    L4_gate: 0.535\n    L0_gate: 0.777\n    L_NTP_final: 0.7787\n    L_GAR_final: -0.9606\n    elapsed_seconds: 3565.9\n    optimizer_steps: 500\n    gate_grad_received: true\n- exp_id: phase2_tg_s42_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: phase2_tg_s42_v5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step2000_gate_std: 0.0225\n    step2000_gate_mean: 0.9586\n    step2000_gate_min: 0.9062\n    step2000_gate_max: 0.9961\n    step2000_L_GAR: -0.8977\n    step2000_L_NTP: 0.7611\n    step2000_total_loss: -0.1365\n    step2400_gate_std: 0.0219\n    step2400_gate_mean: 0.9651\n    step2400_gate_min: 0.918\n    step2400_gate_max: 0.9961\n    step2400_profile: L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\n    L_GAR_saturated_at: -0.91\n    gate_range_compression: 0.918-0.996\n- exp_id: phase2_tg_s42_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    dryrun_step0_L_NTP: 2.0275\n    dryrun_step0_L_GAR: -0.0161\n    dryrun_step0_total_loss: 2.0114\n    dryrun_step4_L_NTP: 1.6544\n    dryrun_step4_L_GAR: -0.0147\n    dryrun_step4_total_loss: 1.6397\n    dryrun_gate_grad: true\n    dryrun_gate_mean_init: 0.8097\n    dryrun_gate_std_init: 0.0341\n    dryrun_gate_min_init: 0.6836\n    dryrun_gate_max_init: 0.8672\n    dryrun_gate_mean_step5: 0.8025\n    dryrun_gate_std_step5: 0.0842\n    dryrun_gate_min_step5: 0.5547\n    dryrun_gate_max_step5: 0.9805\n    gs50_gate_mean: 0.8117\n    gs50_gate_std: 0.0612\n    gs50_gate_min: 0.6836\n    gs50_gate_max: 0.9805\n    gs100_gate_mean: 0.8737\n    gs100_gate_std: 0.0367\n    gs100_gate_min: 0.8164\n    gs100_gate_max: 0.9766\n    gs100_L_NTP: 0.8151\n    gs100_L_GAR: -0.158\n    gs100_total_loss: 0.6571\n    gs100_profile_bottom3: L12=0.816 L4=0.824 L13=0.824\n    gs100_profile_top3: L27=0.977 L26=0.961 L23=0.914\n    gs143_L_GAR: -0.3876\n    gs143_gate_mean: 0.9227\n- exp_id: phase2_tg_s42_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5035\n    eval_iid_dongre_mid_gar: 0.0152\n    eval_iid_ppl: 2.784\n    eval_heldout_ours_mid_gar: 0.5035\n    eval_heldout_dongre_mid_gar: 0.0152\n    eval_heldout_ppl: 2.78\n    eval_modelgen_ours_mid_gar: 0.0157\n    eval_modelgen_dongre_mid_gar: 0.0194\n    eval_modelgen_ppl: 1.36\n    gate_mean_final: 0.9336\n    gate_std_final: 0.0492\n- exp_id: phase2_lora_only_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    global_steps: 3000\n    training_time_seconds: 20588.6\n    training_time_hours: 5.7\n    gate_fixed: 1\n    gate_type_actual: none\n    final_lora_size_mb: 20\n    eval_modelgen_ours_mid_gar: 0.0245\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.371\n- exp_id: phase2_4way_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    base_ours_mid_gar: 0.0107\n    base_ours_recovery_pp: -0.15\n    base_dongre_mid_gar: 0.003\n    base_dongre_recovery_pp: -0.92\n    base_ppl: 4.23\n    base_ntp: 1.4162\n    tg_ours_mid_gar: 0.4866\n    tg_ours_recovery_pp: 47.44\n    tg_dongre_mid_gar: 0.0157\n    tg_dongre_recovery_pp: 0.35\n    tg_ppl: 2.63\n    tg_ntp: 0.9484\n    ug_ours_mid_gar: 0.4923\n    ug_ours_recovery_pp: 48.01\n    ug_dongre_mid_gar: 0.013\n    ug_dongre_recovery_pp: 0.08\n    ug_ppl: 2.62\n    ug_ntp: 0.9433\n    lora_ours_mid_gar: 0.486\n    lora_ours_recovery_pp: 47.39\n    lora_dongre_mid_gar: 0.0137\n    lora_dongre_recovery_pp: 0.15\n    lora_ppl: 2.63\n    lora_ntp: 0.9482\n    route_b_confirmed: true\n    gating_incremental_benefit: none\n- exp_id: phase2_4way_eval_heldout\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base_ours_mid_gar: 0.0128\n    base_ours_recovery_pp: 0.06\n    base_dongre_mid_gar: 0.0031\n    base_dongre_recovery_pp: -0.91\n    base_ppl: 4.34\n    base_ntp: 1.4045\n    tg_ours_mid_gar: 0.5035\n    tg_ours_recovery_pp: 49.13\n    tg_dongre_mid_gar: 0.0152\n    tg_dongre_recovery_pp: 0.3\n    tg_ppl: 2.78\n    tg_ntp: 0.9771\n    ug_ours_mid_gar: 0.5053\n    ug_ours_recovery_pp: 49.31\n    ug_dongre_mid_gar: 0.0124\n    ug_dongre_recovery_pp: 0.02\n    ug_ppl: 2.78\n    ug_ntp: 0.9752\n    lora_ours_mid_gar: 0.4978\n    lora_ours_recovery_pp: 48.56\n    lora_dongre_mid_gar: 0.0132\n    lora_dongre_recovery_pp: 0.1\n    lora_ppl: 2.78\n    lora_ntp: 0.9771\n    three_way_convergence_confirmed: true\n    gar_ours_spread_pp: 0.75\n    ppl_spread: 0\n    data_overlap: false\n- exp_id: phase2_tg_s42_v8_schedsampling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    killed_at_microstep: 1950\n    total_microsteps: 24000\n    completion_pct: 8.1\n    global_step_approx: 244\n    total_global_steps: 3000\n    ss_steps_observed: 1\n    tf_lgar_mean_step850_1400: 0.0062\n    tf_lgar_std: 0.0082\n    tf_lgar_collapse_step: 800\n    gate_mean_final: 0.93\n    ss_ratio_at_kill: 0.081\n    crash_reason: 'killed by director: SS path code bug (D026) makes experiment invalid,\n      GPU needed for PCGrad'\n    design_flaw_ss_ramp_too_slow: true\n    design_flaw_no_ss_tf_separate_logging: true\n- exp_id: analysis_gradient_conflict\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_cos_sim: -0.089\n    epoch1_cos_sim: -0.054\n    epoch2_cos_sim: -0.042\n    epoch0_neg_layers_pct: 78.6\n    epoch1_neg_layers_pct: 71.4\n    epoch2_neg_layers_pct: 67.9\n    epoch0_mag_ratio: 7.5\n    epoch1_mag_ratio: 13.7\n    epoch2_mag_ratio: 14.7\n- exp_id: analysis_attention_heatmap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base_mean_goal_attn: 0.0136\n    base_decay: 0.875\n    tg_mean_goal_attn: 0.0232\n    tg_decay: 0.777\n    ug_mean_goal_attn: 0.0216\n    ug_decay: 0.803\n    lora_mean_goal_attn: 0.0216\n    lora_decay: 0.81\n    gating_incremental_benefit: none\n- exp_id: phase2_tg_s42_v9_pcgrad\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5002\n    eval_iid_dongre_mid_gar: 0.0123\n    eval_iid_ppl: 2.78\n    eval_iid_ntp: 0.9752\n    eval_heldout_ours_mid_gar: 0.5002\n    eval_heldout_dongre_mid_gar: 0.0123\n    eval_heldout_ppl: 2.78\n    eval_heldout_ntp: 0.9752\n    eval_modelgen_ours_mid_gar: 0.0151\n    eval_modelgen_dongre_mid_gar: 0.0173\n    eval_modelgen_ppl: 1.5\n    vs_v7_iid_ppl_diff: 0.004\n    vs_v7_iid_gar_diff: -0.0033\n- exp_id: phase2_tg_s42_v8b_ss_fixed\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: attention_steering_v7_tg_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beta_0.0:\n      mid_turns_avg_gar: 0.028\n      avg_ppl: 1.409\n    beta_0.5:\n      mid_turns_avg_gar: 0.0287\n      avg_ppl: 1.387\n    beta_1.0:\n      mid_turns_avg_gar: 0.0349\n      avg_ppl: 1.36\n    beta_2.0:\n      mid_turns_avg_gar: 0.062\n      avg_ppl: 1.411\n    beta_5.0:\n      mid_turns_avg_gar: 0.6795\n      avg_ppl: 1.908\n    beta_10.0:\n      mid_turns_avg_gar: 0.959\n      avg_ppl: 4.22\n    phase_transition_range: '[2, 5]'\n    baseline_gar: 0.028\n    max_gar_at_acceptable_ppl: 0.6795\n    max_gar_at_acceptable_ppl_beta: 5\n- exp_id: trc_baseline_v7_tg\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v7_tg:\n      tf_trc: 0.3339\n      gen_trc: 0.3323\n      trc_gap: 0.0016\n      tf_tbp_ppl: 1.05\n      gen_tbp_ppl: 1.05\n    lora_only:\n      tf_trc: 0.349\n      gen_trc: 0.4106\n      trc_gap: -0.0617\n      tf_tbp_ppl: 9.5\n      gen_tbp_ppl: 12\n    base:\n      tf_trc: 0.1494\n      gen_trc: 0.1494\n      trc_gap: 0\n      tf_tbp_ppl: 2.05\n      gen_tbp_ppl: 2.05\n- exp_id: attention_steering_eval200_tf\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beta_0.0:\n      mid_gar: 0.5353\n      ppl: 2.62\n    beta_2.0:\n      mid_gar: 0.6112\n      ppl: 2.69\n    beta_3.0:\n      mid_gar: 0.788\n      ppl: 2.93\n    beta_4.0:\n      mid_gar: 0.8165\n      ppl: 3.49\n    beta_5.0:\n      mid_gar: 0.8325\n      ppl: 6.15\n    beta_10.0:\n      mid_gar: 0.977\n      ppl: 505.21\n    n_convs: 200\n    mode: tf\n- exp_id: phase2_tg_s42_v8b_resume\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training:\n      total_steps: 3000\n      epochs_completed: 3\n      wall_clock_hours: 8.1\n      final_loss: 0.933\n      final_ntp_loss: 0.9322\n      final_gar_loss: 0.0008\n      final_gate_mean: 0.9586\n      final_gate_std: 0.0582\n      ss_ratio: 0.5\n    eval_iid:\n      gar_ours: 0.4983\n      gar_dongre: 0.3855\n      ppl: 2.78\n    eval_modelgen:\n      gar_ours: 0.3177\n      gar_dongre: 0.3533\n      ppl: 1.38\n    vs_v7:\n      iid_gar_ours_delta: -0.005\n      modelgen_gar_ours_delta: 0.302\n      gap_ratio_v7: 32\n      gap_ratio_v8b: 1.57\n- exp_id: eval_v8b_ss\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    iid_gar_ours: 0.4983\n    iid_gar_dongre: 0.3855\n    iid_ppl: 2.78\n    iid_ngar_ours: 13.5\n    iid_ngar_dongre: 22.68\n    modelgen_gar_ours: 0.3177\n    modelgen_gar_dongre: 0.3533\n    modelgen_ppl: 1.38\n    modelgen_ngar_ours: 4.47\n    modelgen_ngar_dongre: 5.92\n    iid_turn1_gar_ours: 0.5398\n    modelgen_turn1_gar_ours: 0.4333\n- exp_id: attention_steering_gen_n50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    corrected: true\n    aggregation: per-conv mid_gar(turns 2-7), >=3 turns only\n    beta_0.0:\n      mid_gar: 0.0641\n      mid_gar_std: 0.0809\n      ppl: 1.4324\n      ppl_std: 0.1029\n      n_valid: 39\n    beta_2.0:\n      mid_gar: 0.128\n      mid_gar_std: 0.1101\n      ppl: 1.4822\n      ppl_std: 0.1385\n      n_valid: 39\n    beta_3.0:\n      mid_gar: 0.5558\n      mid_gar_std: 0.0601\n      ppl: 1.5605\n      ppl_std: 0.1719\n      n_valid: 39\n    beta_4.0:\n      mid_gar: 0.6439\n      mid_gar_std: 0.0607\n      ppl: 1.6674\n      ppl_std: 0.2241\n      n_valid: 39\n    beta_5.0:\n      mid_gar: 0.7271\n      mid_gar_std: 0.0605\n      ppl: 1.7723\n      ppl_std: 0.2693\n      n_valid: 38\n    beta_10.0:\n      mid_gar: 0.9612\n      mid_gar_std: 0.0152\n      ppl: 3.4517\n      ppl_std: 1.7813\n      n_valid: 39\n    n_convs_total: 50\n    n_convs_valid: 39\n    mode: gen\n    phase_transition_range: '[2, 3]'\n- exp_id: llama_phase1_gar_diag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_turn_gar:\n      turn_1: 0.0263\n      turn_2: 0.0183\n      turn_3: 0.0087\n      turn_4: 0.0055\n      turn_5: 0.006\n      turn_6: 0.0035\n      turn_7: 0.0038\n      turn_8: 0.0037\n      turn_9: 0.005\n      turn_10: 0.0026\n    t1_t10_decay_pct: 90.1\n    t1_mid38_drop_pct: 80.2\n    n_topics: 5\n    model: Meta-Llama-3.1-8B-Instruct\n    mode: gen\n    n_conversations: 5\n    n_turns: 10\n- exp_id: llama_tg_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    total_steps: 3000\n    wall_clock_seconds: 26212\n    wall_clock_hours: 7.28\n    final_avg_loss: 0.9233\n    final_avg_ntp: 0.9224\n    final_avg_gar: 0.0009\n    final_avg_div: 0\n    final_gate_mean: 0.9099\n    final_gate_std: 0.0701\n    final_gate_min: 0.7188\n    final_gate_max: 0.9922\n    gate_profile_step3000:\n      L0: 0.957\n      L1: 0.973\n      L2: 0.977\n      L3: 0.965\n      L4: 0.992\n      L5: 0.969\n      L6: 0.957\n      L7: 0.957\n      L8: 0.961\n      L9: 0.949\n      L10: 0.938\n      L11: 0.934\n      L12: 0.969\n      L13: 0.953\n      L14: 0.957\n      L15: 0.965\n      L16: 0.953\n      L17: 0.961\n      L18: 0.922\n      L19: 0.902\n      L20: 0.883\n      L21: 0.863\n      L22: 0.836\n      L23: 0.844\n      L24: 0.809\n      L25: 0.719\n      L26: 0.762\n      L27: 0.805\n      L28: 0.801\n      L29: 0.855\n      L30: 0.898\n      L31: 0.934\n    checkpoint_size_gate_mb: 4.2\n    checkpoint_size_lora_mb: 26\n    gpu: NVIDIA RTX PRO 6000 Blackwell\n    vram_gb: 102\n    mem_used_gb: 63.4\n- exp_id: llama_eval_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf_base:\n      gar_ours: 0.0166\n      ngar_ours: 0.3882\n      gar_dongre: 0.0038\n      ngar_dongre: 0.163\n      ppl: 3.45\n      N: 50\n      T: 4\n    tf_tg:\n      gar_ours: 0.4836\n      ngar_ours: 11.8818\n      gar_dongre: 0.018\n      ngar_dongre: 0.7922\n      ppl: 2.57\n      N: 50\n      T: 4\n    ar_base:\n      gar_ours: 0.0086\n      ngar_ours: 0.0798\n      gar_dongre: 0.0118\n      ngar_dongre: 0.1265\n      ppl: 1.24\n      N: 5\n      T: 10\n    ar_tg:\n      gar_ours: 0.0304\n      ngar_ours: 0.2632\n      gar_dongre: 0.0217\n      ngar_dongre: 0.2459\n      ppl: 1.32\n      N: 5\n      T: 10\n    gap_ratio_tg_ours: 15.9\n    gap_ratio_base_ours: 1.93\n    gap_ratio_tg_dongre: 0.83\n    vs_qwen_v7_gap_ratio: 32.1\n    baseline_mid_gar: 0.0122\n- exp_id: llama_tg_training\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: instruction_retention_test\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    late_turn_rate_beta0: 0.759\n    late_turn_rate_beta3: 0.87\n    late_turn_delta: 0.111\n    mcnemar_chi2: 3.125\n    mcnemar_p: 0.0771\n    gar_compliance_r: 0.2003\n    gar_compliance_p: 0.007\n    category_content_constraint:\n      beta0: 0.619\n      beta3: 0.857\n      delta: 0.238\n    category_count_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_format_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_position_constraint:\n      beta0: 0.667\n      beta3: 0.733\n      delta: 0.067\n- exp_id: llama_ar_matched_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ar_base_ours:\n      mid_gar: 0.0082\n      ngar: 0.1\n      ppl: 1.267\n    ar_tg_ours:\n      mid_gar: 0.0388\n      ngar: 0.493\n      ppl: 1.413\n    ar_base_dongre:\n      mid_gar: 0.0051\n      ngar: 0.12\n      ppl: 1.267\n    ar_tg_dongre:\n      mid_gar: 0.018\n      ngar: 0.431\n      ppl: 1.413\n    tf_reference:\n      tf_tg_ours_ngar: 11.88\n      tf_base_ours_ngar: 0.388\n      tf_tg_ours_raw: 0.4836\n      tf_tg_dongre_raw: 0.018\n    matched_gap_analysis:\n      gar_ours_raw_gap: 12.5x (TF 0.484 / AR 0.039)\n      gar_ours_ngar_gap: 24.1x (TF 11.88 / AR 0.493)\n      gar_dongre_raw_gap: 1.002x (TF 0.018 / AR 0.018) — zero gap\n      tg_over_base_ar_ours: 4.71x\n      tg_over_base_ar_dongre: 3.54x\n      conclusion: 'GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure\n        bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure\n        bias selectively destroys learned goal-attention routing while leaving content-overlap-based\n        attention unaffected.'\n- exp_id: v8b_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.9316\n    final_ntp_loss: 0.9307\n    final_gar_loss: 0.0009\n    final_gate_mean: 0.9505\n    final_gate_std: 0.0508\n    final_gate_min: 0.7383\n    final_gate_max: 1\n    ss_used_ratio: 0.371\n    training_time_s: 38773.4\n    epoch0_loss: 1.0092\n    epoch1_loss: 0.9444\n    epoch2_loss: 0.9316\n- exp_id: v7_tg_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch_1:\n      avg_loss: 0.9447\n      avg_ntp_loss: 0.9434\n      avg_gar_loss: 0.0013\n      avg_div_loss: 0\n    epoch_2:\n      avg_loss: 0.9315\n      avg_ntp_loss: 0.9305\n      avg_gar_loss: 0.001\n      avg_div_loss: 0\n    final_gate:\n      mean: 0.9467\n      std: 0.051\n      min: 0.793\n      max: 1\n    final_gate_profile:\n      L0: 0.883\n      L1: 0.793\n      L2: 0.996\n      L3: 0.988\n      L4: 0.984\n      L5: 0.797\n      L6: 0.961\n      L7: 0.918\n      L8: 0.965\n      L9: 0.934\n      L10: 0.969\n      L11: 0.918\n      L12: 0.926\n      L13: 0.941\n      L14: 0.93\n      L15: 0.965\n      L16: 0.941\n      L17: 0.91\n      L18: 0.961\n      L19: 0.965\n      L20: 0.973\n      L21: 0.988\n      L22: 0.969\n      L23: 0.98\n      L24: 0.98\n      L25: 0.984\n      L26: 0.988\n      L27: 1\n    training_time_s: 21425.2\n- exp_id: eval_v8b_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    iid:\n      gar_ours: 0.503\n      gar_dongre: 0.394\n      ppl: 2.781\n      ntp_loss: 0.976\n      n_conv: 50\n      n_turns: 3\n    modelgen:\n      gar_ours: 0.418\n      gar_dongre: 0.441\n      ppl: 1.389\n      ntp_loss: 0.325\n      n_conv: 5\n      n_turns: 10\n    gap_ratio: 1.2\n    base_iid_ppl: 4.338\n    base_modelgen_ppl: 1.351\n- exp_id: eval_v7_tg_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    iid_tf:\n      gar_ours_mid: 0.5052\n      gar_dongre_mid: 0.0119\n      ppl: 2.7802\n      ntp: 0.9752\n    modelgen_ar:\n      gar_ours_mid: 0.0165\n      gar_dongre_mid: 0.0177\n      ppl: 1.3855\n      ntp: 0.3223\n    gap_ratio: 30.6\n    comparison_s42:\n      tf_gar_ours_delta: 0.0017\n      ar_gar_ours_delta: 0.0008\n      gap_ratio_delta: -1.4\n- exp_id: llama_lora_only_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_avg_loss: 0.9288\n    final_avg_ntp: 0.9279\n    final_avg_gar: 0.0009\n    gate_fixed: 1\n    gate_type: none\n    wall_clock_s: 25317\n    wall_clock_h: 7.03\n    epochs_completed: 3\n- exp_id: eval_llama_lora_only_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf:\n      gar_ours: 0.4807\n      gar_dongre: 0.0188\n      ngar_ours: 11.8031\n      ngar_dongre: 0.8261\n      ppl: 2.6\n      ntp_loss: 0.9366\n      n_conversations: 50\n      n_turns: 4\n    ar:\n      gar_ours: 0.0617\n      gar_dongre: 0.0226\n      ngar_ours: 0.6065\n      ngar_dongre: 0.2537\n      ppl: 1.32\n      ntp_loss: 0.2787\n      n_conversations: 5\n      n_turns: 10\n    gap_ratio_gar_ours: 7.79\n- exp_id: eval_llama_ar_n20\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base:\n      gar_ours_mean: 0.0088\n      gar_ours_std: 0.0056\n      gar_ours_median_per_conv: 0.0093\n      gar_ours_median_per_turn_pool: 0.0071\n      gar_ours_spike_ratio: 0%\n      gar_dongre_mean: 0.0049\n      gar_dongre_std: 0.0013\n      gar_dongre_median: 0.0047\n      ngar_ours_mid: 0.1019\n      ngar_dongre_mid: 0.1171\n      ppl: 1.293\n      ppl_std: 0.07\n      ntp_loss: 0.2552\n    tg:\n      gar_ours_mean: 0.0434\n      gar_ours_std: 0.1002\n      gar_ours_median_per_conv: 0.0179\n      gar_ours_median_per_turn_pool: 0.0126\n      gar_ours_spike_ratio: 5% (2/40 turns GAR>=0.4)\n      gar_dongre_mean: 0.0183\n      gar_dongre_std: 0.0198\n      gar_dongre_median: 0.0152\n      ngar_ours_mid: 0.5357\n      ngar_dongre_mid: 0.4436\n      ppl: 1.437\n      ppl_std: 0.077\n      ntp_loss: 0.3612\n    lora_only:\n      gar_ours_mean: 0.0284\n      gar_ours_std: 0.0481\n      gar_ours_median_per_conv: 0.0184\n      gar_ours_median_per_turn_pool: 0.0133\n      gar_ours_spike_ratio: 0%\n      gar_dongre_mean: 0.0205\n      gar_dongre_std: 0.0241\n      gar_dongre_median: 0.016\n      ngar_ours_mid: 0.3488\n      ngar_dongre_mid: 0.4997\n      ppl: 1.419\n      ppl_std: 0.075\n      ntp_loss: 0.3483\n    n_conversations: 20\n    n_turns: 4\n    mid_turns_definition: turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2).\n      All 16 eval entries use same definition.\n    stat_pool: 'median_per_conv: median of 20 per-conversation mid-turn averages.\n      median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).'\n    ranking_gar_ours_mean: TG(0.0434) > LO(0.0284) > Base(0.0088)\n    ranking_gar_ours_median_per_conv: TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\n    ranking_gar_ours_median_per_turn_pool: TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\n    ranking_gar_dongre: LO(0.0205) > TG(0.0183) > Base(0.0049)\n    note: Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages\n      across N=20). median_per_turn_pool is the alternative statistic from pooled\n      individual turns. Both confirm TG ≈ LO (zero-increment).\n- exp_id: d048_ss_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_avg_loss: 0.9326\n    final_ntp_loss: 0.932\n    final_gar_loss: 0.0007\n    gate_mean: 0.9527\n    gate_std: 0.0589\n    gate_min: 0.7383\n    gate_min_layer: L4\n    gate_max: 1\n    ss_usage: 4750/16000 (29.7%)\n    ss_fallback: 0\n    epochs_completed: 3\n    wall_clock_s: 23418\n    wall_clock_h: 6.5\n- exp_id: d048_ss_s42_resume\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d048_eval_ss_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf:\n      base_gar_ours_mid: 0.0128\n      base_gar_dongre_mid: 0.0031\n      base_ppl: 4.34\n      base_ntp: 1.4\n      tg_gar_ours_mid: 0.5025\n      tg_gar_dongre_mid: 0.389\n      tg_ppl: 2.78\n      tg_ntp: 0.98\n      baseline_mid_gar: 0.0122\n    ar:\n      gar_ours_mid: 0.3887\n      gar_ours_ci_95:\n      - 0.3692\n      - 0.3934\n      ppl: 1.35\n    gap_ratio: 1.29\n    n_conversations_tf: 50\n    n_conversations_ar: 5\n    bootstrap_turns: curve[2:] (turns 3-T)\n    note: AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch\n      with eval_200.json N=50.\n- exp_id: d048_queue_runner\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: d048_ss_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d048_final_ar_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beta0:\n      base_gar: 0.019\n      tg_gar: 0.064\n      ug_gar: 0.033\n      lo_gar: 0.037\n      pcgrad_gar: 0.03\n      ss_gar: 0.347\n    beta3:\n      base_gar: 0.531\n      tg_gar: 0.556\n      ss_gar: 0.593\n    beta5:\n      base_gar: 0.704\n      tg_gar: 0.727\n      ss_gar: 0.717\n    wilcoxon_beta0:\n      tg_vs_base_p: <0.001\n      tg_vs_base_r: 0.802\n      ss_vs_tg_p: <0.001\n      ss_vs_tg_r: 0.869\n    ppl:\n      base: 1.447\n      tg: 1.432\n      ss: 1.442\n    n_convs: 39\n- exp_id: qwen15b_phase1_diag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mmlu_eval_all\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base_qwen: 0.7423\n    pcgrad_v9_s42: 0.7386\n    ss_v8b_s42: 0.7375\n    lo_s42: 0.7357\n    tg_v7_s42: 0.7347\n    ug_s42: 0.7346\n- exp_id: d048_split_softmax_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d048_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d048_eval_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf_gar_ours: 0.5536\n    tf_gar_dongre: 0.4106\n    tf_ppl: 2.6123\n    ar_beta0_gar: 0.4231\n    ar_beta0_ppl: 1.4408\n    ar_beta3_gar: 0.5903\n    ar_beta3_ppl: 1.607\n    ar_beta5_gar: 0.7174\n    ar_beta5_ppl: 1.7852\n    n_convs_tf: 200\n    n_convs_ar: 39\n- exp_id: p0_ss_steering_eval\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: p1_tf_ar_kl_divergence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tg_delta_gar: 0.0165\n    base_delta_gar: 0.0122\n    tg_mean_kl: 0.054\n    base_mean_kl: 0.043\n    gate_kl_correlation: 0.11\n    high_kl_layers: L23-L27, L9\n    gar_robustness_ours_tg_base_ratio: 21.4\n    gar_robustness_goal_only_ratio: 63\n    gar_robustness_ours_all_ratio: 1.7\n    gar_robustness_ours_first_ratio: 1.8\n- exp_id: p1_llama_ss_training\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: p2_llama_gradient_conflict\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cos_sim_mean: 0.0045\n    cos_sim_std: 0.07\n    neg_cos_sim_layers_pct: 53.1\n    mag_ratio_median: 25.7\n    conclusion_note: 'cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion\n      text ''widespread conflict'' is misleading — actual finding: NTP and GAR gradients\n      are nearly orthogonal on Llama, consistent with Qwen pattern.'\n- exp_id: d048_eval_ss_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf_gar_ours_mid: 0.4964\n    tf_gar_dongre_mid: 0.3862\n    ar_beta0_gar: 0.4325\n    ar_beta0_ppl: 1.4394\n    ar_beta3_gar: 0.605\n    ar_beta3_ppl: 1.5868\n    ar_beta5_gar: 0.7157\n    ar_beta5_ppl: 1.8045\n    n_convs_ar: 50\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-24T08:13:19.715Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T08:13:19.715Z",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-24T08:13:19.742Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画
核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general mitigation', "Exposure bias 对 auxiliary attention loss 的 8×–27× gap 被审稿人接受为该场景下的 novel 实证贡献（非 'exposure bias is already known' 驳回）", 'PCGrad 因果排除链（观察→假设→排除→指向真因）被认为方法论严谨，非 trivial ablation', "SS + β-steering 双路径 mitigation 被视为 substantive constructive contribution（非 'just applied known technique'）", '3-seed 统计 + bootstrap CI + 跨模型 + alternative GAR definitions 充分回应 W7/W1/W3', '论文写作成功执行 gromov/sun/xiao 对标模式，56 references 解决 W6']
关键指标范围：{'llama_ss_ar_gar_beta0': [0.3, 0.5], 'llama_ss_tf_ar_gap_ratio': [1.0, 2.0], 'qwen_ss_ar_gar_beta0_3seed': [0.38, 0.45], 'qwen_ss_tf_ar_gap_ratio': [1.1, 1.5], 'dream_review_score': [3.5, 4.0], 'fatal_severe_concerns_remaining': [0, 1], 'reviewer_novelty_objection_probability': [0.0, 0.3], 'alternative_gar_defs_ss_improves': [3, 4]}
叙事方向：原始 framing 完全成立。Title 用 T2（'From Collapse to Recovery'）强调完整弧。5 个 contributions 均可 full-strength claim。SS 跨模型通用性升级 C5 为 'cross-model validated mitigation'。Paper 定位 solid EMNLP main conference，不需要 Findings fallback。核心叙事：首次定量刻画 exposure bias 如何摧毁 auxiliary attention loss（8×–27×），因果排除梯度冲突后精确定位 distribution shift 为根因，SS 提供通用初步修复（gap 8×→~1.3×），构成完整的诊断-修复循环。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: turn_residual_gating
venue: emnlp-2026

## paper_framing.md

# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering

> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**
> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + "观察→假设→排除→指向真因" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result
> **⚠️ Dream review D024: "Cannot" overclaims, novelty "first measurement" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 "Fails to", novelty 降级 "first empirical characterization"**
> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)
> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 "发现→定位→修复" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。

---

## 1. Title Candidates

- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating
- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）
- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）
- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）

推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 "selectively destroys"，去掉冗长副标题。T2 强调 "发现→定位→修复" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。

---

## 2. Story Arc

Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete "discover → diagnose → initial remedy" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).

---

## 3. Core Claims

| # | Claim | 支撑 | 状态 |
|---|-------|------|------|
| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |
| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |
| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |
| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |
| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |

---

## 4. Negative Findings (NF)

| # | Finding | 证据 | 叙事角色 |
|---|---------|------|----------|
| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |
| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |

---

## 5. Key Selling Points

**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**

**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 "PPL -46%" 和 "selective dissociation" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。

**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。

**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。

**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。

---

## 6. Anticipated Reviewer Concerns

| # | 严重度 | 预期质疑 | 回应策略 |
|---|--------|----------|----------|
| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|
| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 "zero benefit"。必要时追加 2 个 seed 的训练。|
| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 "negative result" 升级为 "negative result + constructive direction"。|
| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 "gate attenuation 2-7%" 指子层贡献缩放，表述正确但需明确。|

---

## 7. Dongre et al. 关系定位

| 维度 | Dongre et al. | 本文 |
|------|---------------|------|
| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |
| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |

**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。

共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）

---

## 8. GAR 定义策略

| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
|------|------|------------|----------------|------|
| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |

**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。

---

## 9. 论文结构草案

1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**
7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication
8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**
9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)

### 贡献列表（按 novelty 排序）

1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆
2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) "Parallel Attention Forcing" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明

---

## 10. 竞争力评估

### Dream Review 结果 (2026-05-19, dream_20260519T135115)
- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。
- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。
- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。

### 修正后预期（2026-05-23 Framing 升级后）
- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。
- **Best case**: 3.5 (Borderline Conference / Accept)。完整 "发现→定位→修复" 弧匹配 gromov/sun/xiao 模式。
- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。
- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。
- **核心差异化**: 不是 "gating 失败了"（弱），而是 "exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复"（强）。
- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。


## experiment_plan (with registry status)

- id: plan_001
  claim: C1
  description: Phase 1 GAR degradation diagnosis on Qwen-2.5-7B (70.8% raw drop)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: phase1_gar_diag
  status: DONE
  conclusion: success
  metrics:
    turn1_avg_gar: 0.0418
    mid_turns_avg_gar: 0.0122
    relative_drop: 0.708
    num_conversations: 5
    num_turns: 10
    per_turn_avg_gar:
    - 0.0418
    - 0.0241
    - 0.0224
    - 0.013
    - 0.0133
    - 0.0086
    - 0.0078
    - 0.008
    - 0.0157
    - 0.0064
- id: plan_002
  claim: C2
  description: ThreadGate v7 training (MSE+gate_div) - training GAR 0.48, inference
    GAR 0.016
  priority: P0
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: phase2_tg_s42_v7
  status: DONE
  conclusion: success
  metrics:
    eval_iid_ours_mid_gar: 0.5035
    eval_iid_dongre_mid_gar: 0.0152
    eval_iid_ppl: 2.784
    eval_heldout_ours_mid_gar: 0.5035
    eval_heldout_dongre_mid_gar: 0.0152
    eval_heldout_ppl: 2.78
    eval_modelgen_ours_mid_gar: 0.0157
    eval_modelgen_dongre_mid_gar: 0.0194
    eval_modelgen_ppl: 1.36
    gate_mean_final: 0.9336
    gate_std_final: 0.0492
- id: plan_003
  claim: C4
  description: Uniform Gate ablation - isolate turn conditioning contribution
  priority: P0
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: phase2_ug_s42
  status: DONE
  conclusion: success
  metrics:
    epoch0_avg_loss: 1.0019
    epoch0_avg_ntp: 0.9755
    epoch0_avg_gar: 0.0259
    epoch0_avg_div: 0.0005
    epoch1_avg_loss: 0.9447
    epoch1_avg_ntp: 0.9435
    epoch1_avg_gar: 0.0013
    epoch1_avg_div: 0
    epoch2_avg_loss: 0.9319
    epoch2_avg_ntp: 0.9309
    epoch2_avg_gar: 0.001
    epoch2_avg_div: 0
    final_gate_mean: 0.9598
    final_gate_std: 0.0518
    final_gate_min: 0.7773
    final_gate_max: 1
    final_profile_L3: 0.777
    final_profile_L5: 0.812
    final_profile_L0: 0.875
    final_profile_L27: 1
    training_time_seconds: 21994.5
    training_time_hours: 6.1
    global_steps: 7950
    unexpected_per_layer_variation: true
    eval_modelgen_ours_mid_gar: 0.0149
    eval_modelgen_dongre_mid_gar: 0.0185
    eval_modelgen_ppl: 1.396
- id: plan_004
  claim: C4
  description: LoRA-only ablation - isolate gating mechanism contribution
  priority: P0
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: phase2_lora_only_s42
  status: DONE
  conclusion: success
  metrics:
    epochs_completed: 3
    global_steps: 3000
    training_time_seconds: 20588.6
    training_time_hours: 5.7
    gate_fixed: 1
    gate_type_actual: none
    final_lora_size_mb: 20
    eval_modelgen_ours_mid_gar: 0.0245
    eval_modelgen_dongre_mid_gar: 0.0185
    eval_modelgen_ppl: 1.371
- id: plan_005
  claim: C4
  description: Four-way eval (Base/TG/UG/LoRA-only x GAR-ours/Dongre + PPL)
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_002
  - plan_003
  - plan_004
  registry_id: phase2_4way_eval
  status: DONE
  conclusion: negative
  metrics:
    base_ours_mid_gar: 0.0107
    base_ours_recovery_pp: -0.15
    base_dongre_mid_gar: 0.003
    base_dongre_recovery_pp: -0.92
    base_ppl: 4.23
    base_ntp: 1.4162
    tg_ours_mid_gar: 0.4866
    tg_ours_recovery_pp: 47.44
    tg_dongre_mid_gar: 0.0157
    tg_dongre_recovery_pp: 0.35
    tg_ppl: 2.63
    tg_ntp: 0.9484
    ug_ours_mid_gar: 0.4923
    ug_ours_recovery_pp: 48.01
    ug_dongre_mid_gar: 0.013
    ug_dongre_recovery_pp: 0.08
    ug_ppl: 2.62
    ug_ntp: 0.9433
    lora_ours_mid_gar: 0.486
    lora_ours_recovery_pp: 47.39
    lora_dongre_mid_gar: 0.0137
    lora_dongre_recovery_pp: 0.15
    lora_ppl: 2.63
    lora_ntp: 0.9482
    route_b_confirmed: true
    gating_incremental_benefit: none
- id: plan_006
  claim: C3
  description: Gradient conflict analysis on v7 (3 epoch checkpoints) - NTP vs GAR
    gradient cos_sim + magnitude ratio
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - plan_002
  registry_id: analysis_gradient_conflict
  status: DONE
  conclusion: success
  metrics:
    epoch0_cos_sim: -0.089
    epoch1_cos_sim: -0.054
    epoch2_cos_sim: -0.042
    epoch0_neg_layers_pct: 78.6
    epoch1_neg_layers_pct: 71.4
    epoch2_neg_layers_pct: 67.9
    epoch0_mag_ratio: 7.5
    epoch1_mag_ratio: 13.7
    epoch2_mag_ratio: 14.7
- id: plan_007
  claim: C3
  description: Attention heatmap visualization (4 models x 3 conversations x 28 layers)
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - plan_002
  - plan_003
  - plan_004
  registry_id: analysis_attention_heatmap
  status: DONE
  conclusion: success
  metrics:
    base_mean_goal_attn: 0.0136
    base_decay: 0.875
    tg_mean_goal_attn: 0.0232
    tg_decay: 0.777
    ug_mean_goal_attn: 0.0216
    ug_decay: 0.803
    lora_mean_goal_attn: 0.0216
    lora_decay: 0.81
    gating_incremental_benefit: none
- id: plan_008
  claim: C2, C4
  description: 'Held-out eval: create truly held-out eval set (50 convs, idx>=8000
    from UltraChat full) and re-run 4-way eval to validate conclusions on unseen data'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_005
  status: DONE
  registry_id: phase2_4way_eval_heldout
  conclusion: success
  metrics:
    base_ours_mid_gar: 0.0128
    base_ours_recovery_pp: 0.06
    base_dongre_mid_gar: 0.0031
    base_dongre_recovery_pp: -0.91
    base_ppl: 4.34
    base_ntp: 1.4045
    tg_ours_mid_gar: 0.5035
    tg_ours_recovery_pp: 49.13
    tg_dongre_mid_gar: 0.0152
    tg_dongre_recovery_pp: 0.3
    tg_ppl: 2.78
    tg_ntp: 0.9771
    ug_ours_mid_gar: 0.5053
    ug_ours_recovery_pp: 49.31
    ug_dongre_mid_gar: 0.0124
    ug_dongre_recovery_pp: 0.02
    ug_ppl: 2.78
    ug_ntp: 0.9752
    lora_ours_mid_gar: 0.4978
    lora_ours_recovery_pp: 48.56
    lora_dongre_mid_gar: 0.0132
    lora_dongre_recovery_pp: 0.1
    lora_ppl: 2.78
    lora_ntp: 0.9771
    three_way_convergence_confirmed: true
    gar_ours_spread_pp: 0.75
    ppl_spread: 0
    data_overlap: false
- id: plan_009
  claim: C5
  description: Llama-3.1-8B Phase 1 GAR degradation diagnosis - confirm GAR decay
    exists on different architecture
  priority: P0
  gpu_budget_hours: 0.5
  deps: []
  status: DONE
  registry_id: llama_phase1_gar_diag
  conclusion: success
  metrics:
    per_turn_gar:
      turn_1: 0.0263
      turn_2: 0.0183
      turn_3: 0.0087
      turn_4: 0.0055
      turn_5: 0.006
      turn_6: 0.0035
      turn_7: 0.0038
      turn_8: 0.0037
      turn_9: 0.005
      turn_10: 0.0026
    t1_t10_decay_pct: 90.1
    t1_mid38_drop_pct: 80.2
    n_topics: 5
    model: Meta-Llama-3.1-8B-Instruct
    mode: gen
    n_conversations: 5
    n_turns: 10
- id: plan_010
  claim: C5
  description: Llama-3.1-8B ThreadGate v7 training - replicate Qwen setup on Llama
  priority: P0
  gpu_budget_hours: 7
  deps:
  - plan_009
  status: DONE
  registry_id: llama_tg_s42
  conclusion: success
  metrics:
    epochs_completed: 3
    total_steps: 3000
    wall_clock_seconds: 26212
    wall_clock_hours: 7.28
    final_avg_loss: 0.9233
    final_avg_ntp: 0.9224
    final_avg_gar: 0.0009
    final_avg_div: 0
    final_gate_mean: 0.9099
    final_gate_std: 0.0701
    final_gate_min: 0.7188
    final_gate_max: 0.9922
    gate_profile_step3000:
      L0: 0.957
      L1: 0.973
      L2: 0.977
      L3: 0.965
      L4: 0.992
      L5: 0.969
      L6: 0.957
      L7: 0.957
      L8: 0.961
      L9: 0.949
      L10: 0.938
      L11: 0.934
      L12: 0.969
      L13: 0.953
      L14: 0.957
      L15: 0.965
      L16: 0.953
      L17: 0.961
      L18: 0.922
      L19: 0.902
      L20: 0.883
      L21: 0.863
      L22: 0.836
      L23: 0.844
      L24: 0.809
      L25: 0.719
      L26: 0.762
      L27: 0.805
      L28: 0.801
      L29: 0.855
      L30: 0.898
      L31: 0.934
    checkpoint_size_gate_mb: 4.2
    checkpoint_size_lora_mb: 26
    gpu: NVIDIA RTX PRO 6000 Blackwell
    vram_gb: 102
    mem_used_gb: 63.4
- id: plan_011
  claim: C5
  description: Llama-3.1-8B LoRA-only training - cross-model gating redundancy validation
    (D020)
  priority: P0
  gpu_budget_hours: 7
  deps:
  - plan_009
  status: DONE
  registry_id: llama_lora_only_s42
  conclusion: success
  metrics:
    final_avg_loss: 0.9288
    final_avg_ntp: 0.9279
    final_avg_gar: 0.0009
    gate_fixed: 1
    gate_type: none
    wall_clock_s: 25317
    wall_clock_h: 7.03
    epochs_completed: 3
- id: plan_012
  claim: C5
  description: Llama-3.1-8B 3-way eval (Base/TG/LoRA-only x GAR + PPL) on held-out
    data
  priority: P0
  gpu_budget_hours: 1
  deps:
  - plan_010
  - plan_011
  status: DONE
  registry_id: llama_eval_s42
  conclusion: success
  metrics:
    tf_base:
      gar_ours: 0.0166
      ngar_ours: 0.3882
      gar_dongre: 0.0038
      ngar_dongre: 0.163
      ppl: 3.45
      N: 50
      T: 4
    tf_tg:
      gar_ours: 0.4836
      ngar_ours: 11.8818
      gar_dongre: 0.018
      ngar_dongre: 0.7922
      ppl: 2.57
      N: 50
      T: 4
    ar_base:
      gar_ours: 0.0086
      ngar_ours: 0.0798
      gar_dongre: 0.0118
      ngar_dongre: 0.1265
      ppl: 1.24
      N: 5
      T: 10
    ar_tg:
      gar_ours: 0.0304
      ngar_ours: 0.2632
      gar_dongre: 0.0217
      ngar_dongre: 0.2459
      ppl: 1.32
      N: 5
      T: 10
    gap_ratio_tg_ours: 15.9
    gap_ratio_base_ours: 1.93
    gap_ratio_tg_dongre: 0.83
    vs_qwen_v7_gap_ratio: 32.1
    baseline_mid_gar: 0.0122
- id: plan_013
  claim: C3
  description: Llama-3.1-8B gradient conflict analysis - verify NTP-GAR competition
    is model-agnostic
  priority: P1
  gpu_budget_hours: 0.5
  deps:
  - plan_010
  status: planned
  result: 'cos_sim=0.0045 (near-orthogonal, not conflict), neg_layers=53.1% (near
    random), mag_ratio_median=25.7×. Cross-model confirms: gradients not conflicting,
    NTP magnitude dominates. Consistent with Qwen. D054.'
- id: plan_014
  claim: W3
  description: Downstream task sanity check - simple instruction retention test across
    turns to link GAR to task performance
  priority: P2
  gpu_budget_hours: 1
  deps:
  - plan_005
  status: DONE
  registry_id: instruction_retention_test
  result: β=3 late-turn retention 87.0% vs β=0 75.9%, delta=+11.1pp. GAR-compliance
    correlation r=0.200, p=0.007. Written to Appendix C. D046.
  conclusion: success
  metrics:
    late_turn_rate_beta0: 0.759
    late_turn_rate_beta3: 0.87
    late_turn_delta: 0.111
    mcnemar_chi2: 3.125
    mcnemar_p: 0.0771
    gar_compliance_r: 0.2003
    gar_compliance_p: 0.007
    category_content_constraint:
      beta0: 0.619
      beta3: 0.857
      delta: 0.238
    category_count_constraint:
      beta0: 1
      beta3: 1
      delta: 0
    category_format_constraint:
      beta0: 1
      beta3: 1
      delta: 0
    category_position_constraint:
      beta0: 0.667
      beta3: 0.733
      delta: 0.067
- id: plan_015
  claim: C4, W7
  description: Statistical significance analysis - paired bootstrap CI from held-out
    eval (50 convs) for TG-LoRA-only comparison. If CI includes 0 → statistically
    supports 'zero benefit'. Addresses Dream W3 (single seed).
  priority: P1
  gpu_budget_hours: 0.5
  deps:
  - plan_008
  status: orphaned
  registry_id: worker_analysis_bootstrap_ci_tg_vs_lora_20260519T144212
  result: 'PASS: All GAR-ours and PPL 95% CIs include 0 (TG-LO GAR: [-0.0018,+0.0036],
    UG-LO: [-0.0006,+0.0045], TG-UG: [-0.0030,+0.0006]). Statistically confirms zero
    benefit. W7 addressed.'
- id: plan_016
  claim: W8
  description: Exposure-bias mitigation test - train ThreadGate v7 with scheduled
    sampling applied to GAR loss (mix teacher-forced + model-generated contexts).
    Test whether closing exposure bias gap narrows the 30x training-inference GAR
    gap. Constructive direction that upgrades paper from pure negative result.
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_008
  status: DONE
  registry_id: phase2_tg_s42_v8_schedsampling
  conclusion: failed
  metrics:
    killed_at_microstep: 1950
    total_microsteps: 24000
    completion_pct: 8.1
    global_step_approx: 244
    total_global_steps: 3000
    ss_steps_observed: 1
    tf_lgar_mean_step850_1400: 0.0062
    tf_lgar_std: 0.0082
    tf_lgar_collapse_step: 800
    gate_mean_final: 0.93
    ss_ratio_at_kill: 0.081
    crash_reason: 'killed by director: SS path code bug (D026) makes experiment invalid,
      GPU needed for PCGrad'
    design_flaw_ss_ramp_too_slow: true
    design_flaw_no_ss_tf_separate_logging: true
- id: plan_017
  claim: R4
  description: Code-paper architecture verification - confirm ThreadGate implementation
    matches paper Eq.3 (gate on residual vs gate on sub-layer output). Quick code
    audit, no GPU.
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: orphaned
  registry_id: worker_analysis_code_paper_arch_verify_20260519T144058
  result: 'CRITICAL: code implements x+g·f(x) (ReZero-style), dream paper.tex wrote
    g·x+f(x). Semantically opposite when g→0. Data unaffected. D023.'
- id: plan_018
  claim: C3, W8
  description: PCGrad baseline - project NTP gradient onto GAR-orthogonal plane for
    gate params only. If 30x gap persists after removing gradient conflict → causal
    evidence that exposure bias (not gradient competition) is the root cause.
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_006
  registry_id: phase2_tg_s42_v9_pcgrad
  status: DONE
  conclusion: success
  metrics:
    eval_iid_ours_mid_gar: 0.5002
    eval_iid_dongre_mid_gar: 0.0123
    eval_iid_ppl: 2.78
    eval_iid_ntp: 0.9752
    eval_heldout_ours_mid_gar: 0.5002
    eval_heldout_dongre_mid_gar: 0.0123
    eval_heldout_ppl: 2.78
    eval_heldout_ntp: 0.9752
    eval_modelgen_ours_mid_gar: 0.0151
    eval_modelgen_dongre_mid_gar: 0.0173
    eval_modelgen_ppl: 1.5
    vs_v7_iid_ppl_diff: 0.004
    vs_v7_iid_gar_diff: -0.0033
- id: plan_019
  claim: C2, MF5
  description: Multi-seed validation — train TG v7 + LoRA-only with seed=123 on Qwen.
    Provide mean±std for 30x gap. 1 extra seed sufficient given extreme effect size.
  priority: P1
  gpu_budget_hours: 6
  deps:
  - plan_002
  status: DONE
  registry_id: v7_tg_s123
  conclusion: success
  metrics:
    epoch_1:
      avg_loss: 0.9447
      avg_ntp_loss: 0.9434
      avg_gar_loss: 0.0013
      avg_div_loss: 0
    epoch_2:
      avg_loss: 0.9315
      avg_ntp_loss: 0.9305
      avg_gar_loss: 0.001
      avg_div_loss: 0
    final_gate:
      mean: 0.9467
      std: 0.051
      min: 0.793
      max: 1
    final_gate_profile:
      L0: 0.883
      L1: 0.793
      L2: 0.996
      L3: 0.988
      L4: 0.984
      L5: 0.797
      L6: 0.961
      L7: 0.918
      L8: 0.965
      L9: 0.934
      L10: 0.969
      L11: 0.918
      L12: 0.926
      L13: 0.941
      L14: 0.93
      L15: 0.965
      L16: 0.941
      L17: 0.91
      L18: 0.961
      L19: 0.965
      L20: 0.973
      L21: 0.988
      L22: 0.969
      L23: 0.98
      L24: 0.98
      L25: 0.984
      L26: 0.988
      L27: 1
    training_time_s: 21425.2
- id: plan_020
  claim: C4, MF6
  description: Expanded eval set — increase from 50 to 200 conversations (idx>=7000
    from UltraChat). Boost bootstrap CI statistical power.
  priority: P1
  gpu_budget_hours: 2
  deps:
  - plan_008
  status: planned
  result: 'Partially done: TF eval uses eval_200 (N=200), AR eval uses d048_final_ar
    (N=50). AR N=200 not planned — N=50 sufficient given extreme effect sizes. No
    additional GPU needed.'
- id: plan_022
  claim: C3, SF4
  description: λ_GAR sensitivity — train v7 with λ_GAR=10 (1 epoch only). Show gradient
    competition trend under higher GAR weight. If budget allows, add λ=0.1.
  priority: P2
  gpu_budget_hours: 2
  deps:
  - plan_002
  status: planned
- id: plan_023
  claim: W8, C3
  description: 'v8b: Fixed Scheduled Sampling — fix compute_gar_loss len==1 bug (Option
    A: handle single-turn mse_target), fix OOM (reduce batch/gen_length), use lambda_gar=1.0
    (match v7). Tests whether training on model-generated text closes the 30x distribution
    shift gap. If successful, paper upgrades from pure negative to ''diagnosis + initial
    remedy''. D026.'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_002
  status: DONE
  registry_id: phase2_tg_s42_v8b_resume
  conclusion: success
  metrics:
    training:
      total_steps: 3000
      epochs_completed: 3
      wall_clock_hours: 8.1
      final_loss: 0.933
      final_ntp_loss: 0.9322
      final_gar_loss: 0.0008
      final_gate_mean: 0.9586
      final_gate_std: 0.0582
      ss_ratio: 0.5
    eval_iid:
      gar_ours: 0.4983
      gar_dongre: 0.3855
      ppl: 2.78
    eval_modelgen:
      gar_ours: 0.3177
      gar_dongre: 0.3533
      ppl: 1.38
    vs_v7:
      iid_gar_ours_delta: -0.005
      modelgen_gar_ours_delta: 0.302
      gap_ratio_v7: 32
      gap_ratio_v8b: 1.57
- id: plan_024
  claim: C4
  description: 'SS + β-steering combined eval — CANCELLED. Data already exists in
    ss_s42_ar_n50.json (β=0,3,5). SS and steering are substitutes not complements
    (β=5: SS 0.717 ≈ TG 0.727). No need to re-run.'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - plan_023
  status: PREPARING
  registry_id: p0_ss_steering_eval
  result: 'Cancelled — existing data shows SS+steering do not stack. β=0: SS 0.347
    (independent value). β=3: SS +0.037 marginal. β=5: SS ≈ TG (converge). Discussion
    added to paper.'
  conclusion: killed
- id: plan_025
  claim: C1
  description: TF vs AR attention KL divergence — compute per-head KL(P_TF||P_AR)
    on 50 conversations to quantify attention distribution shift. If GAR-relevant
    heads show larger KL → mechanistic evidence for why GAR collapses. Pure CPU analysis.
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_002
  status: planned
- id: plan_026
  claim: C5, C4
  description: Llama-3.1-8B Scheduled Sampling — replicate SS training on Llama to
    verify cross-model gap compression. If Llama gap also compresses → SS is a general
    mitigation, not model-specific.
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_010
  status: planned
- id: plan_027
  claim: C4, W7
  description: 'SS 3-seed validation — s42 (gap 1.45×), s123 (TF NaN, AR 0.423), s456
    (gap 1.15×). 3-seed AR GAR β=0: 0.401±0.047. β=3/5 extremely stable (std<0.01).
    Addresses single-seed reviewer concern.'
  priority: P0
  gpu_budget_hours: 16
  deps:
  - plan_023
  status: planned
  result: '3-seed complete. TF GAR 0.498±0.004 (s42=0.503, s123=0.495, s456=0.496).
    AR GAR β=0: 0.401±0.047 (s42=0.347, s123=0.423, s456=0.433). Gap 1.26±0.17 (range
    1.15–1.45×, 3 valid seeds). β=3: 0.596±0.008. β=5: 0.717±0.001. PPL β=0: 1.441±0.001.
    W7 addressed.'
- id: plan_028
  claim: C2, W5
  description: Alternative GAR definition robustness — 4 token selections (last/all/first/goal-only)
    × 3 checkpoints (Base/TG/SS). Needed GPU re-eval (raw attention not saved).
  priority: P1
  gpu_budget_hours: 0.5
  deps:
  - plan_027
  status: planned
  result: TG only improves last-token GAR (0.325), all/first-token near-zero (0.025/0.039).
    SS improves ALL 4 definitions >0.36. SS builds broader goal-attention pattern,
    not position-specific overfitting. Base consistently <0.022. D054.
- id: plan_029
  claim: C2, W7
  description: SS 4th seed (s789) — additional seed to strengthen mean±std. Training
    ~6.5h + eval ~1h. ROI lower than Llama SS (cross-model > extra seed given extreme
    effect size). Run if time permits after plan_026.
  priority: P2
  gpu_budget_hours: 8
  deps:
  - plan_027
  status: planned
- id: plan_030
  claim: C1, C2
  description: Long conversation eval (>10 turns) — test whether exposure bias gap
    worsens with conversation length. Need to identify suitable long conversations
    from UltraChat. Eval ~1-2h.
  priority: P2
  gpu_budget_hours: 2
  deps:
  - plan_027
  status: planned


## registry (completed experiments)

- exp_id: phase1_gar_diag
  name: ''
  status: DONE
  conclusion: success
  metrics:
    turn1_avg_gar: 0.0418
    mid_turns_avg_gar: 0.0122
    relative_drop: 0.708
    num_conversations: 5
    num_turns: 10
    per_turn_avg_gar:
    - 0.0418
    - 0.0241
    - 0.0224
    - 0.013
    - 0.0133
    - 0.0086
    - 0.0078
    - 0.008
    - 0.0157
    - 0.0064
- exp_id: phase2_tg_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    final_ntp_loss: 0.94
    final_gar_loss: 0
    gate_mean: 0.988
    gar_loss_zero_pct: 87.6
    epochs_completed: 1.67
    killed_reason: SIGTERM by diagnose worker (unauthorized)
- exp_id: phase2_ug_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epoch0_avg_loss: 1.0019
    epoch0_avg_ntp: 0.9755
    epoch0_avg_gar: 0.0259
    epoch0_avg_div: 0.0005
    epoch1_avg_loss: 0.9447
    epoch1_avg_ntp: 0.9435
    epoch1_avg_gar: 0.0013
    epoch1_avg_div: 0
    epoch2_avg_loss: 0.9319
    epoch2_avg_ntp: 0.9309
    epoch2_avg_gar: 0.001
    epoch2_avg_div: 0
    final_gate_mean: 0.9598
    final_gate_std: 0.0518
    final_gate_min: 0.7773
    final_gate_max: 1
    final_profile_L3: 0.777
    final_profile_L5: 0.812
    final_profile_L0: 0.875
    final_profile_L27: 1
    training_time_seconds: 21994.5
    training_time_hours: 6.1
    global_steps: 7950
    unexpected_per_layer_variation: true
    eval_modelgen_ours_mid_gar: 0.0149
    eval_modelgen_dongre_mid_gar: 0.0185
    eval_modelgen_ppl: 1.396
- exp_id: phase2_tg_s42_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: phase2_tg_s42_v3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    gate_mean_step0: 0.8743
    gate_mean_step500: 0.8761
    gate_delta: 0.004
    gate_std: 0.001
    final_ntp_loss: 0.94
    final_gar_loss: -0.019
    gar_contribution_pct: 2-4%
    diagnosis: gate frozen, GAR indirect gradient too weak
- exp_id: phase2_tg_s42_v3b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gate_std_final: 0.087
    gate_mean_final: 0.9388
    gate_min_final: 0.5352
    gate_max_final: 0.9922
    L4_gate: 0.535
    L0_gate: 0.777
    L_NTP_final: 0.7787
    L_GAR_final: -0.9606
    elapsed_seconds: 3565.9
    optimizer_steps: 500
    gate_grad_received: true
- exp_id: phase2_tg_s42_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: phase2_tg_s42_v5
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    step2000_gate_std: 0.0225
    step2000_gate_mean: 0.9586
    step2000_gate_min: 0.9062
    step2000_gate_max: 0.9961
    step2000_L_GAR: -0.8977
    step2000_L_NTP: 0.7611
    step2000_total_loss: -0.1365
    step2400_gate_std: 0.0219
    step2400_gate_mean: 0.9651
    step2400_gate_min: 0.918
    step2400_gate_max: 0.9961
    step2400_profile: L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996
    L_GAR_saturated_at: -0.91
    gate_range_compression: 0.918-0.996
- exp_id: phase2_tg_s42_v6
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    dryrun_step0_L_NTP: 2.0275
    dryrun_step0_L_GAR: -0.0161
    dryrun_step0_total_loss: 2.0114
    dryrun_step4_L_NTP: 1.6544
    dryrun_step4_L_GAR: -0.0147
    dryrun_step4_total_loss: 1.6397
    dryrun_gate_grad: true
    dryrun_gate_mean_init: 0.8097
    dryrun_gate_std_init: 0.0341
    dryrun_gate_min_init: 0.6836
    dryrun_gate_max_init: 0.8672
    dryrun_gate_mean_step5: 0.8025
    dryrun_gate_std_step5: 0.0842
    dryrun_gate_min_step5: 0.5547
    dryrun_gate_max_step5: 0.9805
    gs50_gate_mean: 0.8117
    gs50_gate_std: 0.0612
    gs50_gate_min: 0.6836
    gs50_gate_max: 0.9805
    gs100_gate_mean: 0.8737
    gs100_gate_std: 0.0367
    gs100_gate_min: 0.8164
    gs100_gate_max: 0.9766
    gs100_L_NTP: 0.8151
    gs100_L_GAR: -0.158
    gs100_total_loss: 0.6571
    gs100_profile_bottom3: L12=0.816 L4=0.824 L13=0.824
    gs100_profile_top3: L27=0.977 L26=0.961 L23=0.914
    gs143_L_GAR: -0.3876
    gs143_gate_mean: 0.9227
- exp_id: phase2_tg_s42_v7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_iid_ours_mid_gar: 0.5035
    eval_iid_dongre_mid_gar: 0.0152
    eval_iid_ppl: 2.784
    eval_heldout_ours_mid_gar: 0.5035
    eval_heldout_dongre_mid_gar: 0.0152
    eval_heldout_ppl: 2.78
    eval_modelgen_ours_mid_gar: 0.0157
    eval_modelgen_dongre_mid_gar: 0.0194
    eval_modelgen_ppl: 1.36
    gate_mean_final: 0.9336
    gate_std_final: 0.0492
- exp_id: phase2_lora_only_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epochs_completed: 3
    global_steps: 3000
    training_time_seconds: 20588.6
    training_time_hours: 5.7
    gate_fixed: 1
    gate_type_actual: none
    final_lora_size_mb: 20
    eval_modelgen_ours_mid_gar: 0.0245
    eval_modelgen_dongre_mid_gar: 0.0185
    eval_modelgen_ppl: 1.371
- exp_id: phase2_4way_eval
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    base_ours_mid_gar: 0.0107
    base_ours_recovery_pp: -0.15
    base_dongre_mid_gar: 0.003
    base_dongre_recovery_pp: -0.92
    base_ppl: 4.23
    base_ntp: 1.4162
    tg_ours_mid_gar: 0.4866
    tg_ours_recovery_pp: 47.44
    tg_dongre_mid_gar: 0.0157
    tg_dongre_recovery_pp: 0.35
    tg_ppl: 2.63
    tg_ntp: 0.9484
    ug_ours_mid_gar: 0.4923
    ug_ours_recovery_pp: 48.01
    ug_dongre_mid_gar: 0.013
    ug_dongre_recovery_pp: 0.08
    ug_ppl: 2.62
    ug_ntp: 0.9433
    lora_ours_mid_gar: 0.486
    lora_ours_recovery_pp: 47.39
    lora_dongre_mid_gar: 0.0137
    lora_dongre_recovery_pp: 0.15
    lora_ppl: 2.63
    lora_ntp: 0.9482
    route_b_confirmed: true
    gating_incremental_benefit: none
- exp_id: phase2_4way_eval_heldout
  name: ''
  status: DONE
  conclusion: success
  metrics:
    base_ours_mid_gar: 0.0128
    base_ours_recovery_pp: 0.06
    base_dongre_mid_gar: 0.0031
    base_dongre_recovery_pp: -0.91
    base_ppl: 4.34
    base_ntp: 1.4045
    tg_ours_mid_gar: 0.5035
    tg_ours_recovery_pp: 49.13
    tg_dongre_mid_gar: 0.0152
    tg_dongre_recovery_pp: 0.3
    tg_ppl: 2.78
    tg_ntp: 0.9771
    ug_ours_mid_gar: 0.5053
    ug_ours_recovery_pp: 49.31
    ug_dongre_mid_gar: 0.0124
    ug_dongre_recovery_pp: 0.02
    ug_ppl: 2.78
    ug_ntp: 0.9752
    lora_ours_mid_gar: 0.4978
    lora_ours_recovery_pp: 48.56
    lora_dongre_mid_gar: 0.0132
    lora_dongre_recovery_pp: 0.1
    lora_ppl: 2.78
    lora_ntp: 0.9771
    three_way_convergence_confirmed: true
    gar_ours_spread_pp: 0.75
    ppl_spread: 0
    data_overlap: false
- exp_id: phase2_tg_s42_v8_schedsampling
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    killed_at_microstep: 1950
    total_microsteps: 24000
    completion_pct: 8.1
    global_step_approx: 244
    total_global_steps: 3000
    ss_steps_observed: 1
    tf_lgar_mean_step850_1400: 0.0062
    tf_lgar_std: 0.0082
    tf_lgar_collapse_step: 800
    gate_mean_final: 0.93
    ss_ratio_at_kill: 0.081
    crash_reason: 'killed by director: SS path code bug (D026) makes experiment invalid,
      GPU needed for PCGrad'
    design_flaw_ss_ramp_too_slow: true
    design_flaw_no_ss_tf_separate_logging: true
- exp_id: analysis_gradient_conflict
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epoch0_cos_sim: -0.089
    epoch1_cos_sim: -0.054
    epoch2_cos_sim: -0.042
    epoch0_neg_layers_pct: 78.6
    epoch1_neg_layers_pct: 71.4
    epoch2_neg_layers_pct: 67.9
    epoch0_mag_ratio: 7.5
    epoch1_mag_ratio: 13.7
    epoch2_mag_ratio: 14.7
- exp_id: analysis_attention_heatmap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    base_mean_goal_attn: 0.0136
    base_decay: 0.875
    tg_mean_goal_attn: 0.0232
    tg_decay: 0.777
    ug_mean_goal_attn: 0.0216
    ug_decay: 0.803
    lora_mean_goal_attn: 0.0216
    lora_decay: 0.81
    gating_incremental_benefit: none
- exp_id: phase2_tg_s42_v9_pcgrad
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_iid_ours_mid_gar: 0.5002
    eval_iid_dongre_mid_gar: 0.0123
    eval_iid_ppl: 2.78
    eval_iid_ntp: 0.9752
    eval_heldout_ours_mid_gar: 0.5002
    eval_heldout_dongre_mid_gar: 0.0123
    eval_heldout_ppl: 2.78
    eval_heldout_ntp: 0.9752
    eval_modelgen_ours_mid_gar: 0.0151
    eval_modelgen_dongre_mid_gar: 0.0173
    eval_modelgen_ppl: 1.5
    vs_v7_iid_ppl_diff: 0.004
    vs_v7_iid_gar_diff: -0.0033
- exp_id: phase2_tg_s42_v8b_ss_fixed
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: attention_steering_v7_tg_gen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    beta_0.0:
      mid_turns_avg_gar: 0.028
      avg_ppl: 1.409
    beta_0.5:
      mid_turns_avg_gar: 0.0287
      avg_ppl: 1.387
    beta_1.0:
      mid_turns_avg_gar: 0.0349
      avg_ppl: 1.36
    beta_2.0:
      mid_turns_avg_gar: 0.062
      avg_ppl: 1.411
    beta_5.0:
      mid_turns_avg_gar: 0.6795
      avg_ppl: 1.908
    beta_10.0:
      mid_turns_avg_gar: 0.959
      avg_ppl: 4.22
    phase_transition_range: '[2, 5]'
    baseline_gar: 0.028
    max_gar_at_acceptable_ppl: 0.6795
    max_gar_at_acceptable_ppl_beta: 5
- exp_id: trc_baseline_v7_tg
  name: ''
  status: DONE
  conclusion: success
  metrics:
    v7_tg:
      tf_trc: 0.3339
      gen_trc: 0.3323
      trc_gap: 0.0016
      tf_tbp_ppl: 1.05
      gen_tbp_ppl: 1.05
    lora_only:
      tf_trc: 0.349
      gen_trc: 0.4106
      trc_gap: -0.0617
      tf_tbp_ppl: 9.5
      gen_tbp_ppl: 12
    base:
      tf_trc: 0.1494
      gen_trc: 0.1494
      trc_gap: 0
      tf_tbp_ppl: 2.05
      gen_tbp_ppl: 2.05
- exp_id: attention_steering_eval200_tf
  name: ''
  status: DONE
  conclusion: success
  metrics:
    beta_0.0:
      mid_gar: 0.5353
      ppl: 2.62
    beta_2.0:
      mid_gar: 0.6112
      ppl: 2.69
    beta_3.0:
      mid_gar: 0.788
      ppl: 2.93
    beta_4.0:
      mid_gar: 0.8165
      ppl: 3.49
    beta_5.0:
      mid_gar: 0.8325
      ppl: 6.15
    beta_10.0:
      mid_gar: 0.977
      ppl: 505.21
    n_convs: 200
    mode: tf
- exp_id: phase2_tg_s42_v8b_resume
  name: ''
  status: DONE
  conclusion: success
  metrics:
    training:
      total_steps: 3000
      epochs_completed: 3
      wall_clock_hours: 8.1
      final_loss: 0.933
      final_ntp_loss: 0.9322
      final_gar_loss: 0.0008
      final_gate_mean: 0.9586
      final_gate_std: 0.0582
      ss_ratio: 0.5
    eval_iid:
      gar_ours: 0.4983
      gar_dongre: 0.3855
      ppl: 2.78
    eval_modelgen:
      gar_ours: 0.3177
      gar_dongre: 0.3533
      ppl: 1.38
    vs_v7:
      iid_gar_ours_delta: -0.005
      modelgen_gar_ours_delta: 0.302
      gap_ratio_v7: 32
      gap_ratio_v8b: 1.57
- exp_id: eval_v8b_ss
  name: ''
  status: DONE
  conclusion: success
  metrics:
    iid_gar_ours: 0.4983
    iid_gar_dongre: 0.3855
    iid_ppl: 2.78
    iid_ngar_ours: 13.5
    iid_ngar_dongre: 22.68
    modelgen_gar_ours: 0.3177
    modelgen_gar_dongre: 0.3533
    modelgen_ppl: 1.38
    modelgen_ngar_ours: 4.47
    modelgen_ngar_dongre: 5.92
    iid_turn1_gar_ours: 0.5398
    modelgen_turn1_gar_ours: 0.4333
- exp_id: attention_steering_gen_n50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    corrected: true
    aggregation: per-conv mid_gar(turns 2-7), >=3 turns only
    beta_0.0:
      mid_gar: 0.0641
      mid_gar_std: 0.0809
      ppl: 1.4324
      ppl_std: 0.1029
      n_valid: 39
    beta_2.0:
      mid_gar: 0.128
      mid_gar_std: 0.1101
      ppl: 1.4822
      ppl_std: 0.1385
      n_valid: 39
    beta_3.0:
      mid_gar: 0.5558
      mid_gar_std: 0.0601
      ppl: 1.5605
      ppl_std: 0.1719
      n_valid: 39
    beta_4.0:
      mid_gar: 0.6439
      mid_gar_std: 0.0607
      ppl: 1.6674
      ppl_std: 0.2241
      n_valid: 39
    beta_5.0:
      mid_gar: 0.7271
      mid_gar_std: 0.0605
      ppl: 1.7723
      ppl_std: 0.2693
      n_valid: 38
    beta_10.0:
      mid_gar: 0.9612
      mid_gar_std: 0.0152
      ppl: 3.4517
      ppl_std: 1.7813
      n_valid: 39
    n_convs_total: 50
    n_convs_valid: 39
    mode: gen
    phase_transition_range: '[2, 3]'
- exp_id: llama_phase1_gar_diag
  name: ''
  status: DONE
  conclusion: success
  metrics:
    per_turn_gar:
      turn_1: 0.0263
      turn_2: 0.0183
      turn_3: 0.0087
      turn_4: 0.0055
      turn_5: 0.006
      turn_6: 0.0035
      turn_7: 0.0038
      turn_8: 0.0037
      turn_9: 0.005
      turn_10: 0.0026
    t1_t10_decay_pct: 90.1
    t1_mid38_drop_pct: 80.2
    n_topics: 5
    model: Meta-Llama-3.1-8B-Instruct
    mode: gen
    n_conversations: 5
    n_turns: 10
- exp_id: llama_tg_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epochs_completed: 3
    total_steps: 3000
    wall_clock_seconds: 26212
    wall_clock_hours: 7.28
    final_avg_loss: 0.9233
    final_avg_ntp: 0.9224
    final_avg_gar: 0.0009
    final_avg_div: 0
    final_gate_mean: 0.9099
    final_gate_std: 0.0701
    final_gate_min: 0.7188
    final_gate_max: 0.9922
    gate_profile_step3000:
      L0: 0.957
      L1: 0.973
      L2: 0.977
      L3: 0.965
      L4: 0.992
      L5: 0.969
      L6: 0.957
      L7: 0.957
      L8: 0.961
      L9: 0.949
      L10: 0.938
      L11: 0.934
      L12: 0.969
      L13: 0.953
      L14: 0.957
      L15: 0.965
      L16: 0.953
      L17: 0.961
      L18: 0.922
      L19: 0.902
      L20: 0.883
      L21: 0.863
      L22: 0.836
      L23: 0.844
      L24: 0.809
      L25: 0.719
      L26: 0.762
      L27: 0.805
      L28: 0.801
      L29: 0.855
      L30: 0.898
      L31: 0.934
    checkpoint_size_gate_mb: 4.2
    checkpoint_size_lora_mb: 26
    gpu: NVIDIA RTX PRO 6000 Blackwell
    vram_gb: 102
    mem_used_gb: 63.4
- exp_id: llama_eval_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tf_base:
      gar_ours: 0.0166
      ngar_ours: 0.3882
      gar_dongre: 0.0038
      ngar_dongre: 0.163
      ppl: 3.45
      N: 50
      T: 4
    tf_tg:
      gar_ours: 0.4836
      ngar_ours: 11.8818
      gar_dongre: 0.018
      ngar_dongre: 0.7922
      ppl: 2.57
      N: 50
      T: 4
    ar_base:
      gar_ours: 0.0086
      ngar_ours: 0.0798
      gar_dongre: 0.0118
      ngar_dongre: 0.1265
      ppl: 1.24
      N: 5
      T: 10
    ar_tg:
      gar_ours: 0.0304
      ngar_ours: 0.2632
      gar_dongre: 0.0217
      ngar_dongre: 0.2459
      ppl: 1.32
      N: 5
      T: 10
    gap_ratio_tg_ours: 15.9
    gap_ratio_base_ours: 1.93
    gap_ratio_tg_dongre: 0.83
    vs_qwen_v7_gap_ratio: 32.1
    baseline_mid_gar: 0.0122
- exp_id: llama_tg_training
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: instruction_retention_test
  name: ''
  status: DONE
  conclusion: success
  metrics:
    late_turn_rate_beta0: 0.759
    late_turn_rate_beta3: 0.87
    late_turn_delta: 0.111
    mcnemar_chi2: 3.125
    mcnemar_p: 0.0771
    gar_compliance_r: 0.2003
    gar_compliance_p: 0.007
    category_content_constraint:
      beta0: 0.619
      beta3: 0.857
      delta: 0.238
    category_count_constraint:
      beta0: 1
      beta3: 1
      delta: 0
    category_format_constraint:
      beta0: 1
      beta3: 1
      delta: 0
    category_position_constraint:
      beta0: 0.667
      beta3: 0.733
      delta: 0.067
- exp_id: llama_ar_matched_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ar_base_ours:
      mid_gar: 0.0082
      ngar: 0.1
      ppl: 1.267
    ar_tg_ours:
      mid_gar: 0.0388
      ngar: 0.493
      ppl: 1.413
    ar_base_dongre:
      mid_gar: 0.0051
      ngar: 0.12
      ppl: 1.267
    ar_tg_dongre:
      mid_gar: 0.018
      ngar: 0.431
      ppl: 1.413
    tf_reference:
      tf_tg_ours_ngar: 11.88
      tf_base_ours_ngar: 0.388
      tf_tg_ours_raw: 0.4836
      tf_tg_dongre_raw: 0.018
    matched_gap_analysis:
      gar_ours_raw_gap: 12.5x (TF 0.484 / AR 0.039)
      gar_ours_ngar_gap: 24.1x (TF 11.88 / AR 0.493)
      gar_dongre_raw_gap: 1.002x (TF 0.018 / AR 0.018) — zero gap
      tg_over_base_ar_ours: 4.71x
      tg_over_base_ar_dongre: 3.54x
      conclusion: 'GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure
        bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure
        bias selectively destroys learned goal-attention routing while leaving content-overlap-based
        attention unaffected.'
- exp_id: v8b_ss_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.9316
    final_ntp_loss: 0.9307
    final_gar_loss: 0.0009
    final_gate_mean: 0.9505
    final_gate_std: 0.0508
    final_gate_min: 0.7383
    final_gate_max: 1
    ss_used_ratio: 0.371
    training_time_s: 38773.4
    epoch0_loss: 1.0092
    epoch1_loss: 0.9444
    epoch2_loss: 0.9316
- exp_id: v7_tg_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epoch_1:
      avg_loss: 0.9447
      avg_ntp_loss: 0.9434
      avg_gar_loss: 0.0013
      avg_div_loss: 0
    epoch_2:
      avg_loss: 0.9315
      avg_ntp_loss: 0.9305
      avg_gar_loss: 0.001
      avg_div_loss: 0
    final_gate:
      mean: 0.9467
      std: 0.051
      min: 0.793
      max: 1
    final_gate_profile:
      L0: 0.883
      L1: 0.793
      L2: 0.996
      L3: 0.988
      L4: 0.984
      L5: 0.797
      L6: 0.961
      L7: 0.918
      L8: 0.965
      L9: 0.934
      L10: 0.969
      L11: 0.918
      L12: 0.926
      L13: 0.941
      L14: 0.93
      L15: 0.965
      L16: 0.941
      L17: 0.91
      L18: 0.961
      L19: 0.965
      L20: 0.973
      L21: 0.988
      L22: 0.969
      L23: 0.98
      L24: 0.98
      L25: 0.984
      L26: 0.988
      L27: 1
    training_time_s: 21425.2
- exp_id: eval_v8b_ss_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    iid:
      gar_ours: 0.503
      gar_dongre: 0.394
      ppl: 2.781
      ntp_loss: 0.976
      n_conv: 50
      n_turns: 3
    modelgen:
      gar_ours: 0.418
      gar_dongre: 0.441
      ppl: 1.389
      ntp_loss: 0.325
      n_conv: 5
      n_turns: 10
    gap_ratio: 1.2
    base_iid_ppl: 4.338
    base_modelgen_ppl: 1.351
- exp_id: eval_v7_tg_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    iid_tf:
      gar_ours_mid: 0.5052
      gar_dongre_mid: 0.0119
      ppl: 2.7802
      ntp: 0.9752
    modelgen_ar:
      gar_ours_mid: 0.0165
      gar_dongre_mid: 0.0177
      ppl: 1.3855
      ntp: 0.3223
    gap_ratio: 30.6
    comparison_s42:
      tf_gar_ours_delta: 0.0017
      ar_gar_ours_delta: 0.0008
      gap_ratio_delta: -1.4
- exp_id: llama_lora_only_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_avg_loss: 0.9288
    final_avg_ntp: 0.9279
    final_avg_gar: 0.0009
    gate_fixed: 1
    gate_type: none
    wall_clock_s: 25317
    wall_clock_h: 7.03
    epochs_completed: 3
- exp_id: eval_llama_lora_only_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tf:
      gar_ours: 0.4807
      gar_dongre: 0.0188
      ngar_ours: 11.8031
      ngar_dongre: 0.8261
      ppl: 2.6
      ntp_loss: 0.9366
      n_conversations: 50
      n_turns: 4
    ar:
      gar_ours: 0.0617
      gar_dongre: 0.0226
      ngar_ours: 0.6065
      ngar_dongre: 0.2537
      ppl: 1.32
      ntp_loss: 0.2787
      n_conversations: 5
      n_turns: 10
    gap_ratio_gar_ours: 7.79
- exp_id: eval_llama_ar_n20
  name: ''
  status: DONE
  conclusion: success
  metrics:
    base:
      gar_ours_mean: 0.0088
      gar_ours_std: 0.0056
      gar_ours_median_per_conv: 0.0093
      gar_ours_median_per_turn_pool: 0.0071
      gar_ours_spike_ratio: 0%
      gar_dongre_mean: 0.0049
      gar_dongre_std: 0.0013
      gar_dongre_median: 0.0047
      ngar_ours_mid: 0.1019
      ngar_dongre_mid: 0.1171
      ppl: 1.293
      ppl_std: 0.07
      ntp_loss: 0.2552
    tg:
      gar_ours_mean: 0.0434
      gar_ours_std: 0.1002
      gar_ours_median_per_conv: 0.0179
      gar_ours_median_per_turn_pool: 0.0126
      gar_ours_spike_ratio: 5% (2/40 turns GAR>=0.4)
      gar_dongre_mean: 0.0183
      gar_dongre_std: 0.0198
      gar_dongre_median: 0.0152
      ngar_ours_mid: 0.5357
      ngar_dongre_mid: 0.4436
      ppl: 1.437
      ppl_std: 0.077
      ntp_loss: 0.3612
    lora_only:
      gar_ours_mean: 0.0284
      gar_ours_std: 0.0481
      gar_ours_median_per_conv: 0.0184
      gar_ours_median_per_turn_pool: 0.0133
      gar_ours_spike_ratio: 0%
      gar_dongre_mean: 0.0205
      gar_dongre_std: 0.0241
      gar_dongre_median: 0.016
      ngar_ours_mid: 0.3488
      ngar_dongre_mid: 0.4997
      ppl: 1.419
      ppl_std: 0.075
      ntp_loss: 0.3483
    n_conversations: 20
    n_turns: 4
    mid_turns_definition: turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2).
      All 16 eval entries use same definition.
    stat_pool: 'median_per_conv: median of 20 per-conversation mid-turn averages.
      median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).'
    ranking_gar_ours_mean: TG(0.0434) > LO(0.0284) > Base(0.0088)
    ranking_gar_ours_median_per_conv: TG(0.0179) ≈ LO(0.0184) > Base(0.0093)
    ranking_gar_ours_median_per_turn_pool: TG(0.0126) ≈ LO(0.0133) > Base(0.0071)
    ranking_gar_dongre: LO(0.0205) > TG(0.0183) > Base(0.0049)
    note: Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages
      across N=20). median_per_turn_pool is the alternative statistic from pooled
      individual turns. Both confirm TG ≈ LO (zero-increment).
- exp_id: d048_ss_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_avg_loss: 0.9326
    final_ntp_loss: 0.932
    final_gar_loss: 0.0007
    gate_mean: 0.9527
    gate_std: 0.0589
    gate_min: 0.7383
    gate_min_layer: L4
    gate_max: 1
    ss_usage: 4750/16000 (29.7%)
    ss_fallback: 0
    epochs_completed: 3
    wall_clock_s: 23418
    wall_clock_h: 6.5
- exp_id: d048_ss_s42_resume
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d048_eval_ss_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tf:
      base_gar_ours_mid: 0.0128
      base_gar_dongre_mid: 0.0031
      base_ppl: 4.34
      base_ntp: 1.4
      tg_gar_ours_mid: 0.5025
      tg_gar_dongre_mid: 0.389
      tg_ppl: 2.78
      tg_ntp: 0.98
      baseline_mid_gar: 0.0122
    ar:
      gar_ours_mid: 0.3887
      gar_ours_ci_95:
      - 0.3692
      - 0.3934
      ppl: 1.35
    gap_ratio: 1.29
    n_conversations_tf: 50
    n_conversations_ar: 5
    bootstrap_turns: curve[2:] (turns 3-T)
    note: AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch
      with eval_200.json N=50.
- exp_id: d048_queue_runner
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: d048_ss_s456
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: d048_final_ar_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    beta0:
      base_gar: 0.019
      tg_gar: 0.064
      ug_gar: 0.033
      lo_gar: 0.037
      pcgrad_gar: 0.03
      ss_gar: 0.347
    beta3:
      base_gar: 0.531
      tg_gar: 0.556
      ss_gar: 0.593
    beta5:
      base_gar: 0.704
      tg_gar: 0.727
      ss_gar: 0.717
    wilcoxon_beta0:
      tg_vs_base_p: <0.001
      tg_vs_base_r: 0.802
      ss_vs_tg_p: <0.001
      ss_vs_tg_r: 0.869
    ppl:
      base: 1.447
      tg: 1.432
      ss: 1.442
    n_convs: 39
- exp_id: qwen15b_phase1_diag
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mmlu_eval_all
  name: ''
  status: DONE
  conclusion: success
  metrics:
    base_qwen: 0.7423
    pcgrad_v9_s42: 0.7386
    ss_v8b_s42: 0.7375
    lo_s42: 0.7357
    tg_v7_s42: 0.7347
    ug_s42: 0.7346
- exp_id: d048_split_softmax_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d048_ss_s123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: d048_eval_ss_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tf_gar_ours: 0.5536
    tf_gar_dongre: 0.4106
    tf_ppl: 2.6123
    ar_beta0_gar: 0.4231
    ar_beta0_ppl: 1.4408
    ar_beta3_gar: 0.5903
    ar_beta3_ppl: 1.607
    ar_beta5_gar: 0.7174
    ar_beta5_ppl: 1.7852
    n_convs_tf: 200
    n_convs_ar: 39
- exp_id: p0_ss_steering_eval
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: p1_tf_ar_kl_divergence
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tg_delta_gar: 0.0165
    base_delta_gar: 0.0122
    tg_mean_kl: 0.054
    base_mean_kl: 0.043
    gate_kl_correlation: 0.11
    high_kl_layers: L23-L27, L9
    gar_robustness_ours_tg_base_ratio: 21.4
    gar_robustness_goal_only_ratio: 63
    gar_robustness_ours_all_ratio: 1.7
    gar_robustness_ours_first_ratio: 1.8
- exp_id: p1_llama_ss_training
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: p2_llama_gradient_conflict
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cos_sim_mean: 0.0045
    cos_sim_std: 0.07
    neg_cos_sim_layers_pct: 53.1
    mag_ratio_median: 25.7
    conclusion_note: 'cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion
      text ''widespread conflict'' is misleading — actual finding: NTP and GAR gradients
      are nearly orthogonal on Llama, consistent with Qwen pattern.'
- exp_id: d048_eval_ss_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tf_gar_ours_mid: 0.4964
    tf_gar_dongre_mid: 0.3862
    ar_beta0_gar: 0.4325
    ar_beta0_ppl: 1.4394
    ar_beta3_gar: 0.605
    ar_beta3_ppl: 1.5868
    ar_beta5_gar: 0.7157
    ar_beta5_ppl: 1.8045
    n_convs_ar: 50

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "03ba6bd2-f669-4de4-a1f2-b6a252b87fca",
  "type": "user",
  "uuid": "f01f776a-25ca-43d5-862f-f1dbb519fed0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T08:13:19.739Z_

```json
{
  "parentUuid": "f01f776a-25ca-43d5-862f-f1dbb519fed0",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cd0621fd-4b3c-4759-98c0-8e6e74d9e788",
  "timestamp": "2026-05-24T08:13:19.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T08:13:19.739Z_

```json
{
  "parentUuid": "cd0621fd-4b3c-4759-98c0-8e6e74d9e788",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "898afa45-075b-4a0b-a999-973e7d46a935",
  "timestamp": "2026-05-24T08:13:19.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T08:13:19.739Z_

```json
{
  "parentUuid": "898afa45-075b-4a0b-a999-973e7d46a935",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4e06a138-dc9a-42fb-8c68-b2f46ef7c5a2",
  "timestamp": "2026-05-24T08:13:19.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画 核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general miti…",
  "leafUuid": "4e06a138-dc9a-42fb-8c68-b2f46ef7c5a2",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Exposure bias destroys auxiliary attention losses",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Assistant

_source line 9 · 2026-05-24T08:13:27.252Z_

我先读取 experiment_plan 文件确认所有 planned 实验的最新状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e06a138-dc9a-42fb-8c68-b2f46ef7c5a2",
  "isSidechain": false,
  "requestId": "req_011CbM4M2EPT1pfvuHjpVqzD",
  "type": "assistant",
  "uuid": "9a596553-5bbd-48bf-a30a-28d9beecc0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPksdNdMUcSJjzjEYvFgVJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36395,
      "cache_read_input_tokens": 11447,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 85,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 36395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36395
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T08:13:27.255Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KRVSjuMKruXnfya2YSeuzo`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a596553-5bbd-48bf-a30a-28d9beecc0f9",
  "isSidechain": false,
  "requestId": "req_011CbM4M2EPT1pfvuHjpVqzD",
  "type": "assistant",
  "uuid": "3a7026f1-5422-484d-9a13-d2c6f1c3d7b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPksdNdMUcSJjzjEYvFgVJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 36395,
      "cache_read_input_tokens": 11447,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 85,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 36395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36395
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T08:13:27.289Z_

<details><summary>↩ Tool result · `toolu_01KRVSjuMKruXnfya2YSeuzo`</summary>

```text
projects/redundancy-compound-sparsity/experiment_plan.yaml
projects/redundancy-compound-sparsity-2/experiment_plan.lock
projects/redundancy-compound-sparsity-2/experiment_plan.yaml
projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log
projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829_result.json
projects/phase-gated-compound-sparse/experiment_plan.yaml
projects/turn_residual_gating/experiment_plan.lock
projects/turn_residual_gating/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a7026f1-5422-484d-9a13-d2c6f1c3d7b3",
  "isSidechain": false,
  "promptId": "03ba6bd2-f669-4de4-a1f2-b6a252b87fca",
  "type": "user",
  "uuid": "eace28b4-30f2-45bf-bc7b-ac093f8e0204",
  "toolUseResult": {
    "filenames": [
      "projects/redundancy-compound-sparsity/experiment_plan.yaml",
      "projects/redundancy-compound-sparsity-2/experiment_plan.lock",
      "projects/redundancy-compound-sparsity-2/experiment_plan.yaml",
      "projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829_result.json",
      "projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "projects/turn_residual_gating/experiment_plan.lock",
      "projects/turn_residual_gating/experiment_plan.yaml"
    ],
    "durationMs": 25,
    "numFiles": 8,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3a7026f1-5422-484d-9a13-d2c6f1c3d7b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T08:13:30.752Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FPCssf7W9cEsih9bRxFC1F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eace28b4-30f2-45bf-bc7b-ac093f8e0204",
  "isSidechain": false,
  "requestId": "req_011CbM4Maw9hxAcWG89t5kNU",
  "type": "assistant",
  "uuid": "7c431950-bcdc-4e79-bdee-6557f349c6a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxiBqSguWsoKfCETip9Rnh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 47842,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 47842,
          "cache_creation_input_tokens": 271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 271
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T08:13:30.762Z_

<details><summary>↩ Tool result · `toolu_01FPCssf7W9cEsih9bRxFC1F`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: C1
4	  description: Phase 1 GAR degradation diagnosis on Qwen-2.5-7B (70.8% raw drop)
5	  priority: P0
6	  gpu_budget_hours: 2
7	  deps: []
8	  registry_id: phase1_gar_diag
9	  status: done
10	- id: plan_002
11	  claim: C2
12	  description: ThreadGate v7 training (MSE+gate_div) - training GAR 0.48, inference
13	    GAR 0.016
14	  priority: P0
15	  gpu_budget_hours: 6
16	  deps:
17	  - plan_001
18	  registry_id: phase2_tg_s42_v7
19	  status: done
20	- id: plan_003
21	  claim: C4
22	  description: Uniform Gate ablation - isolate turn conditioning contribution
23	  priority: P0
24	  gpu_budget_hours: 6
25	  deps:
26	  - plan_001
27	  registry_id: phase2_ug_s42
28	  status: done
29	- id: plan_004
30	  claim: C4
31	  description: LoRA-only ablation - isolate gating mechanism contribution
32	  priority: P0
33	  gpu_budget_hours: 6
34	  deps:
35	  - plan_001
36	  registry_id: phase2_lora_only_s42
37	  status: done
38	- id: plan_005
39	  claim: C4
40	  description: Four-way eval (Base/TG/UG/LoRA-only x GAR-ours/Dongre + PPL)
41	  priority: P0
42	  gpu_budget_hours: 2
43	  deps:
44	  - plan_002
45	  - plan_003
46	  - plan_004
47	  registry_id: phase2_4way_eval
48	  status: done
49	- id: plan_006
50	  claim: C3
51	  description: Gradient conflict analysis on v7 (3 epoch checkpoints) - NTP vs GAR
52	    gradient cos_sim + magnitude ratio
53	  priority: P0
54	  gpu_budget_hours: 0.5
55	  deps:
56	  - plan_002
57	  registry_id: analysis_gradient_conflict
58	  status: done
59	- id: plan_007
60	  claim: C3
61	  description: Attention heatmap visualization (4 models x 3 conversations x 28 layers)
62	  priority: P0
63	  gpu_budget_hours: 0.5
64	  deps:
65	  - plan_002
66	  - plan_003
67	  - plan_004
68	  registry_id: analysis_attention_heatmap
69	  status: done
70	- id: plan_008
71	  claim: C2, C4
72	  description: 'Held-out eval: create truly held-out eval set (50 convs, idx>=8000
73	    from UltraChat full) and re-run 4-way eval to validate conclusions on unseen data'
74	  priority: P0
75	  gpu_budget_hours: 2
76	  deps:
77	  - plan_005
78	  status: planned
79	  registry_id: phase2_4way_eval_heldout
80	- id: plan_009
81	  claim: C5
82	  description: Llama-3.1-8B Phase 1 GAR degradation diagnosis - confirm GAR decay
83	    exists on different architecture
84	  priority: P0
85	  gpu_budget_hours: 0.5
86	  deps: []
87	  status: planned
88	  registry_id: llama_phase1_gar_diag
89	- id: plan_010
90	  claim: C5
91	  description: Llama-3.1-8B ThreadGate v7 training - replicate Qwen setup on Llama
92	  priority: P0
93	  gpu_budget_hours: 7
94	  deps:
95	  - plan_009
96	  status: planned
97	  registry_id: llama_tg_s42
98	- id: plan_011
99	  claim: C5
100	  description: Llama-3.1-8B LoRA-only training - cross-model gating redundancy validation
101	    (D020)
102	  priority: P0
103	  gpu_budget_hours: 7
104	  deps:
105	  - plan_009
106	  status: planned
107	  registry_id: llama_lora_only_s42
108	- id: plan_012
109	  claim: C5
110	  description: Llama-3.1-8B 3-way eval (Base/TG/LoRA-only x GAR + PPL) on held-out
111	    data
112	  priority: P0
113	  gpu_budget_hours: 1
114	  deps:
115	  - plan_010
116	  - plan_011
117	  status: planned
118	  registry_id: llama_eval_s42
119	- id: plan_013
120	  claim: C3
121	  description: Llama-3.1-8B gradient conflict analysis - verify NTP-GAR competition
122	    is model-agnostic
123	  priority: P1
124	  gpu_budget_hours: 0.5
125	  deps:
126	  - plan_010
127	  status: done
128	  result: 'cos_sim=0.0045 (near-orthogonal, not conflict), neg_layers=53.1% (near
129	    random), mag_ratio_median=25.7×. Cross-model confirms: gradients not conflicting,
130	    NTP magnitude dominates. Consistent with Qwen. D054.'
131	- id: plan_014
132	  claim: W3
133	  description: Downstream task sanity check - simple instruction retention test across
134	    turns to link GAR to task performance
135	  priority: P2
136	  gpu_budget_hours: 1
137	  deps:
138	  - plan_005
139	  status: done
140	  registry_id: instruction_retention_test
141	  result: 'β=3 late-turn retention 87.0% vs β=0 75.9%, delta=+11.1pp. GAR-compliance
142	    correlation r=0.200, p=0.007. Written to Appendix C. D046.'
143	- id: plan_015
144	  claim: C4, W7
145	  description: Statistical significance analysis - paired bootstrap CI from held-out
146	    eval (50 convs) for TG-LoRA-only comparison. If CI includes 0 → statistically
147	    supports 'zero benefit'. Addresses Dream W3 (single seed).
148	  priority: P1
149	  gpu_budget_hours: 0.5
150	  deps:
151	  - plan_008
152	  status: done
153	  registry_id: worker_analysis_bootstrap_ci_tg_vs_lora_20260519T144212
154	  result: 'PASS: All GAR-ours and PPL 95% CIs include 0 (TG-LO GAR: [-0.0018,+0.0036],
155	    UG-LO: [-0.0006,+0.0045], TG-UG: [-0.0030,+0.0006]). Statistically confirms zero
156	    benefit. W7 addressed.'
157	- id: plan_016
158	  claim: W8
159	  description: Exposure-bias mitigation test - train ThreadGate v7 with scheduled
160	    sampling applied to GAR loss (mix teacher-forced + model-generated contexts).
161	    Test whether closing exposure bias gap narrows the 30x training-inference GAR
162	    gap. Constructive direction that upgrades paper from pure negative result.
163	  priority: P1
164	  gpu_budget_hours: 8
165	  deps:
166	  - plan_008
167	  status: planned
168	  registry_id: phase2_tg_s42_v8_schedsampling
169	- id: plan_017
170	  claim: R4
171	  description: Code-paper architecture verification - confirm ThreadGate implementation
172	    matches paper Eq.3 (gate on residual vs gate on sub-layer output). Quick code
173	    audit, no GPU.
174	  priority: P0
175	  gpu_budget_hours: 0
176	  deps: []
177	  status: done
178	  registry_id: worker_analysis_code_paper_arch_verify_20260519T144058
179	  result: 'CRITICAL: code implements x+g·f(x) (ReZero-style), dream paper.tex wrote
180	    g·x+f(x). Semantically opposite when g→0. Data unaffected. D023.'
181	- id: plan_018
182	  claim: C3, W8
183	  description: PCGrad baseline - project NTP gradient onto GAR-orthogonal plane for
184	    gate params only. If 30x gap persists after removing gradient conflict → causal
185	    evidence that exposure bias (not gradient competition) is the root cause.
186	  priority: P0
187	  gpu_budget_hours: 8
188	  deps:
189	  - plan_006
190	  registry_id: phase2_tg_s42_v9_pcgrad
191	  status: done
192	- id: plan_019
193	  claim: C2, MF5
194	  description: Multi-seed validation — train TG v7 + LoRA-only with seed=123 on Qwen.
195	    Provide mean±std for 30x gap. 1 extra seed sufficient given extreme effect size.
196	  priority: P1
197	  gpu_budget_hours: 6
198	  deps:
199	  - plan_002
200	  status: planned
201	  registry_id: v7_tg_s123
202	- id: plan_020
203	  claim: C4, MF6
204	  description: Expanded eval set — increase from 50 to 200 conversations (idx>=7000
205	    from UltraChat). Boost bootstrap CI statistical power.
206	  priority: P1
207	  gpu_budget_hours: 2
208	  deps:
209	  - plan_008
210	  status: superseded
211	  result: 'Partially done: TF eval uses eval_200 (N=200), AR eval uses d048_final_ar
212	    (N=50). AR N=200 not planned — N=50 sufficient given extreme effect sizes. No
213	    additional GPU needed.'
214	- id: plan_022
215	  claim: C3, SF4
216	  description: λ_GAR sensitivity — train v7 with λ_GAR=10 (1 epoch only). Show gradient
217	    competition trend under higher GAR weight. If budget allows, add λ=0.1.
218	  priority: P2
219	  gpu_budget_hours: 2
220	  deps:
221	  - plan_002
222	  status: planned
223	- id: plan_023
224	  claim: W8, C3
225	  description: 'v8b: Fixed Scheduled Sampling — fix compute_gar_loss len==1 bug (Option
226	    A: handle single-turn mse_target), fix OOM (reduce batch/gen_length), use lambda_gar=1.0
227	    (match v7). Tests whether training on model-generated text closes the 30x distribution
228	    shift gap. If successful, paper upgrades from pure negative to ''diagnosis + initial
229	    remedy''. D026.'
230	  priority: P1
231	  gpu_budget_hours: 8
232	  deps:
233	  - plan_002
234	  status: planned
235	  registry_id: phase2_tg_s42_v8b_resume
236	- id: plan_024
237	  claim: C4
238	  description: 'SS + β-steering combined eval — CANCELLED. Data already exists in
239	    ss_s42_ar_n50.json (β=0,3,5). SS and steering are substitutes not complements
240	    (β=5: SS 0.717 ≈ TG 0.727). No need to re-run.'
241	  priority: P0
242	  gpu_budget_hours: 1
243	  deps:
244	  - plan_023
245	  status: killed
246	  registry_id: p0_ss_steering_eval
247	  result: 'Cancelled — existing data shows SS+steering do not stack. β=0: SS 0.347
248	    (independent value). β=3: SS +0.037 marginal. β=5: SS ≈ TG (converge). Discussion
249	    added to paper.'
250	- id: plan_025
251	  claim: C1
252	  description: 'TF vs AR attention KL divergence — compute per-head KL(P_TF||P_AR)
253	    on 50 conversations to quantify attention distribution shift. If GAR-relevant heads
254	    show larger KL → mechanistic evidence for why GAR collapses. Pure CPU analysis.'
255	  priority: P1
256	  gpu_budget_hours: 0
257	  deps:
258	  - plan_002
259	  status: planned
260	- id: plan_026
261	  claim: C5, C4
262	  description: 'Llama-3.1-8B Scheduled Sampling — replicate SS training on Llama to
263	    verify cross-model gap compression. If Llama gap also compresses → SS is a general
264	    mitigation, not model-specific.'
265	  priority: P1
266	  gpu_budget_hours: 10
267	  deps:
268	  - plan_010
269	  status: planned
270	- id: plan_027
271	  claim: C4, W7
272	  description: 'SS 3-seed validation — s42 (gap 1.45×), s123 (TF NaN, AR 0.423),
273	    s456 (gap 1.15×). 3-seed AR GAR β=0: 0.401±0.047. β=3/5 extremely stable (std<0.01).
274	    Addresses single-seed reviewer concern.'
275	  priority: P0
276	  gpu_budget_hours: 16
277	  deps:
278	  - plan_023
279	  status: done
280	  result: '3-seed complete. TF GAR 0.498±0.004 (s42=0.503, s123=0.495, s456=0.496).
281	    AR GAR β=0: 0.401±0.047 (s42=0.347, s123=0.423, s456=0.433). Gap 1.26±0.17 (range
282	    1.15–1.45×, 3 valid seeds). β=3: 0.596±0.008. β=5: 0.717±0.001. PPL β=0: 1.441±0.001.
283	    W7 addressed.'
284	- id: plan_028
285	  claim: C2, W5
286	  description: 'Alternative GAR definition robustness — 4 token selections (last/all/first/goal-only)
287	    × 3 checkpoints (Base/TG/SS). Needed GPU re-eval (raw attention not saved).'
288	  priority: P1
289	  gpu_budget_hours: 0.5
290	  deps:
291	  - plan_027
292	  status: done
293	  result: 'TG only improves last-token GAR (0.325), all/first-token near-zero (0.025/0.039).
294	    SS improves ALL 4 definitions >0.36. SS builds broader goal-attention pattern,
295	    not position-specific overfitting. Base consistently <0.022. D054.'
296	- id: plan_029
297	  claim: C2, W7
298	  description: 'SS 4th seed (s789) — additional seed to strengthen mean±std. Training
299	    ~6.5h + eval ~1h. ROI lower than Llama SS (cross-model > extra seed given extreme
300	    effect size). Run if time permits after plan_026.'
301	  priority: P2
302	  gpu_budget_hours: 8
303	  deps:
304	  - plan_027
305	  status: planned
306	- id: plan_030
307	  claim: C1, C2
308	  description: 'Long conversation eval (>10 turns) — test whether exposure bias gap
309	    worsens with conversation length. Need to identify suitable long conversations
310	    from UltraChat. Eval ~1-2h.'
311	  priority: P2
312	  gpu_budget_hours: 2
313	  deps:
314	  - plan_027
315	  status: planned
316	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c431950-bcdc-4e79-bdee-6557f349c6a6",
  "isSidechain": false,
  "promptId": "03ba6bd2-f669-4de4-a1f2-b6a252b87fca",
  "type": "user",
  "uuid": "fe957898-0c07-4217-9f60-b6fe0469fd8c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: C1\n  description: Phase 1 GAR degradation diagnosis on Qwen-2.5-7B (70.8% raw drop)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: phase1_gar_diag\n  status: done\n- id: plan_002\n  claim: C2\n  description: ThreadGate v7 training (MSE+gate_div) - training GAR 0.48, inference\n    GAR 0.016\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_tg_s42_v7\n  status: done\n- id: plan_003\n  claim: C4\n  description: Uniform Gate ablation - isolate turn conditioning contribution\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_ug_s42\n  status: done\n- id: plan_004\n  claim: C4\n  description: LoRA-only ablation - isolate gating mechanism contribution\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_lora_only_s42\n  status: done\n- id: plan_005\n  claim: C4\n  description: Four-way eval (Base/TG/UG/LoRA-only x GAR-ours/Dongre + PPL)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_002\n  - plan_003\n  - plan_004\n  registry_id: phase2_4way_eval\n  status: done\n- id: plan_006\n  claim: C3\n  description: Gradient conflict analysis on v7 (3 epoch checkpoints) - NTP vs GAR\n    gradient cos_sim + magnitude ratio\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  registry_id: analysis_gradient_conflict\n  status: done\n- id: plan_007\n  claim: C3\n  description: Attention heatmap visualization (4 models x 3 conversations x 28 layers)\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  - plan_003\n  - plan_004\n  registry_id: analysis_attention_heatmap\n  status: done\n- id: plan_008\n  claim: C2, C4\n  description: 'Held-out eval: create truly held-out eval set (50 convs, idx>=8000\n    from UltraChat full) and re-run 4-way eval to validate conclusions on unseen data'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  status: planned\n  registry_id: phase2_4way_eval_heldout\n- id: plan_009\n  claim: C5\n  description: Llama-3.1-8B Phase 1 GAR degradation diagnosis - confirm GAR decay\n    exists on different architecture\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps: []\n  status: planned\n  registry_id: llama_phase1_gar_diag\n- id: plan_010\n  claim: C5\n  description: Llama-3.1-8B ThreadGate v7 training - replicate Qwen setup on Llama\n  priority: P0\n  gpu_budget_hours: 7\n  deps:\n  - plan_009\n  status: planned\n  registry_id: llama_tg_s42\n- id: plan_011\n  claim: C5\n  description: Llama-3.1-8B LoRA-only training - cross-model gating redundancy validation\n    (D020)\n  priority: P0\n  gpu_budget_hours: 7\n  deps:\n  - plan_009\n  status: planned\n  registry_id: llama_lora_only_s42\n- id: plan_012\n  claim: C5\n  description: Llama-3.1-8B 3-way eval (Base/TG/LoRA-only x GAR + PPL) on held-out\n    data\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_010\n  - plan_011\n  status: planned\n  registry_id: llama_eval_s42\n- id: plan_013\n  claim: C3\n  description: Llama-3.1-8B gradient conflict analysis - verify NTP-GAR competition\n    is model-agnostic\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_010\n  status: done\n  result: 'cos_sim=0.0045 (near-orthogonal, not conflict), neg_layers=53.1% (near\n    random), mag_ratio_median=25.7×. Cross-model confirms: gradients not conflicting,\n    NTP magnitude dominates. Consistent with Qwen. D054.'\n- id: plan_014\n  claim: W3\n  description: Downstream task sanity check - simple instruction retention test across\n    turns to link GAR to task performance\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_005\n  status: done\n  registry_id: instruction_retention_test\n  result: 'β=3 late-turn retention 87.0% vs β=0 75.9%, delta=+11.1pp. GAR-compliance\n    correlation r=0.200, p=0.007. Written to Appendix C. D046.'\n- id: plan_015\n  claim: C4, W7\n  description: Statistical significance analysis - paired bootstrap CI from held-out\n    eval (50 convs) for TG-LoRA-only comparison. If CI includes 0 → statistically\n    supports 'zero benefit'. Addresses Dream W3 (single seed).\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_008\n  status: done\n  registry_id: worker_analysis_bootstrap_ci_tg_vs_lora_20260519T144212\n  result: 'PASS: All GAR-ours and PPL 95% CIs include 0 (TG-LO GAR: [-0.0018,+0.0036],\n    UG-LO: [-0.0006,+0.0045], TG-UG: [-0.0030,+0.0006]). Statistically confirms zero\n    benefit. W7 addressed.'\n- id: plan_016\n  claim: W8\n  description: Exposure-bias mitigation test - train ThreadGate v7 with scheduled\n    sampling applied to GAR loss (mix teacher-forced + model-generated contexts).\n    Test whether closing exposure bias gap narrows the 30x training-inference GAR\n    gap. Constructive direction that upgrades paper from pure negative result.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_008\n  status: planned\n  registry_id: phase2_tg_s42_v8_schedsampling\n- id: plan_017\n  claim: R4\n  description: Code-paper architecture verification - confirm ThreadGate implementation\n    matches paper Eq.3 (gate on residual vs gate on sub-layer output). Quick code\n    audit, no GPU.\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: done\n  registry_id: worker_analysis_code_paper_arch_verify_20260519T144058\n  result: 'CRITICAL: code implements x+g·f(x) (ReZero-style), dream paper.tex wrote\n    g·x+f(x). Semantically opposite when g→0. Data unaffected. D023.'\n- id: plan_018\n  claim: C3, W8\n  description: PCGrad baseline - project NTP gradient onto GAR-orthogonal plane for\n    gate params only. If 30x gap persists after removing gradient conflict → causal\n    evidence that exposure bias (not gradient competition) is the root cause.\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_006\n  registry_id: phase2_tg_s42_v9_pcgrad\n  status: done\n- id: plan_019\n  claim: C2, MF5\n  description: Multi-seed validation — train TG v7 + LoRA-only with seed=123 on Qwen.\n    Provide mean±std for 30x gap. 1 extra seed sufficient given extreme effect size.\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_002\n  status: planned\n  registry_id: v7_tg_s123\n- id: plan_020\n  claim: C4, MF6\n  description: Expanded eval set — increase from 50 to 200 conversations (idx>=7000\n    from UltraChat). Boost bootstrap CI statistical power.\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  status: superseded\n  result: 'Partially done: TF eval uses eval_200 (N=200), AR eval uses d048_final_ar\n    (N=50). AR N=200 not planned — N=50 sufficient given extreme effect sizes. No\n    additional GPU needed.'\n- id: plan_022\n  claim: C3, SF4\n  description: λ_GAR sensitivity — train v7 with λ_GAR=10 (1 epoch only). Show gradient\n    competition trend under higher GAR weight. If budget allows, add λ=0.1.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_002\n  status: planned\n- id: plan_023\n  claim: W8, C3\n  description: 'v8b: Fixed Scheduled Sampling — fix compute_gar_loss len==1 bug (Option\n    A: handle single-turn mse_target), fix OOM (reduce batch/gen_length), use lambda_gar=1.0\n    (match v7). Tests whether training on model-generated text closes the 30x distribution\n    shift gap. If successful, paper upgrades from pure negative to ''diagnosis + initial\n    remedy''. D026.'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  status: planned\n  registry_id: phase2_tg_s42_v8b_resume\n- id: plan_024\n  claim: C4\n  description: 'SS + β-steering combined eval — CANCELLED. Data already exists in\n    ss_s42_ar_n50.json (β=0,3,5). SS and steering are substitutes not complements\n    (β=5: SS 0.717 ≈ TG 0.727). No need to re-run.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_023\n  status: killed\n  registry_id: p0_ss_steering_eval\n  result: 'Cancelled — existing data shows SS+steering do not stack. β=0: SS 0.347\n    (independent value). β=3: SS +0.037 marginal. β=5: SS ≈ TG (converge). Discussion\n    added to paper.'\n- id: plan_025\n  claim: C1\n  description: 'TF vs AR attention KL divergence — compute per-head KL(P_TF||P_AR)\n    on 50 conversations to quantify attention distribution shift. If GAR-relevant heads\n    show larger KL → mechanistic evidence for why GAR collapses. Pure CPU analysis.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_026\n  claim: C5, C4\n  description: 'Llama-3.1-8B Scheduled Sampling — replicate SS training on Llama to\n    verify cross-model gap compression. If Llama gap also compresses → SS is a general\n    mitigation, not model-specific.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_010\n  status: planned\n- id: plan_027\n  claim: C4, W7\n  description: 'SS 3-seed validation — s42 (gap 1.45×), s123 (TF NaN, AR 0.423),\n    s456 (gap 1.15×). 3-seed AR GAR β=0: 0.401±0.047. β=3/5 extremely stable (std<0.01).\n    Addresses single-seed reviewer concern.'\n  priority: P0\n  gpu_budget_hours: 16\n  deps:\n  - plan_023\n  status: done\n  result: '3-seed complete. TF GAR 0.498±0.004 (s42=0.503, s123=0.495, s456=0.496).\n    AR GAR β=0: 0.401±0.047 (s42=0.347, s123=0.423, s456=0.433). Gap 1.26±0.17 (range\n    1.15–1.45×, 3 valid seeds). β=3: 0.596±0.008. β=5: 0.717±0.001. PPL β=0: 1.441±0.001.\n    W7 addressed.'\n- id: plan_028\n  claim: C2, W5\n  description: 'Alternative GAR definition robustness — 4 token selections (last/all/first/goal-only)\n    × 3 checkpoints (Base/TG/SS). Needed GPU re-eval (raw attention not saved).'\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_027\n  status: done\n  result: 'TG only improves last-token GAR (0.325), all/first-token near-zero (0.025/0.039).\n    SS improves ALL 4 definitions >0.36. SS builds broader goal-attention pattern,\n    not position-specific overfitting. Base consistently <0.022. D054.'\n- id: plan_029\n  claim: C2, W7\n  description: 'SS 4th seed (s789) — additional seed to strengthen mean±std. Training\n    ~6.5h + eval ~1h. ROI lower than Llama SS (cross-model > extra seed given extreme\n    effect size). Run if time permits after plan_026.'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_027\n  status: planned\n- id: plan_030\n  claim: C1, C2\n  description: 'Long conversation eval (>10 turns) — test whether exposure bias gap\n    worsens with conversation length. Need to identify suitable long conversations\n    from UltraChat. Eval ~1-2h.'\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_027\n  status: planned\n",
      "numLines": 316,
      "startLine": 1,
      "totalLines": 316
    }
  },
  "sourceToolAssistantUUID": "7c431950-bcdc-4e79-bdee-6557f349c6a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-24T08:13:30.790Z_

````json
{
  "parentUuid": "fe957898-0c07-4217-9f60-b6fe0469fd8c",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**turn_residual_gating**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"turn_residual_gating\")` 或 `load_project_config(\"turn_residual_gating\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n- **[项目]** method overview效果不好，不要了，我们直接将headline result作为主图。注意要把最重要的结果图放到最前面，不一定是文中对应位置提到的，而是和paper topic最相关的，这很关键，正文里至少放4-5个可视化图吧，美观度一定要高；附录中内容注意别和正文重复\n- **[项目]** 在配图中使用的配色饱和度对比别太高了，美观性很重要，从distilled论文中吸取经验\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成高品质学术概念图（架构/流程/framework）。统计图不要用 PaperBanana，用 draw-paper-figure。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **distilled-research** — Multi-turn LLM depth/gating/attention research patterns — baselines, metrics, experimental design consensus, competitor landscape, and research gaps distilled from 25 papers  →  `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/skills/projects/turn_residual_gating/distilled-research.skill.md`\n- **distilled-writing** — Narrative structure, figure/table design, and visual rhetoric patterns for multi-turn/depth/gating LLM papers — distilled from 8 deep-read papers at ICLR/NeurIPS/ACL/COLM 2024-2025  →  `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/skills/projects/turn_residual_gating/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/turn_residual_gating/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "add04f58-0ec3-496b-a0f1-8bb63cbee956",
  "timestamp": "2026-05-24T08:13:30.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画 核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general miti…",
  "leafUuid": "add04f58-0ec3-496b-a0f1-8bb63cbee956",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Exposure bias destroys auxiliary attention losses",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Assistant

_source line 17 · 2026-05-24T08:15:04.644Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for every "planned" experiment in the experiment_plan, under the "best" tier scenario. Let me identify which experiments have status "planned":

Looking at the experiment_plan from the CLAUDE.md context (which has more up-to-date status info than the file):

From the CLAUDE.md context, let me check each plan's status:
- plan_001: DONE
- plan_002: DONE
- plan_003: DONE


- plan_004 through plan_012: DONE
- plan_013: planned (but has a result string)
- plan_014: DONE
- plan_015: orphaned (has result)
- plan_016: DONE (failed)
- plan_017: orphaned (has result)
- plan_018 through plan_019: DONE
- plan_020: planned (has result - partially done)

So the experiments I need to generate predicted data for are plan_013 and plan_020, both marked as "planned" even though they have some result data already.

Looking at the rest of the experiment plan, I see plan_022 through plan_030 have various statuses. Many of them are marked "planned" but some actually have result fields, which means they're already done. Let me sort through which ones are truly planned versus which ones have already been executed. I'm noticing the discrepancy between what the user provided and what's actually in the system—some experiments marked as "planned" already have results attached. Looking at the request more carefully, they want detailed data predictions for every experiment with "planned" status, regardless of whether results exist elsewhere. I should generate comprehensive imagined results for the truly unfinished experiments while incorporating the existing data from those that already have outcomes. I need to clarify what the user is actually asking for—they want predictions for all planned experiments in the tier scenario, regardless of whether results already exist. For experiments with existing results, I should validate those results align with the best tier assumptions, and for the truly unfinished ones, I'll generate predictions. Let me map out which experiments are actually planned and need coverage. Now I'm looking at the performance metrics ranges across the different model configurations and evaluation criteria to establish what constitutes success under the best-case scenario. I need to structure these predictions into a YAML output, being careful with the formatting.

Looking at the experimental plans, I'm reviewing the gradient conflict analysis results which show that NTP magnitude dominance holds consistently across models, then examining the evaluation set expansion where the current AR sample size appears adequate, and finally considering the sensitivity analysis for the GAR loss weight where increasing it to 10× still doesn't overcome the fundamental gradient magnitude imbalance that drives the model collapse at inference.

For the attention analysis, I'm planning to compute KL divergence between teacher-forcing and autoregressive attention patterns per head, expecting to find that goal-attending heads in later layers show the largest divergence and mechanistically explain the GAR failure mode. The Llama self-supervised training should yield performance in the target range with modest gap ratios, and the three-seed validation confirms the autoregressive GAR performance is stable around 0.40.

Now I'm looking at alternative GAR definitions—teacher-forcing only helps the final token while self-supervised improves across all four metrics above 0.36. Adding a fourth seed should tighten the confidence intervals and keep the mean close to the three-seed estimate. For the longer conversation evaluation, I expect exposure bias to compound with sequence length, but self-supervised training should maintain its advantage even as conversations get longer.

Let me pull together the full YAML configuration now, using the detailed experiment plan from the context as the authoritative source. Writing the YAML with experiment predictions...

For plan_022, I'm expecting the λ_GAR sensitivity test to show that even aggressive weighting doesn't fix the inference collapse—training GAR might reach 0.55-0.60 but autoregressive GAR stays near 0.02, confirming the gap is driven by distribution shift rather than gradient magnitude. For plan_025, I'm setting up the per-head KL divergence analysis to quantify how much the attention distributions diverge between teacher forcing and autoregressive modes. Now looking at the additional seeds for plan_029, the mean GAR values are tightening slightly with the fourth seed included, and the β=3 and β=5 results show the expected scaling behavior. For plan_030, I'm testing how the gap between TG and SS evolves across longer conversations—TG's gap degrades significantly at 20 turns while SS remains stable, confirming its robustness to extended context. Now I'm thinking through what tables and figures would best present these results in the paper and planning to write out the full experimental configuration in YAML format.

I need to double-check the status of a few experiments—plan_013 and plan_020 show results in the registry despite being marked as planned, and plan_026 (Llama SS training) is currently running. Let me compile the comprehensive output with proper table formatting using YAML flow sequences for the data.

For the experiments with known results, I'll present those actual findings as the best-tier predictions since they already demonstrate the outcomes. For the truly unfinished ones like plan_022, plan_025, plan_029, and plan_030, I'll generate predictions that align with the cross-model NTP magnitude dominance narrative. Plan_013's gradient conflict results show cos_sim=0.0045 with 53.1% negative layers, plan_020's expanded evaluation used different sample sizes across frameworks, and plan_022's λ_GAR sensitivity should peak around λ=10 under the best-tier scenario.

For plan_025, I expect to see clear mechanistic evidence with high KL divergence in late layers correlating with gate suppression. Plan_026 should show the semantic similarity gap compressing to 2× or less, confirming the generality of the approach. Plan_027's known results show AR GAR at 0.401±0.047 with a gap of 1.26±0.17 across three seeds. Plan_028 already demonstrates that semantic similarity improves all four alternative GAR definitions while token-generation only improves the last-token variant. For plan_029, adding a fourth seed should tighten the variance while keeping the mean around 0.40. Plan_030's long conversation evaluation should reveal that the gap worsens with conversation length for token-generation but remains stable for semantic similarity.

Now I'm organizing the YAML structure with analysis fields and figure descriptions. For each plan, I need to specify the key tables and figures—like cross-model gradient comparisons for plan_013, bootstrap confidence intervals for plan_020, sensitivity curves for plan_022, KL heatmaps and scatter plots for plan_025, and cross-model summaries for plan_026 and beyond.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "add04f58-0ec3-496b-a0f1-8bb63cbee956",
  "isSidechain": false,
  "requestId": "req_011CbM4MqQnraWfmWNMLthwd",
  "type": "assistant",
  "uuid": "0f549cd5-d912-4b38-ab11-7a76cc0f1068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191dBUnPMZPhBYz7MxPQz9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10496,
      "cache_read_input_tokens": 48113,
      "output_tokens": 4398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4398,
          "cache_read_input_tokens": 48113,
          "cache_creation_input_tokens": 10496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10496
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-24T08:15:04.790Z_

Now let me check the Llama SS training status since it's listed as RUNNING in the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f549cd5-d912-4b38-ab11-7a76cc0f1068",
  "isSidechain": false,
  "requestId": "req_011CbM4MqQnraWfmWNMLthwd",
  "type": "assistant",
  "uuid": "7b0e876d-0c22-44c4-bcf3-0aad1ef198d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191dBUnPMZPhBYz7MxPQz9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10496,
      "cache_read_input_tokens": 48113,
      "output_tokens": 4398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4398,
          "cache_read_input_tokens": 48113,
          "cache_creation_input_tokens": 10496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10496
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T08:15:06.416Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GWvhfSBfBTcR5WNU1yJNwR`</summary>

```json
{
  "pattern": "p1_llama_ss_training",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b0e876d-0c22-44c4-bcf3-0aad1ef198d3",
  "isSidechain": false,
  "requestId": "req_011CbM4MqQnraWfmWNMLthwd",
  "type": "assistant",
  "uuid": "3c3092d7-e632-43e1-bcb9-952836733f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191dBUnPMZPhBYz7MxPQz9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10496,
      "cache_read_input_tokens": 48113,
      "output_tokens": 4398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4398,
          "cache_read_input_tokens": 48113,
          "cache_creation_input_tokens": 10496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10496
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T08:15:06.607Z_

<details><summary>↩ Tool result · `toolu_01GWvhfSBfBTcR5WNU1yJNwR`</summary>

```text
&lt;persisted-output>
Output too large (58.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11/642a24ab-9637-448d-be97-8ff6319b4917/tool-results/toolu_01GWvhfSBfBTcR5WNU1yJNwR.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-1-{
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json:2:  "exp_id": "p1_llama_ss_training",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-3-  "project": "turn_residual_gating",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-4-  "state": "RUNNING",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-5-  "previous_state": "QUEUED",
--
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-17-      "model_name": "meta-llama/Llama-3.1-8B-Instruct",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-18-      "seed": 42,
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-19-      "checkpoint_path": "runs/llama_ss_s42/",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json:20:      "log_path": "logs/p1_llama_ss_training.log",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-21-      "pid": 158507,
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-22-      "hyperparams": {
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-23-        "lr": "2e-4",
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json-1-{
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json:2:  "exp_id": "p1_llama_ss_training",
projects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json-3-  "project": "turn_residual_gating",
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c3092d7-e632-43e1-bcb9-952836733f09",
  "isSidechain": false,
  "promptId": "03ba6bd2-f669-4de4-a1f2-b6a252b87fca",
  "type": "user",
  "uuid": "1dc1a873-3bde-48b6-9e9c-75da9325713e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-1-{\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json:2:  \"exp_id\": \"p1_llama_ss_training\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-3-  \"project\": \"turn_residual_gating\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-4-  \"state\": \"RUNNING\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-5-  \"previous_state\": \"QUEUED\",\n--\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-17-      \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-18-      \"seed\": 42,\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-19-      \"checkpoint_path\": \"runs/llama_ss_s42/\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json:20:      \"log_path\": \"logs/p1_llama_ss_training.log\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-21-      \"pid\": 158507,\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-22-      \"hyperparams\": {\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json-23-        \"lr\": \"2e-4\",\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json-1-{\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json:2:  \"exp_id\": \"p1_llama_ss_training\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json-3-  \"project\": \"turn_residual_gating\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json-4-  \"state\": \"QUEUED\",\nprojects/turn_residual_gating/checkpoints/p1_llama_ss_training_QUEUED_20260524T072050.json-5-  \"previous_state\": \"PREPARING\",\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-5-## 运行中\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-6-| exp_id | 假设 | 状态 | 关键指标 | W&B |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-7-|--------|------|------|---------|-----|\nprojects/turn_residual_gating/report.md:8:| p1_llama_ss_training | SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims. | — | — | — |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-9-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-10-## 待处理\nprojects/turn_residual_gating/report.md-11-- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\n--\nprojects/turn_residual_gating/registry.yaml-2353-      log_path: logs/p1_kl_divergence_step2.log\nprojects/turn_residual_gating/registry.yaml-2354-    conclusion: success\nprojects/turn_residual_gating/registry.yaml-2355-    completed_at: '2026-05-24T07:18:06.521Z'\nprojects/turn_residual_gating/registry.yaml:2356:  p1_llama_ss_training:\nprojects/turn_residual_gating/registry.yaml-2357-    status: RUNNING\nprojects/turn_residual_gating/registry.yaml-2358-    retry_count: 0\nprojects/turn_residual_gating/registry.yaml-2359-    created_at: '2026-05-23T19:37:48.689Z'\n--\nprojects/turn_residual_gating/registry.yaml-2369-      model_name: meta-llama/Llama-3.1-8B-Instruct\nprojects/turn_residual_gating/registry.yaml-2370-      seed: 42\nprojects/turn_residual_gating/registry.yaml-2371-      checkpoint_path: runs/llama_ss_s42/\nprojects/turn_residual_gating/registry.yaml:2372:      log_path: logs/p1_llama_ss_training.log\nprojects/turn_residual_gating/registry.yaml-2373-      pid: 158507\nprojects/turn_residual_gating/registry.yaml-2374-      hyperparams:\nprojects/turn_residual_gating/registry.yaml-2375-        lr: 2e-4\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-44-{\"ts\": \"2026-05-23T19:49:10.493674+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called Grep\", \"tool\": \"Grep\", \"tool_args\": {\"pattern\": \"~30\", \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper_framing.md\", \"output_mode\": \"content\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-45-{\"ts\": \"2026-05-23T19:49:10.494034+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"7:> 最后更新: 2026-05-23 (Framing 升级 + 数字同步: gap 统一为 8×–27×（论文 N=50 数据），~30× 旧数字已替换; SS 升为独立 Results; 新增第 5 条贡献; narrative arc 改为\\\"发现+定位+修复\\\")\", \"tool\": \"Grep\", \"elapsed_ms\": 0}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-46-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:47:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-48-{\"ts\": \"2026-05-23T19:50:58.570799+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_resource_inventory,mcp__agent-ml-research__director_post_to_paper_agent,mcp__agent-ml-research__director_reply_to_user,mcp__agent-ml-research__director_post_to_main_agent\", \"max_results\": \"5\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-49-{\"ts\": \"2026-05-23T19:50:58.571260+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 0}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-50-{\"ts\": \"2026-05-23T19:51:01.808981+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__load_project_config\", \"tool\": \"mcp__agent-ml-research__load_project_config\", \"tool_args\": {\"project_name\": \"turn_residual_gating\", \"section\": \"execution\"}}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-64-{\"ts\": \"2026-05-23T19:58:36.772684+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"Agent 确认 P0 取消并更新了排期。KL divergence 可 CPU 并行，Agent 处理完审计修复后可随时启动。队列后续两条（审计修复 + worker done）会自动处理，无需干预。\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-65-{\"ts\": \"2026-05-23T19:58:38.762005+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"[Agent 回复]:\\nP0 已取消并记录原因。Worker (p0 脚本准备) 已派出但无 GPU 影响——脚本不会被执行。\", \"source\": \"main_agent\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-66-{\"ts\": \"2026-05-23T19:58:43.197900+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"No response requested.\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:67:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-68-{\"ts\": \"2026-05-23T20:00:08.109944+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"No response requested.\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-69-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-70-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-96-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-97-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-98-{\"ts\": \"2026-05-23T20:11:46.495974+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"No response requested.\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:99:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-100-{\"ts\": \"2026-05-23T20:21:26.230541+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__urgent_agent_message\", \"max_results\": \"1\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-101-{\"ts\": \"2026-05-23T20:21:26.281605+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 51}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-102-[Omitted long context line]\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-315-{\"ts\": \"2026-05-24T04:00:45.142716+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__director_get_project_overview\", \"tool\": \"mcp__agent-ml-research__director_get_project_overview\", \"tool_args\": {\"project\": \"turn_residual_gating\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-316-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-317-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:318:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-319-{\"ts\": \"2026-05-24T04:01:04.590575+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__get_agent_queue_status\", \"tool\": \"mcp__agent-ml-research__get_agent_queue_status\", \"tool_args\": {\"project\": \"turn_residual_gating\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-320-{\"ts\": \"2026-05-24T04:01:04.641592+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"found\\\\\\\":true,\\\\\\\"processing\\\\\\\":true,\\\\\\\"depth\\\\\\\":0,\\\\\\\"current\\\\\\\":{\\\\\\\"source\\\\\\\":\\\\\\\"system:restart_recovery\\\\\\\",\\\\\\\"preview\\\\\\\":\\\\\\\"[系统通知] 服务重启，自动恢复 ralph loop。\\\\\\\"},\\\\\\\"pending\\\\\\\":[],\\\\\\\"idle_seconds\\\\\\\":null}\\\"}\", \"tool\": \"mcp__agent-ml-research__get_agent_queue_status\", \"elapsed_ms\": 51}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-321-[Omitted long context line]\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-386-{\"ts\": \"2026-05-24T06:09:38.503000+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__director_get_project_overview\", \"tool\": \"mcp__agent-ml-research__director_get_project_overview\", \"tool_args\": {\"project\": \"turn_residual_gating\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-387-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-388-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:389:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-390-{\"ts\": \"2026-05-24T06:09:58.787541+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__get_agent_queue_status\", \"tool\": \"mcp__agent-ml-research__get_agent_queue_status\", \"tool_args\": {\"project\": \"turn_residual_gating\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-391-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-392-[Omitted long context line]\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-406-{\"ts\": \"2026-05-24T06:15:57.891106+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__read_project_file\", \"max_results\": \"1\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-407-{\"ts\": \"2026-05-24T06:15:57.991953+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 100}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-408-{\"ts\": \"2026-05-24T06:16:03.514253+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__read_project_file\", \"tool\": \"mcp__agent-ml-research__read_project_file\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"file\": \"report.md\", \"max_chars\": \"12000\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:409:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-410-{\"ts\": \"2026-05-24T06:16:10.348680+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__feishu_read_chat_history,mcp__agent-ml-research__auto_build_provenance\", \"max_results\": \"2\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-411-{\"ts\": \"2026-05-24T06:16:10.399359+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 50}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-412-{\"ts\": \"2026-05-24T06:16:14.264767+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__feishu_read_chat_history\", \"tool\": \"mcp__agent-ml-research__feishu_read_chat_history\", \"tool_args\": {\"chat_id\": \"oc_640e53b6afbbd5e34eb7273cd5a707a0\", \"limit\": \"15\"}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-540-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-541-{\"ts\": \"2026-05-24T07:19:33.499110+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/experiment_plan.yaml has been updated successfully.\", \"tool\": \"Edit\", \"elapsed_ms\": 101}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-542-{\"ts\": \"2026-05-24T07:19:38.917577+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"Now update plan_013 in experiment_plan.yaml.\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:543:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-544-{\"ts\": \"2026-05-24T07:21:45.426073+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"No response requested.\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-545-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-546-{\"ts\": \"2026-05-24T07:22:54.652623+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"called mcp__agent-ml-research__director_post_to_main_agent\", \"tool\": \"mcp__agent-ml-research__director_post_to_main_agent\", \"tool_args\": {\"text\": \"小修复：MMLU registry 的 `ss_v8b_s42` 仍标为 `pending_final`。实际值 0.7375 已在结果文件中。更新 registry metric 即可。\", \"project\": \"turn_residual_gating\"}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-548-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-549-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-550-{\"ts\": \"2026-05-24T07:23:11.994030+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"Paper Agent queue depth=2（Intro/Abstract reframe 处理中 → KL+GAR patch → MMLU+1.5B patch → β=3 约束）。Llama SS 在 GPU 上跑着。所有任务都在推进。\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl:551:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-552-{\"ts\": \"2026-05-24T07:24:04.706841+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\", \"text\": \"No response requested.\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-553-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_640e53b6afbbd5e34eb7273cd5a707a0_director.jsonl-554-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2545-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2546-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2547-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2548:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2549:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2550-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2551-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2552-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2564-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2565-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2566-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2567:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2568-{\"ts\": \"2026-05-23T19:59:18.178063+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"director_session\\\\\\\": \\\\\\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\\\\\"}, \\\\\\\"error\\\\\\\": \\\\\\\"\\\\\\\"}\\\"}\", \"tool\": \"mcp__agent-ml-research__main_agent_post_to_director\", \"elapsed_ms\": 1204}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2569-{\"ts\": \"2026-05-23T19:59:20.785140+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"已派 Worker 修复全部 5 项审计问题。同时汇报 Director。\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2570-{\"ts\": \"2026-05-23T19:59:21.309863+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"[WORKER DONE] Worker worker_code_p0_ss_steering_eval_script_20260523T193821 已完成（status=done）。用 `get_worker_status('worker_code_p0_ss_steering_eval_script_20260523T193821')` 读取结果，然后处理。\\n\\n- worker_id: worker_code_p0_ss_steering_eval_script_20260523T193821\\n- project: turn_residual_gating\\n- status: done\", \"source\": \"worker:done\"}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2585-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2586-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2587-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2588:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2589-{\"ts\": \"2026-05-23T20:20:50.250821+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"director_session\\\\\\\": \\\\\\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\\\\\"}, \\\\\\\"error\\\\\\\": \\\\\\\"\\\\\\\"}\\\"}\", \"tool\": \"mcp__agent-ml-research__main_agent_post_to_director\", \"elapsed_ms\": 1304}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2590-{\"ts\": \"2026-05-23T20:20:53.038823+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"向 Director 汇报进展。\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2591-{\"ts\": \"2026-05-23T20:20:53.629362+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"[WORKER DONE] Worker worker_fix_audit_d1_d6_all_20260523T195857 已完成（status=done）。用 `get_worker_status('worker_fix_audit_d1_d6_all_20260523T195857')` 读取结果，然后处理。\\n\\n- worker_id: worker_fix_audit_d1_d6_all_20260523T195857\\n- project: turn_residual_gating\\n- status: done\", \"source\": \"worker:done\"}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2757-{\"ts\": \"2026-05-24T02:21:20.561464+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && find . -name \\\"*.md\\\" -type f 2>/dev/null | head -20\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2758-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2759-{\"ts\": \"2026-05-24T02:21:22.419810+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"head -50 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2760:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2761-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2762-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2763-{\"ts\": \"2026-05-24T02:22:13.881778+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"director_session\\\\\\\": \\\\\\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\\\\\"}, \\\\\\\"error\\\\\\\": \\\\\\\"\\\\\\\"}\\\"}\", \"tool\": \"mcp__agent-ml-research__main_agent_post_to_director\", \"elapsed_ms\": 3765}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2768-{\"ts\": \"2026-05-24T02:25:28.455609+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"experiments\\\\\\\": {}, \\\\\\\"count\\\\\\\": 0, \\\\\\\"total\\\\\\\": 0, \\\\\\\"baseline\\\\\\\": null}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {\\\\\\\"elapsed_seconds\\\\\\\": 0.1487}}\\\"}\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"elapsed_ms\": 553}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2769-{\"ts\": \"2026-05-24T02:25:28.455871+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__read_project_file\", \"tool\": \"mcp__agent-ml-research__read_project_file\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"file\": \"report.md\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2770-{\"ts\": \"2026-05-24T02:25:28.506361+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"reconciled\\\\\\\": 0, \\\\\\\"results\\\\\\\": []}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {}}\\\"}\", \"tool\": \"mcp__agent-ml-research__reconcile_crons\", \"elapsed_ms\": 51}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2771:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2772-{\"ts\": \"2026-05-24T02:25:37.544433+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__check_job_status,mcp__agent-ml-research__spawn_worker\", \"max_results\": \"3\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2773-{\"ts\": \"2026-05-24T02:25:37.544799+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 0}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2774-{\"ts\": \"2026-05-24T02:25:40.571660+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__check_job_status\", \"tool\": \"mcp__agent-ml-research__check_job_status\", \"tool_args\": {\"server\": \"westd-20861\", \"pid\": \"131153\"}}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2824-{\"ts\": \"2026-05-24T04:00:31.655067+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"experiments\\\\\\\": {}, \\\\\\\"count\\\\\\\": 0, \\\\\\\"total\\\\\\\": 0, \\\\\\\"baseline\\\\\\\": null}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {\\\\\\\"elapsed_seconds\\\\\\\": 0.2544}}\\\"}\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"elapsed_ms\": 503}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2825-{\"ts\": \"2026-05-24T04:00:32.208479+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"reconciled\\\\\\\": 0, \\\\\\\"results\\\\\\\": []}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {}}\\\"}\", \"tool\": \"mcp__agent-ml-research__reconcile_crons\", \"elapsed_ms\": 553}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2826-{\"ts\": \"2026-05-24T04:00:32.208998+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__read_project_file\", \"tool\": \"mcp__agent-ml-research__read_project_file\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"file\": \"report.md\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:2827:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2828-{\"ts\": \"2026-05-24T04:00:32.310683+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__read_roadmap\", \"tool\": \"mcp__agent-ml-research__read_roadmap\", \"tool_args\": {\"project\": \"turn_residual_gating\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2829-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-2830-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3005-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3006-{\"ts\": \"2026-05-24T07:15:36.003368+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__get_worker_status\", \"tool\": \"mcp__agent-ml-research__get_worker_status\", \"tool_args\": {\"worker_id\": \"worker_chain_read_kl_run_gar_20260524T071233\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3007-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3008:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3009-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3010-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3011-{\"ts\": \"2026-05-24T07:16:34.007667+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"director_session\\\\\\\": \\\\\\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\\\\\"}, \\\\\\\"error\\\\\\\": \\\\\\\"\\\\\\\"}\\\"}\", \"tool\": \"mcp__agent-ml-research__main_agent_post_to_director\", \"elapsed_ms\": 1255}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3032-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3033-{\"ts\": \"2026-05-24T07:19:33.444582+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__check_job_status\", \"tool\": \"mcp__agent-ml-research__check_job_status\", \"tool_args\": {\"server\": \"westd-20861\", \"pid\": \"python\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3034-{\"ts\": \"2026-05-24T07:19:34.950609+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"status\\\\\\\": \\\\\\\"not_found\\\\\\\", \\\\\\\"running\\\\\\\": false, \\\\\\\"pid\\\\\\\": \\\\\\\"python\\\\\\\", \\\\\\\"detection\\\\\\\": \\\\\\\"ps\\\\\\\", \\\\\\\"tmux_session_alive\\\\\\\": false}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {\\\\\\\"elapsed_seconds\\\\\\\": 1.48}}\\\"}\", \"tool\": \"mcp__agent-ml-research__check_job_status\", \"elapsed_ms\": 1506}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3035:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3036-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3037-{\"ts\": \"2026-05-24T07:19:57.475724+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__update_registry\", \"tool\": \"mcp__agent-ml-research__update_registry\", \"tool_args\": {\"exp_id\": \"p2_llama_gradient_conflict\", \"field\": \"status\", \"value\": \"QUEUED\", \"project\": \"turn_residual_gating\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3038-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3050-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3051-{\"ts\": \"2026-05-24T07:20:44.036484+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__get_worker_status\", \"tool\": \"mcp__agent-ml-research__get_worker_status\", \"tool_args\": {\"worker_id\": \"worker_check_llama_ss_startup_20260524T071947\", \"verbose\": \"True\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3052-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3053:{\"ts\": \"2026-05-24T07:20:49.963551+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"called mcp__agent-ml-research__update_registry\", \"tool\": \"mcp__agent-ml-research__update_registry\", \"tool_args\": {\"exp_id\": \"p1_llama_ss_training\", \"field\": \"status\", \"value\": \"QUEUED\", \"project\": \"turn_residual_gating\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3054:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3055:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3056:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl:3057:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3058-{\"ts\": \"2026-05-24T07:21:27.691882+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"director_session\\\\\\\": \\\\\\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\\\\\"}, \\\\\\\"error\\\\\\\": \\\\\\\"\\\\\\\"}\\\"}\", \"tool\": \"mcp__agent-ml-research__main_agent_post_to_director\", \"elapsed_ms\": 4198}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3059-{\"ts\": \"2026-05-24T07:21:30.132202+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"Llama SS training 确认运行中：98% GPU 利用率，86GB VRAM，Step 100/3000。更新 registry 并汇报。\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118.jsonl-3060-{\"ts\": \"2026-05-24T07:21:30.824975+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118\", \"text\": \"[WORKER DONE] Worker worker_check_llama_ss_startup_20260524T071947 已完成（status=done）。用 `get_worker_status('worker_check_llama_ss_startup_20260524T071947')` 读取结果，然后处理。\\n\\n- worker_id: worker_check_llama_ss_startup_20260524T071947\\n- project: turn_residual_gating\\n- status: done\", \"source\": \"worker:done\"}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-42-{\"ts\": \"2026-05-23T19:47:47.296496+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"grep -n \\\"GATE-PROFILE\\\" /root/turn_residual_gating/runs/d048_ss_s123/train.log\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-43-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-44-{\"ts\": \"2026-05-23T19:47:47.830979+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'PREPARING'}\", \"fields\": \"['*']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:45:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-46-{\"ts\": \"2026-05-23T19:49:07.182605+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git log --oneline -10 --since=\\\"2026-05-23T12:00:00\\\"\", \"description\": \"Check recent commits since Loop #5\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-47-{\"ts\": \"2026-05-23T19:49:07.734801+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921\", \"tool\": \"Bash\", \"elapsed_ms\": 552}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-48-{\"ts\": \"2026-05-23T19:49:07.835484+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"head -80 /tmp/gpu_chain.log\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-49-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-50-{\"ts\": \"2026-05-23T19:49:36.412087+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__reviewer_post_to_director\", \"max_results\": \"1\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-51-{\"ts\": \"2026-05-23T19:49:36.462697+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 50}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:52:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-53-{\"ts\": \"2026-05-23T19:50:01.301689+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"director_session\\\\\\\": \\\\\\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\\\\\"}, \\\\\\\"error\\\\\\\": \\\\\\\"\\\\\\\"}\\\"}\", \"tool\": \"mcp__agent-ml-research__reviewer_post_to_director\", \"elapsed_ms\": 3810}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-54-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-55-{\"ts\": \"2026-05-23T20:00:53.602982+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"[系统通知 — worker_done:worker_run_p0_after_chain_start_20260523T195947]:\\nWorker worker_run_p0_after_chain_start_20260523T195947 已完成（status=done），请审查 Agent 的处理结果。\", \"source\": \"worker_done:worker_run_p0_after_chain_start_20260523t195947\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-56-{\"ts\": \"2026-05-23T20:01:01.678103+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"limit\": \"5\", \"fields\": \"['*']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:57:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-58-{\"ts\": \"2026-05-23T20:01:18.786221+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"limit\": \"15\", \"fields\": \"['status', 'hypothesis', 'conclusion', 'notes', 'updated_at', 'created_at']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:59:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-60-{\"ts\": \"2026-05-23T20:01:19.540109+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"ls -la /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-61-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-62-[Omitted long context line]\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-64-{\"ts\": \"2026-05-23T20:02:16.915714+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git log --oneline -10\", \"description\": \"Check recent commits for audit fixes\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-65-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-66-{\"ts\": \"2026-05-23T20:02:17.821394+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"limit\": \"5\", \"fields\": \"['status', 'conclusion', 'notes', 'updated_at']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:67:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-68-{\"ts\": \"2026-05-23T20:02:29.068058+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git diff --stat HEAD\", \"description\": \"Check uncommitted changes from worker\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-69-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-70-{\"ts\": \"2026-05-23T20:02:37.468703+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git diff HEAD -- paper/sections/discussion.tex\", \"description\": \"Check discussion.tex changes\"}}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-116-{\"ts\": \"2026-05-23T20:31:59.270934+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'DONE'}\", \"limit\": \"3\", \"fields\": \"['*']\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-117-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-118-{\"ts\": \"2026-05-23T20:32:05.604026+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'PREPARING'}\", \"limit\": \"5\", \"fields\": \"['status', 'hypothesis', 'conclusion', 'notes', 'updated_at']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:119:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-120-{\"ts\": \"2026-05-23T20:32:14.734772+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"find /root/turn_residual_gating/src/ -name \\\"*kl*\\\" -o -name \\\"*divergence*\\\"\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-121-{\"ts\": \"2026-05-23T20:32:14.835684+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"find /root/turn_residual_gating/scripts/ -name \\\"*kl*\\\" -o -name \\\"*divergence*\\\"\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-122-{\"ts\": \"2026-05-23T20:32:15.788990+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"stdout\\\\\\\": \\\\\\\"\\\\\\\", \\\\\\\"stderr\\\\\\\": \\\\\\\"\\\\\\\", \\\\\\\"return_code\\\\\\\": 0}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {\\\\\\\"elapsed_seconds\\\\\\\": 1.03}}\\\"}\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"elapsed_ms\": 1054}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-238-{\"ts\": \"2026-05-23T21:44:42.113343+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__read_registry\", \"max_results\": \"1\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-239-{\"ts\": \"2026-05-23T21:44:42.214161+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 100}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-240-{\"ts\": \"2026-05-23T21:44:51.797562+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"limit\": \"5\", \"fields\": \"['*']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:241:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-242-{\"ts\": \"2026-05-23T21:45:00.613456+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called ToolSearch\", \"tool\": \"ToolSearch\", \"tool_args\": {\"query\": \"select:mcp__agent-ml-research__read_project_file\", \"max_results\": \"1\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-243-{\"ts\": \"2026-05-23T21:45:00.664023+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"\", \"tool\": \"ToolSearch\", \"elapsed_ms\": 50}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-244-{\"ts\": \"2026-05-23T21:45:06.242212+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_project_file\", \"tool\": \"mcp__agent-ml-research__read_project_file\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"file\": \"report.md\", \"max_chars\": \"6000\"}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-278-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-279-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-280-{\"ts\": \"2026-05-23T22:25:32.038029+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"limit\": \"0\", \"fields\": \"['status', 'conclusion']\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:281:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-282-{\"ts\": \"2026-05-23T22:26:12.117926+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'DONE'}\", \"fields\": \"['conclusion', 'metrics']\", \"limit\": \"1\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-283-[Omitted long context line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-284-{\"ts\": \"2026-05-23T22:26:15.537579+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'DONE'}\", \"fields\": \"['conclusion', 'metrics']\", \"limit\": \"1\"}}\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-641-{\"ts\": \"2026-05-24T03:42:46.629898+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"Eval 运行中，4.5 分钟后检查进展。\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-642-{\"ts\": \"2026-05-24T04:00:12.159888+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"[系统通知] 服务重启，自动恢复 ralph loop。\", \"source\": \"system:restart_recovery\"}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-643-{\"ts\": \"2026-05-24T04:00:39.486598+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_project_file\", \"tool\": \"mcp__agent-ml-research__read_project_file\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"file\": \"report.md\", \"max_chars\": \"12000\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl:644:[Omitted long matching line]\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-645-{\"ts\": \"2026-05-24T04:00:40.442568+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"tail -80 /tmp/gpu_chain.log\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-646-{\"ts\": \"2026-05-24T04:00:41.146912+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__ssh_read_only\", \"tool\": \"mcp__agent-ml-research__ssh_read_only\", \"tool_args\": {\"server\": \"westd-20861\", \"command\": \"nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-647-[Omitted long context line]\n--\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-729-{\"ts\": \"2026-05-24T04:42:28.673310+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'RUNNING'}\"}}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-730-{\"ts\": \"2026-05-24T04:42:28.874525+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"{\\\"result\\\":\\\"{\\\\\\\"success\\\\\\\": true, \\\\\\\"data\\\\\\\": {\\\\\\\"experiments\\\\\\\": {}, \\\\\\\"count\\\\\\\": 0, \\\\\\\"total\\\\\\\": 0, \\\\\\\"baseline\\\\\\\": null}, \\\\\\\"error\\\\\\\": null, \\\\\\\"metadata\\\\\\\": {\\\\\\\"elapsed_seconds\\\\\\\": 0.1475}}\\\"}\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"elapsed_ms\": 201}\nprojects/turn_residual_gating/logs/chats/feishu_group_oc_934666158b769e82a2351d9206410118_reviewer.jsonl-731-{\"ts\": \"2026-05-24T04:42:28.874972+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_934666158b769e82a2351d9206410118:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"turn_residual_gating\", \"filters\": \"{'status': 'PREPARING'}\"}}",
    "numLines": 250,
    "appliedLimit": 250
  },
  "sourceToolAssistantUUID": "3c3092d7-e632-43e1-bcb9-952836733f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画 核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general miti…",
  "leafUuid": "1dc1a873-3bde-48b6-9e9c-75da9325713e",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Exposure bias destroys auxiliary attention losses",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Tool call

_source line 23 · 2026-05-24T08:15:10.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DYeyeEgv2n17ojevuqqSUU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dc1a873-3bde-48b6-9e9c-75da9325713e",
  "isSidechain": false,
  "requestId": "req_011CbM4UuDgiFjLmyRDXETNi",
  "type": "assistant",
  "uuid": "a9e32218-871f-4d53-b388-91fd211a49b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2oxCdxMoz6PGk14o2a95Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5310,
      "cache_read_input_tokens": 58609,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 58609,
          "cache_creation_input_tokens": 5310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5310
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T08:15:10.109Z_

<details><summary>↩ Tool result · `toolu_01DYeyeEgv2n17ojevuqqSUU`</summary>

```text
1	{
2	  "exp_id": "p1_llama_ss_training",
3	  "project": "turn_residual_gating",
4	  "state": "RUNNING",
5	  "previous_state": "QUEUED",
6	  "experiment_data": {
7	    "status": "RUNNING",
8	    "retry_count": 0,
9	    "created_at": "2026-05-23T19:37:48.689Z",
10	    "updated_at": "2026-05-24T07:21:06.008Z",
11	    "hypothesis": "SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.",
12	    "spec": {
13	      "command": "bash scripts/p1_llama_ss_train.sh",
14	      "server": "westd-20861",
15	      "data_path": "/root/turn-residual-gating/data/train_400.json",
16	      "data_count": 400,
17	      "model_name": "meta-llama/Llama-3.1-8B-Instruct",
18	      "seed": 42,
19	      "checkpoint_path": "runs/llama_ss_s42/",
20	      "log_path": "logs/p1_llama_ss_training.log",
21	      "pid": 158507,
22	      "hyperparams": {
23	        "lr": "2e-4",
24	        "batch_size": 1,
25	        "grad_accum": 8,
26	        "epochs": 3,
27	        "ss_max_ratio": 0.3,
28	        "lora_rank": 16
29	      }
30	    }
31	  },
32	  "timestamp": "2026-05-24T07:21:06.157028+00:00",
33	  "trigger": "update_registry"
34	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9e32218-871f-4d53-b388-91fd211a49b2",
  "isSidechain": false,
  "promptId": "03ba6bd2-f669-4de4-a1f2-b6a252b87fca",
  "type": "user",
  "uuid": "06b5b095-574f-4cc7-9e26-deb2e8df47ed",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/checkpoints/p1_llama_ss_training_RUNNING_20260524T072106.json",
      "content": "{\n  \"exp_id\": \"p1_llama_ss_training\",\n  \"project\": \"turn_residual_gating\",\n  \"state\": \"RUNNING\",\n  \"previous_state\": \"QUEUED\",\n  \"experiment_data\": {\n    \"status\": \"RUNNING\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-23T19:37:48.689Z\",\n    \"updated_at\": \"2026-05-24T07:21:06.008Z\",\n    \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\",\n    \"spec\": {\n      \"command\": \"bash scripts/p1_llama_ss_train.sh\",\n      \"server\": \"westd-20861\",\n      \"data_path\": \"/root/turn-residual-gating/data/train_400.json\",\n      \"data_count\": 400,\n      \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\",\n      \"seed\": 42,\n      \"checkpoint_path\": \"runs/llama_ss_s42/\",\n      \"log_path\": \"logs/p1_llama_ss_training.log\",\n      \"pid\": 158507,\n      \"hyperparams\": {\n        \"lr\": \"2e-4\",\n        \"batch_size\": 1,\n        \"grad_accum\": 8,\n        \"epochs\": 3,\n        \"ss_max_ratio\": 0.3,\n        \"lora_rank\": 16\n      }\n    }\n  },\n  \"timestamp\": \"2026-05-24T07:21:06.157028+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "a9e32218-871f-4d53-b388-91fd211a49b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-24T08:24:16.957Z_

<details><summary>Logged reasoning block</summary>

```text
Good, so the Llama SS training is currently running. The key hyperparams: ss_max_ratio=0.3 (vs Qwen's which ramps to 0.5). This is plan_026.

Now I have all the context I need. Let me generate the comprehensive YAML prediction for the "best" tier.

Let me organize all planned experiments:

1. plan_013 - Llama gradient conflict (has result, effectively done)
2. plan_020 - Expanded eval (superseded/partially done)
3. plan_022 - λ_GAR sensitivity (truly planned, no result)


4. plan_025 - TF vs AR KL divergence (truly planned, no result)
5. plan_026 - Llama SS (RUNNING, no result yet)
6. plan_027 - SS 3-seed (has result)
7. plan_028 - Alternative GAR defs (has result)
8. plan_029 - SS 4th seed (truly planned, no result)
9. plan_030 - Long conversation eval (truly planned, no result)

For the ones with existing results, I'll use those directly as the best tier predictions. For the ones without results yet, I'll generate predictions based on the best tier ranges I've established.

Now I'm drafting the full YAML structure, paying attention to how flow sequences with quoted strings should be formatted, making sure each experiment has a clear result_rationale, getting the table formatting right, writing proper figures_descriptions, and laying out the analysis section.

For plan_026 specifically, since Llama SS is still running with ss_max_ratio=0.3 (lower than Qwen's 0.5), I'm predicting that under best tier conditions the AR GAR β=0 should reach around 0.35, compressing the gap to roughly 1.5× compared to the TG baseline of 15.9×. For plan_022 with λ_GAR sensitivity, the λ=10 setting represents the GAR loss weight I'm varying to test robustness.

With λ=10 the loss weight is 10× default, so GAR might converge faster but NTP still dominates in absolute magnitude, and critically at inference AR GAR still collapses around 0.02 because exposure bias is the fundamental issue—this directly addresses the concern about just tuning hyperparameters. The λ=0.1 case shows GAR barely trains with low TF GAR performance. For plan_025, I'm using per-head KL divergence between TF and AR attention distributions to provide mechanistic evidence, with late layers L20-L27 showing higher KL and GAR-relevant heads showing systematic shifts that explain the 8×-27× gap at the head level. For plan_029, the fourth seed s789 should give AR GAR β=0 around 0.41.

The 4-seed mean tightens to approximately 0.404±0.037, which is consistent with the 3-seed mean of 0.401 and provides useful confidence for reviewers. For plan_030, I'm testing at N=15 and 20 turns on Qwen to see how the gaps scale with conversation length—TG gap worsens to maybe 10-15× at 20 turns while SS gap stays stable around 1.5-2.0×, and base GAR continues declining, showing that SS is robust to length. Now I need to reconsider the numbers for plan_022 more carefully since the current v7 with λ_GAR=1.0 shows TF GAR at 0.5035, AR GAR at 0.0157, and PPL at 2.

78.

If I increase λ_GAR to 10, the GAR loss gets 10× more weight, bringing gradient magnitudes closer to NTP's, but NTP still dominates the optimization—TF GAR might improve slightly to 0.52-0.55 while PPL degrades to 2.9-3.1, AR GAR stays collapsed around 0.02-0.03, and the gate profile shifts slightly, but the core issue is distribution shift which matching gradients won't solve. With λ_GAR=0.1, GAR gets 10× less weight instead.

Actually, the most compelling framing is that λ=10 shows higher TF GAR but the same AR collapse, proving it's not about gradient weight—and the gap might even widen because TF overfits more to the gold distribution. Let me lock in the numbers: at λ=10, TF GAR reaches 0.55 with AR at 0.018 (30.6× gap) and PPL of 3.05, while at λ=0.1, TF GAR drops to 0.32 with AR at 0.015 (21.3× gap) and PPL of 2.78.

The key insight is that regardless of loss weighting, AR GAR stays pinned near baseline—the exposure bias gap is fundamentally independent of λ. For the KL divergence analysis, I'm looking at how the distribution divergence varies across heads: early layers show minimal divergence around 0.03-0.05 nats, while late layers spike to 0.15-0.25 nats, with the heads most critical for goal-token attention exceeding 0.20 nats. There's a moderate correlation (r = 0.35-0.45) between a head's KL divergence and its contribution to the overall GAR gap, suggesting the heads driving exposure bias are also the ones with the largest distribution shifts.

Switching to the Llama self-supervised results, the configuration uses a lower substitution ratio of 0.3 compared to Qwen, and the performance metrics align closely with the supervised baseline: TF GAR reaches 0.47, AR GAR sits at 0.35, and the gap is 1.34×, all within expected ranges. The perplexity degradation is minimal at 1.35, confirming that self-supervised training generalizes across model architectures.

For the long conversation evaluation, I'm testing whether the GAR decay continues as context extends to 15-20 turns, with the base GAR already dropping to around 0.008 by turn 15.

Now I'm ready to compile the full YAML configuration with all these results.

Looking at the Llama gradient analysis—the near-orthogonal directions confirm that gradient conflict isn't the real issue across models; instead, NTP's 25.7× magnitude advantage is what actually matters. This pattern holds whether we see genuine conflict like Qwen or orthogonal directions like Llama, which makes the case that direction misalignment is a red herring.

The expanded evaluation is mostly complete with TF at N=200 for tighter confidence intervals and AR at N=50, which is already sufficient given how large the effect sizes are. For the 3-seed SS run, I have the AR GAR β=0 result at 0.401±.

047 with a gap ratio of 1.26±0.17—both falling squarely within the best tier ranges. The alternative GAR definitions all show SS improving across all 4 variants, hitting the target. Everything checks out against the best tier thresholds.

Now I'm preparing the YAML output...

Actually, let me first map out which experiments contribute to which paper sections so I can organize the results properly. Plan 013 feeds into the cross-model replication and PCGrad analysis sections, plan 020 provides the statistical robustness for main results, plan 022 covers gradient competition robustness, plan 025 gives mechanistic evidence through distribution shift, plans 026 and 027 both support scheduled sampling with different seed counts, plan 028 validates mechanism specificity with alternative GAR definitions, and the remaining plans go into appendices or supplementary analyses like length scaling.

Now I'm structuring the output carefully—for each experiment I need to specify the name, plan ID, what it tests, expected metric values, the reasoning behind those results under best-tier conditions, associated tables and figures, and what it means for the paper's narrative. I'm also noting that the scheduled sampling ratio difference between Qwen (linear ramp to 0.5) and Llama (fixed 0.3 max) actually demonstrates robustness, since even the lower exposure ratio still compresses the performance gap effectively.

Writing the detailed output now... I'm settling on specific values that fit the narrative: AR GAR at 0.35 sits comfortably in the expected range, the gap compresses to 1.34× showing that scheduled sampling is a general mitigation strategy rather than model-specific, and perplexity lands at 1.36—all of which align with the tier constraints and tell a coherent story about how lower scheduled sampling ratios still produce meaningful improvements. Looking at the improvement from 15.9× down to 1.34× with the self-supervised approach—that's a really strong result for the best tier configuration. Now I need to decide how to present plan_013 and the other experiments that already have results. Since they're marked as done and their outcomes align with what the best tier would predict, I'll present them as predictions that happen to match the actual data. Let me organize this carefully and make sure I'm not creating too many redundant tables and figures while covering all the planned experiments comprehensively.

Writing YAML structure...

Wait, I need to check the actual statuses in the file more carefully. Looking at the experiment plan, most of these aren't actually marked as "planned" — several are already "done" or "superseded". The user asked specifically for planned experiments, so I should focus only on those with status "planned": plan_022, plan_025, plan_026, plan_029, and plan_030. I need to check which experiments actually need predictions generated. Looking at the statuses in the user's data, most are already marked as done or in other states, but there's a subset marked as "planned" that I need to handle. For the ones that already have results listed, I can use those as-is since they align with the expected tier. For the ones without results, I'll need to generate appropriate predictions based on the experimental design. Writing YAML config... I'm checking off the remaining parameters—most are already within range, though I need to predict 1.34 for the Llama gap ratio. Now I should add the narrative_guidance field at the top level before finalizing the YAML.

Looking at how plan_013 and plan_022 connect: plan_013 reveals that Llama has non-conflicting gradients while Qwen shows genuine conflict, but NTP magnitude dominates in both cases. Plan_022 confirms that boosting λ_GAR doesn't resolve this. Together they eliminate gradient competition as the root cause, which is a key insight to capture.

Writing the final YAML now...

Generating YAML structure... I'm noting that across both Llama and Qwen architectures, the core gradient relationship holds—NTP's magnitude dominates gate updates regardless of whether gradient directions conflict, align, or stay orthogonal. For the expanded evaluation set, increasing the TF sample size to 200 tightens confidence intervals without shifting conclusions, while the AR evaluation stays at N=50 since the effect sizes are so large that even smaller samples would reliably detect them.

Now examining how the GAR weight parameter λ affects the trade-off: at λ=10, GAR gradients amplify enough to slightly boost TF performance but still can't prevent AR collapse, widening the gap to 28.9× while slightly degrading perplexity as GAR competes with NTP for the gate; at λ=0.1, the gap narrows to 22.9× with better perplexity, showing the sensitivity of this balance. 充分的 TF GAR（0.32）下，AR GAR 同样坍塌到 0.014，这进一步证实了 exposure bias 是独立于 loss weighting 的结构性问题。现在看 plan_025 的预期结果，我在检查 KL 散度指标——平均跨所有注意力头为 0.087，后期层显著更高（0.18），而早期层较低（0.034），单个头的最大值达到 0.42。

关键发现是在 goal-token attention 贡献最大的 heads 中，72% 属于高 KL 组，Pearson 相关系数 0.38 表明 head 级 KL 与 GAR 贡献显著正相关——这提供了机制证据，说明 exposure bias 精确地针对那些负责 goal-attention routing 的 heads。

这解释了为什么我们的方法在 summary-position 到 goal 的路由上会坍塌，而 Dongre 的方法由于不依赖特定的 learned routing heads，所以没有这个问题。现在看一下 plan_026 的预期结果，包括训练指标、损失值和各种 GAR 配置下的性能数据。 The pattern holds across different architectures—Llama's grouped query attention behaves differently than Qwen's multi-head attention in deeper layers, but the gap compression effect remains consistent, suggesting that selective scaling addresses a fundamental training-inference mismatch rather than architecture-specific behavior. The perplexity of 1.36 shows no degradation compared to Llama's baseline models. For plan_027, I'm seeing consistent results across multiple seeds that align with the best tier performance. 现在看到 PPL 在 β=0 时的极低方差（1.441±0.001）确认了 SS 训练不会损害语言建模能力，而 TF GAR 的方差同样极低（0.498±0.004），说明训练在金标准分布上高度一致，变异只在跨分布泛化时才显现——这正是 exposure bias 的特征。对比 plan_028 的结果，SS 在所有四种 GAR 定义上都有改善（>0.36），而 TG 只在最后一个 token 上改善（0.325），在全序列和首 token 上几乎没有提升（0.025/0.039），揭示了两种方法的根本差异：TG 在教师强制下学到的是位置特定的注意力模式。

这种模式严重依赖金标准上下文分布，在自回归生成时会崩溃，而 SS 通过在训练中暴露模型生成的上下文，学到了更鲁棒的目标注意力路由，在各个 token 位置都有效。现在预期 plan_029 在 β=0 和 β=3 时分别达到 0.41 和 0.60。

第四个种子 s789 的 AR GAR 结果 0.41 与三种子均值 0.401 高度一致，四种子标准差从 0.047 收窄到 0.037，95% 置信区间 [0.345, 0.463] 完全在 0.3 以上，这排除了 SS 改善可能只是噪声的假设。

不过投资回报率较低——三种子的效应量已经足够大（Cohen's d>5 相比基线 0.019），第四个种子的边际信息增益有限。在最优档位下，这个实验的主要价值在于展示方法论的严谨性而非改变结论。β=3 和 β=5 继续显示跨种子极低方差（标准差<0.01），确认推理时间引导是高度稳定的。现在我在查看 plan_030 的预期结果，测试不同轮次数（10、15、20 轮）下的基线 GAR 表现，数值随轮次增加而递减。

接着对比了目标引导和自我监督方法在这些轮次下的 GAR 和性能差距指标，自我监督方法在 GAR 上显著更优（0.27-0.35 范围），而目标引导方法的差距更大（31.5-55.6），困惑度在 20 轮时两种方法基本持平。 result_rationale: "随着对话长度增加，所有方法的 AR GAR 均下降，但下降速率不同。TG gap 加剧（10T: 31.5× → 20T: 55.6×），因为更长对话意味着更多 model-generated tokens 积累，distribution shift 进一步放大。SS gap 也轻微增加（10T: 1.45× → 20T: 1.84×），但仍在 2× 以内，说明 SS 训练赋予的 distribution robustness 在长对话中持续有效。SS AR GAR 从 0.347（T=10）降到 0.270（T=20），降幅 22%，远小于 TG 的 44% 降幅和 base 的 50% 降幅。这为 SS 作为可扩展的缓解方案提供了证据——在最需要干预的长对话场景中，SS 的相对优势反而更大。PPL 在 T=20 时 SS 与 base 几乎无差异（1.47 vs 1.48），确认 SS 不损害生成质量。现在我在分析跨模型的梯度特征，比较 Qwen-2.5-7B 和 Llama-3.1-8B 在余弦相似度、负梯度层占比和幅度比等方面的差异，以理解不同模型架构下的梯度冲突模式。"

Generating markdown table... Now I'm looking at the KL divergence patterns across different layer groups, seeing how the divergence increases significantly in later layers—from 0.034 in early layers up to 0.180 in the late layers—with corresponding increases in the percentage of GAR-relevant heads. I'm also comparing the Llama speculative sampling approach against traditional generation, where the gap compression metric shows how much the speculative sampling reduces the performance gap, and then examining cross-model results to see how this generalizes across different model architectures like Qwen. I'm noticing a discrepancy in the TF GAR values for seed s123 — the plan_027 description mentions it as NaN, but the actual statistics show 0.495, and the registry entry has a TF value of 0.5536 from the 200-conv evaluation. Let me reconcile what's actually available across these different sources to clarify which TF measurement is correct. Looking at the breakdown across different seeds, the TF GAR stays consistent around 0.498±0.004, while the AR β=0 values vary more substantially from 0.347 to 0.433, creating gaps that range from 1.15× to 1.45×. Now I'm examining plan_028, which compares alternative GAR definitions — the last-token approach (ours) shows the strongest improvement with SS reaching 0.401, while the all-token definition achieves 0.385 and the first-token variant trails significantly behind. Looking at the robustness ratios across different GAR definitions for the TG model—last-token shows a massive 21.4× gap, goal-only has 63×, while all-token and first-token are much smaller at 1.7× and 1.8×. This makes sense because the all-token and first-token metrics don't capture the learned routing behavior that's actually vulnerable to distribution shift. Now I need to reconcile these numbers with the plan_028 results, where the base AR GAR stays consistently below 0.022 across all definitions, but the TG AR GAR for last-token appears to be 0.325—though I should verify if that's the right value from the actual results. I'm trying to figure out what metric these numbers represent—the 0.325 for TG last-token GAR doesn't match the 0.064 I see in the registry for AR evaluation, so either plan_028 used a different evaluation protocol or these are TF values instead. Let me check if there's a discrepancy in how the eval was set up or if different aggregation methods were applied. Writing the YAML output...

With λ=10, the GAR gradient becomes 10× larger, which flips the magnitude ratio—at epoch 0, GAR would actually dominate NTP's gradient (mag_ratio ≈ 0.75), meaning the gates get pushed more aggressively for GAR optimization even though NTP is the primary objective.

By epoch 2, NTP catches up as its gradient grows (mag_ratio ≈ 1.47), but the real issue is that GAR loss collapses once the model finds a good solution on the training data, making the gradient small regardless. So with λ=10, I'd expect faster GAR convergence on TF data (maybe 0.55-0.58), more gate modulation (gate_mean around 0.88 instead of 0.93), slightly worse NTP convergence due to the competing objective (NTP loss ~0.94 vs 0.93), and marginally worse perplexity (3.0-3.1)—but the AR GAR collapse persists because the fundamental problem is distribution shift, not the training dynamics.

The critical insight is that even when GAR's gradient becomes comparable to or stronger than NTP's gradient, the AR GAR still collapses, which rules out gradient competition as the root cause. With λ=0.1, the GAR gradient is 10× weaker, creating a 75× magnitude ratio at epoch 0, so GAR barely optimizes on TF data (maybe 0.30-0.35), gates stay nearly at identity (gate_mean ~0.97), NTP remains essentially unaffected (PPL ~2.78), and AR GAR collapses regardless.

Looking at the full spectrum across λ values, AR GAR stays remarkably constant around 0.014-0.019 across all settings, hovering near the baseline of 0.012, while TF GAR varies from 0.32 to 0.55 depending on λ. The gap between them changes only because TF GAR improves, not because AR GAR gets better—this is the smoking gun for exposure bias. I should double-check the plan_022 scope since the description mentions only 1 epoch for λ=10. I'm sketching out the predicted metrics for different λ values at 1 epoch, comparing them against the 3-epoch baseline—the λ=10 variant pushes the TF GAR higher while keeping AR GAR tight, whereas λ=0.1 trades some TF performance for better perplexity and gate selectivity. I'm settling on which experiments to include in the output—I'll organize them by status, starting with completed results and moving to planned work, then write out the YAML structure.

Now I need to think through the narrative contribution of each experiment and how it supports the paper's overall argument. For plan_026, I should also predict the β steering results on Llama SS since that hasn't been tested yet, estimating the accuracy and perplexity values across different β settings.

Writing the YAML configuration... W2）。KL divergence（plan_025）提供 head-level 机制证据，锁定 '为什么 exposure bias 选择性破坏 GAR-ours 而非 GAR-Dongre'。3-seed 统计（plan_027）+ 4th seed（plan_029）+ alternative GAR definitions（plan_028）形成方法论防火墙。长对话 eval（plan_030）展示 SS 在 20+ turn 场景下仍有效，增强实用价值叙事。Paper 定位 EMNLP main conference 3.5-4.0，title 用 T2 'From Collapse to Recovery' 突出完整弧。现在我在设计 Llama-3.1-8B 的梯度冲突跨模型分析（plan_013），验证 NTP-GAR 梯度竞争模式是否在不同架构间保持一致，尽管 Llama 的 GQA 和 RoPE 实现与 Qwen 存在差异。

Looking at the Llama results, the core pattern holds: NTP gradients suppress GAR across both models, with Llama showing an even stronger magnitude ratio of 25.7× compared to Qwen's 14.7×, reflecting NTP's dominance in the 32-layer architecture. The key difference is that Llama shows near-orthogonal gradients (cos_sim ≈ 0) rather than Qwen's directional conflict (cos_sim < 0), meaning NTP and GAR gradients barely interact on Llama—the 53.1% negative layer percentage is close to random chance, indicating no systematic conflict. This cross-model evidence supports the PCGrad causal exclusion findings: Qwen exhibits real directional conflict but the mechanism differs across architectures. Generating analysis table... Expanding the TF eval set to 200 conversations narrows the bootstrap confidence intervals by about 28%, and all pairwise comparisons still include zero, confirming that TG, UG, and LoRA-only show no meaningful differences in GAR performance within the TF regime. The AR eval at N=50 remains sufficient given the effect sizes are 8-27× larger than any reasonable statistical threshold, so expanding the TF eval set provides the tighter confidence bounds needed for the best performance tier.

Generating comparison table... ours)", "[-0.0030, +0.0006]", "[-0.0022, +0.0004]", "Yes"]
    figures_description: []
    analysis: "数据进入 §5.2 Main Results 的统计注脚。N=200 CI 收窄但结论不变，表明 N=50 的原始评估已足够。此实验的主要叙事价值是方法论防御——审稿人无法以 'insufficient eval size' 为由质疑 zero-benefit 结论。"

  - name: "λ_GAR Sensitivity Ablation"
    plan_id: "plan_022"
    description: "Training v7 with different λ_GAR weights at 0.1 and 10 to see how the loss scaling impacts the exposure bias gap."
    expected_results: Looking at the performance metrics across these different lambda values... Looking at the results across different λ values, the AR GAR consistently collapses into a narrow band around 0.013-0.018, which essentially matches the baseline model's natural GAR level of 0.012—this suggests exposure bias is completely overwhelming any attention steering improvements we're trying to train, regardless of how much gradient budget we allocate. The PPL degradation and the consistent failure of AR GAR across all three λ settings definitively rules out the possibility that we simply hadn't tuned the parameters correctly. Now I'm looking at the bar chart showing how AR GAR stays consistently near baseline across the full 100× range of λ values, with error bars from held-out evaluation, while the inset reveals that TF GAR increases monotonically with λ—indicating the training signal is being received but failing to transfer. This connects to the gradient competition hypothesis: when λ=10 makes the GAR gradient actually dominate training (magnitude ratio drops below 1), AR GAR remains unchanged, which mirrors the PCGrad results—eliminating directional conflicts doesn't close the gap, and eliminating magnitude differences doesn't either, suggesting gradient competition isn't the causal factor in the exposure bias gap regardless of whether we're looking at direction or magnitude.

Next I'm analyzing the per-head KL divergence between teacher-forced and autoregressive attention distributions to pinpoint which attention heads are most disrupted by exposure bias, with results showing early layers have minimal divergence while later layers show substantial shifts, and notably the heads most affected by exposure bias correlate with GAR contribution scores. The key insight is that token-to-goal routing in the last layer relies on a small set of specialized attention heads, and these are precisely the ones most affected by distribution shift. GAR-Dongre avoids this problem because it uses all-token attention and doesn't depend on these specialized heads, explaining why it shows no performance gap. The 45% KL reduction in the self-supervised model confirms that the training actually narrows the attention distribution differences between teacher-forcing and autoregressive modes, rather than improving GAR through some other mechanism. Now I'm looking at the per-layer breakdown of KL divergence across different layer groups to see how this effect varies. early)", "0.058", "0.021", "22%", "18%"]
          - ["L14-L19 (mid-late)", "0.092", "0.031", "28%", "25%"]
          - ["L20-L27 (late)", "0.180", "0.065", "35%", "49%"]
    figures_description:
      - "28×N heatmap (layers × heads): KL divergence intensity, red=high KL, blue=low KL. Stars mark heads with top-10 GAR contribution. Stars cluster visibly in the high-KL red zone of late layers. Colorbar: 0-0.45 nats."
      - "Scatter plot: head-level KL (x) vs head-level GAR contribution (y), r=0.38. Points colored by layer depth (gradient blue→red). Regression line with 95% band. Clear positive trend with late-layer heads in upper-right quadrant."
    analysis: Now I'm moving into the distribution shift analysis as the core mechanistic evidence. This elevates the 8×-27× gap from just an aggregate observation to a head-level explanation. The causal chain is: distribution shift changes attention patterns (KL > 0), this KL divergence peaks in the heads responsible for goal-routing (r=0.38), these are exactly the heads that GAR-ours depends on for routing from summary position to goal, while GAR-Dongre doesn't rely on these heads so it shows no gap.

Now I need to verify that scheduled sampling actually works as a universal mitigation by replicating it on Llama-3.1-8B, which would show the gap compression isn't just a Qwen artifact but a general principle. The results show that Llama's selective synchronization achieves similar gap compression to Qwen despite significant architectural differences, with the AR GAR metric falling in the optimal range and the final gap ratio within expected bounds. This suggests selective synchronization is a model-agnostic mitigation strategy that addresses the fundamental training-inference distribution mismatch rather than relying on specific attention mechanisms, though Llama's slightly higher gap compared to Qwen may stem from its different synchronization ratio configuration.

Generating comparison table... Generating markdown table... Running statistical validation across three random seeds (42, 123, 456) on Qwen to establish mean and standard deviation for the key metrics, with bootstrap confidence intervals—the results show tight clustering around target values like TF-GAR at 0.498±0.004 and AR-GAR beta coefficients varying as expected across the seed runs. The key insight is that AR GAR shows much higher variance across seeds (std=0.047) with s42 as a clear outlier, which is the hallmark of exposure bias—the model generalizes consistently under IID conditions but becomes sensitive to training randomness in OOD settings. Meanwhile, when β increases to 3 or 5, this variance essentially disappears (std<0.01) because attention steering during inference overrides the training randomness and aligns TF and AR behavior. The perplexity metric confirms that supervised signal training doesn't degrade language modeling quality. Generating results table...

Now I'm planning the visualization as a strip plot showing how the confidence intervals tighten dramatically as beta increases from 0 to 5, with the base model performance as a reference band. Moving into section 5.4 to present these scheduled sampling results—the three-seed statistics directly validate the single-seed finding and upgrade it to a statistically robust result. The beta-dependent variance pattern reveals something interesting for the discussion: inference-time steering appears to act as an implicit ensemble that averages over training randomness, and three seeds provide sufficient statistical power given the large effect size.

Next I'm testing whether the scheduled sampling improvement holds across different token-selection variants—comparing last token, all tokens, first token, and goal-only approaches across the base, target guidance, and scheduled sampling methods to rule out position-specific overfitting. Generating results table... Looking at the mechanism behind these results—the exposure bias gap is so severe for TG because it learns position-fragile attention patterns, whereas SS achieves smaller gaps through distribution-robust patterns. This also addresses the concern about whether our GAR metric is too narrow: SS's consistent improvements across all four GAR definitions demonstrate genuine attention steering rather than metric gaming.

Now I'm planning an additional validation run with a fourth seed to reduce variance in the results, which would strengthen confidence for reviewers, though this is lower priority than the main Llama experiments. The 4-seed results confirm s789 isn't an outlier and validate that s42 is the low-end anomaly in the 3-seed set. The confidence interval narrowed from the original range to [0.345, 0.463], still dramatically above baseline, so the effect remains robust. Though the marginal value is limited since the 3-seed Cohen's d already showed an extremely strong effect, adding the fourth seed serves mainly as due diligence—it reassures reviewers without changing the core conclusions.

Given the ROI is lower than the Llama experiments and cross-model comparisons take priority over additional seeds, I should only run this if there's leftover GPU budget after plan_026 completes. Looking at the 4-seed statistics across the different beta values and perplexity scores, the results are fairly consistent across seeds.

Now I'm moving on to the long conversation evaluation, which will test whether the exposure bias gap increases with longer conversations and if the proposed method maintains its advantage beyond 20 turns. Looking at the performance metrics across different conversation lengths, I'm seeing that as dialogues extend from 10 to 20 turns, all three methods show declining AR GAR scores, but the degradation patterns diverge significantly. The token gap widens dramatically by 77%, suggesting that longer conversations amplify the distribution shift problem—more model-generated tokens accumulate, making the attention patterns learned during teacher forcing increasingly misaligned with actual inference behavior.

In contrast, the self-sampling gap grows more modestly to 1.84×, staying well under 2×, which indicates the method's robustness holds up better in longer contexts since the training with mixed-length model-generated sequences gives the model stronger generalization. Across all three approaches, the absolute GAR scores decline, but self-sampling shows the smallest relative drop at 22%, compared to 50% for the base model and 44% for token gap, confirming that the attention steering mechanism remains most resilient in extended dialogue scenarios.

Generating markdown table...

The visualization shows how exposure bias compounds differently across methods—teacher forcing's gap explodes exponentially with conversation length while self-sampling degrades much more gracefully, demonstrating that exposure bias isn't a static problem but one that worsens super-linearly as model-generated tokens accumulate distribution drift over longer exchanges. 验证各个实验计划中的数值一致性，确保 gap ratio 的计算准确——特别是检查 plan_012 中的 TG gap 比率是否与 plan_026 中的数据对齐。

对于 plan_030，我在核实 Qwen 的 TF GAR 和 AR GAR 数值，确认 gap 计算结果约为 31.5。

现在我发现 d048_final_ar_eval 中的 beta0 tg_gar 是 0.064，这与之前 plan_002 中的 0.0157 不同——原因是两次评估使用了不同的协议和数据量。为了保持一致性，我应该在 plan_030 表格中使用 d048_final_ar_eval 的最终数值。

用这个 0.064 的数字，TG TF GAR 与 beta0 的差距是 7.8 倍，这与论文中提到的 Qwen N=50 时的 7.8 倍差距相符。之前看到的 32 倍差距是来自更早的评估（N=5，10 轮对话），而不是最终的 N=50 评估。

现在我需要理清在不同对话长度下"差距"的含义，特别是对于 plan_030 的长对话评估。

关键是认识到 AR GAR 会随着评估协议而变化：v7 使用 5 个对话、10 轮得到 32 倍的差距，而 d048 使用 50 个对话、可变轮数得到 7.8 倍的差距。由于 plan_030 测试的是 15-20 轮的更长对话，基线差距应该会比 10 轮的情况更大。

现在我在计算不同轮数下的预测值：10 轮时 TG 差距约 31 倍、SS 差距 1.44 倍，而 15 轮和 20 轮时这些差距会进一步扩大，TG 差距分别达到 41.7 倍和 55.6 倍。

TF GAR 保持在 0.50 左右是因为它总是在黄金文本上评估，不受对话长度影响，而 AR GAR 随着长度增加而下降，因为模型生成的上下文不断累积。现在我需要用这些数字来完成 YAML 配置，但要先确认 plan_030 中的测试轮数设置是否与计划描述一致。

我还需要考虑 UltraChat 中是否有足够长的对话（15-20 轮），如果没有可能需要生成或使用其他数据集。最后，我应该在叙述指导中说明这些实验如何共同影响梦想评审分数和论文的竞争力。

现在我来映射每个实验如何解决关键的弱点：单模型问题由 Llama 自监督学习处理，调优不足由 λ_GAR 敏感性分析解决，GAR 作为唯一指标的问题通过替代定义来处理，而暴露偏差的已知性通过 KL 散度机制证据和长度缩放分析来应对。种子数量的问题也通过多种子实验覆盖。这样所有严重问题都得到了解决，剩余的风险主要在于某些评审者可能仍然认为暴露偏差是已知的，但 KL 散度和替代 GAR 分析提供了具体的新颖性主张。

现在开始写 YAML 配置。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06b5b095-574f-4cc7-9e26-deb2e8df47ed",
  "isSidechain": false,
  "requestId": "req_011CbM4VAGZNMwkSRLjM5RQx",
  "type": "assistant",
  "uuid": "50ed477c-3eb8-487c-b19b-c8d179da3342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014k2qTUF5wTWHnrGNA1DkMw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 63919,
      "output_tokens": 39701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 39701,
          "cache_read_input_tokens": 63919,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-24T08:28:48.223Z_

Now I have all context needed. Let me produce the comprehensive predictions for every planned experiment under the "best" tier.

```yaml
tier: best
narrative_guidance: >-
  完整 'discover→diagnose→remedy' 弧全面成立。9 项 planned 实验中，Llama SS 跨模型验证（plan_026）
  和 λ_GAR 敏感性消融（plan_022）是最关键的新增证据——前者将 SS 升级为 model-general mitigation（C5），
  后者彻底消除 'gradient weight insufficient' 反驳（W2）。KL divergence（plan_025）提供 head-level
  机制证据，锁定 '为什么 exposure bias 选择性破坏 GAR-ours 而非 GAR-Dongre'。3-seed 统计（plan_027）
  + 4th seed（plan_029）+ alternative GAR definitions（plan_028）形成方法论防火墙。长对话 eval
  （plan_030）展示 SS 在 20+ turn 场景下仍有效，增强实用价值叙事。所有 fatal/severe reviewer concerns
  归零或降为 medium。Paper 定位 EMNLP main conference 3.5–4.0，Title 用 T2 'From Collapse to
  Recovery' 突出完整弧。核心差异化从 'gating 失败了' 升级为 '首个 exposure bias 对 auxiliary attention
  loss 的定量测量 + PCGrad 因果排除 + SS/steering 跨模型修复'。

imagined_experiments:

  # ──────────────────────────────────────────
  # plan_013: Llama Gradient Conflict Analysis
  # ──────────────────────────────────────────
  - name: "Llama-3.1-8B Gradient Conflict Cross-Model Analysis"
    plan_id: "plan_013"
    description: >-
      Verify NTP-GAR gradient competition pattern on Llama-3.1-8B. Test whether
      gradient direction conflict is model-agnostic or architecture-dependent.
    expected_results:
      cos_sim_mean: 0.0045
      cos_sim_std: 0.07
      neg_cos_sim_layers_pct: 53.1
      mag_ratio_median: 25.7
      cross_model_ntp_dominance: true
      gradient_direction_pattern: "near-orthogonal, not systematic conflict"
    result_rationale: >-
      Llama 架构与 Qwen 不同（GQA vs MHA, 32 vs 28 层, RoPE 实现差异），但 NTP-GAR 梯度关系的
      核心模式——NTP 幅度压制 GAR——在两模型上一致。Llama mag_ratio=25.7× 甚至高于 Qwen 的 14.7×
      （epoch 2），反映 32 层架构中 NTP 梯度沿更长残差链积累，GAR 信号在相同层数中被更强稀释。
      cos_sim≈0（近正交）而非 Qwen 的 cos_sim<0（冲突），说明 Llama 上 NTP 和 GAR 梯度方向几乎
      无系统性交互——53.1% 负层比例接近随机期望 50%。这为 PCGrad 因果排除提供完美跨模型补充：
      Qwen 有真实方向冲突，PCGrad 消除后 gap 不变；Llama 连方向冲突都不存在，gap 同样严重（15.9×）。
      两者共同构成 modus tollens：方向冲突既非必要条件（Llama 无冲突仍有 gap）也非充分条件
      （Qwen 有冲突但 PCGrad 消除后无改善），对 exposure bias gap 完全无因果影响。
    tables:
      - caption: "Cross-model NTP-GAR gradient analysis on gate parameters"
        columns: ["Model", "cos_sim", "neg_layers %", "mag_ratio", "Direction Pattern"]
        rows:
          - ["Qwen-2.5-7B (ep0)", "-0.089", "78.6%", "7.5x", "Systematic conflict"]
          - ["Qwen-2.5-7B (ep2)", "-0.042", "67.9%", "14.7x", "Conflict weakens, amp grows"]
          - ["Llama-3.1-8B (ep2)", "+0.005", "53.1%", "25.7x", "Near-orthogonal, strong amp"]
    figures_description:
      - >-
        Per-layer cos_sim violin plot: Qwen (blue, 28 layers) vs Llama (orange, 32 layers).
        Qwen distribution sits below zero (systematic conflict); Llama distribution centered
        at zero (random). Horizontal dashed line at cos_sim=0. Inset: per-layer mag_ratio
        bar chart showing NTP dominance in both models. Low saturation colors per CLAUDE.md
        style guidance.
    analysis: >-
      进入 §6.2 PCGrad Gradient Conflict Exclusion 和 §6.5 Cross-Model Replication。
      与 plan_018（Qwen PCGrad）形成 modus tollens：消除冲突→gap 不变（Qwen v9），
      本无冲突→gap 同样严重（Llama），∴ 方向冲突在任何模型上都不是 gap 的因果因素。
      mag_ratio 的跨模型一致性（Qwen 14.7×, Llama 25.7×）支撑 '幅度主导使方向无关紧要'
      论述。此数据可合并到 cross-model summary table。

  # ──────────────────────────────────────────
  # plan_020: Expanded Eval Set
  # ──────────────────────────────────────────
  - name: "Expanded TF Eval Set (N=200)"
    plan_id: "plan_020"
    description: >-
      Increase TF eval from 50 to 200 conversations for tighter bootstrap CI.
      AR eval stays at N=50 (sufficient given extreme effect sizes).
    expected_results:
      tf_n_conversations: 200
      ar_n_conversations: 50
      tg_lo_gar_ci_n200: [-0.0012, 0.0028]
      ug_lo_gar_ci_n200: [-0.0004, 0.0035]
      tg_ug_gar_ci_n200: [-0.0022, 0.0004]
      tg_lo_ppl_ci_n200: [-0.003, 0.003]
      all_cis_include_zero: true
      ci_width_reduction_vs_n50_pct: 28
    result_rationale: >-
      N=200 TF eval 将 bootstrap CI 宽度缩小约 28%（CI 宽度 ∝ 1/√N，√(50/200)=0.5，
      从 N=50 的 width 0.0054 收窄到 N=200 的 ~0.0040）。所有 pairwise comparison 的
      95% CI 仍包含 0，统计上确认 TG/UG/LoRA-only 三者在 TF regime 下 GAR-ours 无差异。
      AR eval 保持 N=50 因为效应量极大（8×–27× gap 下即使 N=10 也足以检测 SS vs TG 差异）。
      在 best 档位下，此实验是纯方法论稳健性增量——不改变任何结论，但为 bootstrap CI
      提供更窄的置信带，提升论文的统计可信度。W7 的统计维度由此全面覆盖。
    tables:
      - caption: "Bootstrap 95% CI: zero-benefit test at N=50 vs N=200"
        columns: ["Comparison", "N=50 CI", "N=200 CI", "Zero in CI?"]
        rows:
          - ["TG - LoRA (GAR)", "[-0.0018, +0.0036]", "[-0.0012, +0.0028]", "Yes"]
          - ["UG - LoRA (GAR)", "[-0.0006, +0.0045]", "[-0.0004, +0.0035]", "Yes"]
          - ["TG - UG (GAR)", "[-0.0030, +0.0006]", "[-0.0022, +0.0004]", "Yes"]
          - ["TG - LoRA (PPL)", "[-0.004, +0.004]", "[-0.003, +0.003]", "Yes"]
    figures_description: []
    analysis: >-
      数据进入 §5.2 Main Results 统计注脚或 Appendix A。N=200 CI 收窄但结论不变——
      审稿人无法以 'insufficient eval size' 为由质疑 zero-benefit 结论。此实验与
      plan_015（bootstrap CI）和 plan_027（3-seed）共同构成方法论防火墙。

  # ──────────────────────────────────────────
  # plan_022: λ_GAR Sensitivity Ablation
  # ──────────────────────────────────────────
  - name: "λ_GAR Sensitivity Ablation (λ=0.1 and λ=10)"
    plan_id: "plan_022"
    description: >-
      Train v7 with λ_GAR=10 and λ_GAR=0.1 (1 epoch each). Test whether GAR loss
      weight affects the exposure bias gap. Directly addresses W2 (hyperparameter tuning).
    expected_results:
      # λ=10 (1 epoch)
      lambda10_tf_gar_ours: 0.52
      lambda10_ar_gar_ours: 0.018
      lambda10_gap: 28.9
      lambda10_ppl: 2.95
      lambda10_gate_mean: 0.905
      lambda10_mag_ratio_epoch0: 0.75
      lambda10_ntp_loss: 0.951
      # λ=0.1 (1 epoch)
      lambda01_tf_gar_ours: 0.28
      lambda01_ar_gar_ours: 0.013
      lambda01_gap: 21.5
      lambda01_ppl: 2.79
      lambda01_gate_mean: 0.975
      lambda01_mag_ratio_epoch0: 75.0
      # Reference: v7 λ=1.0 (3 epoch)
      v7_tf_gar_ours: 0.50
      v7_ar_gar_ours: 0.016
      v7_gap: 31.3
      v7_ppl: 2.78
      ar_gar_invariant_to_lambda: true
      ar_gar_range_across_lambda: [0.013, 0.018]
      baseline_ar_gar: 0.012
    result_rationale: >-
      λ_GAR=10 使 GAR 梯度幅度在训练初期实际超过 NTP（epoch 0 mag_ratio 降到 0.75×，
      即 GAR gradient 1.33× > NTP），gate 获得充足梯度学习 GAR-optimal 配置（gate_mean
      降到 0.905，比 v7 的 0.934 有更大调制幅度）。TF GAR 确实提升到 0.52（vs v7 0.50），
      证明更高 λ 推动了更强的 gold-distribution GAR 优化。但 AR GAR 仍停在 0.018——
      仅比 baseline 0.012 高 0.006，在 baseline 噪声范围内。Gap 28.9× 与 v7 的 31.3×
      基本相当（差异来自 TF GAR 分子变化，非 AR GAR 分母改善）。PPL 轻微恶化（2.95 vs
      2.78）反映 GAR 梯度竞争了 NTP 的优化预算。λ=0.1 时 GAR 训练不充分（TF 0.28），
      gate 近乎 identity（0.975），但 AR GAR（0.013）同样停在 baseline 水平。三个 λ
      值跨 100× 范围，AR GAR 始终在 [0.013, 0.018] 窄带内——此窄带恰好覆盖 base model
      的自然 GAR（0.012），说明 exposure bias 完全抵消了训练获得的 attention steering
      能力。这是最直接的 W2 消除证据：即使让 GAR gradient 幅度主导训练（λ=10,
      mag_ratio<1），推理时的 distribution shift 仍然摧毁所有训练收益。
    tables:
      - caption: "lambda_GAR sensitivity: AR GAR invariant to loss weight"
        columns: ["lambda_GAR", "Epochs", "TF GAR", "AR GAR", "Gap", "PPL", "mag_ratio (ep0)"]
        rows:
          - ["0.1", "1", "0.28", "0.013", "21.5x", "2.79", "75x"]
          - ["1.0 (v7)", "3", "0.50", "0.016", "31.3x", "2.78", "7.5x"]
          - ["10.0", "1", "0.52", "0.018", "28.9x", "2.95", "0.75x"]
          - ["Baseline", "-", "-", "0.012", "-", "-", "-"]
    figures_description:
      - >-
        Dual-panel figure. Left: bar chart of AR GAR across λ values (0.1, 1.0, 10.0),
        dashed horizontal line at baseline 0.012. All three bars cluster near baseline,
        despite 100× range in λ. Right: scatter of TF GAR (y) vs λ (x, log scale),
        showing monotonic increase from 0.28→0.52 — training signal is received but
        doesn't transfer. Muted blue/green palette per style guidance.
    analysis: >-
      进入 Appendix B 或 §6.1 Gate Turn Conditioning Analysis 作为补充消融。核心论点：
      λ=10 使 GAR gradient 实际主导训练（mag_ratio<1），但 AR GAR 不变——与 PCGrad
      结果（plan_018）形成正交互补：PCGrad 消除方向冲突→gap 不变，λ=10 消除幅度差距
      →gap 不变。两者共同排除 gradient competition 在方向和幅度两个维度上的因果作用，
      仅剩 exposure bias（distribution shift）作为唯一未被排除的根因。W2 彻底消除。

  # ──────────────────────────────────────────
  # plan_025: TF vs AR Attention KL Divergence
  # ──────────────────────────────────────────
  - name: "TF vs AR Per-Head Attention KL Divergence"
    plan_id: "plan_025"
    description: >-
      Compute KL(P_TF||P_AR) per attention head on 50 conversations. Quantify which
      heads are most disrupted by distribution shift and correlate with GAR contribution.
    expected_results:
      mean_kl_all_heads: 0.087
      std_kl_all_heads: 0.052
      mean_kl_early_L0_L5: 0.034
      mean_kl_mid_early_L6_L13: 0.058
      mean_kl_mid_late_L14_L19: 0.092
      mean_kl_late_L20_L27: 0.180
      max_kl_single_head: 0.42
      max_kl_head_id: "L25H3"
      pct_high_kl_heads_in_gar_relevant_top_quartile: 72
      pearson_r_kl_vs_gar_contribution: 0.38
      pearson_p_kl_vs_gar_contribution: 0.002
      ss_model_mean_kl: 0.048
      ss_kl_reduction_vs_tg_pct: 45
      n_conversations: 50
      n_heads_total: 196
    result_rationale: >-
      KL(P_TF||P_AR) 量化每个 attention head 在 teacher-forced vs autoregressive context
      下的注意力分布差异。Late layers（L20-L27）平均 KL 0.180，是 early layers（L0-L5,
      0.034）的 5.3×——深层负责高层语义整合和跨 turn goal-relevant routing，对 input
      distribution 的变化最敏感。早期层主要处理局部 token 关系（syntax, local coherence），
      对 gold vs model-generated text 的差异不敏感。最关键发现是 head-GAR 相关性：对
      goal-token attention 贡献最大的 heads 中 72% 落入高 KL quartile（r=0.38, p=0.002）。
      这提供了 exposure bias 选择性破坏 GAR-ours 的 head-level 因果路径：last-token →
      goal 的 summary attention routing 由少数 specialized heads 执行（集中在 L20-L27），
      这些 heads 恰好是 distribution shift 影响最大的。GAR-Dongre（all-token attention）
      不依赖这些 specialized routing heads，而是利用较低层的 content-overlap attention，
      所以 TF-AR 无 gap。SS 模型的 mean KL 下降 45%（0.087→0.048），证明 SS 训练确实
      通过缩小 TF-AR attention 分布差异来改善 GAR，而非通过其他间接机制。L25H3 的
      max KL=0.42 表明个别 head 的 distribution shift 极度严重。
    tables:
      - caption: "Per-layer-group attention KL divergence (TG v7 model)"
        columns: ["Layer Group", "Mean KL (nats)", "Std", "GAR-relevant heads %", "Top KL quartile %"]
        rows:
          - ["L0-L5 (early)", "0.034", "0.012", "15%", "8%"]
          - ["L6-L13 (mid-early)", "0.058", "0.021", "22%", "18%"]
          - ["L14-L19 (mid-late)", "0.092", "0.031", "28%", "25%"]
          - ["L20-L27 (late)", "0.180", "0.065", "35%", "49%"]
      - caption: "KL divergence: TG vs SS model"
        columns: ["Model", "Mean KL", "Late-layer KL", "GAR-KL correlation r"]
        rows:
          - ["TG v7", "0.087", "0.180", "0.38"]
          - ["SS v8b", "0.048", "0.098", "0.22"]
          - ["Reduction", "-45%", "-46%", "-"]
    figures_description:
      - >-
        28x7 heatmap (layers × heads per layer group): KL divergence intensity for TG v7.
        Sequential colormap (cream→burnt orange) with star markers on heads with top-10
        GAR contribution. Stars cluster in the warm-colored zone of late layers (L20-L27).
        Colorbar: 0–0.45 nats. Clean grid with thin lines. Subplot below: same heatmap
        for SS model showing overall cooler colors (lower KL).
      - >-
        Scatter plot: head-level KL (x-axis) vs head-level GAR contribution (y-axis),
        r=0.38 annotation. Points colored by layer depth (gradient light-blue → deep-blue).
        Regression line with translucent 95% confidence band. Late-layer heads cluster
        in upper-right quadrant. Marginal density strips on both axes.
    analysis: >-
      进入 §6.3 Distribution Shift Analysis 作为核心机制证据。论点链：(1) distribution
      shift 导致 attention 分布改变 (KL>0)；(2) KL 在负责 goal-routing 的 heads 上最大
      (r=0.38)；(3) 这些 heads 是 GAR-ours 依赖的 (summary-position → goal)；(4)
      GAR-Dongre 不依赖这些 heads 所以无 gap。将 8×–27× gap 从 aggregate observation
      升级为 head-level mechanistic explanation。SS 的 45% KL 降低与 plan_028（SS 改善
      所有 GAR 定义）形成一致叙事——SS 的有效性来自真正缩小了 TF-AR attention distribution
      的差异，不是 metric hacking。此 figure 适合作为论文 Fig.3 或 Fig.4。

  # ──────────────────────────────────────────
  # plan_026: Llama-3.1-8B Scheduled Sampling
  # ──────────────────────────────────────────
  - name: "Llama-3.1-8B Scheduled Sampling Training + Eval"
    plan_id: "plan_026"
    description: >-
      Replicate SS on Llama-3.1-8B. If gap also compresses, SS upgrades from
      Qwen-specific finding to model-general mitigation. MUST-HAVE for best tier.
    expected_results:
      # Training
      training_epochs: 3
      training_wall_clock_hours: 8.5
      final_loss: 0.924
      final_ntp_loss: 0.923
      final_gar_loss: 0.001
      final_gate_mean: 0.935
      final_gate_std: 0.062
      ss_max_ratio: 0.3
      ss_steps_observed_pct: 29
      # TF eval
      tf_gar_ours: 0.47
      tf_gar_dongre: 0.35
      tf_ppl: 2.55
      # AR eval
      ar_gar_beta0: 0.35
      ar_gar_beta0_ci_95: [0.32, 0.38]
      ar_gar_beta3: 0.56
      ar_gar_beta5: 0.70
      ar_ppl_beta0: 1.36
      ar_ppl_beta3: 1.52
      ar_ppl_beta5: 1.71
      # Gap analysis
      gap_ratio: 1.34
      vs_llama_tg_gap: 15.9
      gap_compression_factor: 11.9
      vs_qwen_ss_gap: 1.26
      cross_model_consistency: true
    result_rationale: >-
      Llama SS 的 gap 压缩（15.9× → 1.34×）与 Qwen 上的模式一致（32× → 1.26×），
      尽管两个模型架构差异显著（GQA vs MHA, 32 vs 28 层, 不同 tokenizer/vocab size）
      且 ss_max_ratio 不同（Llama 0.3 vs Qwen 0.5）。AR GAR β=0=0.35 落在 best 档位
      要求的 [0.3, 0.5] 范围内。Gap 1.34× 落在 [1.0, 2.0] 范围内。SS 有效性的跨模型
      一致性源于其解决的是 fundamental distributional problem——训练时 context 是 gold
      text，推理时是 model-generated text，SS 通过在训练中混入 model-generated context
      缩小这一分布差距。这个机制不依赖特定的 attention 架构（MHA 或 GQA），因为 exposure
      bias 是所有 teacher-forced 训练的共性问题。Llama gap 略高于 Qwen（1.34× vs 1.26×），
      可能因 ss_max_ratio 0.3 暴露的 model-generated context 比例更低——若提升到 0.5
      预计可进一步压缩。PPL 1.36 与 Llama TG（1.32）可比（Δ=0.04），Llama base（1.24）
      差距也很小，确认 SS 训练不损害语言建模质量。β steering 同样有效且跨模型一致：
      β=3 时 Llama 0.56（Qwen 0.596），β=5 时 Llama 0.70（Qwen 0.717）。
    tables:
      - caption: "Llama-3.1-8B inference comparison: SS vs baselines"
        columns: ["Method", "TF GAR", "AR GAR (beta=0)", "Gap", "PPL", "Gap Compression"]
        rows:
          - ["Base", "0.017", "0.009", "1.9x", "1.24", "-"]
          - ["TG v7", "0.484", "0.030", "15.9x", "1.32", "1.0x (ref)"]
          - ["LoRA-only", "0.481", "0.028", "17.2x", "1.32", "0.93x"]
          - ["SS (ours)", "0.47", "0.35", "1.34x", "1.36", "11.9x"]
      - caption: "Cross-model SS gap compression (main contribution table)"
        columns: ["Model", "Arch", "TG Gap", "SS Gap", "SS AR GAR", "Compression", "PPL delta"]
        rows:
          - ["Qwen-2.5-7B", "MHA 28L", "32.1x", "1.26x", "0.401+-0.047 (3-seed)", "25.5x", "+0.01"]
          - ["Llama-3.1-8B", "GQA 32L", "15.9x", "1.34x", "0.35", "11.9x", "+0.04"]
      - caption: "Llama SS: beta-steering response"
        columns: ["beta", "AR GAR (Llama SS)", "AR GAR (Qwen SS 3-seed)", "PPL (Llama SS)"]
        rows:
          - ["0", "0.35", "0.401+-0.047", "1.36"]
          - ["3", "0.56", "0.596+-0.008", "1.52"]
          - ["5", "0.70", "0.717+-0.001", "1.71"]
    figures_description:
      - >-
        Side-by-side grouped bar chart: Qwen (left panel) and Llama (right panel).
        Each panel has 4 bars (Base, TG, LoRA, SS) showing AR GAR at β=0. SS bar
        dramatically taller than others in both panels. Y-axis linear 0–0.5. Inset
        text: gap ratio for each method. Shared legend at top. Muted palette:
        gray (Base), coral (TG), salmon (LoRA), teal (SS).
      - >-
        Overlay line plot: AR GAR vs β (0, 3, 5) for Qwen SS (solid blue, 3-seed
        mean with error band) and Llama SS (dashed orange). Nearly parallel ascending
        lines. Both converge toward TG steering values at β=5. Horizontal gray band
        at Qwen/Llama base GAR levels.
    analysis: >-
      进入 §5.4 Scheduled Sampling Results 和 §6.5 Cross-Model Replication。这是 best
      档位的核心实验——将 C5 从 'cross-model failure replication' 升级为 'cross-model
      mitigation validation'，也是 Title T2 'From Collapse to Recovery' 的跨模型支撑。
      Cross-model SS summary table 是论文的 flagship contribution table，直接支撑
      5th contribution claim。两模型 gap compression 的一致性（均 >10×）确认 SS 解决
      的是 fundamental distributional issue。Discussion 需注明 Llama compression 稍低
      可能因 ss_max_ratio=0.3（vs Qwen 0.5），未来工作可测试 ratio 提升的效果。
      W1（single model）至此彻底消除。

  # ──────────────────────────────────────────
  # plan_027: SS 3-Seed Validation
  # ──────────────────────────────────────────
  - name: "SS 3-Seed Statistical Validation (Qwen-2.5-7B)"
    plan_id: "plan_027"
    description: >-
      3 seeds (42, 123, 456) for SS training. Provide mean±std and bootstrap CI for
      all key metrics. Addresses W7 (single seed).
    expected_results:
      tf_gar_mean: 0.498
      tf_gar_std: 0.004
      tf_gar_s42: 0.503
      tf_gar_s123: 0.495
      tf_gar_s456: 0.496
      ar_gar_beta0_mean: 0.401
      ar_gar_beta0_std: 0.047
      ar_gar_beta0_s42: 0.347
      ar_gar_beta0_s123: 0.423
      ar_gar_beta0_s456: 0.433
      ar_gar_beta3_mean: 0.596
      ar_gar_beta3_std: 0.008
      ar_gar_beta5_mean: 0.717
      ar_gar_beta5_std: 0.001
      ppl_beta0_mean: 1.441
      ppl_beta0_std: 0.001
      gap_mean: 1.26
      gap_std: 0.17
      gap_range_min: 1.15
      gap_range_max: 1.45
      cohens_d_ss_vs_baseline: 8.1
    result_rationale: >-
      3-seed 均值 AR GAR β=0=0.401±0.047 落在 best 档位 [0.38, 0.45] 范围内。Gap
      1.26±0.17 落在 [1.1, 1.5] 范围内。关键发现：(1) TF GAR 跨 seed 极稳定（std=0.004），
      证明 SS 在 gold distribution 上的训练高度可复现——三个 seed 的 TF GAR 仅在
      0.495–0.503 范围内波动（相对变异 0.8%）。(2) AR GAR β=0 变异较大（std=0.047,
      相对变异 11.7%），s42 是低端 outlier（0.347 vs s123/s456 的 0.423/0.433）。这种
      IID 稳定 + OOD 变异大的模式本身就是 exposure bias 的统计 signature：模型在 IID
      条件下行为高度一致，但在 OOD 条件下对训练随机性更敏感——distribution shift 放大了
      random seed 对 learned attention pattern 的影响。(3) β=3/5 的跨 seed 方差消失
      （std<0.01），因为推理时 steering 主导了 attention pattern，覆盖了训练 seed 的
      随机效应——β 越大，TF/AR 行为越趋同。(4) PPL 1.441±0.001 跨 seed 几乎无差异，
      确认 SS 训练不损害语言建模质量。Cohen's d=8.1（SS vs baseline AR GAR）是极强效应。
    tables:
      - caption: "3-seed SS results on Qwen-2.5-7B"
        columns: ["Seed", "TF GAR", "AR GAR beta=0", "AR GAR beta=3", "AR GAR beta=5", "PPL beta=0", "Gap"]
        rows:
          - ["s42", "0.503", "0.347", "0.593", "0.717", "1.442", "1.45x"]
          - ["s123", "0.495", "0.423", "0.590", "0.717", "1.441", "1.17x"]
          - ["s456", "0.496", "0.433", "0.605", "0.716", "1.439", "1.15x"]
          - ["Mean+-std", "0.498+-0.004", "0.401+-0.047", "0.596+-0.008", "0.717+-0.001", "1.441+-0.001", "1.26+-0.17"]
    figures_description:
      - >-
        Strip plot with mean+CI overlay: x-axis has β=0, β=3, β=5. For each β, 3 seeds
        shown as jittered dots, horizontal bar for mean, translucent band for ±1 std.
        CI band narrows dramatically from β=0 (wide) to β=5 (near-zero), visually
        conveying that steering stabilizes across training randomness. Gray horizontal
        band at bottom shows base model GAR range. Soft blue dots, teal mean bars.
    analysis: >-
      进入 §5.4 Scheduled Sampling Results 主表。3-seed 统计直接回应 W7（single seed），
      将 SS 从 'one-shot finding' 升级为 'statistically validated result'。β-dependent
      variance pattern 提供额外 insight 写入 Discussion §7.2：推理时 steering 是一种
      implicit variance reduction mechanism，对训练随机性的敏感性随 β 单调下降。3-seed
      足够因为 Cohen's d=8.1（vs baseline 0.019）是极强效应——即使 s42 这个最弱的 seed
      的 AR GAR（0.347）也是 baseline 的 18.3×。

  # ──────────────────────────────────────────
  # plan_028: Alternative GAR Definitions
  # ──────────────────────────────────────────
  - name: "Alternative GAR Definition Robustness (4 definitions x 3 models)"
    plan_id: "plan_028"
    description: >-
      Test 4 token-selection GAR variants (last/all/first/goal-only) on Base/TG/SS
      in AR regime. Verify SS improvement is broad, not position-specific overfitting.
    expected_results:
      base_last_token: 0.019
      base_all_token: 0.015
      base_first_token: 0.018
      base_goal_only: 0.022
      tg_last_token: 0.325
      tg_all_token: 0.025
      tg_first_token: 0.039
      tg_goal_only: 0.020
      ss_last_token: 0.401
      ss_all_token: 0.385
      ss_first_token: 0.362
      ss_goal_only: 0.378
      n_definitions_ss_improves: 4
      n_definitions_tg_improves: 1
      ss_min_improvement_over_base: 16.4
      tg_only_last_token_ratio_vs_others: 8.1
    result_rationale: >-
      TG 仅改善 last-token GAR（0.325），all/first/goal-only 接近 baseline（0.020–0.039），
      揭示 TG 在 teacher-forcing 下学到的是 position-specific attention shortcut：
      专门将 last token 的 attention 导向 goal tokens。这种 narrow routing pattern
      高度依赖 gold context 的 token 位置分布——model-generated text 的 token 组织方式
      不同，learned shortcut 即失效。SS 改善所有 4 种定义（均 >0.36），说明 SS 学到的
      是更 broad 的 goal-attention encoding：不仅 summary position（last token），而是
      response 的多个位置都建立了 goal attention。机制解释：SS 训练中 model-generated
      context 的分布多样性迫使模型不能依赖 position-specific cue，因为 model-generated
      text 的 token 位置特征与 gold text 不同（不同的 word choice → 不同的 sequence
      length → 不同的 positional pattern）。模型被迫学习基于 semantic goal-relevance
      而非 positional shortcut 的 attention pattern，这种 pattern 天然 distribution-robust。
      4/4 定义改善满足 best 档位 [3, 4] 要求。Base 一致 <0.022 排除随机性。
    tables:
      - caption: "AR GAR across 4 token-selection definitions (beta=0)"
        columns: ["GAR Definition", "Response Tokens", "Base", "TG", "SS", "SS/Base"]
        rows:
          - ["Last-token (GAR-ours)", "Last token per turn", "0.019", "0.325", "0.401", "21.1x"]
          - ["All-token (GAR-Dongre)", "All response tokens", "0.015", "0.025", "0.385", "25.7x"]
          - ["First-token", "First token per turn", "0.018", "0.039", "0.362", "20.1x"]
          - ["Goal-only", "Goal-adjacent tokens", "0.022", "0.020", "0.378", "17.2x"]
    figures_description:
      - >-
        Grouped bar chart: 4 GAR definitions (x-axis groups) × 3 methods (Base=light gray,
        TG=coral, SS=teal). TG profile: one tall bar (last-token 0.325) with three short
        bars (~0.02-0.04). SS profile: four uniformly tall bars (~0.36-0.40). The visual
        contrast between TG's 'spiky' and SS's 'flat' profiles is the key takeaway.
        Dashed line at max base value (0.022) for reference. Y-axis 0–0.45.
    analysis: >-
      进入 §6.4 Mechanism Specificity 或 Appendix D。双重叙事价值：(1) 解释为什么 TG 的
      exposure bias gap 如此严重——TG 学到 position-fragile shortcut；(2) 解释为什么
      SS 的 gap 更小——SS 学到 distribution-robust semantic attention。也回应 W3
      'GAR-ours 是否过于 narrow 的指标'：SS 在所有 4 种定义上的改善表明改善是 genuine
      attention steering 而非对特定 metric 的 overfitting。与 plan_025（KL divergence）
      互补：KL 从 head 维度解释 'why GAR-ours collapses'，alternative GAR defs 从
      token-position 维度解释 'why SS works broadly'。

  # ──────────────────────────────────────────
  # plan_029: SS 4th Seed
  # ──────────────────────────────────────────
  - name: "SS 4th Seed (s789) Supplementary Validation"
    plan_id: "plan_029"
    description: >-
      Additional seed to tighten mean±std. Lower ROI than Llama SS but adds reviewer
      confidence. Run only if GPU budget remains after plan_026.
    expected_results:
      s789_tf_gar: 0.497
      s789_ar_gar_beta0: 0.41
      s789_ar_gar_beta3: 0.598
      s789_ar_gar_beta5: 0.716
      s789_ppl_beta0: 1.441
      s789_gap: 1.21
      four_seed_mean_beta0: 0.404
      four_seed_std_beta0: 0.037
      four_seed_ci_95: [0.345, 0.463]
      ci_width_reduction_vs_3seed_pct: 21
      cohens_d_4seed: 9.2
    result_rationale: >-
      s789 的 AR GAR β=0=0.41 与 3-seed 均值 0.401 高度一致，不是 outlier。加入后
      4-seed std 从 0.047 收窄到 0.037（CI 宽度缩小 21%），95% CI [0.345, 0.463]
      下限 0.345 仍远高于 baseline 0.019（18.2×）。Cohen's d 从 8.1 提升到 9.2。
      但此实验的边际信息量有限——3-seed 的效应量已经足够极端，第 4 seed 不改变统计
      结论或审稿人评分。s789 gap=1.21× 略低于 3-seed 均值 1.26×，进一步确认 s42
      的 1.45× 是高端离群值而非 typical behavior。β=3/5 继续显示极低跨 seed 方差
      （std<0.01），steering 稳定性不随 seed 数量变化。PPL 1.441 与所有前 3 seed
      完全一致（std 仍为 0.001），语言建模质量不受训练随机性影响。ROI 明确低于
      plan_026（Llama SS）——跨模型验证的 novelty 贡献远大于 same-model 额外 seed
      的统计边际值。建议仅在 Llama SS 完成后有剩余 GPU 预算时执行。
    tables:
      - caption: "4-seed SS statistics (Qwen-2.5-7B, Appendix)"
        columns: ["Seed", "AR GAR beta=0", "AR GAR beta=3", "AR GAR beta=5", "PPL", "Gap"]
        rows:
          - ["s42", "0.347", "0.593", "0.717", "1.442", "1.45x"]
          - ["s123", "0.423", "0.590", "0.717", "1.441", "1.17x"]
          - ["s456", "0.433", "0.605", "0.716", "1.439", "1.15x"]
          - ["s789", "0.41", "0.598", "0.716", "1.441", "1.21x"]
          - ["Mean+-std", "0.404+-0.037", "0.597+-0.006", "0.717+-0.001", "1.441+-0.001", "1.25+-0.14"]
    figures_description: []
    analysis: >-
      进入 Appendix 表格。4-seed 不改变 §5.4 主表（仍用 3-seed），但可在 rebuttal
      中作为补充证据使用。主要价值：展示 due diligence + 确认 s42 是 low-end outlier。

  # ──────────────────────────────────────────
  # plan_030: Long Conversation Eval
  # ──────────────────────────────────────────
  - name: "Long Conversation Eval (15-20 turns)"
    plan_id: "plan_030"
    description: >-
      Test exposure bias gap scaling with conversation length (10/15/20 turns).
      Verify SS maintains advantage at longer conversations where mitigation matters most.
    expected_results:
      turns_tested: [10, 15, 20]
      # Base model
      base_gar_t10: 0.012
      base_gar_t15: 0.008
      base_gar_t20: 0.006
      base_gar_decay_10to20_pct: 50
      # TG model
      tg_ar_gar_t10: 0.016
      tg_ar_gar_t15: 0.012
      tg_ar_gar_t20: 0.009
      tg_ar_gar_decay_10to20_pct: 44
      # SS model
      ss_ar_gar_t10: 0.347
      ss_ar_gar_t15: 0.305
      ss_ar_gar_t20: 0.270
      ss_ar_gar_decay_10to20_pct: 22
      # Gap scaling
      tg_gap_t10: 31.5
      tg_gap_t15: 41.7
      tg_gap_t20: 55.6
      tg_gap_growth_10to20_pct: 77
      ss_gap_t10: 1.45
      ss_gap_t15: 1.63
      ss_gap_t20: 1.84
      ss_gap_growth_10to20_pct: 27
      # PPL at T=20
      ss_ppl_t20: 1.47
      base_ppl_t20: 1.48
      tg_ppl_t20: 1.46
      n_conversations_t15: 30
      n_conversations_t20: 20
    result_rationale: >-
      随着对话长度从 10→20 turn，三种方法的 AR GAR 均下降——更长对话意味着 goal
      信息在 attention 中更难触及（Dongre et al. 原始发现）。但下降速率揭示本质差异：
      Base 降幅 50%（0.012→0.006），TG 降幅 44%（0.016→0.009），SS 降幅仅 22%
      （0.347→0.270）。TG gap 从 31.5× 加剧到 55.6×（+77%），因为更长对话 = 更多
      model-generated tokens 积累 = distribution shift 以 compounding 方式放大。每个
      额外 turn 的 model-generated response 都在原有 context 基础上叠加新的分布偏移，
      使 TF 训练获得的 attention pattern 在 20 turn 时比 10 turn 更无法迁移。SS gap
      也增加（1.45× → 1.84×），但增幅仅 27%，且仍在 2× 以内。SS 的亚线性 gap 增长
      说明 SS 训练赋予的 distribution robustness 具有 lasting effect——ss_max_ratio=0.5
      的训练使模型见过了不同长度的 model-generated context，学到的 attention pattern
      对 context length 有一定泛化能力。PPL 在 T=20 时 SS 与 base 几乎无差异
      （1.47 vs 1.48），排除 SS 在长对话中引入 perplexity trade-off。N=20/30 conversations
      在 T=15/20 长度下足够检测 effect——SS 的绝对 GAR 优势（0.270 vs 0.009）是 30×，
      噪声无法遮蔽。
    tables:
      - caption: "Exposure bias gap scaling with conversation length (Qwen-2.5-7B)"
        columns: ["Turns", "Base GAR", "TG GAR", "SS GAR", "TG Gap", "SS Gap", "SS advantage"]
        rows:
          - ["10", "0.012", "0.016", "0.347", "31.5x", "1.45x", "21.7x over TG"]
          - ["15", "0.008", "0.012", "0.305", "41.7x", "1.63x", "25.4x over TG"]
          - ["20", "0.006", "0.009", "0.270", "55.6x", "1.84x", "30.0x over TG"]
          - ["Decay 10->20", "-50%", "-44%", "-22%", "+77%", "+27%", "+38% (growing)"]
    figures_description:
      - >-
        Dual-axis line plot: x-axis = conversation length (10, 15, 20 turns).
        Left y-axis = AR GAR (log scale): three declining lines — Base (gray, dashed),
        TG (coral, dotted), SS (teal, solid thick). SS line stays far above the others
        and declines more gently. Right y-axis = TF/AR gap ratio: two ascending lines —
        TG gap (coral) shoots up steeply, SS gap (teal) rises gently. Shaded area between
        TG and SS gap lines expands rightward, visually showing SS advantage grows with
        length. Background gradient from light (10T) to darker (20T) suggesting
        increasing difficulty.
    analysis: >-
      进入 §6.3 Distribution Shift Analysis 或 Appendix E。核心论点：exposure bias
      不是 static 现象——它随对话长度 super-linearly 恶化（TG gap +77% from 10→20T），
      因为 model-generated tokens 的累积 distribution drift 是 compounding 的。SS 的
      sub-linear 恶化（gap 仅 +27%）表明 SS 训练提供了 lasting distributional alignment。
      更重要的是 practical framing：真实对话经常超过 10 turn，SS 恰好在最需要
      intervention 的场景中表现最 robust——SS 的相对优势（SS over TG）从 10T 的 21.7×
      扩大到 20T 的 30.0×。此 figure 适合放在 §5.4 或 §6.3，可视化 'SS advantage
      grows with conversation length' 的叙事非常有力。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ed477c-3eb8-487c-b19b-c8d179da3342",
  "isSidechain": false,
  "requestId": "req_011CbM4VAGZNMwkSRLjM5RQx",
  "type": "assistant",
  "uuid": "8595df29-1053-4c00-a581-a86df7bc93fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014k2qTUF5wTWHnrGNA1DkMw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 63919,
      "output_tokens": 39701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 39701,
          "cache_read_input_tokens": 63919,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画 核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general miti…",
  "leafUuid": "8595df29-1053-4c00-a581-a86df7bc93fe",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Exposure bias destroys auxiliary attention losses",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画 核心假设：['Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general miti…",
  "leafUuid": "8595df29-1053-4c00-a581-a86df7bc93fe",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Exposure bias destroys auxiliary attention losses",
  "sessionId": "642a24ab-9637-448d-be97-8ff6319b4917"
}
```

---
