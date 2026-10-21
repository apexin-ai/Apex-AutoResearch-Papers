# Phase B: B-IAVR 选择性验证机制 — 代码实现报告

## 1. 代码架构

```
RAGEN/ragen/biavr/
├── __init__.py                 # 公共 API 导出
├── action_canonicalize.py      # ALFWorld action 规范化
├── reward.py                   # B-IAVR reward + Lagrangian dual update + BIAVRTracker
├── verify_mechanism.py         # <VERIFY> token 解析 + prompt 构造
├── pre_action.py               # a_pre 反事实 action 计算
└── tests/
    ├── __init__.py
    └── test_biavr.py           # 52 个单元测试

RAGEN/config/envs.yaml          # 新增 AlfworldBIAVR 环境标签
```

## 2. 模块设计

### (a) `<VERIFY>` 选择性验证 (`verify_mechanism.py`)

- `parse_verify_token(response)` → `(bool, str)`: 检测 agent 输出是否以 `<VERIFY>` 开头，返回 verify 决策和清理后的 response
- `build_biavr_system_prompt()`: B-IAVR 专用系统 prompt，告知 agent 两种选择（verify-then-act / act-directly）
- `build_no_guidance_prompt()`: 用于 a_pre 反事实生成的无 self-guidance prompt
- **AlfworldBIAVR 环境标签**: 在 `envs.yaml` 中新增，使用 `env_type: alfworld`（复用现有 AlfredTXTEnv），仅修改 `env_instruction` 告知 agent 可选 verify

### (b) a_pre 计算 (`pre_action.py`)

- `build_pre_action_messages(history, observation)`: 替换系统 prompt 为无 self-guidance 版本，保留对话历史
- `compute_pre_action_prompt(history, observation)`: 返回完整的 greedy decode 配置（messages + sampling_params: temperature=0, top_k=1）
- `compare_actions(a_pre, a_post)`: 使用语义比较判断 verification 是否 informative

**设计选择**: a_pre 通过替换系统 prompt 实现，而非 fork 整个 conversation state。保留了完整的 user/assistant 对话历史，仅移除 self-guidance 指令，让模型在相同上下文下做 greedy decode。这比重建整个 rollout 更轻量。

### (c) B-IAVR Reward (`reward.py`)

- `biavr_reward(verify, action_changed, lambda_cost, alpha)`:
  - `r_step(t) = -λ·1[verify] + α·1[verify ∧ action_changed]`
  - 不 verify → 0；verify 但没改 action → -λ（白费资源）；verify 且改了 action → -λ+α（有效验证）
- `lagrangian_update(lambda_t, verify_rate, beta, eta)`:
  - `λ_{t+1} = max(0, λ_t + η·(verify_rate - β))`
  - 验证率高于目标 β → 提高成本 λ → 抑制过度验证
- `BIAVRTracker`: 有状态的 tracker，跟踪 verify_rate、informativeness_rate，支持 per-batch lambda 更新和 metrics 导出

### (d) Action Canonicalization (`action_canonicalize.py`)

- `canonicalize_action(action_str)` → `(verb, object, receptacle)`: 将 ALFWorld action 映射为三元组
  - 支持全部 ALFWorld action 格式: go to, take...from, put...in/on, heat/cool/clean...with, open/close/toggle/use/examine, inventory, look
  - 大小写无关、多余空格鲁棒
- `actions_equivalent(a, b)`: 语义等价比较

**设计选择**: 使用正则模式匹配而非字符串精确比较。ALFWorld action 格式固定（verb + object + optional preposition + optional receptacle），正则解析足够可靠且不需要维护 action 词表。

## 3. 与 RAGEN 框架的集成点

| 集成点 | 位置 | 说明 |
|--------|------|------|
| 环境标签 | `config/envs.yaml` → `AlfworldBIAVR` | 复用 `AlfredTXTEnv`，仅修改 prompt |
| Action 解析 | `ctx_manager.py` 的 `_extract_actions` | 需增加 `<VERIFY>` token stripping |
| Reward 叠加 | `ctx_manager._normalize_episode_rewards` | `R_total = R_task + Σ_t r_step(t)` |
| a_pre 生成 | `agent_proxy.rollout` 循环内 | VERIFY step 做一次额外 greedy decode |
| Lambda 更新 | `trainer` 主循环 | 每个 training batch 后调用 `tracker.update_lambda()` |

## 4. 单元测试结果

```
52 passed in 3.24s
```

覆盖范围:
- **Action canonicalization**: 16 tests — 全部 ALFWorld action 格式 + 大小写/空格鲁棒性
- **B-IAVR reward**: 5 tests — verify/no-verify × action_changed 组合
- **Lagrangian update**: 5 tests — 增/减/不变/非负/精确值
- **BIAVRTracker**: 4 tests — 空 tracker、多步记录、lambda 更新重置、metrics
- **Verify token parsing**: 5 tests — 有/无/空白/非首位/空字符串
- **Action extraction**: 4 tests — 正常/空白/无标签/多行
- **Pre-action messages**: 3 tests — 系统 prompt 替换、对话保留、去重
- **Action comparison**: 6 tests — 相同/不同/None/大小写

## 5. Phase B 训练还需要什么

1. **Phase A checkpoint**: 从 exp_001 完成后获取最佳 checkpoint 路径，作为 Phase B 的 `actor_rollout_ref.model.path`
2. **集成代码修改**: 需要在 `ctx_manager.py` 和 `agent_proxy.py` 中接入 B-IAVR 逻辑（action 解析加入 verify token 处理、reward 叠加 step reward、rollout 循环中插入 a_pre 计算）
3. **训练配置**: 基于 Phase A 的 config 创建 `_alfworld_exp002_biavr.yaml`，设置:
   - `env_configs.tags: [AlfworldBIAVR]`
   - B-IAVR 超参: `lambda_init=0.1, alpha=1.0, beta=0.3, eta=0.01`
   - 学习率、batch size 等沿用 Phase A 参数
4. **`<VERIFY>` token 注册**: 确认 tokenizer 对 `<VERIFY>` 的 token 化行为（可能需要作为 special token 添加）
5. **性能考量**: a_pre 额外 greedy decode 增加约 1× 推理开销（仅在 verify step），需评估是否在 rollout 循环中做或用 vLLM batch 合并
