# ACR-VLA Competitor Analysis

> 生成日期: 2026-05-14

## 方法对比表

| 维度 | ACR-VLA (Ours) | SC-VLA | VLA-Pilot | ACoT-VLA | ReconVLA |
|------|---------------|--------|-----------|----------|----------|
| **核心机制** | Per-DOF conformal statistics + learned CRM correction | Sparse world imagination + residual RL refinement | MLLM verifier + evolutionary diffusion optimizer | Action chain-of-thought (EAR+IAR) | CQR uncertainty + SMD failure detection |
| **方法类别** | Inference-time statistical correction | Inference-time RL refinement | Inference-time MLLM-guided steering | Training-time reasoning augmentation | Inference-time uncertainty gating |
| **是否需要额外训练** | CRM 需要训练（~轻量 MLP）；VLA backbone 冻结 | 需要训练 residual policy + auxiliary heads | 不需要（zero-shot plug-and-play） | 需要训练 EAR+IAR 模块 | 不需要（post-hoc calibration） |
| **不确定性量化** | Per-DOF (40D) conformal intervals via CGS | 无显式 UQ；用 task progress prediction 间接评估 | 无显式 UQ；MLLM 打分替代 | 无 UQ；通过 CoT reasoning 隐式提升可靠性 | Scalar CQR-based confidence + state-space anomaly |
| **统计保证** | ✅ Marginal coverage guarantee via CP; online ACI+COC 维持 | ❌ 无 | ❌ 无 | ❌ 无 | ✅ Marginal coverage via CQR（scalar level） |
| **Per-DOF 粒度** | ✅ 40D 维度独立 intervals + selective correction | ❌ 全局 residual adjustment | ❌ 全局 action scoring | ❌ 全局 CoT reasoning | ❌ Scalar aggregation（丢失维度信息） |
| **在线适应** | ✅ ACI+COC 在线调阈值 | ✅ Online RL refinement（需交互） | ✅ Iterative steering refinement | ❌ 静态模型 | ❌ Static calibration set |
| **推理开销** | K 次 flow-matching 采样 + CGS + CRM（~中等） | Residual policy forward + world model prediction（~低-中） | MLLM reasoning + evolutionary search（~高，2.41s/step） | EAR+IAR forward（~低） | 多次采样 + CQR quantile computation（~中等） |
| **主要 benchmark** | LIBERO / LIBERO-Plus | ManiSkill / ARX5 real-world | 6 real-world tasks (Franka Panda) | LIBERO / LIBERO-Plus / VLABench | LIBERO (待确认具体数据) |
| **代表性结果** | TBD (实验中) | ManiSkill avg 86%; +9% SR, -16% steps | OOD avg 0.50 vs baseline 0.12-0.19 | LIBERO 98.5%, LIBERO-Plus 84.1% | 改善 failure anticipation（具体 SR 未公开） |

## 逐竞品深度分析

### SC-VLA (arXiv:2602.21633)

**方法概述**：SC-VLA 通过 Sparse World Imagination (SPI) 和 Online Action Refinement (OAR) 实现自我纠正。SPI 在 VLA backbone 上附加辅助预测头，预测当前任务进度和未来轨迹趋势（sparse future states），从而迫使 policy 编码短期物理演化信息。OAR 利用这些预测构建 progress-dependent dense reward，通过 residual RL 在线调整动作。

**关键设计决策**：
- **Endogenous rewards**：奖励信号完全来自 world imagination 的内部一致性，不依赖外部 dense supervision
- **Sparse prediction**：只预测关键未来状态而非完整 world model，降低计算开销
- **Residual policy**：保留原始 VLA 输出，仅学习 residual correction

**实验结果**：
- ManiSkill 平均成功率 86%，PegInsertion 比 π₀/GR00T N1.5 高 28%/10%
- 任务吞吐量最高（-16% steps），成功率 +9%
- 真实世界 ARX5 实验 +14%

**局限性**：
1. **需要 RL 训练**：residual policy 和 auxiliary heads 需在目标任务上训练，限制 zero-shot 泛化
2. **无统计保证**：correction 基于 RL reward shaping，无法量化不确定性或提供 coverage guarantee
3. **全局纠正**：residual 作用在整个 action vector 上，无法区分哪些维度需要纠正
4. **未在 LIBERO-Plus 评估**：主要在 ManiSkill 上验证，与 ACR-VLA 的 benchmark 不完全重叠

**与 ACR-VLA 的本质区别**：SC-VLA 通过 learned world model + RL 做 action refinement，是 "学出来的纠正"；ACR-VLA 通过 conformal statistics 做 "有保证的纠正"。SC-VLA 无法告诉你 "哪个维度不确定"，也无法在不重新训练的情况下适应新任务。

---

### VLA-Pilot (arXiv:2511.14178)

**方法概述**：VLA-Pilot 采用三阶段 inference-time steering：(1) EPS-CoT (Embodied Policy Steering Chain-of-Thought) 利用 MLLM 推理 task-aligned steering objective 并生成 scoring reward code；(2) Evolutionary Diffusion 从 frozen VLA 采样多个 action proposals，基于 MLLM reward 进行进化优化；(3) Iterative Steering Refinement 将执行后反馈整合到下一轮 EPS-CoT 推理中。

**关键设计决策**：
- **MLLM as open-world verifier**：利用 VLM 的开放世界推理能力进行动作评估，不限于预定义 reward
- **Evolutionary optimization on diffusion latents**：在 diffusion denoising 过程中进行进化搜索，而非简单 best-of-K selection
- **Spatial keypoints augmentation**：EPS-CoT 融合 robot end-effector 和 object 的空间关键点信息

**实验结果**：
- 6 个真实世界任务（Franka Panda），相比 DiVLA baseline 提升 +0.21~+0.31
- OOD 场景平均成功率 0.50，vs baseline V-GPS 0.12 / FOREWARN 0.19
- Ablation：去掉 EPS-CoT → -8% MSR，去掉 Evolutionary Diffusion → -11% MSR

**局限性**：
1. **推理延迟极高**：2.41s/step，MLLM reasoning 是瓶颈，不适合实时控制
2. **依赖 MLLM 质量**：steering 效果完全取决于 MLLM 的推理质量，无 fallback
3. **无统计保证**：MLLM scoring 是启发式的，无法提供 calibrated confidence
4. **无 simulation benchmark 对比**：主要在真实世界评估，缺乏 LIBERO 等标准 benchmark 数据

**与 ACR-VLA 的本质区别**：VLA-Pilot 用 MLLM 做 "智能评委" 来选/优化动作，是 language-guided 的启发式方法；ACR-VLA 用 conformal prediction 做 distribution-free statistical correction。VLA-Pilot 的优势在 zero-shot OOD 泛化（靠 MLLM 的开放世界知识），劣势在延迟和缺乏理论保证。

---

### ACoT-VLA (arXiv:2601.11404, CVPR 2026)

**方法概述**：ACoT-VLA 提出 Action Chain-of-Thought 范式，将动作推理过程分解为两个互补组件：(1) Explicit Action Reasoner (EAR)——轻量 Transformer 生成粗粒度参考轨迹作为显式动作空间引导；(2) Implicit Action Reasoner (IAR)——通过 cross-attention 从 multimodal representations 中提取 latent action priors。两者共同形成 ACoT conditioning，引导下游 action head 的生成。

**关键设计决策**：
- **双推理器架构**：EAR 提供 kinematically plausible 的运动学引导，IAR 提供 dense semantic priors
- **Training-time integration**：EAR+IAR 在训练时与 VLA 联合优化（LLM backbone 冻结），属于训练阶段方法
- **50 demos/task**：仅需少量示教数据

**实验结果**：
- LIBERO 98.5%，LIBERO-Plus **84.1%**（当前最高之一），VLABench 47.4%
- Ablation：仅 EAR → 83.7%，仅 IAR → 80.4%，双路径互补效应显著
- AgibotTech 开源，ICRA 2026 AgiBot World Challenge 官方 baseline

**局限性**：
1. **Training-time 方法**：需要在目标任务上训练 EAR+IAR，不是 plug-and-play
2. **无不确定性量化**：CoT reasoning 不输出 confidence，无法识别何时 "不确定"
3. **静态模型**：部署后不在线适应，calibration drift 无法处理
4. **与 ACR-VLA 互补**：ACoT 提升 VLA 基础能力，ACR-VLA 在其之上提供 safety net

**与 ACR-VLA 的本质区别**：ACoT-VLA 是 training-time 的 "思考能力增强"，让 VLA 在生成动作前先做结构化推理。ACR-VLA 是 inference-time 的 "统计安全网"，在 VLA 生成动作后检测和纠正异常。两者正交且互补——可以先用 ACoT 增强 VLA backbone，再套 ACR-VLA 做 conformal correction。

---

### ReconVLA (arXiv:2604.16677)

**方法概述**：ReconVLA 将 conformal prediction 应用于 VLA action token 输出，提供两层保护：(1) CQR-based action uncertainty estimator——对 VLA 的多次采样输出计算 conformalized quantile regression intervals，用于量化动作级不确定性；(2) SMD-based state anomaly detector——监控 latent state distributions 检测 OOD/failure-prone 条件。框架将不确定性分解为 input uncertainty（OOD observations）和 noise uncertainty（generative stochasticity）。

**关键设计决策**：
- **Post-hoc, no retraining**：完全在 frozen VLA 上 post-hoc 应用，与 ACR-VLA 理念一致
- **Scalar CQR**：使用标准 CQR 产生 scalar-level confidence，非 per-DOF
- **Static calibration**：使用固定 calibration set，不做在线适应
- **Dual uncertainty decomposition**：input vs noise uncertainty 有利于 root cause analysis

**局限性**：
1. **Scalar uncertainty**：CQR 输出聚合为 scalar 置信度，丢失维度级信息——无法告诉你 "第 3 个关节不确定但其余都好"
2. **Static calibration**：calibration set 固定后不更新，distribution shift 下 coverage 可能退化
3. **Detection-only vs correction**：ReconVLA 的 UQ 主要用于 failure detection 和 action selection，不做 learned correction（从 K candidates 选而非合成新 action）
4. **实验数据有限**：具体 success rate 数据未充分公开，方法验证深度待加强

**与 ACR-VLA 的本质区别**：ReconVLA 是 ACR-VLA 最直接的竞争者——同样使用 conformal prediction + frozen VLA。关键差异在三个层面：

| 差异维度 | ACR-VLA | ReconVLA |
|---------|---------|----------|
| UQ 粒度 | Per-DOF 40D intervals (CGS) | Scalar CQR aggregation |
| 纠正策略 | Learned CRM 合成新动作 | Sample selection from K candidates |
| 在线适应 | ACI+COC 在线阈值调整 | Static calibration |

ACR-VLA 在每个维度上都比 ReconVLA 更进一步：更细粒度的 UQ → 更精准的纠正 → 更鲁棒的在线部署。

---

## ACR-VLA 独特卖点 (USP)

### 1. Statistical Guarantees from Conformal Prediction
- 提供 distribution-free marginal coverage guarantee，不依赖模型假设
- SC-VLA 和 VLA-Pilot 完全无统计保证；ACoT-VLA 无 UQ 能力
- ReconVLA 有 CP 保证但仅在 scalar level

### 2. Per-DOF Granularity (Dimension-Selective Correction)
- 40D 维度独立的 conformal intervals 通过 CGS (Conformalized Gaussian Scoring)
- 唯一能做到 "第 3 个关节 ±0.02 rad 不确定，第 7 个关节 ±0.15 rad 很不确定" 的方法
- 其他所有方法要么无 UQ（SC-VLA/VLA-Pilot/ACoT-VLA），要么 scalar aggregation（ReconVLA）
- **核心论点**：机器人动作是 structured 的（position/orientation/gripper 有不同语义），scalar UQ 会将关键维度的异常淹没在整体均值中

### 3. Learned Correction (CRM) vs Sample Selection
- CRM 学习在 conformal interval 约束下合成新动作，而非从 K candidates 中选
- SC-VLA 用 residual RL 做纠正（但需要环境交互训练）
- VLA-Pilot 用 evolutionary search 优化（但依赖 MLLM scoring）
- ReconVLA 仅做 sample selection（信息利用率低——只用了 1/K 的采样信息）
- **核心论点**：当 K 个样本都不够好时，selection 失效；CRM 可以合成更优动作

### 4. Online Adaptation via ACI+COC
- Adaptive Conformal Inference + Coverage-Oriented Calibration 实现在线阈值自适应
- 处理 deployment 中的 distribution shift，coverage guarantee 在线维持
- SC-VLA 需要在线 RL 交互（costly），VLA-Pilot 需要 MLLM 每步推理（slow）
- ACoT-VLA 和 ReconVLA 都是 static models，无法在线适应
- **核心论点**：real-world deployment 必然遇到 distribution shift，static calibration 的 coverage 会退化

### 5. No Additional Training for VLA Backbone
- VLA backbone 完全冻结，仅需训练轻量 CRM
- SC-VLA 需训练 residual policy + auxiliary heads；ACoT-VLA 需训练 EAR+IAR
- VLA-Pilot 和 ReconVLA 同样 training-free（对 backbone），但各有其他局限

---

## Related Work 定位建议

### 推荐的 Related Work 叙事结构

**Paragraph 1: VLA Foundation & Robustness Problem**
- 引出 VLA 范式 (RT-2, OpenVLA, pi0, SmolVLA) 及其脆弱性问题
- 引用 LIBERO-Plus 的 robustness evaluation 结果

**Paragraph 2: Training-Time Robustness Methods**
- ACoT-VLA (action reasoning)、RobustVLA/SRPO (RL post-training)、DiG-Flow (geometric regularization)
- 定位：这些方法提升 VLA 基础能力，但部署后无法适应新分布
- 关键句："These training-time approaches are orthogonal and complementary to ACR-VLA's inference-time correction."

**Paragraph 3: Inference-Time Correction Methods**
- SC-VLA (world model + residual RL)、VLA-Pilot (MLLM steering)、A2C2 (async chunk correction)
- 定位：同为 inference-time，但缺乏统计保证和维度粒度
- 关键句："While effective, these methods provide no formal uncertainty quantification or coverage guarantees."

**Paragraph 4: Uncertainty Quantification for VLAs**
- ReconVLA (CQR on action tokens)、SAFE (internal feature CP)、Zollo & Zemel (VLA calibration)
- 定位：ReconVLA 是最近的竞争者，但 scalar UQ + static calibration + selection-only
- 关键句："ReconVLA applies CQR to VLA action tokens but aggregates to scalar uncertainty, losing the per-DOF granularity critical for structured robot actions."

**Paragraph 5: Conformal Prediction in Robotics**
- Conformalized Teleoperation (RSS'24)、CP-Loop、CLAPS、SafeDiffCon
- 定位：CP 在 robotics 的成功应用，但尚未有 per-DOF multivariate CP + learned correction for VLAs
- 关键句："ACR-VLA bridges multivariate conformal prediction with VLA action correction, uniquely combining per-DOF statistical guarantees with learned dimension-selective refinement."

### 关键差异化表述（供论文使用）

> "Unlike SC-VLA which requires task-specific residual RL training, VLA-Pilot which introduces 2.4s MLLM latency per step, and ReconVLA which aggregates to scalar uncertainty, ACR-VLA provides **per-DOF conformal intervals** with **online coverage guarantees** and **learned correction** that synthesizes improved actions beyond sample selection — all without modifying the frozen VLA backbone."

---

## 竞争格局总结

```
                    Training-Time ←────────→ Inference-Time
                         │                        │
    ACoT-VLA ────────────┤                        │
    (CoT reasoning,      │                        │
     LIBERO+ 84.1%)      │                        │
                         │    SC-VLA ─────────────┤
                         │    (Residual RL,        │
                         │     needs RL training)  │
                         │                        │
                         │    VLA-Pilot ──────────┤
                         │    (MLLM steering,      │
                         │     2.41s latency)      │
                         │                        │
                         │    ReconVLA ───────────┤
                         │    (Scalar CP,          │
                         │     detection only)     │
                         │                        │
                         │    ACR-VLA (Ours) ─────┤
                         │    (Per-DOF CP +        │
                         │     learned correction  │
                         │     + online adaptation)│

    Has Statistical Guarantee: ACR-VLA ✅, ReconVLA ✅(scalar), Others ❌
    Per-DOF Granularity:       ACR-VLA ✅, Others ❌
    Online Adaptation:         ACR-VLA ✅, SC-VLA ✅(RL), VLA-Pilot ✅(MLLM), Others ❌
```
