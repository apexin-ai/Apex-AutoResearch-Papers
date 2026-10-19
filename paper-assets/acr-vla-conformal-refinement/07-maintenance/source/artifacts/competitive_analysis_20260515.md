# Competitive Analysis (2026-05-15)

## 竞品对比表

| 方法 | 核心思路 | LIBERO / LIBERO-Plus 结果 | 与 ACR-VLA 关键差异 | 发表状态 |
|------|---------|--------------------------|---------------------|---------|
| **ACoT-VLA** | EAR (粗粒度参考轨迹) + IAR (latent action priors) 的 action chain-of-thought，联合训练引导 action head | LIBERO 98.5%, LIBERO-Plus **84.1%** (当前 SOTA), VLABench 47.4% | Training-time 方法，需在目标任务上训练 EAR+IAR；无 UQ，部署后不在线适应；与 ACR-VLA 正交互补 | **CVPR 2026** (arXiv:2601.11404) |
| **ReconVLA** | CQR-based scalar uncertainty + SMD state anomaly detection + diffusion 重建 latent gaze regions；从 K 个 action samples 中选最佳 | 长程操作 (block stacking) 达 85%；标准 LIBERO/LIBERO-Plus 具体数值未公开 | Scalar CQR 丢失维度信息；sample selection（非 learned correction）——K 个样本都差时失效；static calibration 不做在线适应 | **AAAI 2026 Outstanding Paper** (arXiv:2604.16677) |
| **SC-VLA** | Sparse World Imagination 预测任务进度 + 未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线纠正 | ManiSkill 平均 ~86% (+9% SR over baselines)，real-world +14%；**未在 LIBERO/LIBERO-Plus 评估** | 需任务级 RL 训练（非 plug-and-play）；无统计保证和 UQ；residual 作用在整个 action vector 无维度选择性 | arXiv:2602.21633 (Feb 2026) |
| **VLA-Pilot** | MLLM verifier + evolutionary diffusion optimizer 的三阶段 inference-time steering，零样本 plug-and-play | OOD 场景 SR 0.50 vs baseline 0.12-0.19；**未在 LIBERO 标准 benchmark 评估** | 推理延迟 2.41s/step 不适合实时；MLLM scoring 为启发式无 calibrated confidence；无统计保证 | arXiv:2511.14178 (Nov 2025) |
| **AsyncVLA** | 异步 flow matching + confidence rater 评估 action token 置信度，选择性 refine 低置信 token | 10% LIBERO-Spatial 数据下 +9.6pp vs SFM；full LIBERO 具体数值未在搜索中找到 | 改进 flow matching 推理过程本身（training-time 架构改动）；非 post-hoc correction；无 conformal guarantee | arXiv:2511.14148 (Nov 2025) |
| **A2C2** | 轻量异步 action chunk correction head，利用最新观测修正已生成的 action chunk | ~+7pp vs RTC baseline；无需重训 base policy | Residual correction 无 UQ conditioning；无维度选择性；correction 基于观测差而非统计不确定性 | arXiv:2509.23224 (2025) |
| **PLD** | Residual RL + scheduled magnitude bound ξ 在 VLA 上做 self-improving | LIBERO 上验证；ICLR 2026 | 需要 RL 训练；magnitude bound 为预设 schedule 而非 data-driven conformal bound | **ICLR 2026** (arXiv:2511.00091) |
| **SRPO** | Self-referential RL post-training for VLA robustness | LIBERO-Plus **82.1%** | Training-time RL 方法；ACR-VLA 旨在 stacking 在其之上进一步提升 | arXiv:2511.15605 (2025) |

## 我们的差异化优势（基于当前实验数据）

### 当前实验数据摘要
- Baseline (K=1): 30% on LIBERO-Spatial
- VLA-mean (K=10 avg): 32%
- Argmin-only selection: ~34%
- **ACR-VLA per-DOF CRM** (K=10, max_norm=0.1): **52.5%** @ 4/10 tasks
- **ACR-VLA obs_only CRM**: **63.3%** @ 3/10 tasks (early, may drop)
- Object benchmark baseline: 13%

### 差异化定位

1. **唯一将 multivariate conformal statistics 作为 learned correction 输入的方法**。所有竞品要么不用 CP（SC-VLA, VLA-Pilot, ACoT-VLA, A2C2, PLD），要么只用 scalar CP（ReconVLA）。ACR-VLA 的 40D 结构化特征（per-DOF std + conformal radius + ellipsoid volume）是当前文献中粒度最细的 action-level UQ。

2. **Learned dimension-selective correction vs. 全局修正/样本选择**。ReconVLA 做 sample selection（上界受限于最佳 sample 质量）；SC-VLA/A2C2/PLD 做全局 residual correction（无维度选择性）。ACR-VLA 的 CRM 可对高不确定 DOF 强纠正，低不确定 DOF 保持原样。

3. **Online coverage adaptation (ACI+COC)**。ReconVLA 使用 static calibration set，分布偏移下 coverage 退化。ACR-VLA 通过 Chunk Overlap Consistency 提供自参考覆盖信号 + ACI 在线更新 threshold，无需外部监督。

4. **与 training-time 方法正交互补**。ACoT-VLA (84.1%) 和 SRPO (82.1%) 是当前 LIBERO-Plus SOTA，但都是 training-time 方法。ACR-VLA 作为 inference-time 模块可叠加使用。

### 当前结果的竞争力评估

ACR-VLA 的 52.5% (4/10 tasks) 在 LIBERO-Spatial 上显著优于自身 baseline (30%)，但与 ACoT-VLA 的 98.5% (full LIBERO) 或 SRPO 的 82.1% (LIBERO-Plus) 不直接可比——这些数值基于更强的 backbone (通常 7B+) 和 full benchmark evaluation。ACR-VLA 使用 SmolVLA (450M) 作为 backbone，重点是证明 **inference-time conformal correction 的增量价值**，而非绝对 SOTA。

**关键叙事策略**: 强调 relative improvement (+22.5pp over baseline) 和 stacking potential（在强 backbone 上的叠加增益），而非绝对数值竞争。

## paper_framing.md 建议更新

### 需要增加的竞品引用

1. **AsyncVLA** (arXiv:2511.14148) — 当前 `literature_map.yaml` 中缺失。AsyncVLA 在 flow matching 推理过程中引入 confidence rater 做选择性 token refinement，是与 ACR-VLA 最接近的 "confidence-guided action refinement" 思路，但在 training-time 层面实现（需修改 VLA 架构），且无 conformal guarantee。建议加入 competitive landscape 作为对比：ACR-VLA 是 post-hoc + conformal + per-DOF，AsyncVLA 是 built-in + heuristic confidence + per-token。

2. **"From Knowing to Doing Precisely"** (arXiv:2602.01811) — self-correction + termination framework for VLA，可能相关但需进一步确认内容。

### positioning 建议调整

1. **paper_framing.md 中 SC-VLA 的描述已准确**，但建议补充其发表状态（目前仍为 arXiv preprint，无顶会录用信息），降低其作为竞品的威胁等级。

2. **ACoT-VLA 的 LIBERO-Plus 84.1% 数据已确认**（CVPR 2026，代码开源），paper_framing.md 中的信息准确无需修改。

3. **ReconVLA 已获 AAAI 2026 Outstanding Paper**，建议在 competitive landscape 中标注此荣誉，凸显我们与之的方法差异（scalar vs per-DOF, selection vs correction, static vs adaptive）的重要性——我们需要令人信服地展示 per-DOF conformal features 相比 scalar CQR 的增量价值。

4. **Gap statement 建议微调**：当前 paper_framing.md 的 Gap 段已覆盖主要竞品，但 AsyncVLA 的 confidence-guided refinement 应作为新增 gap 描述的一部分："AsyncVLA 在 flow matching 内部引入 confidence rater 但需修改 VLA 架构且无 statistical guarantee"。

### 已收录且信息准确的竞品
- ReconVLA ✓ (需补充 AAAI 2026 Outstanding Paper 信息)
- SC-VLA ✓
- VLA-Pilot ✓
- ACoT-VLA ✓
- A2C2 ✓
- SRPO ✓
- PLD ✓
- SAFE ✓

### literature_map.yaml 需新增
- AsyncVLA (arXiv:2511.14148, category: inference_correction, relation: competitor)
