# ManiSkill3 + World Model RL 文献调研

> 调研日期：2026-05-16

---

## 1. DreamerV3 / World Model RL 在 ManiSkill3 上的已知结果

**核心发现：目前没有公开的 DreamerV3 在 ManiSkill3 上的 benchmark 结果。**

### ManiSkill3 官方 Baselines（RSS 2025）

ManiSkill3 论文（[Gu et al., 2024](https://arxiv.org/abs/2410.00425)）提供以下 baseline：

| 类别 | 算法 | 备注 |
|------|------|------|
| Model-Free RL | PPO, SAC | GPU 并行，wall-time efficient |
| Model-Based RL | TD-MPC2 | 唯一的 model-based baseline |
| Online IL | RFCL, RLPD | RFCL 是 sparse reward 最强 baseline |
| Offline IL | BC, Diffusion Policy | 含 Octo, RDT-1B 等 VLA |

**关键性能数据：**
- **PickCube (PPO, state)**: ~100% success rate，训练 ~1 min（RTX 4090）
- **PickCube (PPO, RGB)**: ~100%，训练 ~10 min
- **PegInsertionSide (PPO)**: solved in ~1 hour
- **PegInsertionSide (RFCL)**: solved from 5 demos in <60 min，sparse reward
- **TD-MPC2**: struggles with sparse reward tasks，在 long-horizon manipulation 上几乎无法学习

**空白：** DreamerV3 不在 ManiSkill3 官方 baseline 中。这意味着：
1. 我们的工作填补了 world model RL 在 ManiSkill3 上的评估空白
2. TD-MPC2 是唯一可对比的 model-based 方法
3. TD-MPC2 在 sparse reward 上的失败为 event-gated horizon 提供了 motivation

### TD-MPC2 参考性能（ManiSkill2）

TD-MPC2（[Hansen et al., 2024](https://arxiv.org/abs/2310.16828)）在 ManiSkill2 上报告了 104 个 continuous control task 的结果，包括 Pick YCB（>60% success rate）。但在 ManiSkill3 的 sparse reward 长 horizon 任务上表现不佳。

---

## 2. World Model RL + Manipulation 近期工作（2024-2026）

### 核心论文列表

| 论文 | 年份/Venue | 方法 | 关键结果 |
|------|-----------|------|---------|
| **DreamerV3** ([Hafner et al.](https://www.nature.com/articles/s41586-025-08744-2)) | 2025 / Nature | RSSM world model + imagination | 150+ tasks，DMC manipulation 达 SOTA，但未测 ManiSkill |
| **HarmonyDream** ([Ma et al.](https://arxiv.org/abs/2310.00344)) | 2024 / ICML | Task harmonization in world models | visual robotic tasks +10%-69%，Atari 100K SOTA |
| **DiWA** ([Chandra et al.](https://arxiv.org/abs/2508.03645)) | 2025 / CoRL | Frozen world model + diffusion policy RL fine-tuning | CALVIN benchmark 8 tasks 全面提升，orders of magnitude fewer interactions |
| **World4RL** ([Jiang et al.](https://arxiv.org/abs/2509.19080)) | 2025 / arXiv | Diffusion world model + end-to-end policy optimization | simulation +16%, real robot +25% success rate |
| **DreamTacVLA** ([2024](https://arxiv.org/html/2512.23864v3)) | 2024 | Tactile world model for contact-rich manipulation | 触觉感知填补 VLA 在接触任务的空白 |
| **World-Gymnast** (Quevedo et al., 2025) | 2025 | RL inside video world model | 超越 supervised fine-tuning 和 software simulators |
| **UniSim** (Yang et al., 2024) | 2024 | RL in learned visual simulator | 建立 learned simulator + reward generation 范式 |

### 趋势与挑战

**趋势：**
- World model 从 planning-only → 直接 policy optimization（World4RL, DiWA）
- Diffusion model 替代 RSSM 作为 world model backbone（更高 fidelity）
- Video generation model → action-conditioned world model 的转化（World-Gymnast）
- 从 online 到 offline：frozen world model 做 policy refinement 成为主流

**Manipulation 特有挑战：**
1. **Contact-rich dynamics**: 接触力学难以建模，world model prediction error 在接触瞬间急剧增大
2. **Multi-modal action distributions**: manipulation 动作空间异构（position, rotation, gripper），难以统一建模
3. **Sparse reward + long horizon**: TD-MPC2 等 model-based 方法在此设置下几乎失效
4. **Tactile gap**: 多数 world model 缺乏触觉建模，在 insertion、deformable object 任务失败

### 综合调研来源

"World Model for Robot Learning: A Comprehensive Survey"（[NTU MARS, 2025](https://arxiv.org/html/2605.00080v1)）覆盖至 2026-03-31，是当前最全面的 robot world model 综述。"A Step Toward World Models: A Survey on Robotic Manipulation"（[arXiv 2511.02097](https://arxiv.org/html/2511.02097v2)）聚焦 manipulation。

---

## 3. Temporal Abstraction 在 Manipulation 中的讨论

### 直接相关论文

| 论文 | 年份/Venue | 核心贡献 | 与本项目关系 |
|------|-----------|---------|------------|
| **THICK** ([Gumbsch et al.](https://openreview.net/forum?id=TjCDNssXKU)) | 2024 / ICLR | Hierarchical world model，自动发现 temporal abstraction | 低层 sparse update + 高层预测 context change，与 event-gated 机制直接对应 |
| **"When to Re-Commit"** ([arXiv 2605.09860](https://arxiv.org/abs/2605.09860)) | 2025 | Commitment depth 作为 learnable state-conditioned variable | +12.5pp solve rate，~25% fewer actions；验证了 adaptive vs fixed depth |
| **Emergent Temporal Abstractions** ([arXiv 2512.20605](https://arxiv.org/abs/2512.20605)) | 2024 | Autoregressive model 中涌现 temporal abstraction | higher-order controllers 可 sparse switch，改善 exploration + credit assignment |
| **VTS-RL / MOSEAC** ([arXiv 2407.00290](https://arxiv.org/html/2407.00290v1)) | 2024 / RLC | Action duration 集成到 action space | 减少计算量，task-dependent optimal frequency |
| **Semantic Temporal Abstraction** ([ICLR 2025](https://openreview.net/forum?id=zY37C8d6bS)) | 2025 / ICLR | VLM-guided temporal abstraction | 语义层面发现 temporally extended skills |
| **Autoregressive Action Sequence** ([arXiv 2410.03132](https://arxiv.org/abs/2410.03132)) | 2024 | Variable-length action chunk prediction (CCT) | 支持不同 control frequency 的 manipulation tasks |

### Manipulation vs Locomotion 的已知差异

1. **Phase structure**: Manipulation 有明确的 phase 切换（approach → contact → manipulation → release），locomotion 是周期性 gait。这意味着 manipulation 更适合 event-gated 而非 fixed-rate temporal abstraction。
2. **Contact discontinuity**: 接触/脱离瞬间 dynamics 突变，固定 action repeat 在此处要么太慢（错过接触）要么太快（浪费 free-space navigation 时间）。
3. **Precision vs speed trade-off**: Manipulation 在 free space 需要快速移动（长 horizon），在接触阶段需要精细控制（短 horizon）。Locomotion 的这种差异小得多。
4. **Optimal commitment depth is state-dependent**: "When to Re-Commit" 的核心发现——fixed depth 在 locally optimal depth 变化时次优——直接适用于 manipulation 的 phase-switching 特性。

### 关键 insight

THICK 的 "invariant context kernel" 概念与我们的 event-gated mechanism 高度相关：低层状态在 context 不变时保持（长 action repeat），只在 context change 时触发更新（短 action repeat）。区别在于 THICK 是在 world model 内部学习层次结构，而我们是在 action selection 层面做 event-gated horizon adaptation。

---

## 4. 对本项目实验设计的 Implications

### 支持我们 hypothesis 的发现

1. **TD-MPC2 在 ManiSkill3 sparse reward 上的失败** → 说明 naive model-based RL 不够，需要额外的 temporal structure
2. **THICK 的成功** → 验证了 adaptive temporal abstraction 能改善 MBRL
3. **"When to Re-Commit" 的 state-conditioned depth** → 直接支持 event-gated（而非 fixed）action repeat
4. **没有 DreamerV3 在 ManiSkill3 上的结果** → 我们填补空白，且可同时展示 vanilla DreamerV3 baseline 和 event-gated 改进
5. **Manipulation 的 phase structure** → 天然适合 event-gated 机制（approach / contact / manipulation / release phases 需要不同 temporal resolution）

### 挑战我们 hypothesis 的发现

1. **DreamerV3 声称 single configuration 跨所有 domain** → 如果 DreamerV3 自身已能处理 temporal variation，event-gated 的 marginal gain 可能有限
2. **Diffusion-based world model 趋势** → RSSM-based DreamerV3 可能不是最优 backbone，但改动太大超出 scope
3. **PPO/RFCL 在 ManiSkill3 上已很强** → 需要选择 PPO/RFCL 难以解决的任务来展示优势（如 long-horizon + sparse reward）

### 实验设计建议

- **Task 选择**: 优先选 PegInsertionSide、PlugCharger 等有明确 phase transition 的任务（PPO 需 1h+，TD-MPC2 失败）
- **Baseline**: DreamerV3 (fixed action repeat) vs DreamerV3 + event-gated vs TD-MPC2 vs PPO
- **Reward setting**: 同时测 dense 和 sparse，展示 event-gated 在 sparse reward 下的优势更显著
- **Metrics**: success rate, sample efficiency, wall-time, 以及 learned action repeat 的可视化（展示自动发现 phase structure）

---

## 5. 推荐加入 literature_map.yaml 的论文

```yaml
papers:
  - paper_id: maniskill3_2024
    title: "ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI"
    authors: "Gu et al."
    year: 2024
    venue: RSS 2025
    category: benchmark
    role: experiment_platform

  - paper_id: dreamerv3_2023
    title: "Mastering Diverse Domains through World Models"
    authors: "Hafner et al."
    year: 2023
    venue: Nature 2025
    category: world_model_rl
    role: base_method

  - paper_id: tdmpc2_2024
    title: "TD-MPC2: Scalable, Robust World Models for Continuous Control"
    authors: "Hansen et al."
    year: 2024
    venue: ICLR 2024
    category: world_model_rl
    role: baseline

  - paper_id: thick_2024
    title: "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
    authors: "Gumbsch et al."
    year: 2024
    venue: ICLR 2024
    category: temporal_abstraction
    role: related_method

  - paper_id: when_to_recommit_2025
    title: "When to Re-Commit: Temporal Abstraction Discovery for Long-Horizon Vision-Language Reasoning"
    authors: "Anonymous"
    year: 2025
    venue: arXiv
    category: temporal_abstraction
    role: motivation

  - paper_id: harmonydream_2024
    title: "HarmonyDream: Task Harmonization Inside World Models"
    authors: "Ma et al."
    year: 2024
    venue: ICML 2024
    category: world_model_rl
    role: related_method

  - paper_id: diwa_2025
    title: "DiWA: Diffusion Policy Adaptation with World Models"
    authors: "Chandra et al."
    year: 2025
    venue: CoRL 2025
    category: world_model_manipulation
    role: related_work

  - paper_id: world4rl_2025
    title: "World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation"
    authors: "Jiang et al."
    year: 2025
    venue: arXiv
    category: world_model_manipulation
    role: related_work

  - paper_id: rfcl_2024
    title: "Reverse Forward Curriculum Learning for Extreme Sample and Demonstration Efficiency in Reinforcement Learning"
    authors: "Tao Stone et al."
    year: 2024
    venue: ICLR 2024
    category: manipulation_rl
    role: baseline

  - paper_id: emergent_temporal_2024
    title: "Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical Reinforcement Learning"
    authors: "Anonymous"
    year: 2024
    venue: arXiv
    category: temporal_abstraction
    role: related_method

  - paper_id: vts_rl_2024
    title: "Variable Time Step Reinforcement Learning for Robotic Applications"
    authors: "Anonymous"
    year: 2024
    venue: RLC 2024
    category: temporal_abstraction
    role: related_method

  - paper_id: wm_robot_survey_2025
    title: "World Model for Robot Learning: A Comprehensive Survey"
    authors: "NTU MARS"
    year: 2025
    venue: arXiv
    category: survey
    role: context

  - paper_id: dreamtacvla_2024
    title: "Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation"
    authors: "Anonymous"
    year: 2024
    venue: arXiv
    category: world_model_manipulation
    role: related_work

  - paper_id: semantic_temporal_abstraction_2025
    title: "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning"
    authors: "Anonymous"
    year: 2025
    venue: ICLR 2025
    category: temporal_abstraction
    role: related_method
```
