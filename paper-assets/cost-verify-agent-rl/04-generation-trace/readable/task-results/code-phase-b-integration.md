# code phase b integration

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase_b_integration_20260513T210014_result.json`
- **Structured JSON:** [`71a9da4ce96531ff431f.json`](../../sessions/71/71a9da4ce96531ff431f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**61 tests passed, 0 failures.** 全部通过。

---

## Phase B 集成报告

### 1. 架构

```
Model output
  ↓
ctx_manager.get_env_inputs()  ← 检测 &lt;VERIFY> token，解析 action
  ↓
agent_proxy.rollout()         ← 追踪 verify_t/action_changed per env per step
  ↓                              调用 _build_a_pre_inputs() 构建反事实 prompt
  ↓
_inject_biavr_rewards()       ← BIAVRTracker.record_step() → biavr_reward 注入 history
  ↓
agent_trainer.fit()           ← 每步读取 tracker metrics，执行 lambda 更新
```

模型自由选择首 token：`&lt;VERIFY>&lt;think>...` 或 `&lt;think>...`。GRPO advantage 中自然包含 biavr reward 分量，驱动模型学习何时验证。

### 2. 修改文件

| 文件 | 改动 |
|------|------|
| `config/_alfworld_phase_b.yaml` | 新建，Phase B 训练配置，env tag `AlfworldBIAVR`，biavr 参数 β=0.3/α=1.0/η=0.01 |
| `ragen/llm_agent/ctx_manager.py` | 5 处修改：biavr_enabled 属性、FORMAT_PROMPT 含 `&lt;VERIFY>` 选项、不强制 `&lt;think>` 前缀、get_env_inputs 中解析 verify_t |
| `ragen/llm_agent/agent_proxy.py` | 初始化 BIAVRTracker、rollout 中追踪 verify/changed、`_inject_biavr_rewards()` 和 `_build_a_pre_inputs()` 两个新方法 |
| `ragen/trainer/agent_trainer.py` | fit() 中读取 biavr metrics 并更新 lambda |
| `ragen/biavr/tests/test_biavr.py` | 新增 9 个集成测试（ctx_manager 解析、reward 注入、format prompt、a_pre 消息构建） |

### 3. 关键设计决策

- **不强制 `&lt;think>` 前缀**：RAGEN 原始流程在 prompt 尾部追加 `&lt;think>` 并在解码后补回。B-IAVR 需要模型自主选择 `&lt;VERIFY>` 或直接 `&lt;think>`，因此 biavr 模式跳过这两处强制操作。
- **reward 后注入而非修改 es_manager**：biavr reward 在 `get_rollout_states()` 之后、`formulate_rollouts()` 之前注入到 history entry 的 `reward` 字段，避免侵入式修改 environment step manager。
- **`&lt;VERIFY>` 保留在训练目标中**：解析 action 时临时剥离 `&lt;VERIFY>`，但 `llm_response`（写入 history 供训练用）保留完整的 `&lt;VERIFY>&lt;think>...` 序列，确保 policy gradient 信号覆盖 verify 决策。

### 4. 测试结果

```
61 passed in 3.48s
```

52 个原有单元测试 + 9 个新增集成测试，全部通过，无 GPU 依赖。

### 5. 已知 Gap

**a_pre greedy forward pass 未接线**：`_build_a_pre_inputs()` 已能构建反事实 prompt（移除 self-guidance 的对话历史），但实际 greedy 生成调用未连接到 vLLM engine。原因：vLLM rollout worker 的 sampling params 在初始化时固定（temperature=1.0），per-call 温度覆盖需要深入 verl 的 `RayWorkerGroup` 接口。当前 `biavr_changed` 始终为 `False`，等价于 α 项不生效。

**解决路径**：Phase B 初期可先以 `enable_a_pre=false` 运行（纯 budget penalty `-λ·1[verify]`），待确认基础流程正确后，再实现 a_pre forward pass 以启用 informative verification bonus。

---
