# code intervention c prime bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_intervention_c_prime_bjb1_20260521T213652_result.json`
- **Structured JSON:** [`35cf9506db04ad66907f.json`](../../sessions/35/35cf9506db04ad66907f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出报告

### 1. len_penalty revert 结果
**无需操作。** bjb1 的 `agent_trainer.py` 中不存在 `_lp_coef`、`response_length_penalty`、`_lp_threshold`、`_adjust_token_rewards_with_step_penalties` 的任何引用。代码已是干净状态。

### 2. max_response_length 代码路径分析 — **阻塞**

**`max_response_length` 在 RAGEN 中无实际执行逻辑。** 详细分析：

| 搜索位置 | 结果 |
|----------|------|
| `ragen/llm_agent/agent_proxy.py` (694行, trajectory 主循环) | **零匹配** |
| `ragen/llm_agent/ctx_manager.py` | **零匹配** |
| `ragen/llm_agent/es_manager.py` | **零匹配** |
| `ragen/trainer/agent_trainer.py` | **零匹配** |
| `ragen/env/` 全目录 | **零匹配** |

**trajectory 终止逻辑**（`agent_proxy.py` line 248-272）仅依赖：
- `max_turn`：`for i in range(max_turn)` 循环
- env done 信号：`if len(env_outputs) == 0: break`

**无任何总 token 计数或截断机制。**

`config/base.yaml` 中 `data.max_response_length: null` 通过 verl 的 OmegaConf 插值 `${oc.select:data.max_response_length,512}` 映射到 `rollout.response_length`（per-turn 生成长度），但 exp029 config 已显式设置 `response_length: 1024`，会覆盖此默认值。在 verl 的 `metric_utils.py` 中，`max_response_length` 仅从 tensor shape 推断用于 metric 计算，非执行限制。

**结论**：设置 `max_response_length: 8000` 在当前代码下为 **no-op**（不生效）。仅靠 `max_turn: 25` + `response_length: 1024` 的理论上限为 25,600 tokens，远超预期的 8000 trajectory cap。

### 3. Config 未创建
因 Step 2 阻塞，未进行 config 创建。

### 4. 训练未提交
**阻塞原因：`max_response_length` 无代码实现，trajectory-level cap 不会生效。**

### 可选推进方向（供决策）
1. **实现 trajectory cap 代码**：在 `agent_proxy.py` 的 rollout 循环中增加累计 token 计数，达到 `max_response_length` 时提前终止 trajectory
2. **退而求其次**：仅用 `max_turn=25`（无 token cap），但实验设计与 Intervention C' 描述不符
3. **调整 max_turn 近似 cap**：`max_turn=8`（≈8000/1024）更接近预期效果，但过于激进

---
