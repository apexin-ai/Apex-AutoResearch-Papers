# research verify turn ppo

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-turn-ppo_20260517T120526_result.json`
- **Structured JSON:** [`f2fcbf13348f0fa785de.json`](../../sessions/f2/f2fcbf13348f0fa785de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息充分，下面是结构化报告。

---

## Turn-PPO 竞争分析报告

### 一、基本信息

| 项 | 内容 |
|---|---|
| 标题 | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs |
| 作者 | Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li |
| 日期 | 2025-12-18 提交，2026-01-23 修订 |
| Venue | **EACL 2026** |
| arXiv | 2512.17008，可正常访问 |

---

### 二、核心贡献：GRPO multi-turn instability 分析

他们识别的 GRPO 问题有两个：

1. **Uniform advantage across heterogeneous turns**：GRPO 对一个 episode 内所有 token 施加相同的 advantage，但不同 turn 对最终 reward 贡献不等，导致 credit 分配不准确。
2. **High sampling variance amplification**：环境交互不可控，sample-based advantage 估计在 multi-turn 下方差被放大，训练不稳定。

他们还做了系统性排除实验（Section 3.2）：entropy collapse 缓解、KL removal、batch diversity 增强均无法阻止 GRPO 在难任务上崩溃。

**关键区别**：他们**没有**使用 "advantage sign misattribution" 或 "γ-attenuation" 的概念。他们的诊断框架是 "state representation misalignment" + "uniform advantage"，而非我们的 "sign error"。

---

### 三、与我们诊断的比较

| 维度 | 我们的诊断 | Turn-PPO 的诊断 |
|---|---|---|
| 核心问题命名 | Advantage sign misattribution | Uniform advantage + high variance |
| 具体机制 | (1) Early steps 的 advantage 被 γ-attenuation 削弱到接近零；(2) 失败 episode 中所有 step 获得无差别负 advantage（sign 错误） | 不同 turn 贡献不等但获得相同 advantage；sample-based 估计方差大 |
| 失败模式 | 训练崩溃源于梯度方向错误 | 训练崩溃源于方差和 credit 分配粗糙 |
| 重叠度 | **部分重叠**：都识别了 "uniform advantage across turns" 的问题 | 但未深入分析 sign direction error |

**判断**：问题识别有 ~40-50% 重叠。我们的 sign misattribution 分析更精细（指出 advantage 方向错误而非仅仅是粗糙），他们的分析更偏向方差视角。

---

### 四、解决方案比较

| 维度 | 我们 | Turn-PPO |
|---|---|---|
| 方向 | Episode-level GRPO（更粗粒度） | Turn-level PPO（更细粒度） |
| 算法族 | 仍在 GRPO 框架内 | 切换到 PPO + learned critic |
| Advantage 计算 | Episode-level reward，无 per-step credit | Turn-level GAE（δₕ = rₕ + γvₕ₊₁ - vₕ），learned value function |
| Critic | 无（sample-based） | 有（需额外训练 value network） |
| 关键创新 | 避免 step-level sign error，用 episode reward 直接优化 | Turn-level MDP 重新定义 state/action，整个 response 是一个 action |
| γ/λ 灵活性 | N/A | Turn-level 下 γ=0.99, λ=0.9 可调；token-level 下必须锁定 1.0 否则 early tokens invisible |

**判断**：解决方案方向**完全不同**。他们走向更细粒度的 turn-level credit assignment（PPO + critic），我们走向更粗粒度的 episode-level（GRPO 内部改进，无需 critic）。这是关键差异点。

---

### 五、实验设置

| 项 | Turn-PPO |
|---|---|
| 环境 | WebShop（购物搜索）、Sokoban（空间推理） |
| 模型 | Qwen2.5-3B、Qwen2.5-7B、Qwen3-1.7B |
| Baselines | GRPO、Token-PPO |
| 核心结果 | GRPO 在 Sokoban 和 Qwen3-think 上崩溃；Turn-PPO > Token-PPO > GRPO |

关键数据：
- Sokoban/Qwen2.5-7B: GRPO 崩溃, Token-PPO 2.90, Turn-PPO **3.74**
- WebShop/Qwen3-1.7B(think): GRPO 崩溃, Token-PPO 0.54, Turn-PPO **0.55**

---

### 六、威胁评估

**威胁等级：MEDIUM**

理由：

**重叠点（构成威胁）：**
- 都识别了 GRPO 在 multi-turn 下的训练不稳定/崩溃问题
- 都将问题归因于 advantage 在 turns 间的分配不当
- 都在 agent RL 场景下工作，实验环境可能部分重叠

**差异点（保护 novelty）：**
1. **诊断深度不同**：我们的 sign misattribution 分析（advantage 方向错误 + γ-decay 导致 early step invisible）比他们的 "uniform advantage + variance" 诊断更精细、更有解释力
2. **解决方向相反**：他们 turn-level PPO（更细粒度 + 额外 critic），我们 episode-level GRPO（更粗粒度 + 无 critic）。这是完全不同的技术路线
3. **算法族不同**：他们放弃 GRPO 转向 PPO；我们在 GRPO 框架内修复问题，计算开销更低（无需训练 value network）
4. **他们的 turn-level 方案需要 per-turn reward**，而我们的 episode-level 方案只需 final outcome reward，适用范围更广

**建议行动：**
- 必须在 Related Work 中引用并明确对比
- 强调我们的 sign misattribution 诊断是更深层的因果分析，而非仅仅是 variance/uniformity
- 强调 episode-level GRPO 作为轻量方案的优势（无 critic、无 per-turn reward 需求）
- 如果实验环境有重叠（WebShop），可考虑将 Turn-PPO 作为 baseline

Sources:
- [Turn-PPO arXiv page](https://arxiv.org/abs/2512.17008)
- [Turn-PPO HTML full text](https://arxiv.org/html/2512.17008)
- [HuggingFace paper page](https://huggingface.co/papers/2512.17008)

---
