# research related work audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-audit_20260518T135805_result.json`
- **Structured JSON:** [`bf9033ae0ce2cdd506a3.json`](../../sessions/bf/bf9033ae0ce2cdd506a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。现在编译分析报告。

---

## 已引用论文清单

**Temporal Abstraction 段落 (14篇):**
- Sutton et al. 1999 (Options framework)
- Sharma et al. 2017 (FiGAR)
- Biedenkapp et al. 2021 (TempoRL)
- Lakshminarayanan et al. 2017 (Dynamic action repetition)
- Hafner et al. 2020/2021/2023/2025 (DreamerV1/V2/V3/V4)
- Micheli et al. 2023 (IRIS)
- Robine et al. 2023 (TWM)
- Gumbsch et al. 2024 (THICK)
- Mattes et al. 2024 (Hieros)
- Li et al. 2025 (LS-Imagine)
- Shaj et al. 2023 (MTS3)

**TAWM 段落 (2篇):**
- Nhu et al. 2025 (TAWM)
- Hansen et al. 2024 (TD-MPC2)

**Value Overestimation 段落 (10篇):**
- Thrun & Schwartz 1993, van Hasselt et al. 2016 (Double Q), Fujimoto et al. 2018 (TD3), Haarnoja et al. 2018 (SAC), Chen et al. 2021 (REDQ)
- Janner et al. 2019 (MBPO), Yu et al. 2020 (MOPO), Lu et al. 2018 (Non-delusional)
- Tallec et al. 2019 (Time discretization)

**Model Fidelity 段落 (5篇):**
- Lambert et al. 2020 (Objective mismatch), Asadi et al. 2019, Lambert et al. 2022 (Compounding error)
- Ma et al. 2024 (HarmonyDream)
- Palenicek et al. 2025, Frauenknecht et al. 2025 (Rollout diminishing returns)

**Network Capacity 段落 (5篇):**
- Nikishin et al. 2022 (Primacy bias), Lyle et al. 2022 (Capacity loss), Nikishin et al. 2023 (Plasticity injection)
- Henderson et al. 2018, Engstrom et al. 2020, Andrychowicz et al. 2021

---

## 搜索发现的相关但未引用论文

### 直接相关（建议添加）

**1. Nauman et al., "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning" (ICML 2024)**
- 相关性: **直接相关**
- 与本文关系: 系统性研究 overestimation、overfitting、plasticity loss 三者的耦合关系。对 60+ off-policy agent 进行消融实验，发现适当 regularization 同时缓解三个问题。这与本文将 CIVO（value overestimation）和 seed-dependent divergence（plasticity/capacity）联系起来的分析高度吻合。审稿人极有可能要求引用此文。
- 建议添加位置: **Value Overestimation 段落**末尾或 **Network Capacity 段落**，作为连接 overestimation 与 plasticity 的桥梁文献。

**2. TD-M(PC)² (2025, arXiv 2502.03550)**
- 相关性: **直接相关**
- 与本文关系: 发现并证明 TD-MPC2 中 planner 和 learned policy prior 之间的 structural policy mismatch 导致持续性 value overestimation。由于 TAWM 基于 TD-MPC2，而本文的核心对比就是 TAWM（MPC re-planning）vs DreamerV3（imagination loop）在 overestimation 上的差异，该工作提供了 TD-MPC2 一侧 overestimation 机制的详细分析，有力支撑本文的 "MPC re-plans from real states so errors don't compound into critic" 的论点。
- 建议添加位置: **TAWM 段落**，在讨论 TAWM 与 DreamerV3 架构差异时引用。

**3. "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning" (NeurIPS 2024)**
- 相关性: **直接相关**
- 与本文关系: 已引用 Nikishin 2022/2023 和 Lyle 2022，但缺少 2024 NeurIPS 上的最新 plasticity 研究。该文将 plasticity loss 研究从 off-policy 扩展到 on-policy 场景，提供更全面的理论视角。
- 建议添加位置: **Network Capacity 段落**，与 Nikishin 2022/2023 并列。

**4. "Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn" (ICML 2025)**
- 相关性: **直接相关**
- 与本文关系: 通过 Neural Tangent Kernel (NTK) 矩阵的 rank 下降解释 plasticity loss 的机制，提出 churn 作为 plasticity loss 的直接度量。为本文的 seed-dependent CIVO 现象提供了更精细的机制解释。
- 建议添加位置: **Network Capacity 段落**。

### 间接相关（可考虑添加）

**5. MuDreamer (Burchi & Timofte, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 移除 DreamerV3 的 pixel reconstruction loss，改用 value function + action prediction。与本文 gradient decomposition 中 observation decoder channel 只占 16-22% 但承载关键 Δt spatial information 的发现形成有趣对照：如果去掉 reconstruction，Δt conditioning 的信息传播路径会完全不同。
- 建议添加位置: **Temporal Abstraction 段落**，作为 DreamerV3 变体之一提及。

**6. "Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective" (arXiv 2404.16078)**
- 相关性: 间接相关
- 与本文关系: 从概率角度形式化分层时间抽象 world model，提出 Hidden-Parameter SSMs 和 Multi-Time Scale SSMs。已引用 THICK 和 MTS3，此文是同方向的理论补充。
- 建议添加位置: **Temporal Abstraction 段落**，与 THICK 和 MTS3 并列。

**7. Diffusion World Model (DWM, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 用 diffusion model 一次性预测多步未来状态，回避 step-by-step rollout 的 compounding error。与本文 compounding error 段落讨论的问题直接相关，但方法路线完全不同（offline RL）。
- 建议添加位置: **Model Fidelity 段落**，可一句话提及作为非自回归方案对比。

**8. MACURA / Lenz et al. 2025 "Trust the Model Where It Trusts Itself"**
- 相关性: 间接相关
- 与本文关系: 基于模型不确定性自适应调整 rollout 长度。已在 bib 中（lenz2025macura），但未在 related work 引用。与 Frauenknecht et al. 2025 主题接近。
- 建议添加位置: **Model Fidelity 段落**，与 Frauenknecht et al. 并列。

---

## TAWM 引用验证

当前 bib 条目：
```bibtex
@inproceedings{nhu2025tawm,
  title = {Time-Aware World Model for Adaptive Prediction and Control},
  author = {Nhu, A.N and Son, S and Lin, M.C},
  year = {2025},
  booktitle = {International Conference on Machine Learning},
  eprint = {2506.08441},
  archivePrefix = {arXiv},
}
```

验证结果：
- **Title**: 正确 ✓
- **Authors**: Anh N. Nhu, Sanghyun Son, Ming C. Lin (University of Maryland) ✓
- **Venue**: ICML 2025 ✓ (已通过 OpenReview 和 ICML 2025 schedule 确认)
- **arXiv ID**: 2506.08441 ✓
- **Year**: 2025 ✓

TAWM 引用信息全部准确，无需修改。

---

## 总结建议

**必须添加（2篇）：**
1. **Nauman et al. (ICML 2024)** — 审稿人最可能指出的遗漏。该文是 2024 年 overestimation + plasticity 交叉研究的标杆，与本文横跨 Value Overestimation 和 Network Capacity 两个段落的主题高度重合。
2. **TD-M(PC)² (2025)** — 本文花了整段讨论 TAWM/TD-MPC2 vs DreamerV3 的架构对比，引用在 TD-MPC2 上发现 overestimation 问题的最新工作能强化论证。

**强烈建议添加（2篇）：**
3. **NeurIPS 2024 plasticity study** — 补全 plasticity 文献的时效性
4. **ICML 2025 churn-based plasticity** — 最新 plasticity 机制研究

**可选添加（4篇）：**
5-8. MuDreamer、Probabilistic hierarchical WM、DWM、MACURA — 根据页数空间决定

---
