# GRPO 替代算法调研报告

> 调研日期：2026-05-14
> 背景：ALFWorld + Qwen3-1.7B，GRPO 遇到 sparse reward collapse（zero-advantage 死锁）和 dense reward gaming

---

## 1. SPEAR — 最推荐 ⭐⭐⭐⭐⭐

**论文**: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
**作者**: Tencent YoutuResearch
**日期**: 2025-09 | **arXiv**: [2509.22601](https://arxiv.org/abs/2509.22601)
**发表**: ICLR 2026
**代码**: [TencentYoutuResearch/SPEAR](https://github.com/TencentYoutuResearch/SPEAR)

### 核心机制

SPEAR 是专门针对 long-horizon sparse-reward agentic 任务的课程式自模仿学习（Self-Imitation Learning）框架。分两阶段：

1. **Exploration 阶段**：用 auxiliary tool-use reward（类似我们的 valid_action_bonus）鼓励广泛探索，同时维持策略熵
2. **Exploitation 阶段**：逐步增强 self-imitation，从 replay buffer 中利用成功轨迹进行 off-policy 更新

关键创新是 **curriculum scheduling**：在前期用 intrinsic reward shaping 促进 tool interaction 探索，收敛后切换到 exploitation 模式利用成功经验。通过 advantage recalibration 和 regularization 防止 off-policy 漂移。

### 如何处理 sparse reward / cold-start

- Replay buffer 存储成功轨迹，即使当前 rollout 全失败也能从历史成功中学习
- Auxiliary tool-use reward 在前期提供信号但通过 curriculum 调度逐步退出，避免 reward gaming
- 渐进式熵控制避免 entropy collapse 和 divergence

### 与 GRPO 的关键区别

- GRPO 是纯 on-policy，每轮只看当前 rollout；SPEAR 引入 replay buffer 做 off-policy 补充
- GRPO 在全组 reward 相同时梯度为零；SPEAR 通过 self-imitation 即使当前 batch 全失败也有学习信号
- SPEAR 是 plug-and-play 的，可以叠加在 GRPO/GiGPO 等基础算法之上

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | 直接在 ALFWorld 上验证过，GRPO 基础上 +16.1% success rate；解决 cold-start；plug-and-play 可叠加到现有 GRPO 管线 |
| **劣势** | 需要维护 replay buffer；额外 10-25% 计算开销；需要调 curriculum schedule 超参 |
| **可行性** | ⭐⭐⭐⭐⭐ 代码开源，直接在 ALFWorld 验证，与我们场景完全匹配 |

---

## 2. GiGPO — 强推荐 ⭐⭐⭐⭐⭐

**论文**: "Group-in-Group Policy Optimization for LLM Agent Training"
**作者**: Lang Feng et al. (NTU)
**日期**: 2025-05 | **arXiv**: [2505.10978](https://arxiv.org/abs/2505.10978)
**发表**: NeurIPS 2025

### 核心机制

GiGPO 引入两层分组结构实现细粒度 credit assignment：

1. **Episode-level (macro)**：与 GRPO 一样，基于完整轨迹组计算相对 advantage
2. **Step-level (micro)**：引入 **anchor state grouping** 机制，通过识别轨迹间重复出现的环境状态，回溯构建 step-level 分组，计算 step 级别的相对 advantage

这样即使 episode reward 全部相同（sparse reward collapse），step-level 的 advantage 仍可能不同，因为不同轨迹在同一状态后采取了不同的 action 导致不同的后续结果。

### 如何处理 sparse reward / cold-start

- Step-level grouping 在 episode reward 相同时仍能区分 action 质量
- 不需要额外的 critic 网络，保持 critic-free 低内存特性
- Anchor state 机制天然适合 ALFWorld 这类有重复中间状态的环境

### 与 GRPO 的关键区别

- GRPO 只有 episode-level advantage，全组同 reward 则梯度消失
- GiGPO 增加 step-level advantage，能在 sparse reward 下提供信号
- 保持 GRPO 的 critic-free、低内存优势

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | ALFWorld 上 GRPO 基础上 +12%；ALFWorld 的状态空间天然适合 anchor state grouping；NeurIPS 2025 发表 |
| **劣势** | 需要实现 anchor state 识别逻辑（适配 ALFWorld state 表示）；论文没看到开源代码 |
| **可行性** | ⭐⭐⭐⭐ 直接在 ALFWorld 验证；但可能需要自己实现 |

---

## 3. SPA-RL — 强推荐 ⭐⭐⭐⭐

**论文**: "SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution"
**作者**: Hanlin Wang et al.
**日期**: 2025-05 | **arXiv**: [2505.20732](https://arxiv.org/abs/2505.20732)
**代码**: [WangHanLinHenry/SPA-RL-Agent](https://github.com/WangHanLinHenry/SPA-RL-Agent)

### 核心机制

SPA-RL 将 sparse 的 final reward 重新分配为 step-wise 的 dense signal：

1. 训练一个 **progress estimator**，预测每步 action 对整体任务完成度的贡献
2. 将 final reward 按 stepwise contribution 分解，每个 step 获得与其对任务进展贡献成比例的奖励
3. 结合 environment grounding signal（action 是否在环境中成功执行）作为辅助信号

### 如何处理 sparse reward / cold-start

- 把 binary final reward 转化为 dense per-step reward，彻底消除 zero-advantage 问题
- Progress estimator 提供 intermediate signal，即使最终失败也能区分好坏 action
- Grounding signal 提供即时反馈（类似我们的 valid_action_bonus 但更系统）

### 与 GRPO 的关键区别

- GRPO 用 group-level episode reward 计算 advantage
- SPA-RL 先将 episode reward 分解为 step reward，再用于 policy optimization
- 需要额外训练 progress estimator（轻量级）

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | 直接在 ALFWorld 验证过，success rate +2.5%，grounding accuracy +1.9%；代码开源；从根本上解决 sparse reward 问题 |
| **劣势** | 需要训练 progress estimator（额外工程量）；进展幅度不如 SPEAR/GiGPO 大 |
| **可行性** | ⭐⭐⭐⭐ 代码开源，ALFWorld 验证过，但增加了 estimator 训练的额外复杂度 |

---

## 4. DAPO — 推荐 ⭐⭐⭐

**论文**: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
**作者**: ByteDance Seed
**日期**: 2025-03 | **arXiv**: [2503.14476](https://arxiv.org/abs/2503.14476)
**代码**: 基于 [verl 框架](https://verl.readthedocs.io/en/latest/algo/dapo.html)

### 核心机制

DAPO 在 GRPO 基础上引入 4 项改进：

1. **Clip-Higher**: 增大 importance sampling ratio 的上界 clip 范围，保持策略多样性，防止 entropy collapse
2. **Dynamic Sampling**: 过滤掉 accuracy=0 和 accuracy=1 的 prompt group（即全失败或全成功的组），只保留有 effective gradient 的组
3. **Token-Level Policy Gradient Loss**: 按 token 而非 sequence 归一化 loss，避免长序列主导梯度
4. **Overlong Reward Shaping**: 对超长回复施加 soft penalty

### 如何处理 sparse reward / cold-start

- **Dynamic Sampling 直接过滤 zero-advantage 组**：accuracy=0 的 group 被跳过，不参与梯度更新
- Clip-Higher 保持探索性，增加在 sparse reward 下找到成功轨迹的概率
- 但核心问题是：如果 success rate 长期为 0%，Dynamic Sampling 会过滤掉所有数据，无法学习

### 与 GRPO 的关键区别

- GRPO 在 zero-advantage group 上计算出零梯度但仍参与更新（浪费计算）；DAPO 直接跳过
- Clip-Higher 相当于在 GRPO 基础上做更激进的探索
- 本质上是 GRPO 的工程改良版，不改变核心算法范式

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | 成熟框架（verl）；工程化好；Clip-Higher 帮助探索 |
| **劣势** | 不解决 cold-start（success=0% 时 Dynamic Sampling 无数据可用）；主要针对 math reasoning 的 long-CoT 设计，非 agent 场景 |
| **可行性** | ⭐⭐⭐ 改动小可快速集成，但未必解决我们的核心问题 |

---

## 5. SAGE — 推荐 ⭐⭐⭐

**论文**: "Self-Hinting Language Models Enhance Reinforcement Learning"
**作者**: Baohao Liao et al.
**日期**: 2026-02 | **arXiv**: [2602.03143](https://arxiv.org/abs/2602.03143)
**代码**: [BaohaoLiao/SAGE](https://github.com/BaohaoLiao/SAGE)

### 核心机制

SAGE 在 GRPO 训练时注入 **privileged hints**（参考解法的提示），增加 rollout 的多样性：

1. 对每个 prompt，模型先生成一个 hint（如解题步骤分解），再基于 (prompt + hint) 生成 solution
2. Hint 不改变 reward 定义，只增加 group 内的 outcome diversity
3. Policy-dependent scheduler：仅在检测到 group reward collapse 时激活 hint
4. 推理时不用 hint，直接用 no-hint policy

### 如何处理 sparse reward / cold-start

- Hint 增加了 within-group outcome diversity，使得原本 reward 全相同的 group 出现差异
- 自适应调度：只在 collapse 发生时注入 hint
- 但依赖于能生成有用 hint 的能力（对 1.7B 小模型可能有限）

### 与 GRPO 的关键区别

- GRPO 的 rollout 全部来自当前 policy
- SAGE 在训练时混入 hint-conditioned rollout 增加多样性
- 推理时完全等价于 GRPO

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | 直接针对 zero-advantage collapse；推理时无额外开销；代码开源 |
| **劣势** | 主要在 math/reasoning benchmark 验证（+2.0 on 3B），未在 ALFWorld 验证；hint 质量依赖模型能力，1.7B 模型可能 hint 质量差；需要设计 ALFWorld 的 hint 格式 |
| **可行性** | ⭐⭐⭐ 思路对口但需要适配 ALFWorld hint 设计 |

---

## 6. HAPO — 参考 ⭐⭐⭐

**论文**: "Hindsight-Anchored Policy Optimization: Turning Failure into Feedback in Sparse Reward Settings"
**作者**: Yuning Wu et al. (Amazon)
**日期**: 2026-03 | **arXiv**: [2603.11321](https://arxiv.org/abs/2603.11321)

### 核心机制

HAPO 用 **Synthetic Success Injection (SSI)**：在失败 rollout 中选择性注入 teacher demonstrations：

1. Thompson sampling 风格的 gating：低置信度/失败模式时注入 teacher demo，高置信度时纯 RL 探索
2. 自动退火：随 policy 改善，teacher 信号自然减弱
3. 渐近一致性：最终收敛到无偏 on-policy gradient

### 如何处理 sparse reward / cold-start

- 直接解决 cold-start：初期用 teacher demo 提供成功信号
- 不像静态 mixed-policy（如 LUFFY）有 distributional bias
- 需要 teacher demonstrations（oracle 轨迹）

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | 理论优美（渐近一致性）；专门解决 sparse reward cold-start |
| **劣势** | 需要 teacher demonstrations（我们有 ReAct prompt 的 oracle 轨迹吗？）；Amazon 论文，无开源代码 |
| **可行性** | ⭐⭐⭐ 如果有 oracle 轨迹可尝试；否则需要先收集 |

---

## 7. GDPO — 参考 ⭐⭐

**论文**: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
**作者**: NVIDIA
**日期**: 2025-01 | **arXiv**: [2601.05242](https://arxiv.org/abs/2601.05242)
**发表**: ICML 2026
**代码**: [NVlabs/GDPO](https://github.com/NVlabs/GDPO)

### 核心机制

GDPO 解决 GRPO 在 **multi-reward** 场景下的 advantage collapse：

- GRPO 对多个 reward 的组合做 group normalization，导致不同 reward 组合被映射到相同 advantage
- GDPO 对每个 reward 独立做 group-wise normalization，再聚合，保留更细粒度的 advantage 区分

### 如何处理 sparse reward / cold-start

- 不直接解决 sparse reward 问题
- 解决的是 multi-reward 组合时的 advantage 分辨率丢失
- 对我们的场景：如果同时用 success_reward + valid_action_bonus，GDPO 能更好地保留两者的信号差异，减少 reward gaming

### ALFWorld 场景评估

| 维度 | 评估 |
|------|------|
| **优势** | 代码开源（NVIDIA）；如果用 multi-reward 可直接替换 GRPO 的 normalization |
| **劣势** | 不解决 single sparse reward 的 cold-start；主要针对 multi-reward 设计 |
| **可行性** | ⭐⭐ 对我们的 multi-reward 设计有帮助，但不是核心解法 |

---

## 推荐排序

### Tier 1: exp015 失败后首选 Plan B

| 排名 | 方法 | 理由 |
|------|------|------|
| **#1** | **SPEAR** | ALFWorld 直接验证 +16.1%；plug-and-play 叠加 GRPO；解决 cold-start 和 reward gaming 两个问题；ICLR 2026；代码开源 |
| **#2** | **GiGPO** | ALFWorld 直接验证 +12%；step-level credit assignment 解决 zero-advantage；NeurIPS 2025；anchor state 机制天然适合 ALFWorld |

### Tier 2: 可与 Tier 1 组合或作为补充

| 排名 | 方法 | 理由 |
|------|------|------|
| **#3** | **SPA-RL** | ALFWorld 验证过；reward redistribution 从根本上解决 sparse reward；可与 SPEAR 正交使用 |
| **#4** | **DAPO** | 工程改进快速可集成（Clip-Higher + Dynamic Sampling）；但不解决 cold-start |

### Tier 3: 特定条件下有用

| 排名 | 方法 | 理由 |
|------|------|------|
| **#5** | **SAGE** | 需要适配 ALFWorld hint 设计，1.7B 小模型 hint 质量存疑 |
| **#6** | **HAPO** | 需要 oracle 轨迹，无开源代码 |
| **#7** | **GDPO** | 只解决 multi-reward normalization，非核心问题 |

### 推荐实施路径

```
exp015 (current GRPO + 调参) 
  → 失败 → SPEAR (在 GRPO 上叠加 self-imitation + curriculum)
    → 不够 → SPEAR + GiGPO (替换 GRPO 为 GiGPO 作为 base optimizer)
      → 仍不够 → SPEAR + GiGPO + SPA-RL (加 progress estimator 做 reward redistribution)
```

最小改动路径：先从 DAPO 的 Clip-Higher + Dynamic Sampling 开始（改几行代码），再叠加 SPEAR 的 replay buffer。
