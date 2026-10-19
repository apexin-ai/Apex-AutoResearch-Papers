# research correction magnitude literature

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_correction-magnitude-literature_20260514T181703_result.json`
- **Structured JSON:** [`653280a7885fbdd3632a.json`](../../sessions/65/653280a7885fbdd3632a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无法通过 MCP 写 literature_map.yaml（不在白名单）。直接输出完整调研结果。

---

## 文献调研结果：Correction Magnitude Control in Learned Residual Policies

### 一、关键论文列表

#### A. Residual Policy Learning 核心文献

| # | Paper | Authors | Year/Venue | Magnitude Control 机制 |
|---|-------|---------|------------|----------------------|
| 1 | **Residual Policy Learning** | Silver, Allen, Tenenbaum, Kaelbling | RSS 2018 | Zero-init output layer; action bounded to [-1,1]^D; 无显式 residual clipping |
| 2 | **Residual RL for Robot Control** | Johannink et al. | ICRA 2019 | Residual clipped into **tube** around base action; **Lyapunov stability** under bounded residuals |
| 3 | **TRANSIC: Sim-to-Real via Online Correction** | Jiang et al. | CoRL 2024 | **Learned binary gate** g_ψ: π_deployed = π_B ⊕ 𝟙_g·π_R；无 gate 时"large motions and model collapse" |
| 4 | **ResiP: Residual RL for Precise Assembly** | Ankile et al. | CoRL-W 2024 | **Scaling coefficient α≤1**: a_t = a_base + α·a_res；5%→99% on 0.2mm peg |
| 5 | **PLD: Self-Improving VLA via Residual RL** | Xiao et al. | ICLR 2026 | **Scheduled magnitude bound** [-ξ,ξ]，ξ∈[0,1]；ξ=0.5 LIBERO / ξ=0.1 SimplerEnv；ablation 确认 ξ 选择敏感 |
| 6 | **DRC: Decaying Relative Correction** | Pan et al. | arXiv 2025 | **Temporal decay**：correction vector 随时间衰减，30% less intervention |
| 7 | **DAWN: Value Learning in Residual RL** | Ma et al. | arXiv 2026 | 分析 cold start + scale mismatch bottleneck；critic normalization 解决 residual-too-small 问题 |

#### B. VLA-specific Correction 文献

| # | Paper | Year/Venue | 与 magnitude control 的关系 |
|---|-------|------------|--------------------------|
| 8 | **A2C2: Real-time VLA Chunk Correction** | 2025 | Per-step correction head，无显式 magnitude bound |
| 9 | **SC-VLA: Self-Correcting VLA** | 2026 | Residual RL + world model，无 magnitude 讨论 |
| 10 | **VLA-in-the-Loop** | 2025 | Event-triggered binary gate（关键时刻才修正） |
| 11 | **Residual Policy Adaptation for VLA** | 2026 | 0.9M residual head + impedance-aware loss 隐式约束 |

#### C. CP + Safety Constraint 文献

| # | Paper | Year/Venue | 与 magnitude control 的关系 |
|---|-------|------------|--------------------------|
| 12 | **ACP + CBF for Safe RL** (Zhou et al.) | ICRA 2025 | CP 不确定性 → CBF action constraints，动态调整安全边界 |
| 13 | **Lyapunov Certificates for Safe Residual RL** | 2025 | 闭式 safety filter 将 residual 投影到 Lyapunov-safe 半空间 |
| 14 | **SafeDiffCon** | ICML 2025 | CP uncertainty quantile 指导 diffusion model 安全控制 |

---

### 二、Correction Magnitude 处理方式分类

从文献中提取出 **6 种** correction magnitude 控制策略：

#### 1. Hard Clipping / Tube Constraint
- **做法**：`a_res = clip(a_res, -ε, ε)` 或 `||a_res|| ≤ ε`
- **代表**：Johannink 2019 (tube around base action)
- **理论保证**：Lyapunov 分析证明 bounded residual → uniformly ultimately bounded error
- **与 ACR-VLA 关系**：✅ 已有实现（`max_correction_norm=0.05` 实验）

#### 2. Learned Scaling Coefficient
- **做法**：`a = a_base + α·a_res`，α≤1 为超参数
- **代表**：ResiP (α固定)，PLD (ξ scheduled, 从小到大)
- **关键发现**：PLD 证明 ξ 太大→early degradation，ξ 太小→insufficient correction
- **与 ACR-VLA 关系**：⚠️ 可以做 α sweep 类似 max_norm sweep

#### 3. Learned Binary Gate
- **做法**：`a = a_base + 𝟙[gate(s)]·a_res`，gate 预测是否需要修正
- **代表**：TRANSIC (分类器 gate)，VLA-in-the-Loop (event-triggered)
- **关键发现**：TRANSIC 证明无 gate 时 fine-tuning 导致 model collapse
- **与 ACR-VLA 关系**：✅ Gated CRM 代码已实现（`src/gated_crm.py`）

#### 4. Temporal Decay
- **做法**：correction offset 随时间指数衰减
- **代表**：DRC (Pan 2025)
- **与 ACR-VLA 关系**：🔧 可扩展——correction 在 action chunk 内递减

#### 5. Safety Filter Projection
- **做法**：`a_safe = project(a_res, safe_set)` 基于 Lyapunov/CBF 证书
- **代表**：Lyapunov Certificates (2025)，ACP+CBF (Zhou 2025)
- **关键特点**：形式化安全保证，闭式投影无需在线优化
- **与 ACR-VLA 关系**：🔬 高级方向——用 CP bounds 作为 safe set

#### 6. Uncertainty-Guided Adaptive Bound
- **做法**：CP/uncertainty 量化 → 动态调整 correction 允许范围
- **代表**：Zhou 2025 (ACP → CBF)，SafeDiffCon (CP quantile → diffusion guidance)
- **与 ACR-VLA 关系**：⭐ **最匹配的叙事方向**——ACR-VLA 天然有 per-DOF conformal bounds，可直接用作 correction magnitude constraint

---

### 三、与我们场景的适用性分析

**核心问题回顾**：Full CRM correction 将 VLA 从 34-40% 拖到 2.5%，但 max_norm=0.05（1/28）达到 80%。

**文献对照**：
1. **PLD 的 ξ ablation 最直接可比**：他们发现 LIBERO 上 ξ=0.5 最优，SimplerEnv 上 ξ=0.1 最优——不同环境需要不同 correction scale，完全验证了我们的发现
2. **TRANSIC 的 model collapse** 现象与我们的 40%→2.5% 退化一致：无约束的 correction 破坏了 base policy 的良好行为
3. **ResiP 的 α 不敏感性** 暗示关键不是精确的 scaling 值，而是 "是否在正确 order of magnitude"
4. **DAWN 的 scale mismatch** 分析解释了为什么 CRM 训练效果差——当 correction 幅度与 base action 不在同一量级时，模型难以学到有效修正

**特殊优势**：ACR-VLA 已经有 **per-DOF conformal prediction bounds**——这在所有现有方法中是独一无二的。没有任何现有工作将 CP 的 calibrated uncertainty 直接用作 residual action 的 magnitude constraint。

---

### 四、建议叙事角度

**推荐叙事：Conformally-Calibrated Correction Magnitude**

> Residual policy learning 的核心挑战是 correction magnitude control（TRANSIC/PLD/ResiP 均证实）。现有方法依赖 fixed hyperparameter（α, ξ）或 learned gate，缺乏 principled 的 per-dimension, per-timestep 的 magnitude bound。ACR-VLA 利用 conformal prediction 提供的 **distribution-free, calibrated uncertainty intervals** 作为 correction magnitude 的自然上界——correction 幅度由模型自身的 calibrated uncertainty 决定，而非手工调参。

**具体 framing 策略**：

1. **Problem setup 引用链**：Silver 2018 (residual = additive correction) → Johannink 2019 (bounded residual for stability) → TRANSIC 2024 (unbounded correction → collapse) → PLD 2026 (scheduled ξ but environment-specific)

2. **Gap statement**：所有现有方法的 magnitude bound 要么是全局固定超参数（α, ξ, max_norm），要么是 binary gate（开/关）。**没有方法提供 per-DOF, per-timestep, calibrated magnitude bounds**。

3. **Our contribution**：ACR-VLA 的 conformal intervals 天然提供了 per-DOF calibrated bounds on expected action range。当 CRM correction exceeds these bounds，说明修正超出了模型的 calibrated confidence——应被 clipped 或 gated。

4. **Theoretical grounding 引用**：Zhou 2025 (CP → CBF action constraints) + Lyapunov certificates (bounded residual → stability) 建立了 "uncertainty-derived bounds guarantee safe correction" 的理论叙事。

**对比表格可在论文中使用**：

| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |
|--------|-----------|---------|-------------|------------|
| Silver 2018 | Action space | ✗ | ✗ | ✗ |
| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |
| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |
| ResiP 2024 | Fixed α | ✗ | ✗ | ✗ |
| PLD 2026 | Scheduled ξ | ✗ | ~(via schedule) | ✗ |
| **ACR-VLA (ours)** | **CP intervals** | **✓** | **✓** | **✓** |

---

Sources:
- [Residual Policy Learning (Silver et al., 2018)](https://arxiv.org/abs/1812.06298)
- [Residual RL for Robot Control (Johannink et al., 2019)](https://arxiv.org/abs/1812.03201)
- [TRANSIC: Sim-to-Real via Online Correction (2024)](https://arxiv.org/abs/2405.10315)
- [ResiP: Residual RL for Precise Assembly (2024)](https://arxiv.org/abs/2407.16677)
- [PLD: Self-Improving VLA via Residual RL (ICLR 2026)](https://arxiv.org/abs/2511.00091)
- [DRC: Decaying Relative Correction (2025)](https://arxiv.org/abs/2503.15368)
- [DAWN: Value Learning in Residual RL (2026)](https://arxiv.org/abs/2602.10539)
- [ACP + CBF for Safe RL (ICRA 2025)](https://arxiv.org/abs/2503.17678)
- [Lyapunov Certificates for Safe Residual RL (2025)](https://arxiv.org/abs/2605.06934)
- [SafeDiffCon (ICML 2025)](https://arxiv.org/abs/2502.02205)
- [VLA-in-the-Loop (2025)](https://openreview.net/forum?id=aT4LG8c6DE)
- [Residual Policy Adaptation for VLA (2026)](https://www.researchgate.net/publication/401122606)

新增 12 篇论文条目已准备好，但 literature_map.yaml 不在 MCP 写白名单中，需要手动更新或通过其他方式写入。

---
