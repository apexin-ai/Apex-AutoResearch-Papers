# Phase B Code Readiness Report: B-IAVR

> 分析日期: 2026-05-16 | 分析对象: `/root/cost-verify-agent-rl/RAGEN/`

---

## 1. 当前代码结构摘要（Phase B 相关模块）

### 1.1 已有 B-IAVR 模块 (`ragen/biavr/`)

| 文件 | 行数 | 功能 | 状态 |
|------|------|------|------|
| `reward.py` | 92 | `biavr_reward()`, `lagrangian_update()`, `BIAVRTracker` | 完整 |
| `verify_mechanism.py` | 72 | `parse_verify_token()`, `build_biavr_system_prompt()`, `extract_action_from_response()` | 完整 |
| `action_canonicalize.py` | 62 | ALFWorld action 规范化 (`canonicalize_action`, `actions_equivalent`) | 完整 |
| `pre_action.py` | 60 | a_pre 反事实 action 生成 (`build_pre_action_messages`, `compare_actions`) | 完整 |
| `tests/test_biavr.py` | ~520 | 全面单元测试（action canonicalize, reward, verify parsing, integration patterns） | 完整 |

### 1.2 已集成的宿主模块

| 文件 | 行数 | Phase B 集成点 |
|------|------|-------------|
| `ragen/llm_agent/agent_proxy.py` | 694 | BIAVRTracker 初始化 (L203-214), rollout 循环中 verify 跟踪 (L296-308), biavr_reward 注入 (L327-378), a_pre 生成 (L380-500) |
| `ragen/llm_agent/ctx_manager.py` | 1864 | `biavr_enabled` 属性 (L113), B-IAVR format prompt (L563), `<VERIFY>` 解析 (L1619-1630), 推理时无强制前缀 (L645) |
| `ragen/trainer/agent_trainer.py` | 1705 | biavr metrics 日志 + lambda 更新 (L1205-1210) |
| `ragen/trainer/step_rewards.py` | 109 | 未直接集成 biavr（biavr 通过 history turn reward 注入） |

### 1.3 配置文件

| 文件 | 功能 |
|------|------|
| `config/_alfworld_phase_b.yaml` | 完整 Phase B 训练配置（biavr 参数、AlfworldBIAVR env tag） |
| `config/envs.yaml` L451+ | `AlfworldBIAVR` env tag 定义（含 B-IAVR 系统 prompt） |

---

## 2. Phase B 需要改动的具体文件和函数

### 2.1 无需改动（已完成）

| 文件 | 函数/区域 | 说明 |
|------|----------|------|
| `ragen/biavr/*` | 全部 | 核心 B-IAVR 逻辑完整 |
| `agent_proxy.py` | `__init__`, `rollout`, `_inject_biavr_rewards`, `_build_a_pre_inputs`, `_compute_and_update_a_pre`, `_generate_a_pre_greedy` | B-IAVR rollout 集成完整 |
| `ctx_manager.py` | `biavr_enabled`, `_build_format_prompt`, `get_env_inputs` | prompt 构造 + response 解析完整 |
| `agent_trainer.py` | 训练循环中 biavr metrics | 日志+lambda更新已接入 |
| `config/_alfworld_phase_b.yaml` | 全部 | 训练配置就绪（model_path 待填） |

### 2.2 需要改动

#### P0: 阻塞性改动

| # | 文件 | 函数/区域 | 改动描述 | 预估行数 |
|---|------|----------|---------|---------|
| 1 | `config/_alfworld_phase_b.yaml` | `model_path` | 设为 Phase A 通过后的 checkpoint 路径（当前 `TO_BE_SET`） | 1 |
| 2 | `ragen/trainer/step_rewards.py` | `assign_step_rewards()` | 添加 `biavr_step_reward` 参数，使 biavr reward 显式进入 step reward pipeline，而非仅通过 history turn['reward'] 隐式注入。当前 `assign_step_rewards` 只知道 `episode_rewards`, `is_action_valid`, `is_terminal`，对 biavr per-step reward 无感知 | ~15 |
| 3 | `ragen/llm_agent/ctx_manager.py` | `_normalize_episode_rewards()` | 验证 biavr_reward（已注入到 turn['reward']）在 group normalization 中的行为。biavr_reward 是 per-step 小量（-0.1 ~ +0.9），episode success reward 是 10.0，归一化时 biavr 信号可能被淹没。可能需要分离 reward 通道 | ~20 |

#### P1: 功能完善

| # | 文件 | 函数/区域 | 改动描述 | 预估行数 |
|---|------|----------|---------|---------|
| 4 | `agent_proxy.py` | `_inject_biavr_rewards()` | 增加 per-episode biavr metrics（verify_rate, informativeness_rate）到 rollout_states 的 metrics dict，供 eval 阶段使用 | ~10 |
| 5 | `agent_trainer.py` | 训练循环 L1209 | lambda 更新后增加上界检查（防止 lambda 过大导致 always-skip），添加 `lambda_max` config 参数 | ~5 |
| 6 | `config/envs.yaml` | `AlfworldBIAVR` | 确认 `env_config` 参数（score, valid_action_bonus 等）与 Phase A 使用的 env tag 一致 | ~5 |

#### P2: Ablation 基线（Phase C 前置）

| # | 文件 | 函数/区域 | 改动描述 | 预估行数 |
|---|------|----------|---------|---------|
| 7 | `config/` | 新增 3 个 yaml | `_alfworld_ablation_no_verify.yaml`, `_alfworld_ablation_random_p.yaml`, `_alfworld_ablation_confidence.yaml` | 3x30 |
| 8 | `agent_proxy.py` | `rollout()` | 添加 ablation mode 支持：random-p 随机触发验证，confidence-threshold 基于 entropy 触发 | ~30 |

---

## 3. `<VERIFY>` Token 注册技术方案

### 方案 A: 纯文本字符串（当前实现） -- 推荐

**原理**：`<VERIFY>` 作为普通文本，被 Qwen tokenizer 分词为 `<`, `VER`, `IFY`, `>` 等子词。模型通过 RL 学习在 assistant response 开头生成这个子词序列。

**优点**：
- 零 tokenizer/模型改动，已在 biavr/ 中完全实现
- `parse_verify_token()` 已实现 string-level 解析
- 与 Thinkless (NeurIPS'25) 控制 token 思路一致（他们也用文本 token 而非 special token）
- 不影响 Phase A checkpoint 兼容性

**缺点**：
- 多子词序列可能导致部分生成（如只输出 `<VER` 后被截断）
- 训练初期模型可能混淆 `<VERIFY>` 与 `<think>` 前缀

**风险缓解**：format prompt 明确区分两种格式；`parse_verify_token()` 已实现 startswith 匹配，部分生成会 fallback 到 no-verify。

### 方案 B: 添加 Special Token

**原理**：`tokenizer.add_special_tokens({"additional_special_tokens": ["<VERIFY>"]})` + `model.resize_token_embeddings()`

**优点**：
- 单一 token ID，生成更稳定
- 可用 constrained decoding 强制首 token 为 `<VERIFY>` 或 `<think>`

**缺点**：
- 需要 resize embedding（Qwen3-1.7B 从 151936 -> 151937），引入新的随机初始化 embedding
- 新 embedding 初始化策略影响训练稳定性（mean init / zero init / random init）
- Phase A checkpoint 不兼容，需要 migration
- vLLM rollout worker 需重新加载 tokenizer

**实现量**：~50 行（tokenizer patch + embedding resize + checkpoint migration）

### 方案 C: 复用保留 Token

**原理**：Qwen3 tokenizer 有 `<|reserved_special_token_XXX|>` 保留位。选一个未使用的，在解码时映射为 `<VERIFY>` 语义。

**优点**：
- 无需 resize embedding
- 单 token ID，生成稳定

**缺点**：
- 需确认保留 token embedding 是否经过预训练（全零则等价于方案 B）
- 语义映射需在 prompt 中额外说明
- 可移植性差（换模型时保留 token 不同）

**结论**：推荐方案 A。纯文本方案已完全实现，与 Thinkless 先例一致。方案 B 作为 fallback（当模型无法稳定学会 `<VERIFY>` 子词序列时启用）。

---

## 4. Action-Change Reward 实现方案

### 4.1 当前实现（已完成）

```
r_step(t) = -lambda * 1[verify_t] + alpha * 1[verify_t AND action_changed_t]
```

- **verify_t**：模型在 step t 输出 `<VERIFY>` 前缀 -> `parse_verify_token()` 解析
- **action_changed_t**：a_pre != a_post -> `compare_actions()` 对比
  - a_pre：无 self-guidance prompt 的 greedy decode -> `_generate_a_pre_greedy()`
  - a_post：实际 response 中 `<answer>` 标签内的 action -> `extract_action_from_response()`
- **Lagrangian 约束**：`lambda_{t+1} = max(0, lambda_t + eta * (verify_rate - beta))`
  - beta=0.3（目标验证率）, eta=0.01, alpha=1.0, lambda_init=0.0

### 4.2 Reward 流转路径

```
rollout loop
  -> ctx_manager.get_env_inputs() 解析 verify_t
  -> agent_proxy 记录 biavr_verify[env_id]
  -> _generate_a_pre_greedy() 计算 a_pre (greedy decode, max_tokens=256)
  -> compare_actions(a_pre, a_post) 得 action_changed
  -> _inject_biavr_rewards() 将 biavr_reward 加到 turn['reward']
  -> ctx_manager.formulate_rollouts() 将 turn rewards 构建为 score_tensor
  -> agent_trainer 用 GRPO advantage estimation 训练
```

### 4.3 未完成项

1. **Reward scale 校准**：biavr_reward 范围 [-lambda, alpha-lambda]（当前 [-0.0, 1.0]），episode success reward = 10.0。初始阶段 lambda=0 意味着 verify 无惩罚，模型倾向 always-verify。建议在训练初期就设 `lambda_init > 0`（如 0.05-0.1）让模型从一开始就感受到 verify cost。
2. **a_pre 推理开销量化**：每个 VERIFY step 额外一次 forward pass（greedy decode, max_tokens=256）。若 verify_rate=50%，rollout 推理时间增加约 25-40%（a_pre decode 较短且 greedy，比主 rollout 快）。若 verify_rate=80%，增加约 40-60%。这个开销本身就是论文中 "cost" 的组成部分。

---

## 5. 预估改动量

| 类别 | 文件数 | 新增/修改行数 |
|------|--------|-------------|
| P0 阻塞性 | 3 | ~36 |
| P1 功能完善 | 3 | ~20 |
| P2 ablation 配置 | 4 | ~120 |
| **总计** | **~7** | **~176** |

核心 B-IAVR 功能已实现约 800 行（biavr/ 模块 ~286 行 + tests ~520 行 + 宿主集成 ~100 行）。

**预估工时**：
- P0 改动 + 集成测试: 2-4 小时
- P1 完善: 1-2 小时
- P2 ablation 配置: 2-3 小时
- 端到端调试（含 GPU 训练验证）: 4-8 小时

---

## 6. 潜在风险和依赖

### 6.1 硬依赖

| 依赖 | 状态 | 说明 |
|------|------|------|
| Phase A checkpoint（exp028c >= 20% success） | 等待中 | `model_path: TO_BE_SET`，Phase B 训练必须从 Phase A 成功的 checkpoint 出发 |
| `<VERIFY>` 子词序列在 Qwen3-1.7B tokenizer 中的分词 | 已确认 | `parse_verify_token()` 基于 string prefix match，不依赖特定分词 |

### 6.2 技术风险

| 风险 | 严重性 | 缓解 |
|------|--------|------|
| **模型无法学会 `<VERIFY>` 前缀决策** | 高 | 如果 RL 信号太弱（verify/skip 的 reward 差异小于 noise），模型可能 collapse 到 always-verify 或 never-verify。缓解：(1) warmup 阶段用 higher alpha (2) curriculum: 先在简单任务上学 verify pattern (3) fallback 到方案 B (special token) |
| **a_pre 推理开销过大** | 中 | 每个 VERIFY step 额外一次 forward pass。若 verify_rate 高，rollout 时间显著增加。缓解：batch a_pre 请求；或仅对 sample 的 subset 计算 a_pre（importance sampling） |
| **Lagrangian lambda 震荡/爆炸** | 中 | eta=0.01 较保守，但无上界。缓解：加 `lambda_max=2.0` 上界 |
| **biavr_reward 被 group normalization 淹没** | 中 | episode reward=10.0, biavr_reward 最大 0.9。GRPO group normalization 可能使 biavr reward 的方差贡献接近零。缓解：单独 reward 通道或调 alpha 到 5-10 |
| **action_changed = noise 而非 signal** | 高（论文层面） | paper_framing.md 已识别此为 Reviewer 攻击面 #3。防御实验为 Phase B 必做项：entropy-controlled 分析 + causal intervention |

### 6.3 与 Phase A 的接口

Phase B 代码与 Phase A 代码共存，通过 `config.biavr` section 开关隔离：
- `biavr` section 不存在 -> 走 Phase A always-on self-guidance 路径
- `biavr` section 存在 -> 走 Phase B selective verification 路径

这个设计是干净的，Phase A 和 Phase B 可以互不影响地运行。

---

## 7. 总结

**代码就绪度: ~85%**。核心 B-IAVR 模块已完整实现并集成到 rollout/training 循环中。剩余工作主要是：
1. Phase A checkpoint 路径设置（阻塞于 exp028c 结果）
2. Reward scale 校准和 normalization 验证（~36 行 P0 改动）
3. Ablation 配置（Phase C 前置）

**最大不确定性**不在代码层面，而在于：
- Phase A baseline 能否通过 MVP（exp028c 进行中）
- 1.7B 模型是否有足够的 capacity 学习 verify/skip 的 binary decision
- action_changed reward 是否是 genuine signal（需防御实验证明）
