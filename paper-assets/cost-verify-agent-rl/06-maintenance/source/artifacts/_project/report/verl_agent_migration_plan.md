# verl-agent 迁移调研报告

> 日期：2026-05-15  
> 项目：cost-verify-agent-rl (ALFWorld GRPO训练)

---

## 1. verl-agent 是什么

[verl-agent](https://github.com/langfengQ/verl-agent) 是 veRL 的独立扩展，专为 LLM/VLM agent 的 RL 训练设计。作者 Lang Feng，论文 *"Group-in-Group Policy Optimization for LLM Agent Training"* (GiGPO)。后续论文 *"Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks"* (HiGPO) 进一步扩展。

### 核心特性

| 特性 | 说明 |
|------|------|
| **Step-independent multi-turn rollout** | 每步独立构建输入，不做全历史拼接，context 长度近似恒定 |
| **可定制 memory 模块** | 每步可自定义输入结构、历史管理策略 |
| **GiGPO 算法** | 两层分组优势估计：episode-level + step-level anchor state grouping |
| **并行 gym-style 环境** | 支持批量并行环境交互 |
| **asyncio co-routing rollout** | 异步环境交互，避免 GPU 空闲等待 |
| **长 horizon 支持** | ALFWorld 30-50 步无 token 爆炸问题 |

### 支持的环境

ALFWorld, Sokoban, SkyRL-Gym, Search-R1, Gym Cards, WebShop, AppWorld (experimental)

### 依赖

- Python 3.12, vllm==0.11.0, flash-attn==2.7.4.post1
- 基于 verl（推测 v0.7+）

---

## 2. verl 原生 Agent 支持现状

verl v0.7（当前最新 v0.7.1，2026-03-16）已原生支持 agentic RL：

- **AgentLoop 抽象**：可扩展的 agent task loop 定义
- **Server mode rollout**（默认）：LLM server 在线服务，支持 dynamic batching
- **Multi-turn rollout**：asyncio 异步环境交互
- **BaseTool 接口**：自定义环境工具，YAML 配置
- **TransferQueue**（实验性）：解耦控制流和数据流

关键点：verl v0.7 的原生 agent 支持已经覆盖了 RAGEN 的大部分基础设施需求。

---

## 3. RAGEN 当前架构分析

### verl 版本

RAGEN 子模块使用 **verl 0.6.1**（落后 2 个大版本）。

### 核心模块

```
ragen/
├── env/                    # 环境接口层
│   ├── base.py             # BaseEnv / BaseLanguageBasedEnv 抽象
│   ├── alfworld/env.py     # AlfredTXTEnv（我们的主力环境）
│   └── [15+ 其他环境]
├── llm_agent/              # Agent 交互层
│   ├── agent_proxy.py      # LLMAgentProxy - rollout 编排（29KB）
│   ├── ctx_manager.py      # ContextManager - 上下文/token管理（72KB）
│   ├── es_manager.py       # EnvStateManager - 多环境状态管理（22KB）
│   ├── base_llm.py         # ConcurrentLLM wrapper
│   └── memory/             # Memory 模块
├── trainer/                # 训练层
│   ├── agent_trainer.py    # RayAgentTrainer ← VerlRayPPOTrainer（78KB）
│   ├── core_algos.py       # GRPO advantage 计算（定制版）
│   ├── collapse_metrics.py # Reasoning collapse 检测（RAGEN-2 核心贡献）
│   ├── rollout_filter.py   # Rollout 过滤策略（35KB）
│   └── gradient_reporter.py # 梯度分析工具
├── workers/                # 分布式 worker
│   ├── fsdp_workers.py     # FSDP worker 定制
│   ├── actor/              # Actor worker
│   ├── critic/             # Critic worker
│   └── sharding_manager/
└── biavr/                  # 额外模块
```

### RAGEN-2 更新（2026-03-12，ICML 2026 Spotlight）

- 系统研究 reasoning collapse 现象
- 轻量级干预策略（collapse_metrics.py, rollout_filter.py）
- 更稳定的训练流程

---

## 4. RAGEN vs verl-agent 对比

| 维度 | RAGEN (当前) | verl-agent | 评估 |
|------|-------------|------------|------|
| **verl 基础版本** | 0.6.1 (submodule) | ~0.7+ | verl-agent 更新 |
| **vLLM 版本** | 0.8.2 | 0.11.0 | 巨大跳跃 |
| **Rollout 机制** | 全历史拼接 + masking | Step-independent | verl-agent 更高效 |
| **Context 管理** | ContextManager (72KB 巨型类) | 内置 memory 模块 | verl-agent 更模块化 |
| **ALFWorld 支持** | ✅ 自定义实现 | ✅ 原生支持 | 两者都支持 |
| **RL 算法** | GRPO (定制) | GRPO/PPO/DAPO/GSPO/RLOO/GiGPO | verl-agent 更丰富 |
| **Collapse 检测** | ✅ (核心特性) | ❌ | RAGEN 独有 |
| **Rollout 过滤** | ✅ (35KB) | ❌ | RAGEN 独有 |
| **梯度分析** | ✅ | ❌ | RAGEN 独有 |
| **长 horizon 效率** | ~10 turns 有效 | ~50 turns 有效 | verl-agent 大幅领先 |
| **GPU 利用率** | 同步等待环境 | asyncio 异步 | verl-agent 更高效 |

---

## 5. 迁移可行性评估

### 可直接替代的组件

| RAGEN 组件 | verl-agent 替代 | 难度 |
|-----------|----------------|------|
| `ragen/workers/` (FSDP workers) | verl 原生 workers | 低 |
| `ragen/trainer/core_algos.py` (GRPO) | 内置 GRPO/GiGPO | 低 |
| `ragen/llm_agent/es_manager.py` | 内置环境管理 | 中 |
| `ragen/env/base.py` + env 接口 | agent_system/environments/ | 中 |

### 必须保留/移植的组件

| 组件 | 原因 | 移植难度 |
|------|------|---------|
| `collapse_metrics.py` (34KB) | RAGEN-2 核心研究贡献，verl-agent 无此功能 | 中 |
| `rollout_filter.py` (35KB) | 训练稳定性关键组件 | 中 |
| `gradient_reporter.py` (7KB) | 诊断工具，低耦合 | 低 |
| ALFWorld 环境定制（thread-safe cache 等） | 我们的特定修改 | 低-中 |

### 主要障碍

1. **vLLM 版本跳跃 (0.8.2 → 0.11.0)**：API 变更大，可能需要修改所有 vLLM 相关代码
2. **ctx_manager.py 重构**：72KB 的巨型类，深度耦合 RAGEN 的 rollout 机制，迁移到 step-independent 模式是最大工程量
3. **agent_trainer.py 重构**：78KB，大量定制逻辑需要重新映射到 verl-agent 的 trainer
4. **训练稳定性回归**：collapse 检测和 rollout filter 是经过大量实验调优的，集成到新框架后需要重新验证
5. **实验连续性**：当前实验配置（config/*.yaml）格式不兼容，需要全部重写

---

## 6. 迁移路线图（推荐方案 B：渐进式迁移）

### 方案 A：全量迁移到 verl-agent（不推荐）

- 工作量：3-4 周
- 风险：高 — 所有实验配置、定制逻辑需重写
- 收益：最干净的代码库、最新算法、最好的长 horizon 支持

### 方案 B：渐进式迁移（推荐）

分 3 个阶段，每个阶段可独立验证：

#### Phase 1：升级 verl 子模块 (3-5天)

- 将 verl 子模块从 0.6.1 升级到 0.7.1
- 修复所有 API 兼容性问题
- 保持 RAGEN 上层代码不变
- **验证**：现有实验配置能正常运行

#### Phase 2：采用 step-independent rollout (1-2周)

- 重构 ctx_manager.py，采用 verl-agent 的 step-independent 思路
- 改造 agent_proxy.py 使用 asyncio rollout
- 保留 collapse_metrics 和 rollout_filter 作为插件
- **验证**：ALFWorld 训练效果不退化，长 horizon 性能提升

#### Phase 3：算法升级 (3-5天)

- 引入 GiGPO 算法
- 对比 GRPO vs GiGPO 在 ALFWorld 上的表现
- 保留 GRPO 作为 baseline
- **验证**：GiGPO 在 ALFWorld 上的收敛速度和最终性能

### 方案 C：仅 Cherry-pick（最低风险）

- 保持 RAGEN 架构不变
- 只从 verl-agent 移植 GiGPO 算法到 core_algos.py
- 工作量：3-5天
- 风险：低
- 限制：无法获得 step-independent rollout 的效率提升

---

## 7. 风险评估

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| vLLM 版本升级导致训练 bug | 高 | 中 | Phase 1 做充分验证，保留回退路径 |
| ctx_manager 重构引入回归 | 高 | 高 | 新旧对比实验，逐步切换 |
| collapse 检测失效 | 中 | 低 | 保持独立模块，单元测试覆盖 |
| 配置文件不兼容 | 中 | 确定 | 写配置转换脚本 |
| 实验不可复现 | 高 | 中 | 升级前锁定当前最佳 checkpoint |

---

## 8. 推荐方案

**当前阶段推荐方案 C（Cherry-pick GiGPO）**，原因：

1. 当前项目处于活跃实验阶段（已跑 23 个实验），框架大改风险太高
2. GiGPO 的 step-level credit assignment 对 ALFWorld 多步任务有理论优势
3. 工作量可控（3-5天），不影响现有训练流程
4. 积累了 GiGPO 经验后，再决定是否做 Phase 2 的 rollout 重构

**长期（实验结论明确后）建议方案 B**，因为：

- verl 0.6.1 不再维护，迟早要升级
- step-independent rollout 对 ALFWorld 50步任务有显著效率提升
- asyncio rollout 能更好利用 GPU

---

## 参考链接

- [verl-agent GitHub](https://github.com/langfengQ/verl-agent)
- [verl-agent README](https://github.com/langfengQ/verl-agent/blob/master/README.md)
- [GiGPO 论文](https://arxiv.org/abs/2505.10978)
- [HiGPO 论文](https://arxiv.org/abs/2602.22817)
- [verl v0.7 release blog](https://verl.readthedocs.io/en/latest/blog/v0.7.html)
- [verl Agent Loop 文档](https://verl.readthedocs.io/en/latest/advance/agent_loop.html)
- [verl Multi-turn Rollout](https://verl.readthedocs.io/en/latest/sglang_multiturn/multiturn.html)
- [verl Agent/Env RFC #1172](https://github.com/volcengine/verl/issues/1172)
- [RAGEN GitHub](https://github.com/RAGEN-AI/RAGEN)
- [RAGEN-2 论文 (ICML 2026 Spotlight)](https://ragen-ai.github.io/pdf/RAGEN.pdf)
- [Verlog 框架对比](https://agentic-intelligence-lab.org/2025/08/15/technical-post.html)
