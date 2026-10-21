# Negative Results → ICML Insights Analysis

**目标**: 从 35 个 negative 实验中提取可转化为论文 positive contribution 的 insight，服务于核心 narrative: CIVO 是 dt_emb-driven 的 locomotion-specific 现象，且在所有干预层级上都难以可靠缓解。

---

## 结构化清单

### 高 Insight 价值（证伪本身是重要发现）

| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |
|--------|----------------------|---------|------|-------------------|
| exp_016e | Reward-head SGS 阻断 CIVO 梯度通路 | Reward head 贡献 38-49% 梯度但阻断它是 **no-op**（reward loss 对 dt_emb.weight 梯度=0）。**梯度量级与因果重要性完全脱耦** | 高 | Section 3 核心发现。"Gradient Magnitude ≠ Causal Importance" 作为独立 observation，对 multi-head MBRL 系统有方法论启示。Reviewer 易 resonate——违反直觉且可验证 |
| exp_018v2 + exp_018_s2 | Full-SGS（阻断所有 decoder→dt_emb 梯度）消除 CIVO | Full SGS 0/3 seeds（含 2 环境）。CIVO 仅被延迟 ~30K 步后仍爆发。**Backward-pass 是错误的干预层级**——forward-pass representational damage 不可逆 | 高 | Intervention Hierarchy Table 的 L1 行。Frame: "Even blocking all non-KL gradient pathways (reducing dt_emb gradient by >95%) only delays onset, proving the vulnerability resides in the forward pass" |
| exp_026_obs_sgs_cheetah (s0+s1) | 阻断 obs-decoder→dt_emb 梯度消除 Cheetah CIVO | **补偿放大**：阻断 obs-decoder 后 NVE 从 untreated 8.3× 恶化到 21.9-30.2×（2.6-3.6× 放大）。阻断一条通路导致剩余通路 co-adaptation 加剧 | 高 | Section 3/Discussion 作为 "compensatory amplification" 现象。对 multi-head architecture 干预设计有普适警示：局部干预可能比不干预更糟 |
| exp_030c (TCN σ=1.0 Cheetah) | 高剂量 TCN 噪声可抑制 Cheetah CIVO | **"Impossible dose"**：σ=1.0 完全抑制 CIVO（NVE≤0.30），但 eval 从 peak 372(116% baseline!)→47(15%)。CIVO prevention threshold > noise tolerance threshold，**不存在 Goldilocks zone**。关键：初始学习不受影响（35K=116% baseline），是渐进累积性 policy erosion | 高 | Section 3.6 最有力单点。Frame: "The effective dose exceeds the tolerable dose — CIVO prevention requires noise levels that progressively erode policy quality through cumulative actor gradient interference, even while value calibration remains normal" |
| exp_034 + exp_034_dual_critic_cheetah | Dual-critic pessimism（Double Q）防止 Cheetah CIVO | **v1≈v2**（ρ>0.999）：两个 critic 共享 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值 3-4%。**Pessimism 机制在 pure-imagination MBRL 中失效** | 高 | Section 3 / R9 回应的核心。Frame: "Standard Double Q assumes critic independence; in imagination-based training where both critics consume identical world-model features, this assumption breaks — critics correlate to ρ>0.999, rendering min-based pessimism a near-identity operation" |
| exp_038_dual_critic_walker_s2 | Dual-critic 防止所有 collapse | CIVO 被完全阻止（NVE≤0.3）但 eval 仍 354→99.6 崩溃。**Non-CIVO collapse（Pathway B）**：actor entropy 急升(-3.59→-0.45)，与 CIVO 的 entropy 下降相反。Trained dt_emb 创造**多条脆弱性路径** | 高 | C6 partially falsified 的关键证据。Frame: "Eliminating CIVO (Pathway A) reveals a second vulnerability — trained dt-embedding destabilizes the actor through a distinct mechanism (eval-driven entropy increase) that architectural interventions do not address" |
| exp_008e_v3_s2 | dt=1 imagination 防止 collapse（C6） | dt=1 imagination + trained dt_emb：1/2 seeds 崩溃（715→137），崩溃动力学与 CIVO 定性不同（eval-driven vs value-driven）。**Trained dt_emb 通过 forward pass 创造不依赖 imagination dt 的脆弱性** | 高 | C6 核心，2-3 句 + 对比表。Frame: "Restricting imagination to dt=1 eliminates the value overestimation feedback loop (Pathway A) but not the eval-driven instability (Pathway B), demonstrating that trained dt-embedding creates vulnerability through the forward pass itself, not solely through multi-step imagination" |

### 中 Insight 价值（边界条件或设计约束）

| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |
|--------|----------------------|---------|------|-------------------|
| exp_030a/030b/031/031b (TCN cross-env) | TCN 跨环境泛化 | Effective dose scales with CIVO severity; tolerable dose does not。Walker σ=0.2 成功但 Cheetah/PickCube σ=0.2-0.5 全部失败。**不存在 universal effective dose** | 中 | Section 3.6 "dose-environment dependency" observation。支撑 TCN = diagnostic probe not deployable mitigation 的定位 |
| exp_027_s0/s1 + exp_029b/029d (TCN seed variance) | TCN σ=0.2 在 Walker 上 robust | Walker σ=0.2: 2/4 seeds 成功，2/4 完全失败（NVE>2.0）。**Seed 效应 > dose 效应**。TCN 作为 all-or-nothing gate 运作，无中间态 | 中 | 1-2 句 observation + appendix 详细分析。"Binary protection" 特性表明 CIVO onset 有 phase transition 性质——一旦突破临界点不可逆转 |
| exp_028/028_ceil15 (RAVE) | Value capping 防止 CIVO | **EMA anchor 自身被污染**：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → ceiling 无效。CIVO 根因不在 value 数值大小，而在 **value 的结构性偏差** | 中 | Intervention Hierarchy L2 行。Frame: "Output-level value capping fails because the anchor itself is corrupted by the same overestimation it aims to constrain — a bootstrap failure analogous to the CIVO mechanism itself" |
| exp_006/007/008c/008f_s4/009c (dt>1 degradation) | 解决 CIVO 后 dt>1 可行 | 即使完全消除 CIVO，dt>1 仍带来 40-70% 性能损失（RSSM compounding error）。**CIVO 只是 dt>1 问题的一个维度** | 中 | Discussion/Limitation。Frame: "Even a hypothetical perfect CIVO solution would leave 40-70% performance degradation from RSSM compounding error — temporal abstraction in imagination requires fundamentally better multi-step prediction, not just overestimation control" |
| exp_015b (frozen dt_emb) | 冻结 dt_emb 避免 CIVO | **Gradient starvation**：冻结 dt_emb 导致 actor_loss→0、entropy 异常低。dt_emb 梯度流对正常学习必要——**不能通过冻结触发参数来规避** | 中 | Section 3 简短提及。Frame: "The very parameter that triggers CIVO is also essential for learning — freezing it trades overestimation for starvation, confirming that the vulnerability is architecturally entangled" |
| exp_037_wide_critic_cheetah | Capacity alone（宽 critic）抑制 Cheetah CIVO | NVE 从 baseline 70.64 降至 3.6（但仍远超 1.5 阈值），eval 146（baseline 31%）。**Capacity alone 提供部分 recovery 但不能 prevent** | 中 | 2×2 mechanism factorial 的一格。与 dual-critic 对比支撑 "min+capacity 协同" 发现 |
| exp_036_dual_critic_pickcube | Dual-critic 跨 manipulation 泛化 | NVE 终值 0.2（"prevented"）但 eval 极低（27.7），gate 锁死 dt=2。**功能性失败**：CIVO 指标好但实际性能不可接受 | 中 | Scope limitation discussion。PickCube 任务动态与 locomotion 根本不同——gate/subsample 配置本身对 manipulation 有害（vanilla baseline 58.6 → 加配置后 26.6），非 CIVO 导致 |
| exp_003/004/005 (event-gate v2-v4) | Learned gate 实现 adaptive horizon | Gate 的 dt>1 选择**内在地**引入 CIVO，且 gate 无法学会规避。**这一失败催生了整个 CIVO 研究方向** | 中 | Introduction 叙事起点。Frame: "Our initial attempt at learned temporal abstraction consistently degraded performance. Diagnosing this failure led to the identification of CIVO as the root mechanism" |
| exp_051_stackcube_frozen | Frozen dt_emb 在 manipulation 防止 CIVO | Frozen dt_emb 在 Walker/Cheetah（locomotion）有效但 StackCube（manipulation）失败。**Locomotion 与 manipulation 的 CIVO 机制存在差异** | 中 | Scope boundary 讨论。支撑 "locomotion-specific" 论文 scope 限定 |

### 低 Insight 价值（纯统计补充或已被取代）

| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |
|--------|----------------------|---------|------|-------------------|
| exp_009e (008d s1 延长) | CIVO collapse 复现 | 确认 CIVO collapse，诊断性 negative | 低 | 仅作为 multi-seed 数据点计入统计表 |
| exp_009b (008d s2) | CIVO onset 跨 seed 复现 | NVE>1.5 但 self-corrected（268 eval）。Transient vs sustained 的 early evidence | 低 | 已被更完整的 multi-seed 分析取代，作为 C2 4/4 separation 的一个数据点 |
| exp_008e_v3_s3 | C6 第三 seed 验证 | 又一个 collapse seed，加强统计但无新机制 | 低 | 仅计入 collapse rate（现 3/4），不需独立讨论 |
| exp_008f_s4 | No-dt-emb 控制组 seed 4 | eval 306.5（baseline 33%），无 CIVO（NVE 0.58）。预期内的性能代价 | 低 | 仅作为 no-dt-emb 控制的第 N 个数据点 |
| exp_009c (008f s2) | No-dt-emb 控制 seed 2 | NVE 1.14@105K（borderline），比 seed 1 更高。Protection "不 robust" 的早期 signal | 低 | 已被 008f 系列多 seed 数据取代 |
| exp_008c | Subsample OFF + dt=2 imag 可行 | eval 仅 baseline 39%。Compounding error 是瓶颈 | 低 | 被 C5 discussion 吸收，不需独立列出 |
| exp_025_obs_sgs_walker_s2 | Obs-decoder-only SGS 抑制 CIVO | CIVO 部分抑制但 eval 仅 7-10% baseline。obs-decoder SGS 摧毁性能 | 低 | 被 C7 的 1/6 统计和 universal value collapse 发现吸收 |
| exp_029c (σ=0.1) | σ=0.1 是最低有效剂量 | NVE breach 但最终 eval 尚可（328）。剂量不足 | 低 | dose-response 曲线的一个数据点 |
| exp_027_tcn_walker_s0 (σ=0.5) | TCN σ=0.5 抑制 CIVO | NVE peak 4.0, oscillatory CIVO。σ=0.5 在 Walker 过量 | 低 | dose-response 的 overdose 端参考 |
| exp_027_tcn_walker_s1 (σ=0.5 s1) | TCN σ=0.5 seed 1 复现 | NVE 1.64, oscillatory。与 s0 一致：σ=0.5 过量 | 低 | 同上 |

---

## Coherent Story: Intervention Hierarchy 与多层失败叙事

### 核心 Narrative

35 个 negative 实验组合构成了一个 **escalating intervention failure** 的完整叙事，从最轻量（gradient manipulation）到最重量（architecture redesign），系统性证明 CIVO 在所有干预层级上的抗性：

```
干预层级           方法               成功率      关键失败机制
─────────────────────────────────────────────────────────────
L1 Gradient        Reward SGS         0/2        No-op (梯度≠因果)
                   Full SGS           0/3        Forward-pass damage 不可逆
                   Obs-decoder SGS    1/6        补偿放大 + critic 校准损坏
L2 Output          RAVE               0/2        EMA anchor 自身被污染
L3 Representation  TCN                2/8        Dose-env dependency, 无 Goldilocks zone
L4 Architecture    Dual-critic        3/5*       v1≈v2 (pessimism 失效),
                                                 non-CIVO collapse (Pathway B)
─────────────────────────────────────────────────────────────
Control            dt_emb removal     5/5        不是干预——移除了 feature
```

*Walker 2/3 CIVO prevented + 1 non-CIVO collapse; Cheetah 0/1; PickCube 功能性失败

### 这个 Hierarchy 为什么构成 Positive Contribution

1. **节约社区资源**：7+ 方法 × 3 层级 × 3 环境的系统性 negative evidence，阻止后续研究者重复探索这些 dead ends
2. **揭示 CIVO 的本质**：不是 gradient 问题（SGS 失败）、不是 value magnitude 问题（RAVE 失败）、不是 critic independence 问题（v1≈v2），而是 **forward-pass representational entanglement**
3. **方法论启示**：
   - "梯度量级 ≠ 因果重要性" 对所有 multi-head MBRL 系统的 debugging 有普适价值
   - "补偿放大" 对 partial intervention 设计的警示
   - "impossible dose" 证明某些 failure mode 不能通过 tuning 解决

### 三条辅助 Narrative

**A. Multi-Pathway Vulnerability（多路径脆弱性）**
- exp_008e_v3_s2 + exp_038 共同证明：trained dt_emb 通过至少两条路径创造脆弱性
  - Pathway A (CIVO): value overestimation → actor exploitation → entropy ↓ → collapse
  - Pathway B (IRD): eval-driven destabilization → entropy ↑ → policy randomization
- dt=1 imagination 消除 Pathway A 但不消除 B
- Dual-critic 消除 CIVO 但不消除 non-CIVO collapse
- **论文价值**: 即使"解决" CIVO，trained dt_emb 仍不安全

**B. Environment Severity Boundary（环境严重度边界）**
- Walker（NVE 1.5-5×）: TCN 2/4, dual-critic 2/3 有效
- Cheetah（NVE 8-70×）: TCN 0/3, dual-critic 0/1, σ=1.0 impossible dose
- PickCube: 任务动态本质不同，gate 配置本身有害
- **论文价值**: 所有干预方法都有 CIVO severity ceiling，强化 "根本解决需要架构革新" 的结论

**C. Origin Story（研究方向转向）**
- exp_003→004→005 (event-gate v2-v4) 的连续失败催生了 CIVO 研究方向
- 从 "如何让 temporal abstraction work" 到 "为什么 temporal abstraction fails"
- **论文价值**: Introduction 叙事起点，展示研究动机的自然性

---

## 论文各 Section 对应的 Negative Results 使用建议

| Section | 使用的 Negative Results | 功能 |
|---------|------------------------|------|
| Introduction | exp_003-005 (event-gate 失败) | 研究动机：试图做 temporal abstraction 但反复失败，转向诊断 why |
| Section 3.1-3.2 (CIVO 诊断) | exp_009e/009b (CIVO 复现) | 作为 multi-seed 数据点确认 CIVO 可复现性和随机性 |
| Section 3.3 (Gradient analysis) | exp_016e (reward SGS no-op) | "梯度 ≠ 因果" 核心发现 |
| Section 3.4 (SGS 系列) | exp_018v2/018_s2/021/025/026 | Intervention Hierarchy L1 全面否定；补偿放大 |
| Section 3.5 (RAVE) | exp_028/028_ceil15 | L2 否定；anchor 污染机制 |
| Section 3.6 (TCN) | exp_027-031b 全系列 | L3 部分否定；impossible dose；dose-env dependency |
| Section 3.7 (Dual-critic) | exp_034/036/037/038 | L4 部分否定；v1≈v2；non-CIVO collapse |
| Section 4 (C6 multi-pathway) | exp_008e_v3_s2/s3 + exp_038 | 多路径脆弱性证据 |
| Discussion (dt>1 limitation) | exp_006/007/008c/008f_s4 | 即使解决 CIVO，dt>1 仍有 40-70% 性能损失 |
| Discussion (scope) | exp_051 (StackCube frozen 失败) + exp_036 (PickCube) | Locomotion-specific scope boundary |
| Discussion (frozen dt_emb) | exp_015b | 不能冻结触发参数——architecturally entangled |

---

## 总结

35 个 negative 实验中：
- **7 个高 insight**：构成 Intervention Hierarchy + Multi-Pathway Vulnerability 两大核心贡献
- **10 个中 insight**：提供边界条件、scope limitation、design constraint
- **10+ 个低 insight**：作为统计数据点计入，不需独立讨论

最重要的 framing 策略：这些 negative results **不是 limitation**，而是论文的 **primary contribution**。一篇 diagnostic paper 的价值恰恰在于系统性地证明某个问题有多难解决，以及为什么难。Intervention Hierarchy（7 methods × 3 levels × 3 environments）是同类工作中最全面的 CIVO 干预评估，其 negative nature 本身就是强贡献。
