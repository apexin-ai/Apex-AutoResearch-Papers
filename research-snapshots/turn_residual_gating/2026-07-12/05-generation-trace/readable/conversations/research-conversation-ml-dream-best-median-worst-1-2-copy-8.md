# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/811da4b1-9877-49a9-a3f3-80ee3741d1e0.jsonl`
- **Structured JSON:** [`abb15a14b9aad7b1ba1b.json`](../../sessions/ab/abb15a14b9aad7b1ba1b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T08:11:42.695Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T08:11:42.695Z",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: turn_residual_gating\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**\n> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + \"观察→假设→排除→指向真因\" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result\n> **⚠️ Dream review D024: \"Cannot\" overclaims, novelty \"first measurement\" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 \"Fails to\", novelty 降级 \"first empirical characterization\"**\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 \"发现→定位→修复\" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。\n\n---\n\n## 1. Title Candidates\n\n- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating\n- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）\n- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）\n- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）\n\n推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 \"selectively destroys\"，去掉冗长副标题。T2 强调 \"发现→定位→修复\" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete \"discover → diagnose → initial remedy\" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |\n| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**\n\n**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 \"PPL -46%\" 和 \"selective dissociation\" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**\n7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication\n8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**\n9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) \"Parallel Attention Forcing\" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期（2026-05-23 Framing 升级后）\n- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。\n- **Best case**: 3.5 (Borderline Conference / Accept)。完整 \"发现→定位→修复\" 弧匹配 gromov/sun/xiao 模式。\n- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。\n- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复\"（强）。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: C1\n  description: Phase 1 GAR degradation diagnosis on Qwen-2.5-7B (70.8% raw drop)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: phase1_gar_diag\n  status: DONE\n  conclusion: success\n  metrics:\n    turn1_avg_gar: 0.0418\n    mid_turns_avg_gar: 0.0122\n    relative_drop: 0.708\n    num_conversations: 5\n    num_turns: 10\n    per_turn_avg_gar:\n    - 0.0418\n    - 0.0241\n    - 0.0224\n    - 0.013\n    - 0.0133\n    - 0.0086\n    - 0.0078\n    - 0.008\n    - 0.0157\n    - 0.0064\n- id: plan_002\n  claim: C2\n  description: ThreadGate v7 training (MSE+gate_div) - training GAR 0.48, inference\n    GAR 0.016\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_tg_s42_v7\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5035\n    eval_iid_dongre_mid_gar: 0.0152\n    eval_iid_ppl: 2.784\n    eval_heldout_ours_mid_gar: 0.5035\n    eval_heldout_dongre_mid_gar: 0.0152\n    eval_heldout_ppl: 2.78\n    eval_modelgen_ours_mid_gar: 0.0157\n    eval_modelgen_dongre_mid_gar: 0.0194\n    eval_modelgen_ppl: 1.36\n    gate_mean_final: 0.9336\n    gate_std_final: 0.0492\n- id: plan_003\n  claim: C4\n  description: Uniform Gate ablation - isolate turn conditioning contribution\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_ug_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_avg_loss: 1.0019\n    epoch0_avg_ntp: 0.9755\n    epoch0_avg_gar: 0.0259\n    epoch0_avg_div: 0.0005\n    epoch1_avg_loss: 0.9447\n    epoch1_avg_ntp: 0.9435\n    epoch1_avg_gar: 0.0013\n    epoch1_avg_div: 0\n    epoch2_avg_loss: 0.9319\n    epoch2_avg_ntp: 0.9309\n    epoch2_avg_gar: 0.001\n    epoch2_avg_div: 0\n    final_gate_mean: 0.9598\n    final_gate_std: 0.0518\n    final_gate_min: 0.7773\n    final_gate_max: 1\n    final_profile_L3: 0.777\n    final_profile_L5: 0.812\n    final_profile_L0: 0.875\n    final_profile_L27: 1\n    training_time_seconds: 21994.5\n    training_time_hours: 6.1\n    global_steps: 7950\n    unexpected_per_layer_variation: true\n    eval_modelgen_ours_mid_gar: 0.0149\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.396\n- id: plan_004\n  claim: C4\n  description: LoRA-only ablation - isolate gating mechanism contribution\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: phase2_lora_only_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    global_steps: 3000\n    training_time_seconds: 20588.6\n    training_time_hours: 5.7\n    gate_fixed: 1\n    gate_type_actual: none\n    final_lora_size_mb: 20\n    eval_modelgen_ours_mid_gar: 0.0245\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.371\n- id: plan_005\n  claim: C4\n  description: Four-way eval (Base/TG/UG/LoRA-only x GAR-ours/Dongre + PPL)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_002\n  - plan_003\n  - plan_004\n  registry_id: phase2_4way_eval\n  status: DONE\n  conclusion: negative\n  metrics:\n    base_ours_mid_gar: 0.0107\n    base_ours_recovery_pp: -0.15\n    base_dongre_mid_gar: 0.003\n    base_dongre_recovery_pp: -0.92\n    base_ppl: 4.23\n    base_ntp: 1.4162\n    tg_ours_mid_gar: 0.4866\n    tg_ours_recovery_pp: 47.44\n    tg_dongre_mid_gar: 0.0157\n    tg_dongre_recovery_pp: 0.35\n    tg_ppl: 2.63\n    tg_ntp: 0.9484\n    ug_ours_mid_gar: 0.4923\n    ug_ours_recovery_pp: 48.01\n    ug_dongre_mid_gar: 0.013\n    ug_dongre_recovery_pp: 0.08\n    ug_ppl: 2.62\n    ug_ntp: 0.9433\n    lora_ours_mid_gar: 0.486\n    lora_ours_recovery_pp: 47.39\n    lora_dongre_mid_gar: 0.0137\n    lora_dongre_recovery_pp: 0.15\n    lora_ppl: 2.63\n    lora_ntp: 0.9482\n    route_b_confirmed: true\n    gating_incremental_benefit: none\n- id: plan_006\n  claim: C3\n  description: Gradient conflict analysis on v7 (3 epoch checkpoints) - NTP vs GAR\n    gradient cos_sim + magnitude ratio\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  registry_id: analysis_gradient_conflict\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_cos_sim: -0.089\n    epoch1_cos_sim: -0.054\n    epoch2_cos_sim: -0.042\n    epoch0_neg_layers_pct: 78.6\n    epoch1_neg_layers_pct: 71.4\n    epoch2_neg_layers_pct: 67.9\n    epoch0_mag_ratio: 7.5\n    epoch1_mag_ratio: 13.7\n    epoch2_mag_ratio: 14.7\n- id: plan_007\n  claim: C3\n  description: Attention heatmap visualization (4 models x 3 conversations x 28 layers)\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  - plan_003\n  - plan_004\n  registry_id: analysis_attention_heatmap\n  status: DONE\n  conclusion: success\n  metrics:\n    base_mean_goal_attn: 0.0136\n    base_decay: 0.875\n    tg_mean_goal_attn: 0.0232\n    tg_decay: 0.777\n    ug_mean_goal_attn: 0.0216\n    ug_decay: 0.803\n    lora_mean_goal_attn: 0.0216\n    lora_decay: 0.81\n    gating_incremental_benefit: none\n- id: plan_008\n  claim: C2, C4\n  description: 'Held-out eval: create truly held-out eval set (50 convs, idx>=8000\n    from UltraChat full) and re-run 4-way eval to validate conclusions on unseen data'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  status: DONE\n  registry_id: phase2_4way_eval_heldout\n  conclusion: success\n  metrics:\n    base_ours_mid_gar: 0.0128\n    base_ours_recovery_pp: 0.06\n    base_dongre_mid_gar: 0.0031\n    base_dongre_recovery_pp: -0.91\n    base_ppl: 4.34\n    base_ntp: 1.4045\n    tg_ours_mid_gar: 0.5035\n    tg_ours_recovery_pp: 49.13\n    tg_dongre_mid_gar: 0.0152\n    tg_dongre_recovery_pp: 0.3\n    tg_ppl: 2.78\n    tg_ntp: 0.9771\n    ug_ours_mid_gar: 0.5053\n    ug_ours_recovery_pp: 49.31\n    ug_dongre_mid_gar: 0.0124\n    ug_dongre_recovery_pp: 0.02\n    ug_ppl: 2.78\n    ug_ntp: 0.9752\n    lora_ours_mid_gar: 0.4978\n    lora_ours_recovery_pp: 48.56\n    lora_dongre_mid_gar: 0.0132\n    lora_dongre_recovery_pp: 0.1\n    lora_ppl: 2.78\n    lora_ntp: 0.9771\n    three_way_convergence_confirmed: true\n    gar_ours_spread_pp: 0.75\n    ppl_spread: 0\n    data_overlap: false\n- id: plan_009\n  claim: C5\n  description: Llama-3.1-8B Phase 1 GAR degradation diagnosis - confirm GAR decay\n    exists on different architecture\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps: []\n  status: DONE\n  registry_id: llama_phase1_gar_diag\n  conclusion: success\n  metrics:\n    per_turn_gar:\n      turn_1: 0.0263\n      turn_2: 0.0183\n      turn_3: 0.0087\n      turn_4: 0.0055\n      turn_5: 0.006\n      turn_6: 0.0035\n      turn_7: 0.0038\n      turn_8: 0.0037\n      turn_9: 0.005\n      turn_10: 0.0026\n    t1_t10_decay_pct: 90.1\n    t1_mid38_drop_pct: 80.2\n    n_topics: 5\n    model: Meta-Llama-3.1-8B-Instruct\n    mode: gen\n    n_conversations: 5\n    n_turns: 10\n- id: plan_010\n  claim: C5\n  description: Llama-3.1-8B ThreadGate v7 training - replicate Qwen setup on Llama\n  priority: P0\n  gpu_budget_hours: 7\n  deps:\n  - plan_009\n  status: DONE\n  registry_id: llama_tg_s42\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    total_steps: 3000\n    wall_clock_seconds: 26212\n    wall_clock_hours: 7.28\n    final_avg_loss: 0.9233\n    final_avg_ntp: 0.9224\n    final_avg_gar: 0.0009\n    final_avg_div: 0\n    final_gate_mean: 0.9099\n    final_gate_std: 0.0701\n    final_gate_min: 0.7188\n    final_gate_max: 0.9922\n    gate_profile_step3000:\n      L0: 0.957\n      L1: 0.973\n      L2: 0.977\n      L3: 0.965\n      L4: 0.992\n      L5: 0.969\n      L6: 0.957\n      L7: 0.957\n      L8: 0.961\n      L9: 0.949\n      L10: 0.938\n      L11: 0.934\n      L12: 0.969\n      L13: 0.953\n      L14: 0.957\n      L15: 0.965\n      L16: 0.953\n      L17: 0.961\n      L18: 0.922\n      L19: 0.902\n      L20: 0.883\n      L21: 0.863\n      L22: 0.836\n      L23: 0.844\n      L24: 0.809\n      L25: 0.719\n      L26: 0.762\n      L27: 0.805\n      L28: 0.801\n      L29: 0.855\n      L30: 0.898\n      L31: 0.934\n    checkpoint_size_gate_mb: 4.2\n    checkpoint_size_lora_mb: 26\n    gpu: NVIDIA RTX PRO 6000 Blackwell\n    vram_gb: 102\n    mem_used_gb: 63.4\n- id: plan_011\n  claim: C5\n  description: Llama-3.1-8B LoRA-only training - cross-model gating redundancy validation\n    (D020)\n  priority: P0\n  gpu_budget_hours: 7\n  deps:\n  - plan_009\n  status: DONE\n  registry_id: llama_lora_only_s42\n  conclusion: success\n  metrics:\n    final_avg_loss: 0.9288\n    final_avg_ntp: 0.9279\n    final_avg_gar: 0.0009\n    gate_fixed: 1\n    gate_type: none\n    wall_clock_s: 25317\n    wall_clock_h: 7.03\n    epochs_completed: 3\n- id: plan_012\n  claim: C5\n  description: Llama-3.1-8B 3-way eval (Base/TG/LoRA-only x GAR + PPL) on held-out\n    data\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_010\n  - plan_011\n  status: DONE\n  registry_id: llama_eval_s42\n  conclusion: success\n  metrics:\n    tf_base:\n      gar_ours: 0.0166\n      ngar_ours: 0.3882\n      gar_dongre: 0.0038\n      ngar_dongre: 0.163\n      ppl: 3.45\n      N: 50\n      T: 4\n    tf_tg:\n      gar_ours: 0.4836\n      ngar_ours: 11.8818\n      gar_dongre: 0.018\n      ngar_dongre: 0.7922\n      ppl: 2.57\n      N: 50\n      T: 4\n    ar_base:\n      gar_ours: 0.0086\n      ngar_ours: 0.0798\n      gar_dongre: 0.0118\n      ngar_dongre: 0.1265\n      ppl: 1.24\n      N: 5\n      T: 10\n    ar_tg:\n      gar_ours: 0.0304\n      ngar_ours: 0.2632\n      gar_dongre: 0.0217\n      ngar_dongre: 0.2459\n      ppl: 1.32\n      N: 5\n      T: 10\n    gap_ratio_tg_ours: 15.9\n    gap_ratio_base_ours: 1.93\n    gap_ratio_tg_dongre: 0.83\n    vs_qwen_v7_gap_ratio: 32.1\n    baseline_mid_gar: 0.0122\n- id: plan_013\n  claim: C3\n  description: Llama-3.1-8B gradient conflict analysis - verify NTP-GAR competition\n    is model-agnostic\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_010\n  status: planned\n  result: 'cos_sim=0.0045 (near-orthogonal, not conflict), neg_layers=53.1% (near\n    random), mag_ratio_median=25.7×. Cross-model confirms: gradients not conflicting,\n    NTP magnitude dominates. Consistent with Qwen. D054.'\n- id: plan_014\n  claim: W3\n  description: Downstream task sanity check - simple instruction retention test across\n    turns to link GAR to task performance\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_005\n  status: DONE\n  registry_id: instruction_retention_test\n  result: β=3 late-turn retention 87.0% vs β=0 75.9%, delta=+11.1pp. GAR-compliance\n    correlation r=0.200, p=0.007. Written to Appendix C. D046.\n  conclusion: success\n  metrics:\n    late_turn_rate_beta0: 0.759\n    late_turn_rate_beta3: 0.87\n    late_turn_delta: 0.111\n    mcnemar_chi2: 3.125\n    mcnemar_p: 0.0771\n    gar_compliance_r: 0.2003\n    gar_compliance_p: 0.007\n    category_content_constraint:\n      beta0: 0.619\n      beta3: 0.857\n      delta: 0.238\n    category_count_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_format_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_position_constraint:\n      beta0: 0.667\n      beta3: 0.733\n      delta: 0.067\n- id: plan_015\n  claim: C4, W7\n  description: Statistical significance analysis - paired bootstrap CI from held-out\n    eval (50 convs) for TG-LoRA-only comparison. If CI includes 0 → statistically\n    supports 'zero benefit'. Addresses Dream W3 (single seed).\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_008\n  status: orphaned\n  registry_id: worker_analysis_bootstrap_ci_tg_vs_lora_20260519T144212\n  result: 'PASS: All GAR-ours and PPL 95% CIs include 0 (TG-LO GAR: [-0.0018,+0.0036],\n    UG-LO: [-0.0006,+0.0045], TG-UG: [-0.0030,+0.0006]). Statistically confirms zero\n    benefit. W7 addressed.'\n- id: plan_016\n  claim: W8\n  description: Exposure-bias mitigation test - train ThreadGate v7 with scheduled\n    sampling applied to GAR loss (mix teacher-forced + model-generated contexts).\n    Test whether closing exposure bias gap narrows the 30x training-inference GAR\n    gap. Constructive direction that upgrades paper from pure negative result.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_008\n  status: DONE\n  registry_id: phase2_tg_s42_v8_schedsampling\n  conclusion: failed\n  metrics:\n    killed_at_microstep: 1950\n    total_microsteps: 24000\n    completion_pct: 8.1\n    global_step_approx: 244\n    total_global_steps: 3000\n    ss_steps_observed: 1\n    tf_lgar_mean_step850_1400: 0.0062\n    tf_lgar_std: 0.0082\n    tf_lgar_collapse_step: 800\n    gate_mean_final: 0.93\n    ss_ratio_at_kill: 0.081\n    crash_reason: 'killed by director: SS path code bug (D026) makes experiment invalid,\n      GPU needed for PCGrad'\n    design_flaw_ss_ramp_too_slow: true\n    design_flaw_no_ss_tf_separate_logging: true\n- id: plan_017\n  claim: R4\n  description: Code-paper architecture verification - confirm ThreadGate implementation\n    matches paper Eq.3 (gate on residual vs gate on sub-layer output). Quick code\n    audit, no GPU.\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: orphaned\n  registry_id: worker_analysis_code_paper_arch_verify_20260519T144058\n  result: 'CRITICAL: code implements x+g·f(x) (ReZero-style), dream paper.tex wrote\n    g·x+f(x). Semantically opposite when g→0. Data unaffected. D023.'\n- id: plan_018\n  claim: C3, W8\n  description: PCGrad baseline - project NTP gradient onto GAR-orthogonal plane for\n    gate params only. If 30x gap persists after removing gradient conflict → causal\n    evidence that exposure bias (not gradient competition) is the root cause.\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_006\n  registry_id: phase2_tg_s42_v9_pcgrad\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5002\n    eval_iid_dongre_mid_gar: 0.0123\n    eval_iid_ppl: 2.78\n    eval_iid_ntp: 0.9752\n    eval_heldout_ours_mid_gar: 0.5002\n    eval_heldout_dongre_mid_gar: 0.0123\n    eval_heldout_ppl: 2.78\n    eval_heldout_ntp: 0.9752\n    eval_modelgen_ours_mid_gar: 0.0151\n    eval_modelgen_dongre_mid_gar: 0.0173\n    eval_modelgen_ppl: 1.5\n    vs_v7_iid_ppl_diff: 0.004\n    vs_v7_iid_gar_diff: -0.0033\n- id: plan_019\n  claim: C2, MF5\n  description: Multi-seed validation — train TG v7 + LoRA-only with seed=123 on Qwen.\n    Provide mean±std for 30x gap. 1 extra seed sufficient given extreme effect size.\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_002\n  status: DONE\n  registry_id: v7_tg_s123\n  conclusion: success\n  metrics:\n    epoch_1:\n      avg_loss: 0.9447\n      avg_ntp_loss: 0.9434\n      avg_gar_loss: 0.0013\n      avg_div_loss: 0\n    epoch_2:\n      avg_loss: 0.9315\n      avg_ntp_loss: 0.9305\n      avg_gar_loss: 0.001\n      avg_div_loss: 0\n    final_gate:\n      mean: 0.9467\n      std: 0.051\n      min: 0.793\n      max: 1\n    final_gate_profile:\n      L0: 0.883\n      L1: 0.793\n      L2: 0.996\n      L3: 0.988\n      L4: 0.984\n      L5: 0.797\n      L6: 0.961\n      L7: 0.918\n      L8: 0.965\n      L9: 0.934\n      L10: 0.969\n      L11: 0.918\n      L12: 0.926\n      L13: 0.941\n      L14: 0.93\n      L15: 0.965\n      L16: 0.941\n      L17: 0.91\n      L18: 0.961\n      L19: 0.965\n      L20: 0.973\n      L21: 0.988\n      L22: 0.969\n      L23: 0.98\n      L24: 0.98\n      L25: 0.984\n      L26: 0.988\n      L27: 1\n    training_time_s: 21425.2\n- id: plan_020\n  claim: C4, MF6\n  description: Expanded eval set — increase from 50 to 200 conversations (idx>=7000\n    from UltraChat). Boost bootstrap CI statistical power.\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_008\n  status: planned\n  result: 'Partially done: TF eval uses eval_200 (N=200), AR eval uses d048_final_ar\n    (N=50). AR N=200 not planned — N=50 sufficient given extreme effect sizes. No\n    additional GPU needed.'\n- id: plan_022\n  claim: C3, SF4\n  description: λ_GAR sensitivity — train v7 with λ_GAR=10 (1 epoch only). Show gradient\n    competition trend under higher GAR weight. If budget allows, add λ=0.1.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_002\n  status: planned\n- id: plan_023\n  claim: W8, C3\n  description: 'v8b: Fixed Scheduled Sampling — fix compute_gar_loss len==1 bug (Option\n    A: handle single-turn mse_target), fix OOM (reduce batch/gen_length), use lambda_gar=1.0\n    (match v7). Tests whether training on model-generated text closes the 30x distribution\n    shift gap. If successful, paper upgrades from pure negative to ''diagnosis + initial\n    remedy''. D026.'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  status: DONE\n  registry_id: phase2_tg_s42_v8b_resume\n  conclusion: success\n  metrics:\n    training:\n      total_steps: 3000\n      epochs_completed: 3\n      wall_clock_hours: 8.1\n      final_loss: 0.933\n      final_ntp_loss: 0.9322\n      final_gar_loss: 0.0008\n      final_gate_mean: 0.9586\n      final_gate_std: 0.0582\n      ss_ratio: 0.5\n    eval_iid:\n      gar_ours: 0.4983\n      gar_dongre: 0.3855\n      ppl: 2.78\n    eval_modelgen:\n      gar_ours: 0.3177\n      gar_dongre: 0.3533\n      ppl: 1.38\n    vs_v7:\n      iid_gar_ours_delta: -0.005\n      modelgen_gar_ours_delta: 0.302\n      gap_ratio_v7: 32\n      gap_ratio_v8b: 1.57\n- id: plan_024\n  claim: C4\n  description: 'SS + β-steering combined eval — CANCELLED. Data already exists in\n    ss_s42_ar_n50.json (β=0,3,5). SS and steering are substitutes not complements\n    (β=5: SS 0.717 ≈ TG 0.727). No need to re-run.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_023\n  status: PREPARING\n  registry_id: p0_ss_steering_eval\n  result: 'Cancelled — existing data shows SS+steering do not stack. β=0: SS 0.347\n    (independent value). β=3: SS +0.037 marginal. β=5: SS ≈ TG (converge). Discussion\n    added to paper.'\n  conclusion: killed\n- id: plan_025\n  claim: C1\n  description: TF vs AR attention KL divergence — compute per-head KL(P_TF||P_AR)\n    on 50 conversations to quantify attention distribution shift. If GAR-relevant\n    heads show larger KL → mechanistic evidence for why GAR collapses. Pure CPU analysis.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_026\n  claim: C5, C4\n  description: Llama-3.1-8B Scheduled Sampling — replicate SS training on Llama to\n    verify cross-model gap compression. If Llama gap also compresses → SS is a general\n    mitigation, not model-specific.\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_010\n  status: planned\n- id: plan_027\n  claim: C4, W7\n  description: 'SS 3-seed validation — s42 (gap 1.45×), s123 (TF NaN, AR 0.423), s456\n    (gap 1.15×). 3-seed AR GAR β=0: 0.401±0.047. β=3/5 extremely stable (std<0.01).\n    Addresses single-seed reviewer concern.'\n  priority: P0\n  gpu_budget_hours: 16\n  deps:\n  - plan_023\n  status: planned\n  result: '3-seed complete. TF GAR 0.498±0.004 (s42=0.503, s123=0.495, s456=0.496).\n    AR GAR β=0: 0.401±0.047 (s42=0.347, s123=0.423, s456=0.433). Gap 1.26±0.17 (range\n    1.15–1.45×, 3 valid seeds). β=3: 0.596±0.008. β=5: 0.717±0.001. PPL β=0: 1.441±0.001.\n    W7 addressed.'\n- id: plan_028\n  claim: C2, W5\n  description: Alternative GAR definition robustness — 4 token selections (last/all/first/goal-only)\n    × 3 checkpoints (Base/TG/SS). Needed GPU re-eval (raw attention not saved).\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_027\n  status: planned\n  result: TG only improves last-token GAR (0.325), all/first-token near-zero (0.025/0.039).\n    SS improves ALL 4 definitions >0.36. SS builds broader goal-attention pattern,\n    not position-specific overfitting. Base consistently <0.022. D054.\n- id: plan_029\n  claim: C2, W7\n  description: SS 4th seed (s789) — additional seed to strengthen mean±std. Training\n    ~6.5h + eval ~1h. ROI lower than Llama SS (cross-model > extra seed given extreme\n    effect size). Run if time permits after plan_026.\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_027\n  status: planned\n- id: plan_030\n  claim: C1, C2\n  description: Long conversation eval (>10 turns) — test whether exposure bias gap\n    worsens with conversation length. Need to identify suitable long conversations\n    from UltraChat. Eval ~1-2h.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_027\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: phase1_gar_diag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    turn1_avg_gar: 0.0418\n    mid_turns_avg_gar: 0.0122\n    relative_drop: 0.708\n    num_conversations: 5\n    num_turns: 10\n    per_turn_avg_gar:\n    - 0.0418\n    - 0.0241\n    - 0.0224\n    - 0.013\n    - 0.0133\n    - 0.0086\n    - 0.0078\n    - 0.008\n    - 0.0157\n    - 0.0064\n- exp_id: phase2_tg_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_ntp_loss: 0.94\n    final_gar_loss: 0\n    gate_mean: 0.988\n    gar_loss_zero_pct: 87.6\n    epochs_completed: 1.67\n    killed_reason: SIGTERM by diagnose worker (unauthorized)\n- exp_id: phase2_ug_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_avg_loss: 1.0019\n    epoch0_avg_ntp: 0.9755\n    epoch0_avg_gar: 0.0259\n    epoch0_avg_div: 0.0005\n    epoch1_avg_loss: 0.9447\n    epoch1_avg_ntp: 0.9435\n    epoch1_avg_gar: 0.0013\n    epoch1_avg_div: 0\n    epoch2_avg_loss: 0.9319\n    epoch2_avg_ntp: 0.9309\n    epoch2_avg_gar: 0.001\n    epoch2_avg_div: 0\n    final_gate_mean: 0.9598\n    final_gate_std: 0.0518\n    final_gate_min: 0.7773\n    final_gate_max: 1\n    final_profile_L3: 0.777\n    final_profile_L5: 0.812\n    final_profile_L0: 0.875\n    final_profile_L27: 1\n    training_time_seconds: 21994.5\n    training_time_hours: 6.1\n    global_steps: 7950\n    unexpected_per_layer_variation: true\n    eval_modelgen_ours_mid_gar: 0.0149\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.396\n- exp_id: phase2_tg_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_tg_s42_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    gate_mean_step0: 0.8743\n    gate_mean_step500: 0.8761\n    gate_delta: 0.004\n    gate_std: 0.001\n    final_ntp_loss: 0.94\n    final_gar_loss: -0.019\n    gar_contribution_pct: 2-4%\n    diagnosis: gate frozen, GAR indirect gradient too weak\n- exp_id: phase2_tg_s42_v3b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gate_std_final: 0.087\n    gate_mean_final: 0.9388\n    gate_min_final: 0.5352\n    gate_max_final: 0.9922\n    L4_gate: 0.535\n    L0_gate: 0.777\n    L_NTP_final: 0.7787\n    L_GAR_final: -0.9606\n    elapsed_seconds: 3565.9\n    optimizer_steps: 500\n    gate_grad_received: true\n- exp_id: phase2_tg_s42_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: phase2_tg_s42_v5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step2000_gate_std: 0.0225\n    step2000_gate_mean: 0.9586\n    step2000_gate_min: 0.9062\n    step2000_gate_max: 0.9961\n    step2000_L_GAR: -0.8977\n    step2000_L_NTP: 0.7611\n    step2000_total_loss: -0.1365\n    step2400_gate_std: 0.0219\n    step2400_gate_mean: 0.9651\n    step2400_gate_min: 0.918\n    step2400_gate_max: 0.9961\n    step2400_profile: L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\n    L_GAR_saturated_at: -0.91\n    gate_range_compression: 0.918-0.996\n- exp_id: phase2_tg_s42_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    dryrun_step0_L_NTP: 2.0275\n    dryrun_step0_L_GAR: -0.0161\n    dryrun_step0_total_loss: 2.0114\n    dryrun_step4_L_NTP: 1.6544\n    dryrun_step4_L_GAR: -0.0147\n    dryrun_step4_total_loss: 1.6397\n    dryrun_gate_grad: true\n    dryrun_gate_mean_init: 0.8097\n    dryrun_gate_std_init: 0.0341\n    dryrun_gate_min_init: 0.6836\n    dryrun_gate_max_init: 0.8672\n    dryrun_gate_mean_step5: 0.8025\n    dryrun_gate_std_step5: 0.0842\n    dryrun_gate_min_step5: 0.5547\n    dryrun_gate_max_step5: 0.9805\n    gs50_gate_mean: 0.8117\n    gs50_gate_std: 0.0612\n    gs50_gate_min: 0.6836\n    gs50_gate_max: 0.9805\n    gs100_gate_mean: 0.8737\n    gs100_gate_std: 0.0367\n    gs100_gate_min: 0.8164\n    gs100_gate_max: 0.9766\n    gs100_L_NTP: 0.8151\n    gs100_L_GAR: -0.158\n    gs100_total_loss: 0.6571\n    gs100_profile_bottom3: L12=0.816 L4=0.824 L13=0.824\n    gs100_profile_top3: L27=0.977 L26=0.961 L23=0.914\n    gs143_L_GAR: -0.3876\n    gs143_gate_mean: 0.9227\n- exp_id: phase2_tg_s42_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5035\n    eval_iid_dongre_mid_gar: 0.0152\n    eval_iid_ppl: 2.784\n    eval_heldout_ours_mid_gar: 0.5035\n    eval_heldout_dongre_mid_gar: 0.0152\n    eval_heldout_ppl: 2.78\n    eval_modelgen_ours_mid_gar: 0.0157\n    eval_modelgen_dongre_mid_gar: 0.0194\n    eval_modelgen_ppl: 1.36\n    gate_mean_final: 0.9336\n    gate_std_final: 0.0492\n- exp_id: phase2_lora_only_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    global_steps: 3000\n    training_time_seconds: 20588.6\n    training_time_hours: 5.7\n    gate_fixed: 1\n    gate_type_actual: none\n    final_lora_size_mb: 20\n    eval_modelgen_ours_mid_gar: 0.0245\n    eval_modelgen_dongre_mid_gar: 0.0185\n    eval_modelgen_ppl: 1.371\n- exp_id: phase2_4way_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    base_ours_mid_gar: 0.0107\n    base_ours_recovery_pp: -0.15\n    base_dongre_mid_gar: 0.003\n    base_dongre_recovery_pp: -0.92\n    base_ppl: 4.23\n    base_ntp: 1.4162\n    tg_ours_mid_gar: 0.4866\n    tg_ours_recovery_pp: 47.44\n    tg_dongre_mid_gar: 0.0157\n    tg_dongre_recovery_pp: 0.35\n    tg_ppl: 2.63\n    tg_ntp: 0.9484\n    ug_ours_mid_gar: 0.4923\n    ug_ours_recovery_pp: 48.01\n    ug_dongre_mid_gar: 0.013\n    ug_dongre_recovery_pp: 0.08\n    ug_ppl: 2.62\n    ug_ntp: 0.9433\n    lora_ours_mid_gar: 0.486\n    lora_ours_recovery_pp: 47.39\n    lora_dongre_mid_gar: 0.0137\n    lora_dongre_recovery_pp: 0.15\n    lora_ppl: 2.63\n    lora_ntp: 0.9482\n    route_b_confirmed: true\n    gating_incremental_benefit: none\n- exp_id: phase2_4way_eval_heldout\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base_ours_mid_gar: 0.0128\n    base_ours_recovery_pp: 0.06\n    base_dongre_mid_gar: 0.0031\n    base_dongre_recovery_pp: -0.91\n    base_ppl: 4.34\n    base_ntp: 1.4045\n    tg_ours_mid_gar: 0.5035\n    tg_ours_recovery_pp: 49.13\n    tg_dongre_mid_gar: 0.0152\n    tg_dongre_recovery_pp: 0.3\n    tg_ppl: 2.78\n    tg_ntp: 0.9771\n    ug_ours_mid_gar: 0.5053\n    ug_ours_recovery_pp: 49.31\n    ug_dongre_mid_gar: 0.0124\n    ug_dongre_recovery_pp: 0.02\n    ug_ppl: 2.78\n    ug_ntp: 0.9752\n    lora_ours_mid_gar: 0.4978\n    lora_ours_recovery_pp: 48.56\n    lora_dongre_mid_gar: 0.0132\n    lora_dongre_recovery_pp: 0.1\n    lora_ppl: 2.78\n    lora_ntp: 0.9771\n    three_way_convergence_confirmed: true\n    gar_ours_spread_pp: 0.75\n    ppl_spread: 0\n    data_overlap: false\n- exp_id: phase2_tg_s42_v8_schedsampling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    killed_at_microstep: 1950\n    total_microsteps: 24000\n    completion_pct: 8.1\n    global_step_approx: 244\n    total_global_steps: 3000\n    ss_steps_observed: 1\n    tf_lgar_mean_step850_1400: 0.0062\n    tf_lgar_std: 0.0082\n    tf_lgar_collapse_step: 800\n    gate_mean_final: 0.93\n    ss_ratio_at_kill: 0.081\n    crash_reason: 'killed by director: SS path code bug (D026) makes experiment invalid,\n      GPU needed for PCGrad'\n    design_flaw_ss_ramp_too_slow: true\n    design_flaw_no_ss_tf_separate_logging: true\n- exp_id: analysis_gradient_conflict\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch0_cos_sim: -0.089\n    epoch1_cos_sim: -0.054\n    epoch2_cos_sim: -0.042\n    epoch0_neg_layers_pct: 78.6\n    epoch1_neg_layers_pct: 71.4\n    epoch2_neg_layers_pct: 67.9\n    epoch0_mag_ratio: 7.5\n    epoch1_mag_ratio: 13.7\n    epoch2_mag_ratio: 14.7\n- exp_id: analysis_attention_heatmap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base_mean_goal_attn: 0.0136\n    base_decay: 0.875\n    tg_mean_goal_attn: 0.0232\n    tg_decay: 0.777\n    ug_mean_goal_attn: 0.0216\n    ug_decay: 0.803\n    lora_mean_goal_attn: 0.0216\n    lora_decay: 0.81\n    gating_incremental_benefit: none\n- exp_id: phase2_tg_s42_v9_pcgrad\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_iid_ours_mid_gar: 0.5002\n    eval_iid_dongre_mid_gar: 0.0123\n    eval_iid_ppl: 2.78\n    eval_iid_ntp: 0.9752\n    eval_heldout_ours_mid_gar: 0.5002\n    eval_heldout_dongre_mid_gar: 0.0123\n    eval_heldout_ppl: 2.78\n    eval_heldout_ntp: 0.9752\n    eval_modelgen_ours_mid_gar: 0.0151\n    eval_modelgen_dongre_mid_gar: 0.0173\n    eval_modelgen_ppl: 1.5\n    vs_v7_iid_ppl_diff: 0.004\n    vs_v7_iid_gar_diff: -0.0033\n- exp_id: phase2_tg_s42_v8b_ss_fixed\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: attention_steering_v7_tg_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beta_0.0:\n      mid_turns_avg_gar: 0.028\n      avg_ppl: 1.409\n    beta_0.5:\n      mid_turns_avg_gar: 0.0287\n      avg_ppl: 1.387\n    beta_1.0:\n      mid_turns_avg_gar: 0.0349\n      avg_ppl: 1.36\n    beta_2.0:\n      mid_turns_avg_gar: 0.062\n      avg_ppl: 1.411\n    beta_5.0:\n      mid_turns_avg_gar: 0.6795\n      avg_ppl: 1.908\n    beta_10.0:\n      mid_turns_avg_gar: 0.959\n      avg_ppl: 4.22\n    phase_transition_range: '[2, 5]'\n    baseline_gar: 0.028\n    max_gar_at_acceptable_ppl: 0.6795\n    max_gar_at_acceptable_ppl_beta: 5\n- exp_id: trc_baseline_v7_tg\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v7_tg:\n      tf_trc: 0.3339\n      gen_trc: 0.3323\n      trc_gap: 0.0016\n      tf_tbp_ppl: 1.05\n      gen_tbp_ppl: 1.05\n    lora_only:\n      tf_trc: 0.349\n      gen_trc: 0.4106\n      trc_gap: -0.0617\n      tf_tbp_ppl: 9.5\n      gen_tbp_ppl: 12\n    base:\n      tf_trc: 0.1494\n      gen_trc: 0.1494\n      trc_gap: 0\n      tf_tbp_ppl: 2.05\n      gen_tbp_ppl: 2.05\n- exp_id: attention_steering_eval200_tf\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beta_0.0:\n      mid_gar: 0.5353\n      ppl: 2.62\n    beta_2.0:\n      mid_gar: 0.6112\n      ppl: 2.69\n    beta_3.0:\n      mid_gar: 0.788\n      ppl: 2.93\n    beta_4.0:\n      mid_gar: 0.8165\n      ppl: 3.49\n    beta_5.0:\n      mid_gar: 0.8325\n      ppl: 6.15\n    beta_10.0:\n      mid_gar: 0.977\n      ppl: 505.21\n    n_convs: 200\n    mode: tf\n- exp_id: phase2_tg_s42_v8b_resume\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training:\n      total_steps: 3000\n      epochs_completed: 3\n      wall_clock_hours: 8.1\n      final_loss: 0.933\n      final_ntp_loss: 0.9322\n      final_gar_loss: 0.0008\n      final_gate_mean: 0.9586\n      final_gate_std: 0.0582\n      ss_ratio: 0.5\n    eval_iid:\n      gar_ours: 0.4983\n      gar_dongre: 0.3855\n      ppl: 2.78\n    eval_modelgen:\n      gar_ours: 0.3177\n      gar_dongre: 0.3533\n      ppl: 1.38\n    vs_v7:\n      iid_gar_ours_delta: -0.005\n      modelgen_gar_ours_delta: 0.302\n      gap_ratio_v7: 32\n      gap_ratio_v8b: 1.57\n- exp_id: eval_v8b_ss\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    iid_gar_ours: 0.4983\n    iid_gar_dongre: 0.3855\n    iid_ppl: 2.78\n    iid_ngar_ours: 13.5\n    iid_ngar_dongre: 22.68\n    modelgen_gar_ours: 0.3177\n    modelgen_gar_dongre: 0.3533\n    modelgen_ppl: 1.38\n    modelgen_ngar_ours: 4.47\n    modelgen_ngar_dongre: 5.92\n    iid_turn1_gar_ours: 0.5398\n    modelgen_turn1_gar_ours: 0.4333\n- exp_id: attention_steering_gen_n50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    corrected: true\n    aggregation: per-conv mid_gar(turns 2-7), >=3 turns only\n    beta_0.0:\n      mid_gar: 0.0641\n      mid_gar_std: 0.0809\n      ppl: 1.4324\n      ppl_std: 0.1029\n      n_valid: 39\n    beta_2.0:\n      mid_gar: 0.128\n      mid_gar_std: 0.1101\n      ppl: 1.4822\n      ppl_std: 0.1385\n      n_valid: 39\n    beta_3.0:\n      mid_gar: 0.5558\n      mid_gar_std: 0.0601\n      ppl: 1.5605\n      ppl_std: 0.1719\n      n_valid: 39\n    beta_4.0:\n      mid_gar: 0.6439\n      mid_gar_std: 0.0607\n      ppl: 1.6674\n      ppl_std: 0.2241\n      n_valid: 39\n    beta_5.0:\n      mid_gar: 0.7271\n      mid_gar_std: 0.0605\n      ppl: 1.7723\n      ppl_std: 0.2693\n      n_valid: 38\n    beta_10.0:\n      mid_gar: 0.9612\n      mid_gar_std: 0.0152\n      ppl: 3.4517\n      ppl_std: 1.7813\n      n_valid: 39\n    n_convs_total: 50\n    n_convs_valid: 39\n    mode: gen\n    phase_transition_range: '[2, 3]'\n- exp_id: llama_phase1_gar_diag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_turn_gar:\n      turn_1: 0.0263\n      turn_2: 0.0183\n      turn_3: 0.0087\n      turn_4: 0.0055\n      turn_5: 0.006\n      turn_6: 0.0035\n      turn_7: 0.0038\n      turn_8: 0.0037\n      turn_9: 0.005\n      turn_10: 0.0026\n    t1_t10_decay_pct: 90.1\n    t1_mid38_drop_pct: 80.2\n    n_topics: 5\n    model: Meta-Llama-3.1-8B-Instruct\n    mode: gen\n    n_conversations: 5\n    n_turns: 10\n- exp_id: llama_tg_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epochs_completed: 3\n    total_steps: 3000\n    wall_clock_seconds: 26212\n    wall_clock_hours: 7.28\n    final_avg_loss: 0.9233\n    final_avg_ntp: 0.9224\n    final_avg_gar: 0.0009\n    final_avg_div: 0\n    final_gate_mean: 0.9099\n    final_gate_std: 0.0701\n    final_gate_min: 0.7188\n    final_gate_max: 0.9922\n    gate_profile_step3000:\n      L0: 0.957\n      L1: 0.973\n      L2: 0.977\n      L3: 0.965\n      L4: 0.992\n      L5: 0.969\n      L6: 0.957\n      L7: 0.957\n      L8: 0.961\n      L9: 0.949\n      L10: 0.938\n      L11: 0.934\n      L12: 0.969\n      L13: 0.953\n      L14: 0.957\n      L15: 0.965\n      L16: 0.953\n      L17: 0.961\n      L18: 0.922\n      L19: 0.902\n      L20: 0.883\n      L21: 0.863\n      L22: 0.836\n      L23: 0.844\n      L24: 0.809\n      L25: 0.719\n      L26: 0.762\n      L27: 0.805\n      L28: 0.801\n      L29: 0.855\n      L30: 0.898\n      L31: 0.934\n    checkpoint_size_gate_mb: 4.2\n    checkpoint_size_lora_mb: 26\n    gpu: NVIDIA RTX PRO 6000 Blackwell\n    vram_gb: 102\n    mem_used_gb: 63.4\n- exp_id: llama_eval_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf_base:\n      gar_ours: 0.0166\n      ngar_ours: 0.3882\n      gar_dongre: 0.0038\n      ngar_dongre: 0.163\n      ppl: 3.45\n      N: 50\n      T: 4\n    tf_tg:\n      gar_ours: 0.4836\n      ngar_ours: 11.8818\n      gar_dongre: 0.018\n      ngar_dongre: 0.7922\n      ppl: 2.57\n      N: 50\n      T: 4\n    ar_base:\n      gar_ours: 0.0086\n      ngar_ours: 0.0798\n      gar_dongre: 0.0118\n      ngar_dongre: 0.1265\n      ppl: 1.24\n      N: 5\n      T: 10\n    ar_tg:\n      gar_ours: 0.0304\n      ngar_ours: 0.2632\n      gar_dongre: 0.0217\n      ngar_dongre: 0.2459\n      ppl: 1.32\n      N: 5\n      T: 10\n    gap_ratio_tg_ours: 15.9\n    gap_ratio_base_ours: 1.93\n    gap_ratio_tg_dongre: 0.83\n    vs_qwen_v7_gap_ratio: 32.1\n    baseline_mid_gar: 0.0122\n- exp_id: llama_tg_training\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: instruction_retention_test\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    late_turn_rate_beta0: 0.759\n    late_turn_rate_beta3: 0.87\n    late_turn_delta: 0.111\n    mcnemar_chi2: 3.125\n    mcnemar_p: 0.0771\n    gar_compliance_r: 0.2003\n    gar_compliance_p: 0.007\n    category_content_constraint:\n      beta0: 0.619\n      beta3: 0.857\n      delta: 0.238\n    category_count_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_format_constraint:\n      beta0: 1\n      beta3: 1\n      delta: 0\n    category_position_constraint:\n      beta0: 0.667\n      beta3: 0.733\n      delta: 0.067\n- exp_id: llama_ar_matched_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ar_base_ours:\n      mid_gar: 0.0082\n      ngar: 0.1\n      ppl: 1.267\n    ar_tg_ours:\n      mid_gar: 0.0388\n      ngar: 0.493\n      ppl: 1.413\n    ar_base_dongre:\n      mid_gar: 0.0051\n      ngar: 0.12\n      ppl: 1.267\n    ar_tg_dongre:\n      mid_gar: 0.018\n      ngar: 0.431\n      ppl: 1.413\n    tf_reference:\n      tf_tg_ours_ngar: 11.88\n      tf_base_ours_ngar: 0.388\n      tf_tg_ours_raw: 0.4836\n      tf_tg_dongre_raw: 0.018\n    matched_gap_analysis:\n      gar_ours_raw_gap: 12.5x (TF 0.484 / AR 0.039)\n      gar_ours_ngar_gap: 24.1x (TF 11.88 / AR 0.493)\n      gar_dongre_raw_gap: 1.002x (TF 0.018 / AR 0.018) — zero gap\n      tg_over_base_ar_ours: 4.71x\n      tg_over_base_ar_dongre: 3.54x\n      conclusion: 'GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure\n        bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure\n        bias selectively destroys learned goal-attention routing while leaving content-overlap-based\n        attention unaffected.'\n- exp_id: v8b_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.9316\n    final_ntp_loss: 0.9307\n    final_gar_loss: 0.0009\n    final_gate_mean: 0.9505\n    final_gate_std: 0.0508\n    final_gate_min: 0.7383\n    final_gate_max: 1\n    ss_used_ratio: 0.371\n    training_time_s: 38773.4\n    epoch0_loss: 1.0092\n    epoch1_loss: 0.9444\n    epoch2_loss: 0.9316\n- exp_id: v7_tg_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch_1:\n      avg_loss: 0.9447\n      avg_ntp_loss: 0.9434\n      avg_gar_loss: 0.0013\n      avg_div_loss: 0\n    epoch_2:\n      avg_loss: 0.9315\n      avg_ntp_loss: 0.9305\n      avg_gar_loss: 0.001\n      avg_div_loss: 0\n    final_gate:\n      mean: 0.9467\n      std: 0.051\n      min: 0.793\n      max: 1\n    final_gate_profile:\n      L0: 0.883\n      L1: 0.793\n      L2: 0.996\n      L3: 0.988\n      L4: 0.984\n      L5: 0.797\n      L6: 0.961\n      L7: 0.918\n      L8: 0.965\n      L9: 0.934\n      L10: 0.969\n      L11: 0.918\n      L12: 0.926\n      L13: 0.941\n      L14: 0.93\n      L15: 0.965\n      L16: 0.941\n      L17: 0.91\n      L18: 0.961\n      L19: 0.965\n      L20: 0.973\n      L21: 0.988\n      L22: 0.969\n      L23: 0.98\n      L24: 0.98\n      L25: 0.984\n      L26: 0.988\n      L27: 1\n    training_time_s: 21425.2\n- exp_id: eval_v8b_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    iid:\n      gar_ours: 0.503\n      gar_dongre: 0.394\n      ppl: 2.781\n      ntp_loss: 0.976\n      n_conv: 50\n      n_turns: 3\n    modelgen:\n      gar_ours: 0.418\n      gar_dongre: 0.441\n      ppl: 1.389\n      ntp_loss: 0.325\n      n_conv: 5\n      n_turns: 10\n    gap_ratio: 1.2\n    base_iid_ppl: 4.338\n    base_modelgen_ppl: 1.351\n- exp_id: eval_v7_tg_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    iid_tf:\n      gar_ours_mid: 0.5052\n      gar_dongre_mid: 0.0119\n      ppl: 2.7802\n      ntp: 0.9752\n    modelgen_ar:\n      gar_ours_mid: 0.0165\n      gar_dongre_mid: 0.0177\n      ppl: 1.3855\n      ntp: 0.3223\n    gap_ratio: 30.6\n    comparison_s42:\n      tf_gar_ours_delta: 0.0017\n      ar_gar_ours_delta: 0.0008\n      gap_ratio_delta: -1.4\n- exp_id: llama_lora_only_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_avg_loss: 0.9288\n    final_avg_ntp: 0.9279\n    final_avg_gar: 0.0009\n    gate_fixed: 1\n    gate_type: none\n    wall_clock_s: 25317\n    wall_clock_h: 7.03\n    epochs_completed: 3\n- exp_id: eval_llama_lora_only_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf:\n      gar_ours: 0.4807\n      gar_dongre: 0.0188\n      ngar_ours: 11.8031\n      ngar_dongre: 0.8261\n      ppl: 2.6\n      ntp_loss: 0.9366\n      n_conversations: 50\n      n_turns: 4\n    ar:\n      gar_ours: 0.0617\n      gar_dongre: 0.0226\n      ngar_ours: 0.6065\n      ngar_dongre: 0.2537\n      ppl: 1.32\n      ntp_loss: 0.2787\n      n_conversations: 5\n      n_turns: 10\n    gap_ratio_gar_ours: 7.79\n- exp_id: eval_llama_ar_n20\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base:\n      gar_ours_mean: 0.0088\n      gar_ours_std: 0.0056\n      gar_ours_median_per_conv: 0.0093\n      gar_ours_median_per_turn_pool: 0.0071\n      gar_ours_spike_ratio: 0%\n      gar_dongre_mean: 0.0049\n      gar_dongre_std: 0.0013\n      gar_dongre_median: 0.0047\n      ngar_ours_mid: 0.1019\n      ngar_dongre_mid: 0.1171\n      ppl: 1.293\n      ppl_std: 0.07\n      ntp_loss: 0.2552\n    tg:\n      gar_ours_mean: 0.0434\n      gar_ours_std: 0.1002\n      gar_ours_median_per_conv: 0.0179\n      gar_ours_median_per_turn_pool: 0.0126\n      gar_ours_spike_ratio: 5% (2/40 turns GAR>=0.4)\n      gar_dongre_mean: 0.0183\n      gar_dongre_std: 0.0198\n      gar_dongre_median: 0.0152\n      ngar_ours_mid: 0.5357\n      ngar_dongre_mid: 0.4436\n      ppl: 1.437\n      ppl_std: 0.077\n      ntp_loss: 0.3612\n    lora_only:\n      gar_ours_mean: 0.0284\n      gar_ours_std: 0.0481\n      gar_ours_median_per_conv: 0.0184\n      gar_ours_median_per_turn_pool: 0.0133\n      gar_ours_spike_ratio: 0%\n      gar_dongre_mean: 0.0205\n      gar_dongre_std: 0.0241\n      gar_dongre_median: 0.016\n      ngar_ours_mid: 0.3488\n      ngar_dongre_mid: 0.4997\n      ppl: 1.419\n      ppl_std: 0.075\n      ntp_loss: 0.3483\n    n_conversations: 20\n    n_turns: 4\n    mid_turns_definition: turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2).\n      All 16 eval entries use same definition.\n    stat_pool: 'median_per_conv: median of 20 per-conversation mid-turn averages.\n      median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).'\n    ranking_gar_ours_mean: TG(0.0434) > LO(0.0284) > Base(0.0088)\n    ranking_gar_ours_median_per_conv: TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\n    ranking_gar_ours_median_per_turn_pool: TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\n    ranking_gar_dongre: LO(0.0205) > TG(0.0183) > Base(0.0049)\n    note: Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages\n      across N=20). median_per_turn_pool is the alternative statistic from pooled\n      individual turns. Both confirm TG ≈ LO (zero-increment).\n- exp_id: d048_ss_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_avg_loss: 0.9326\n    final_ntp_loss: 0.932\n    final_gar_loss: 0.0007\n    gate_mean: 0.9527\n    gate_std: 0.0589\n    gate_min: 0.7383\n    gate_min_layer: L4\n    gate_max: 1\n    ss_usage: 4750/16000 (29.7%)\n    ss_fallback: 0\n    epochs_completed: 3\n    wall_clock_s: 23418\n    wall_clock_h: 6.5\n- exp_id: d048_ss_s42_resume\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d048_eval_ss_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf:\n      base_gar_ours_mid: 0.0128\n      base_gar_dongre_mid: 0.0031\n      base_ppl: 4.34\n      base_ntp: 1.4\n      tg_gar_ours_mid: 0.5025\n      tg_gar_dongre_mid: 0.389\n      tg_ppl: 2.78\n      tg_ntp: 0.98\n      baseline_mid_gar: 0.0122\n    ar:\n      gar_ours_mid: 0.3887\n      gar_ours_ci_95:\n      - 0.3692\n      - 0.3934\n      ppl: 1.35\n    gap_ratio: 1.29\n    n_conversations_tf: 50\n    n_conversations_ar: 5\n    bootstrap_turns: curve[2:] (turns 3-T)\n    note: AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch\n      with eval_200.json N=50.\n- exp_id: d048_queue_runner\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: d048_ss_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d048_final_ar_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beta0:\n      base_gar: 0.019\n      tg_gar: 0.064\n      ug_gar: 0.033\n      lo_gar: 0.037\n      pcgrad_gar: 0.03\n      ss_gar: 0.347\n    beta3:\n      base_gar: 0.531\n      tg_gar: 0.556\n      ss_gar: 0.593\n    beta5:\n      base_gar: 0.704\n      tg_gar: 0.727\n      ss_gar: 0.717\n    wilcoxon_beta0:\n      tg_vs_base_p: <0.001\n      tg_vs_base_r: 0.802\n      ss_vs_tg_p: <0.001\n      ss_vs_tg_r: 0.869\n    ppl:\n      base: 1.447\n      tg: 1.432\n      ss: 1.442\n    n_convs: 39\n- exp_id: qwen15b_phase1_diag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mmlu_eval_all\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    base_qwen: 0.7423\n    pcgrad_v9_s42: 0.7386\n    ss_v8b_s42: 0.7375\n    lo_s42: 0.7357\n    tg_v7_s42: 0.7347\n    ug_s42: 0.7346\n- exp_id: d048_split_softmax_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d048_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d048_eval_ss_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf_gar_ours: 0.5536\n    tf_gar_dongre: 0.4106\n    tf_ppl: 2.6123\n    ar_beta0_gar: 0.4231\n    ar_beta0_ppl: 1.4408\n    ar_beta3_gar: 0.5903\n    ar_beta3_ppl: 1.607\n    ar_beta5_gar: 0.7174\n    ar_beta5_ppl: 1.7852\n    n_convs_tf: 200\n    n_convs_ar: 39\n- exp_id: p0_ss_steering_eval\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: p1_tf_ar_kl_divergence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tg_delta_gar: 0.0165\n    base_delta_gar: 0.0122\n    tg_mean_kl: 0.054\n    base_mean_kl: 0.043\n    gate_kl_correlation: 0.11\n    high_kl_layers: L23-L27, L9\n    gar_robustness_ours_tg_base_ratio: 21.4\n    gar_robustness_goal_only_ratio: 63\n    gar_robustness_ours_all_ratio: 1.7\n    gar_robustness_ours_first_ratio: 1.8\n- exp_id: p1_llama_ss_training\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: p2_llama_gradient_conflict\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cos_sim_mean: 0.0045\n    cos_sim_std: 0.07\n    neg_cos_sim_layers_pct: 53.1\n    mag_ratio_median: 25.7\n    conclusion_note: 'cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion\n      text ''widespread conflict'' is misleading — actual finding: NTP and GAR gradients\n      are nearly orthogonal on Llama, consistent with Qwen pattern.'\n- exp_id: d048_eval_ss_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tf_gar_ours_mid: 0.4964\n    tf_gar_dongre_mid: 0.3862\n    ar_beta0_gar: 0.4325\n    ar_beta0_ppl: 1.4394\n    ar_beta3_gar: 0.605\n    ar_beta3_ppl: 1.5868\n    ar_beta5_gar: 0.7157\n    ar_beta5_ppl: 1.8045\n    n_convs_ar: 50\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-24T08:11:42.699Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T08:11:42.699Z",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-24T08:11:42.732Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8f82ac3d-4668-480f-9e07-c530ab7badad",
  "type": "user",
  "uuid": "416bfb43-6e7e-4234-abe7-b22015d6d5ca",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T08:11:42.729Z_

```json
{
  "parentUuid": "416bfb43-6e7e-4234-abe7-b22015d6d5ca",
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
  "uuid": "3f7e00dd-c0d0-454b-a0bb-302714d1f238",
  "timestamp": "2026-05-24T08:11:42.729Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T08:11:42.729Z_

```json
{
  "parentUuid": "3f7e00dd-c0d0-454b-a0bb-302714d1f238",
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
  "uuid": "91f52a00-1435-4d85-bb18-b02afc85f320",
  "timestamp": "2026-05-24T08:11:42.729Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T08:11:42.729Z_

```json
{
  "parentUuid": "91f52a00-1435-4d85-bb18-b02afc85f320",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d3360400-38da-4a3d-9d80-a3954d1a74dd",
  "timestamp": "2026-05-24T08:11:42.729Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "d3360400-38da-4a3d-9d80-a3954d1a74dd",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three exposure bias scenario tiers for dream paper",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0"
}
```

---

### Assistant

_source line 9 · 2026-05-24T08:12:20.712Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research data carefully to define three tiers (best/median/worst) for a Dream simulation. This is a paper about exposure bias destroying auxiliary attention losses in multi-turn dialogue, targeting EMNLP 2026.

Key current state:
- Core finding: 8×–27× TF-AR GAR gap (exposure bias)
- SS mitigation: AR GAR 0.401±0.047 (3-seed), gap compressed to ~1.3×
- PCGrad causal exclusion complete
- Llama cross-model validation complete for core findings


- Llama SS training is currently running, which is critical for establishing whether scheduled sampling generalizes across models
- Dream review indicated a 3.0 best case, and I'm now targeting 3.0-3.5 with improved framing
- KL divergence analysis is done but showed modest results, while alternative GAR definitions all showed SS improvements
- The key assumption driving tier outcomes is whether Llama SS replicates the gap compression we saw, which would support the claim that SS is model-general mitigation
- Reviewers will likely respond well to the discover-diagnose-remedy narrative arc, the novelty of exposure bias measurement for attention objectives, and the methodological rigor of the PCGrad causal analysis
- Best case scenario has Llama SS working with similar gap compression, reviewers finding the exposure bias measurement novel, and the overall contribution landing at 3.5 (borderline accept/solid findings)
- Median case would involve Llama SS working but with weaker effects or higher variance, which might lead reviewers to acknowledge the measurement while questioning its novelty and seeing SS as merely applying an existing technique, landing around 3.0-3.5
- Worst case is Llama SS failing to generalize, reviewers dismissing this as a failed experiment with a known fix applied, and the narrow scope of lightweight gating plus GAR being seen as too limiting, resulting in a 2.5-3.0 weak reject

Now I need to establish concrete metrics to evaluate which scenario is most likely. I'm tracking the Llama SS performance on the AR GAR baseline, the gap compression ratio, the dream review score, any fatal or severe reviewer concerns, and cross-model generalization patterns.

Looking at the actual numbers more carefully: Qwen with SS shows an AR GAR of 0.401±0.047 with roughly a 1.3× gap, while Qwen without SS has 0.064 AR GAR and a 7.8× gap. Llama without SS sits at a median AR GAR of 0.018 with a 27× median gap. The Llama SS results are still running, which is the critical unknown that will determine everything.

For the outcome tiers, best case means all remaining experiments confirm the hypotheses and Llama SS replicates the pattern, giving us the full discover-diagnose-remedy narrative arc with a 3.5+ review score. Median case is the core findings hold but Llama SS shows partial or different characteristics, requiring some claim adjustments.

For Llama SS specifically, I'm setting thresholds: best would be an AR GAR ≥0.30 matching Qwen's performance with a ≤2× gap, median would be 0.15-0.30 showing partial improvement with a 2-4× gap, and worst would be <0.10 where SS doesn't transfer to Llama with a >5× gap. The Dream review score ranges from 3.5-4.0 for best down to 2.5-3.0 for worst.

Now I'm thinking through what matters to reviewers: whether the approach generalizes across models, how consistent the results are, whether the statistical evidence is solid, and whether the overall narrative holds together. I'm going to structure this as a configuration file to organize these outcome scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3360400-38da-4a3d-9d80-a3954d1a74dd",
  "isSidechain": false,
  "requestId": "req_011CbM4Dsanvt7ckinGAVhWH",
  "type": "assistant",
  "uuid": "08f21383-c00a-492a-b4ef-9951169c8722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WnHuN6idTCB4F8RZ76HNE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35837,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3797,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3797,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 35837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35837
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

_source line 10 · 2026-05-24T08:13:16.806Z_

```yaml
tiers:
  best:
    meaning: "完整 'discover→diagnose→remedy' 弧成立，SS 跨模型通用，exposure bias 测量被认可为该场景首次定量刻画"
    key_assumptions:
      - "Llama SS 训练成功复现 gap 压缩（AR GAR β=0 ≥0.30，gap ≤2×），确认 SS 是 model-general mitigation"
      - "Exposure bias 对 auxiliary attention loss 的 8×–27× gap 被审稿人接受为该场景下的 novel 实证贡献（非 'exposure bias is already known' 驳回）"
      - "PCGrad 因果排除链（观察→假设→排除→指向真因）被认为方法论严谨，非 trivial ablation"
      - "SS + β-steering 双路径 mitigation 被视为 substantive constructive contribution（非 'just applied known technique'）"
      - "3-seed 统计 + bootstrap CI + 跨模型 + alternative GAR definitions 充分回应 W7/W1/W3"
      - "论文写作成功执行 gromov/sun/xiao 对标模式，56 references 解决 W6"
    number_ranges:
      llama_ss_ar_gar_beta0: [0.30, 0.50]
      llama_ss_tf_ar_gap_ratio: [1.0, 2.0]
      qwen_ss_ar_gar_beta0_3seed: [0.38, 0.45]  # 已有 0.401±0.047
      qwen_ss_tf_ar_gap_ratio: [1.1, 1.5]  # 已有 1.15–1.45
      dream_review_score: [3.5, 4.0]
      fatal_severe_concerns_remaining: [0, 1]
      reviewer_novelty_objection_probability: [0.0, 0.3]
      alternative_gar_defs_ss_improves: [3, 4]  # 已有 4/4
    narrative_direction: "原始 framing 完全成立。Title 用 T2（'From Collapse to Recovery'）强调完整弧。5 个 contributions 均可 full-strength claim。SS 跨模型通用性升级 C5 为 'cross-model validated mitigation'。Paper 定位 solid EMNLP main conference，不需要 Findings fallback。核心叙事：首次定量刻画 exposure bias 如何摧毁 auxiliary attention loss（8×–27×），因果排除梯度冲突后精确定位 distribution shift 为根因，SS 提供通用初步修复（gap 8×→~1.3×），构成完整的诊断-修复循环。"

  median:
    meaning: "核心诊断成立但 SS 跨模型效果减弱或 novelty 论证部分受挑战，需调整 claim 强度"
    key_assumptions:
      - "Llama SS 训练有改善但 gap 压缩弱于 Qwen（AR GAR β=0 在 0.10–0.30，gap 2–5×），SS 'partially general'"
      - "至少 1 位审稿人以 'exposure bias is a known phenomenon' 挑战 novelty（W5），需靠 8×–27× 定量测量 + mechanism specificity 回应"
      - "PCGrad 因果链被接受但被视为 'expected result'（非 surprising）"
      - "SS 被视为 'promising but preliminary'——单模型强效 + 跨模型弱效 = contribution 降级为 'initial evidence'"
      - "3-seed 统计通过但审稿人仍提 'more seeds / larger eval' minor concern"
      - "论文写作基本到位但个别 claim scope 需要收紧"
    number_ranges:
      llama_ss_ar_gar_beta0: [0.10, 0.30]
      llama_ss_tf_ar_gap_ratio: [2.0, 5.0]
      qwen_ss_ar_gar_beta0_3seed: [0.38, 0.45]  # 已锁定
      qwen_ss_tf_ar_gap_ratio: [1.1, 1.5]  # 已锁定
      dream_review_score: [3.0, 3.5]
      fatal_severe_concerns_remaining: [1, 3]
      reviewer_novelty_objection_probability: [0.3, 0.7]
      alternative_gar_defs_ss_improves: [2, 4]
    narrative_direction: "调整 claim 强度。(1) SS contribution 从 'general mitigation' 降级为 'effective on Qwen, partially effective cross-model, requires further validation'。(2) Title 改 T1（保留 'selectively destroys' 记忆点，不承诺 recovery）。(3) Contribution #5 SS 部分弱化措辞：'demonstrates feasibility of scheduled sampling for auxiliary attention objectives, with model-dependent efficacy'。(4) 核心卖点 SP1（8×–27× 实证刻画）和 SP2（PCGrad 因果排除）不需调整——这两个不依赖 SS 跨模型。(5) Discussion 增加 'limitations of SS transferability' 段落，诚实报告 Llama 效果差异并分析可能原因（attention head 数量差异、layer 结构差异等）。(6) 目标 Findings 3.0–3.5，靠诊断弧（contributions 1–4）拿基础分，SS 作为 bonus。"

  worst:
    meaning: "SS 跨模型失败 + novelty 论证被驳回，核心假设 '可修复' 不成立，需 reframe 为纯诊断论文"
    key_assumptions:
      - "Llama SS 失败：AR GAR β=0 < 0.05（接近 baseline），gap 仍 >10×，或训练不收敛/崩溃"
      - "审稿人多数认为 exposure bias insight incremental（'we already know TF causes distribution shift，you just measured it on one more task'）"
      - "PCGrad ablation 被视为 'confirmatory, not novel'（'of course removing gradient projection doesn't fix distribution shift'）"
      - "论文被定性为 'well-executed negative result but limited novelty'——diagnostic 有价值但不够 conference level"
      - "W3（GAR 作为唯一代理指标）被 escalate：instruction retention test r=0.2 被认为 correlation 太弱"
      - "scope 限制（only lightweight gating + GAR）被认为 too narrow to generalize"
    number_ranges:
      llama_ss_ar_gar_beta0: [0.00, 0.10]
      llama_ss_tf_ar_gap_ratio: [5.0, 30.0]
      qwen_ss_ar_gar_beta0_3seed: [0.38, 0.45]  # 已锁定，Qwen 数据不变
      qwen_ss_tf_ar_gap_ratio: [1.1, 1.5]  # 已锁定
      dream_review_score: [2.5, 3.0]
      fatal_severe_concerns_remaining: [3, 5]
      reviewer_novelty_objection_probability: [0.7, 1.0]
      alternative_gar_defs_ss_improves: [0, 2]
    narrative_direction: "放弃 'discover→diagnose→remedy' 弧，reframe 为纯 mechanistic diagnostic paper，但不降级 venue（仍冲 EMNLP Findings）。具体调整：(1) Title 改为 'Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study'——去掉所有 recovery/remedy 暗示。(2) SS 从 Results 独立小节降级为 Discussion 的 'attempted mitigation'，承认 model-specific 局限。(3) 重新排序 contributions：核心卖点转为 failure mode taxonomy（NF1 反向 turn conditioning + NF2 distribution shift + NF3 干预强度不足）的系统分类学价值——类似 'A Taxonomy of Failure Modes for Auxiliary Attention Losses Under Distribution Shift'。(4) 加强 PCGrad 的 methodological contribution 叙事：不是 'of course'，而是 'without PCGrad ablation, gradient conflict would remain a plausible alternative hypothesis——we provide the first empirical elimination'。(5) 加强与 Dongre 的 convergent evidence 叙事：两种独立干预路线均失败 = 更强的 impossibility signal。(6) Introduction 结尾加 'our negative results establish concrete failure modes that future work must overcome' 的 constructive framing。(7) 补充 Discussion：concrete next steps（data-dependent SS schedule à la Dou & Gales 2022、curriculum-based exposure、inference-time only approaches）。(8) 目标 Findings 2.5-3.0，靠 systematic rigor + cross-model + taxonomy 争取 borderline accept。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f21383-c00a-492a-b4ef-9951169c8722",
  "isSidechain": false,
  "requestId": "req_011CbM4Dsanvt7ckinGAVhWH",
  "type": "assistant",
  "uuid": "99e6ec51-cfa5-4f45-8e64-fd6153c1be76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WnHuN6idTCB4F8RZ76HNE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35837,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3797,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3797,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 35837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35837
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "99e6ec51-cfa5-4f45-8e64-fd6153c1be76",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three exposure bias scenario tiers for dream paper",
  "sessionId": "811da4b1-9877-49a9-a3f3-80ee3741d1e0"
}
```

---
