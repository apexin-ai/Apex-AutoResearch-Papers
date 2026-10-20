# LoRA + Flow Matching Mode Collapse 修复方案：文献调研报告

**项目**: importance_margin_vla_compress (SmolVLA)
**日期**: 2026-05-16
**问题**: LoRA (rank=32, alpha=64, scale=2.0) fine-tune 30K steps 后，inference action std 从 0.104 降至 0.006，所有轨迹收敛到同一固定点

---

## 1. LoRA + Diffusion/Flow Matching 已知问题

### 核心诊断：alpha/rank = 2.0 过于激进

当前配置 alpha=64, rank=32 给出 effective scaling = 2.0x，这在 diffusion/flow matching 模型中已知会导致 collapse。Diffusion 社区（Kohya/sd-scripts）推荐 alpha = rank/2（即 scaling=0.5x），而非 LLM 常用的 alpha=rank 或 2*rank。

- **RSLoRA** 建议 scaling = alpha/sqrt(rank)，对高 rank 更稳定
- **LoRA vs Full FT: An Illusion of Equivalence** (arXiv:2410.21228, NeurIPS 2025)：LoRA 产生 "intruder dimensions"——full FT 中不存在的高阶奇异向量，导致局部遗忘和 OOD 泛化差异。缩小 intruder dimensions 可在几乎不损失下游性能的情况下改善预训练分布建模。

### MSE Loss 平均多模态 velocity field

- **Variational Rectified Flow Matching** (arXiv:2502.09616)：经典 RFM 的 MSE loss 在同一时空坐标处平均不同 noise→data 映射方向，导致 velocity field 退化为均值。引入 latent variable 解耦多模态 velocity。
- **Conditioning Matters (Cocos)** (arXiv:2505.11123, NeurIPS 2025)：识别 "loss collapse" 现象——当 condition 难以区分时，训练目标退化为建模 marginal action 分布，模型忽略 observation 输入，预测数据集平均 action。**直接解释了我们的症状。** 修复方案：使 source distribution 依赖 condition。

**推荐实验**：
1. 立即将 alpha 降至 16（scaling=0.5x）或 32（scaling=1.0x），重新训练
2. 若仍 collapse，尝试 alpha=1（极小扰动），验证是否为 scaling 问题
3. 风险：alpha 过低可能导致适应能力不足，需在 loss 收敛和 inference diversity 间找平衡

---

## 2. Diffusion Policy / Flow Matching Policy Fine-tuning 最佳实践

### 主流 VLA 的 LoRA 配置

| 模型 | LoRA Rank | Alpha 策略 | 训练步数 | LR | 备注 |
|------|-----------|-----------|---------|-----|------|
| Pi0/Pi0.5 | 16 | 未公开 | 20-30K | 5e-5 cosine | 冻结 VLM，只 tune action expert |
| OpenVLA-OFT | 32 | target=all-linear | - | - | L1 regression 替代 256-bin 离散化 |
| Octo | 32 | attention layers | - | - | 无显式 anti-collapse 机制 |
| SmolVLA (HF) | - | - | 20K | - | ~50 episodes 起步 |

### 关键模式

Pi0 的核心设计：**冻结 VLM backbone，只 LoRA tune action expert**。这种架构分离天然限制了 catastrophic forgetting。OpenPI 团队评价 LoRA 和 full FT "没有明显区别"，推荐 LoRA 节省显存。但社区有报告称 LoRA policy "表现不佳"。

- **Much Ado About Noising** (arXiv:2512.01809)：GCP 成功不是因为多模态捕获，而是 iterative computation + 训练时适当随机性。一个 2-step regression policy 可匹配 flow GCP 性能。

**推荐实验**：
1. 遵循 Pi0 配置：rank=16, LR=5e-5, cosine decay, 20-30K steps
2. 尝试只 tune action expert（冻结 VLM 部分）
3. 预期：接近 full FT 效果，显存减半；风险：rank=16 可能表达能力不足

---

## 3. Velocity Field 退化修复 / 正则化

### Wasserstein-2 正则化

- **ORW-CFM-W2** (arXiv:2502.06061, ICLR 2025)：推导了 flow matching 中 W2 距离的可计算上界，防止 policy 坍缩为 delta 分布。核心结论：**没有显式正则化，flow matching fine-tuning 极易 collapse**。

### 渐进式 fine-tuning

- **Gradual Fine-Tuning for Flow Matching** (arXiv:2601.22495)：温度控制的 pretrained↔target drift 插值。高温初期惩罚偏离 base model，逐步退火至目标分布。有收敛保证。

### KL 正则化

- **DPOK** (arXiv:2305.16381, NeurIPS 2023)：diffusion 模型 KL-regularized RL fine-tuning 的奠基工作。无 KL 正则化时，模型产生过饱和颜色和非自然形状。
- **FDPP** (arXiv:2501.08259)：将 KL 正则化应用于 robot diffusion policy 的 preference-based RL fine-tuning。

### Noise Consistency Loss

- **Noise Consistency Regularization** (arXiv:2506.06483, CVPR 2025 Workshop)：两个辅助 loss——(1) prior consistency: 非 subject 图像的 noise prediction 需与预训练模型一致；(2) subject consistency: 对 latent code 乘性噪声的鲁棒性。

**推荐实验**：
1. 添加 velocity field KL loss：`L_reg = λ * ||v_lora(x,t) - v_pretrained(x,t)||^2`，λ=0.1~1.0
2. 实现简单：forward 时同时过 pretrained model（frozen）和 LoRA model，加 MSE penalty
3. 预期：保持训练 loss 收敛同时约束 velocity field 不偏离太远；风险：λ 过大会阻碍适应

---

## 4. ODE → SDE 推理：加 Stochasticity 缓解 Mode Collapse

### 训练无关的 ODE→SDE 转换

- **Stochastic Sampling from Deterministic Flow Models** (arXiv:2410.02217, ICLR 2025)：识别出一族与给定 ODE 具有相同 marginal distribution 的 SDE。noise 参数=0 退化为 ODE，正值给出 SDE。需要 flow field + score function。**直接可用：将我们的 collapsed ODE 转为 SDE 以恢复多样性。**

### Temporal Score Rescaling (TSR)

- **TSR** (arXiv:2510.01184)：训练无关方法，重新缩放 score function 控制 "local sampling temperature"。适用于任何现成 diffusion/flow model。在 robot manipulation 上有验证。**作为 quick fix 最快：提高温度恢复多样性。**

### SDE Prefix + ODE Jump

- **Hybrid Consistency Policy (HCP)** (arXiv:2510.26670)：在高噪声区跑短 SDE prefix（~25 步）形成 mode branches，然后一步 ODE consistency jump。在 7-DoF 真实机器人上验证，接近 80-step DDPM teacher 精度，延迟大幅降低。

### VLA 专用

- **pi_RL** (arXiv:2510.25889)：Flow-SDE 将 ODE 转为 SDE 用于 VLA RL 探索。将 pi0 成功率从 57.6% 提升至 97.6% (LIBERO)。
- **ReinFlow** (arXiv:2505.22094, NeurIPS 2025)：注入可学习噪声到 flow 路径，转为离散时间 MDP。locomotion 任务平均奖励增长 135%。

**推荐实验**：
1. 最快方案：在 sample_actions() 的 ODE 积分中加小幅高斯噪声（σ=0.01~0.1），观察 std 恢复
2. 正式方案：实现 arXiv:2410.02217 的 SDE 转换，需估计 score function（可从 velocity field 近似）
3. 预期：action std 恢复到合理范围；风险：噪声过大会产生无意义 action，需精细调节 σ

---

## 5. LoRA 替代方案

### DoRA (Weight-Decomposed Low-Rank Adaptation)

- **arXiv:2402.09353** (ICML 2024 Oral)：将权重分解为 magnitude + direction，LoRA 只更新方向。在 SDXL DreamBooth 上 DoRA >> LoRA（尤其低 rank 时差距最大）。推理无额外开销（可 merge 回去）。**低 rank 场景首选替代。**

### LoRA+ (不同学习率)

- **arXiv:2402.12354** (ICML 2024)：A 和 B 矩阵用不同学习率，free lunch，1-2% 提升 + 2x 收敛加速。

### VeRA (Vector-based Random Matrix Adaptation)

- **arXiv:2310.11454** (ICLR 2024)：所有层共享一对 frozen random 低秩矩阵，只学 per-layer scaling vectors。参数量比 LoRA 少一个数量级，性能持平。

### T-LoRA (Timestep-dependent LoRA)

- **arXiv:2507.05964** (AAAI 2026)：核心发现——**高噪声 timestep 比低噪声 timestep 更容易 overfit**。用 rank masking 限制高噪声 timestep 的 LoRA 组件 + 正交初始化。**直接针对 diffusion LoRA overfitting 问题。**

**推荐实验**：
1. DoRA 替换 LoRA：rank=16, 预期低 rank 下优于 LoRA，无推理开销
2. LoRA+：在当前 LoRA 基础上设 B 矩阵 LR = 2~8x A 矩阵 LR，零成本
3. T-LoRA 思路：对 flow matching 的 timestep 做 rank masking（高 t 用低 rank）
4. 风险：DoRA 需调参（收敛慢于 LoRA）；T-LoRA 需适配 flow matching 的 time scheduling

---

## 6. Over-training 与 Mode Collapse

### 直接证据

- **DRaFT+** (NVIDIA)：原始 DRaFT 容易 reward over-optimization 和 mode collapse，DRaFT+ 加 KL penalty 解决。
- **Model Collapse in Rectified Flow** (arXiv:2412.08175)：首个 rectified flow collapse 的理论分析。在 reflow 中混入 real data 防止 collapse。
- **Catastrophic Forgetting in Diffusion FT** (arXiv:2509.10529)：early stopping 单独 **不能防止遗忘**，需要 weight regularization + loss-weighted mixing + replay buffer。最少需 ~100 步后 early stopping 才有意义。

### 时间步选择性训练

- **HRF** (arXiv:2410.08315)：不是每个 denoising step 都需要 fine-tune。用 sliding window 只 fine-tune 特定 timestep 范围，固定 high-level features，在 low-level features 生成 variation。**选择性 fine-tuning 防止 mode collapse。**

### EMA

- EMA（指数移动平均）是低成本高收益的 anti-collapse 防线。训练不稳定性表现为 mode collapse 或 color bias，EMA 权重产生更稳定的 FID。注意：OpenPI 对 LoRA 训练 **禁用了 EMA**。

**推荐实验**：
1. 在 10K/15K/20K/25K/30K steps 分别 checkpoint，测试 inference diversity，找 collapse 拐点
2. 启用 EMA（decay=0.999），对比 EMA 权重 vs 最终权重的 action std
3. 预期：可能存在 sweet spot（如 15-20K steps）collapse 尚未发生但 loss 已收敛；风险：early stop 可能损失任务性能

---

## 优先级排序：推荐实验方案

| 优先级 | 方案 | 改动量 | 预期效果 | 风险 |
|--------|------|--------|---------|------|
| **P0** | alpha 64→16（scaling 0.5x） | 改 1 个参数 | 大幅缓解 collapse | alpha 过低→适应不足 |
| **P0** | Inference 时 ODE 加微量噪声 σ=0.01~0.05 | 改 sample_actions() | 立即恢复部分 diversity | σ 过大→action 不稳定 |
| **P1** | Checkpoint sweep 找 collapse 拐点 | 无代码改动 | 确定最优训练步数 | 无 |
| **P1** | Velocity field KL regularization | 加 ~10 行 loss | 约束 velocity 不偏离 | λ 调参 |
| **P2** | DoRA 替换 LoRA (rank=16) | 换 adapter 类型 | 低 rank 下更好泛化 | 需重新调参 |
| **P2** | 冻结 VLM，只 tune action expert | 改 freeze 配置 | 减少遗忘 | 可能降低 vision grounding |
| **P3** | T-LoRA timestep-aware rank masking | 中等改动 | 防止高噪声 timestep overfit | 需适配 flow matching |
| **P3** | Cocos condition-dependent noise | 改 training pipeline | 防止 conditioning collapse | 较大改动 |

---

## 参考文献

1. Variational Rectified Flow Matching — arXiv:2502.09616
2. VFP: Variational Flow-Matching Policy — arXiv:2508.01622
3. Conditioning Matters (Cocos) — arXiv:2505.11123 (NeurIPS 2025)
4. Gradual Fine-Tuning for Flow Matching — arXiv:2601.22495
5. Adjoint Matching — arXiv:2409.08861 (ICLR 2025)
6. ORW-CFM-W2 (Wasserstein Regularization) — arXiv:2502.06061 (ICLR 2025)
7. Stochastic Sampling from Deterministic Flow Models — arXiv:2410.02217 (ICLR 2025)
8. Temporal Score Rescaling (TSR) — arXiv:2510.01184
9. Hybrid Consistency Policy (HCP) — arXiv:2510.26670
10. pi_RL — arXiv:2510.25889
11. ReinFlow — arXiv:2505.22094 (NeurIPS 2025)
12. ACG: Action Coherence Guidance — arXiv:2510.22201
13. DoRA — arXiv:2402.09353 (ICML 2024)
14. LoRA+ — arXiv:2402.12354 (ICML 2024)
15. VeRA — arXiv:2310.11454 (ICLR 2024)
16. T-LoRA — arXiv:2507.05964 (AAAI 2026)
17. LoRA vs Full FT: Illusion of Equivalence — arXiv:2410.21228 (NeurIPS 2025)
18. DPOK — arXiv:2305.16381 (NeurIPS 2023)
19. FDPP — arXiv:2501.08259
20. Noise Consistency Regularization — arXiv:2506.06483 (CVPR 2025W)
21. HRF: Avoiding Mode Collapse in RL-FT Diffusion — arXiv:2410.08315
22. Pi0 — arXiv:2410.24164
23. OpenVLA-OFT — arXiv:2502.19645
24. SmolVLA LoRA FT — arXiv:2512.11921
25. Much Ado About Noising — arXiv:2512.01809
26. Model Collapse in Rectified Flow — arXiv:2412.08175
27. CFG-Zero* — arXiv:2503.18886
