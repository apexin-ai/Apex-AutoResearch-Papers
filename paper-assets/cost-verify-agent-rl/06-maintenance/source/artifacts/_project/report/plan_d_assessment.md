# Plan D Assessment: GiGPO + Step-level Credit Assignment

> 日期: 2026-05-15 | 项目: cost-verify-agent-rl | 优先级: 最高

## Executive Summary

**推荐方案: GiGPO（方案 A），预计 1-2 天可集成并启动实验。**

理由：(1) 官方实现 verl-agent 与我们的 RAGEN/verl 框架同源，API 高度兼容；(2) 我们的 codebase 已有 `anchor_obs` 全链路采集（env → es_manager → ctx_manager → non_tensor_batch），GiGPO 核心算法可直接插入；(3) 论文报告 ALFWorld 上 GRPO → GiGPO +13.3pp（Qwen2.5-1.5B: 72.8% → 86.1%），与我们的 model size 和 env 直接可比；(4) 改动量 ~250 LOC，不需要额外 forward pass，零 GPU 内存开销增量。

---

## 1. GiGPO (Group-in-Group Policy Optimization)

### 1.1 算法机制

**论文**: [arXiv 2505.10978](https://arxiv.org/abs/2505.10978) (Feng et al., NeurIPS 2025)
**代码**: [github.com/langfengQ/verl-agent](https://github.com/langfengQ/verl-agent)

GiGPO 引入两级 advantage 结构：

1. **Episode-level (macro)**: 与 GRPO 相同，按 task group 归一化 episode return
   - `A^E(τ_i) = (R(τ_i) - mean(R)) / std(R)`

2. **Step-level (micro)**: 通过 anchor state grouping 构建 step-level group
   - **Anchor state**: 同一 task group 下，不同 trajectory 中出现的相同环境状态
   - 按 hashmap 精确匹配（或 SequenceMatcher 相似度匹配）聚类
   - 同一 anchor state 下的 action 构成 step group
   - `A^S(a_t) = (R_t - mean(R_t in group)) / normalization`
   - `R_t = Σ_{k=t}^T γ^{k-t} r_k`（从该步起的折扣回报）

3. **Combined advantage**:
   - `A(a_t) = A^E(τ_i) + ω · A^S(a_t)`，其中 ω = 1.0

**关键特性**：
- Critic-free（无需额外 value network）
- 与 GRPO 相同的 GPU 内存开销
- Anchor state grouping 耗时 ~0.01s/iteration（hashmap lookup）
- Step advantage 计算 ~0.53s/iteration
- 总计 < 0.002% 的 per-iteration 训练时间开销

### 1.2 ALFWorld 实验结果

| Model | GRPO | GiGPO | Δ |
|-------|------|-------|---|
| Qwen2.5-1.5B | 72.8% | 86.1% | **+13.3pp** |
| Qwen2.5-3B | 74.2% | 87.5% | +13.3pp |
| Qwen2.5-7B | 77.6% | 90.2% | +12.6pp |

配置：16 env groups × 8 samples = 128, max 50 steps, LR=1e-6, γ=0.95, KL=0.01, 150 iterations

### 1.3 与当前 RAGEN 框架的集成分析

**已有基础设施（无需修改）**：

| 组件 | 文件 | 状态 |
|------|------|------|
| `anchor_obs` 环境采集 | `env/alfworld/env.py:227` | ✅ 已有，step info 中返回 |
| `anchor_obs` 中间存储 | `llm_agent/es_manager.py:377,381` | ✅ 已有 |
| `anchor_obs` 批次打包 | `llm_agent/ctx_manager.py:1056-1141` | ✅ 已有，写入 `non_tensor_batch["anchor_obs"]` |
| Step reward 分配 | `trainer/step_rewards.py` | ✅ 已有 `assign_step_rewards()` + `compute_step_discounted_returns()` |
| Step-level GRPO advantage | `trainer/core_algos.py` | ✅ 已有 `compute_grpo_step_advantage()` |

**需要新增的代码**：

| 改动 | 文件 | 估计 LOC |
|------|------|----------|
| `build_step_group()` — anchor state 分组 | `trainer/core_algos.py` | ~80 LOC |
| `step_norm_reward()` — step 归一化 advantage | `trainer/core_algos.py` | ~40 LOC |
| `compute_gigpo_outcome_advantage()` — 组合函数 | `trainer/core_algos.py` | ~40 LOC |
| `episode_norm_reward()` — episode 归一化（去重） | `trainer/core_algos.py` | ~50 LOC |
| `compute_advantage()` 新增 GiGPO 分支 | `trainer/agent_trainer.py` | ~30 LOC |
| 配置项 `algorithm.gigpo.*` | YAML config | ~10 LOC |
| **总计** | | **~250 LOC** |

**可直接从 verl-agent 移植的代码**：
- `gigpo/core_gigpo.py` 中的 `build_step_group()`, `step_norm_reward()`, `compute_gigpo_outcome_advantage()`, `episode_norm_reward()` 函数基本可以直接复制，仅需调整 import 和参数命名约定。
- 辅助函数 `to_hashable()`, `are_similar()` 可直接复用。

### 1.4 集成路线

```
Day 1 (4-6h):
  1. 从 verl-agent 复制 core_gigpo.py 核心函数到 ragen/trainer/core_algos.py
  2. 在 compute_advantage() 中添加 GiGPO 分支
  3. 创建 YAML 配置（algorithm.gigpo.step_advantage_w=1.0, gamma=0.95）
  4. 单元测试验证 anchor grouping + advantage 计算正确性

Day 2 (2-4h):
  5. 启动 exp028_gigpo 实验（复用 exp027 的 base checkpoint + hyperparams）
  6. 监控 wandb 指标：step_group_avg_size, step_advantage_magnitude
```

---

## 2. Self-Guide (Co-Evolution of Policy and Internal Reward)

### 2.1 算法机制

**论文**: [arXiv 2604.03098](https://arxiv.org/abs/2604.03098) (Wang et al., 2026)

1. **Self-guidance signal**: 每步生成 action 前，模型先生成一段自然语言评估 `z_t`（"making progress" / "off-track" / "approaching subgoal"）
2. **Internal reward**: `z_t` 映射为标量 `r_t^sg`（+0.1 正面 / 0 中性 / -0.1 负面）
3. **Trajectory reward**: `R(τ) = R_env(τ) + λ(u) · Σ r_t^sg`
4. **Trapezoid schedule**: λ(u) 在 step 0-40 = 0, 40-50 线性增至 1, 50-70 = 1, 70-80 线性降至 0
5. **Co-evolution**: 更好的 policy → 更好的 guidance → 更好的 internal reward → 更好的 policy

### 2.2 ALFWorld 实验结果

| Model | GRPO (baseline) | +Self-Guidance (inference) | +Guidance Reward (full) |
|-------|-----------------|---------------------------|------------------------|
| Qwen3-1.7B | 72.7% | 81.3% | **89.8%** |
| Qwen3-4B | — | — | +8% avg over GRPO |

配置：100 epochs, group size 8, KL=0.01, guidance reward 从 step 40 引入

### 2.3 集成评估

**核心问题：需要额外 forward pass。**

每步 rollout 需要：
1. 生成 self-guidance `z_t`（一次 forward pass）
2. 条件于 `z_t` 生成 action `a_t`（标准 forward pass）

这意味着：
- **Rollout 吞吐量减半**（每步 2x forward pass）
- 需要修改 `LLMAgentProxy` 的 rollout 逻辑，在 action 生成前插入 guidance 生成
- 需要修改 prompt template，将 `z_t` 嵌入 context
- 需要实现 `z_t → scalar reward` 的映射器
- 需要实现 trapezoid schedule

**改动量估算**: ~500-800 LOC
- `llm_agent/agent_proxy.py`: ~200 LOC（guidance 生成 + 条件化 action 生成）
- `trainer/agent_trainer.py`: ~100 LOC（guidance reward 计算 + trapezoid schedule）
- Prompt templates: ~50 LOC
- 新文件 `trainer/self_guide.py`: ~150 LOC（signal → reward 映射，schedule）

**风险**：
- Rollout 速度减半直接影响实验迭代速度
- Guidance 质量依赖于模型能力（Qwen3-1.7B 可能 guidance 质量较低）
- 需要精心调优 trapezoid schedule 参数
- 论文用的 verl-agent 框架，但 Self-Guide 的代码尚未开源

### 2.4 与 B-IAVR 的关系

Self-Guide 与 B-IAVR 是**不同的方法**：
- B-IAVR: 基于 verify 决策 + action-change 信号（外部信号），Lagrangian dual 优化
- Self-Guide: 基于模型自身生成的自然语言评估（内部信号），co-evolution

两者可以互补但**不应同时使用**——都在修改 reward signal，同时叠加会引入复杂交互。

---

## 3. Step-level Credit Assignment 方案对比

### 方案 A: GiGPO Anchor State Grouping

| 维度 | 评估 |
|------|------|
| 改动量 | **~250 LOC**（最小） |
| 兼容性 | **极高**（同 verl 框架，anchor_obs 已采集） |
| 额外计算 | **几乎无**（hashmap + 算术运算） |
| 额外内存 | **零** |
| 预期收益 | **+13pp**（论文直接可比数据） |
| 风险 | **低**（算法已验证，代码可直接移植） |
| 开发时间 | **1-2 天** |

### 方案 B: TD-based (GAE)

| 维度 | 评估 |
|------|------|
| 改动量 | ~300-400 LOC |
| 兼容性 | 中等（需要 critic/value network） |
| 额外计算 | **高**（需要训练 value network） |
| 额外内存 | **高**（value network 参数 + optimizer states） |
| 预期收益 | 不确定 |
| 风险 | **高**（bi-level GAE 已在 core_algos.py 中实现但未验证） |
| 开发时间 | 3-5 天 |

注：`compute_bi_level_gae_advantage_return` 已在 `core_algos.py` 中实现（by Kangrui Wang），但需要 critic worker，当前 pipeline 在 GRPO 模式下不启动 critic。

### 方案 C: Heuristic (Invalid Action Penalty)

| 维度 | 评估 |
|------|------|
| 改动量 | **已实现**（`step_rewards.py` + `compute_grpo_step_advantage`） |
| 兼容性 | **已集成** |
| 额外计算 | 无 |
| 预期收益 | **低**（仅惩罚无效 action，不提供正向信号） |
| 风险 | **低**（但效果有限） |
| 开发时间 | 0（已完成） |

这实际上就是 exp026 step_independent 模式已经在做的事情。效果有限因为：
- 仅在无效 action 时给负信号（-0.1），有效 action 时为 0
- 不区分"好的有效 action"和"无用的有效 action"
- 不解决 all-zero reward group 的梯度消失问题

### 方案 D: Self-Guide Internal Reward

| 维度 | 评估 |
|------|------|
| 改动量 | ~500-800 LOC |
| 兼容性 | 中等（需要修改 rollout pipeline） |
| 额外计算 | **高**（2x forward pass per step） |
| 额外内存 | 低（无额外模型） |
| 预期收益 | **+17pp**（论文数据，但 Qwen3-1.7B） |
| 风险 | **中高**（未开源，rollout 速度减半，guidance 质量不确定） |
| 开发时间 | 5-7 天 |

---

## 4. 推荐实现路线图

### Phase 1: GiGPO 集成（Day 1-2）⚡ 最高优先级

```
Step 1: 移植核心算法 (4h)
├── 从 verl-agent/gigpo/core_gigpo.py 复制函数
├── 适配到 ragen/trainer/core_algos.py
├── 添加 to_hashable(), build_step_group(), step_norm_reward()
├── 添加 episode_norm_reward(), compute_gigpo_outcome_advantage()
└── 单元测试

Step 2: 集成到训练循环 (2h)
├── compute_advantage() 添加 GiGPO 分支
├── 验证 non_tensor_batch["anchor_obs"] 正确传递
├── 创建配置 YAML
└── 端到端 dry run

Step 3: 启动实验 (1h)
├── exp028_gigpo 配置
├── base: SFT v4 checkpoint
├── hyperparams: ω=1.0, γ=0.95, LR=5e-7
└── 监控 wandb 指标
```

### Phase 2: 增强型 Heuristic（可选，与 Phase 1 并行）

在 GiGPO 基础上，增强 step reward：
- 除了 invalid action penalty，增加 progress-based signal（ALFWorld 的 admissible actions 变化作为 proxy）
- 这不需要额外 forward pass，仅在 `assign_step_rewards()` 中增加逻辑

### Phase 3: Self-Guide（仅在 GiGPO 效果不够时考虑）

如果 GiGPO 未能突破 40% 瓶颈，再考虑 Self-Guide。但预计 GiGPO 应该足够。

---

## 5. GPU 预算估算

### GiGPO 实验

| 项目 | 估算 |
|------|------|
| GPU 配置 | 2× RTX PRO 6000 (cuda:0, cuda:1) |
| 每 iteration 时间 | ~相同于当前 GRPO（GiGPO 计算开销 < 0.002%） |
| 训练 iterations | 100-150 |
| 预计训练时长 | 与 exp027 相同（约 X 小时） |
| 额外内存开销 | 0（critic-free） |

**GiGPO 的最大优势是零额外 GPU 成本。**

### Self-Guide 实验（如果需要）

| 项目 | 估算 |
|------|------|
| 每 iteration 时间 | ~2x 当前（双 forward pass） |
| 额外内存 | 无（复用同一模型） |
| 预计训练时长 | 2x exp027 |

---

## 6. 风险与 Mitigation

### GiGPO 风险

| 风险 | 概率 | 影响 | Mitigation |
|------|------|------|------------|
| Anchor state 重复率低（grouping 不充分） | 中 | 中 | ALFWorld 天然有状态重复（房间导航），论文验证过。启用 `enable_similarity=True` + `similarity_thresh=0.9` 增加匹配 |
| 与我们的 step_independent 模式冲突 | 低 | 低 | GiGPO 替代 step_independent 的 advantage 计算，不冲突 |
| verl 版本不兼容 | 低 | 中 | 核心算法仅依赖 numpy + torch 基础操作，不依赖 verl 特定 API |

### Self-Guide 风险

| 风险 | 概率 | 影响 | Mitigation |
|------|------|------|------------|
| Qwen3-1.7B guidance 质量差 | 中高 | 高 | 论文用 Qwen3-1.7B 在 ALFWorld 验证过，但 Self-Guide 训练初期 guidance 可能不可靠 |
| Rollout 速度减半 | 确定 | 中 | 无法 mitigate，是 fundamental trade-off |
| Trapezoid schedule 需要精调 | 中 | 中 | 按论文默认值开始 |

---

## 7. 关键结论

1. **GiGPO 是最优选择**：改动最小（~250 LOC）、与现有基础设施完美契合（anchor_obs 已采集）、零额外 GPU 成本、论文有直接可比的 ALFWorld 数据（+13pp）。

2. **Self-Guide 是 fallback 方案**：虽然效果可能更好（+17pp），但开发成本高 5x、rollout 速度减半、代码未开源需要从头实现。

3. **Heuristic step reward 已到上限**：当前的 invalid action penalty 是最简单的 step signal，但缺乏正向 guidance。GiGPO 的 anchor state grouping 从根本上解决了"同一状态下哪个 action 更好"的问题。

4. **两种方案可串行尝试**：先跑 GiGPO（1-2 天），如果效果达到 40%+ success rate，则不需要 Self-Guide。如果 GiGPO 仅提升到 20-30%，再考虑叠加 Self-Guide 或切换到 Self-Guide。

---

## References

- [GiGPO Paper](https://arxiv.org/abs/2505.10978) — Feng et al., NeurIPS 2025
- [verl-agent (GiGPO Official Code)](https://github.com/langfengQ/verl-agent)
- [GiGPO Implementation](https://github.com/langfengQ/verl-agent/tree/master/gigpo)
- [Self-Guide Paper](https://arxiv.org/abs/2604.03098) — Wang et al., 2026
- [GiGPO PDF](https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf)
- [Self-Guide HTML](https://arxiv.org/html/2604.03098)
