# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering

> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 auxiliary attention loss 的泛化性（30x 断层的定量证据）。这个 insight 对所有在 teacher-forcing 下优化的 attention auxiliary loss 都有警示意义。
> Novelty 排序: (1) teacher-forcing→generation 分布偏移 > (2) NTP-GAR 梯度竞争导致 gate 反向学习 > (3) negative result 本身
> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
> 最后更新: 2026-05-19 (Reviewer 评估后 reframe: distribution shift insight 为核心卖点)
> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）

---

## 1. Title Candidates

- **T1 (推荐)**: Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference
- **T3**: Residual Gating Cannot Recover Goal Attention in Multi-Turn Dialogue

推荐 T1: "Lightweight Gating" 比 "Residual Gating" 覆盖更广（含 uniform gate），"Mechanistic Analysis" 突出 insight 而非 negative result。

---

## 2. Story Arc

Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), but this improvement completely fails to transfer to inference (GAR = 0.016, a 30x gap). Our central finding is that teacher-forcing training creates a fundamental distribution shift: attention patterns learned under teacher-forced contexts do not generalize to autoregressive generation, where the model conditions on its own outputs. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Combined with Dongre et al.'s independent failure of goal re-injection, our results demonstrate that auxiliary attention losses optimized under teacher-forcing face a fundamental generalization barrier.

---

## 3. Core Claims

| # | Claim | 支撑 | 状态 |
|---|-------|------|------|
| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | 已验证 |
| C2 | Residual gating 在训练端可有效优化 GAR (0.02→0.48)，但推理时完全不泛化 (GAR=0.016, 30x 断层) | v7 训练曲线 + D015/D017 confirmed non-bug | 已验证 |
| C3 | 三个耦合失败机制的因果分析: NF1 反向 turn conditioning + NF2 30x 泛化 gap + NF3 gate 干预强度不足 2-7% | D014 gate-profile 分析 + D015 代码验证 + 梯度冲突实验 (待做) | NF1/NF2/NF3 已验证，梯度冲突量化待做 |
| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。PPL 对比揭示 gating 是否在不改善 GAR 的同时还损害 NTP 质量 | 四路 eval on standard_conversations: GAR + PPL (待做) | 待 eval 确认 |
| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Llama 实验 (待做) | 待做 |

---

## 4. Negative Findings (NF)

| # | Finding | 证据 | 叙事角色 |
|---|---------|------|----------|
| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
| NF2 | 30x training-inference GAR gap: 训练 GAR=0.48 vs 推理 GAR=0.016 | D015 代码逐行验证非 bug，是 attention pattern 不泛化 | 核心 negative finding，对所有辅助 attention loss 方法有警示意义 |
| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |

---

## 5. Key Selling Points

**SP1 (核心卖点): Teacher-forcing→generation 分布偏移的定量证据。** 30x training-inference GAR gap 不是 gating 的特有问题，而是所有在 teacher-forcing 下优化 auxiliary attention loss 的方法都面临的结构性障碍。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。这个 insight 超越 residual gating，对整个 attention steering 领域有警示意义。

**SP2: NTP-GAR 梯度竞争的逐层量化。** NTP loss 在 gate 参数上的梯度方向与 GAR loss 冲突，且幅度远大于 GAR（定量测量待做）。这导致 gates 学到反向 turn conditioning（NF1），是分布偏移的放大器。

**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融 (TG/UG/LoRA-only/Base) 严格隔离贡献。

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
| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |

---

## 7. Dongre et al. 关系定位

| 维度 | Dongre et al. | 本文 |
|------|---------------|------|
| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |
| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |

**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。

共同推论: 两种独立干预路线均失败 → 在 teacher-forcing 下优化的 auxiliary attention loss 面临结构性泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。

---

## 8. GAR 定义策略

| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
|------|------|------------|----------------|------|
| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |

两种定义下推理 GAR 均极低 (~0.016)，与训练 GAR (0.48) 形成 30x 断层。定义差异不影响 negative finding。

---

## 9. 论文结构草案

1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
5. **Method**: ThreadGate 架构 + MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)
7. **Analysis**: NTP-GAR 梯度冲突 + 30x 泛化 gap 分析 + gate profile + attention 可视化 + 训练动力学三阶段
8. **Discussion**: 为什么 residual gating 不够 → 对所有 attention steering 方法的启示 → 潜在解决方向 (inference-time intervention / decoupled pathway / GAR-aware decoding)
9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议

### 贡献列表（按 novelty 排序）

1. **Teacher-forcing distribution shift 的定量证据**: 首次量化 teacher-forcing→generation 分布偏移如何摧毁 auxiliary attention loss 的泛化性（30x training-inference GAR gap），对所有在 teacher-forcing 下优化的 attention steering 方法有广泛警示意义
2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性

---

## 10. 竞争力评估（Reviewer 估分 2026-05-19）

- **不含 Llama-3**: Findings 3.0（紧绷）。单模型是致命弱点（W1）。
- **含 Llama-3 跨模型验证**: 3.0-3.5。distribution shift insight 的泛化性 + 跨模型 convergent evidence 是升级关键。
- **冲 Main 条件**: Llama-3 复现 + 梯度冲突量化做扎实 + constructive future directions + 可选的下游任务 sanity check。
- **核心差异化**: 不是 "gating 失败了"（弱），而是 "teacher-forcing distribution shift 摧毁了 auxiliary attention loss 的泛化性"（强，对领域有广泛警示意义）。
- **风险**: W2（"没调对参数"）和 W5（"exposure bias 已知"）需要在论文中显式 address。
