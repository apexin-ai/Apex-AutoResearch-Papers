# research plan018 code assessment

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan018-code-assessment_20260517T175332_result.json`
- **Structured JSON:** [`2b1b61423f0b620571ae.json`](../../sessions/2b/2b1b61423f0b620571ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have the full picture. Here's the analysis:

---

## 1. 当前 `context_window_mode` 如何影响 rollout vs advantage

`context_window_mode` 同时控制**三个**不同行为：

| 阶段 | `step_independent` | `full` |
|---|---|---|
| **推理生成** (`ctx_manager.py:1389`) | 每步只看最近 N 步历史 (`step_independent_history_length`) | 完整 episode 历史 |
| **训练样本构建** (`ctx_manager.py:1578`) | 每步一个样本，bounded context → `_build_step_independent_samples()` | 每 episode 一个样本 → `_build_samples_full()` |
| **Advantage 计算** (`agent_trainer.py:272`) | 先算 GRPO outcome advantage，然后**覆盖**为 step-level discounted returns → `compute_grpo_step_advantage()` | 直接用 GRPO outcome advantage (`token_level_rewards.sum`) |

关键耦合点在 `agent_trainer.py:272`:
```python
if context_window_mode == "step_independent" and adv_estimator == AdvantageEstimator.GRPO:
    # ... step-level advantage overlay
```

## 2. 推荐方案：Method A（纯配置项解耦）

添加一个新参数 `advantage_mode`，独立于 `context_window_mode`，仅控制 advantage 计算。

核心思路：在 step_independent overlay 块中，根据 `advantage_mode` 选择用 `compute_step_discounted_returns()`（当前行为）还是 `compute_episode_returns()`（所有步共享同一 episode return）。

`compute_episode_returns()` **已经存在且已导入**（`step_rewards.py:88`），它把 episode return 广播到同一 episode 的所有步。配合 `compute_grpo_step_advantage()` 做 GRPO 归一化，所有步获得相同的 episode-level advantage。

## 3. 具体改动文件和函数

### `ragen/trainer/agent_trainer.py`

| 位置 | 改动 |
|---|---|
| L172 `compute_advantage()` 签名 | 加 `advantage_mode=None` 参数 |
| L272-290 step_independent overlay 块 | 加分支：`advantage_mode == "episode_level"` 时用 `compute_episode_returns()` 替代 `compute_step_discounted_returns()` |
| L958-972 `compute_train_batch` 调用 | 从 config 读取 `advantage_mode` 并传入 |
| L1542-1558 `fit` 循环内调用 | 同上 |

### Config YAML

```yaml
algorithm:
  advantage_mode: episode_level  # "step_level" | "episode_level" | null(默认follow context_window_mode)
```

### 不需要改动的文件
- `ctx_manager.py` — 生成行为保持 `step_independent` 不变
- `core_algos.py` — `compute_grpo_step_advantage` 接口不变（传入 episode_returns 和 step_returns 形状相同）
- `step_rewards.py` — `compute_episode_returns` 已存在

## 4. 改动量估算

| 维度 | 估算 |
|---|---|
| 文件数 | **1 个 Python 文件** + 1 个 config YAML |
| 新增代码 | ~15-20 行 |
| 修改代码 | ~5 行（签名 + 调用处） |
| 总改动 | **~20-25 行** |
| 复杂度 | **低** — 逻辑集中在 `compute_advantage()` 一个函数内的一个 if 分支 |

## 5. 潜在风险

1. **Tensor shape**：无风险。`compute_episode_returns` 返回 `(batch_size,)` 和 `compute_step_discounted_returns` 相同，`compute_grpo_step_advantage` 兼容。

2. **GiGPO 交互**：如果同时使用 `advantage_type: gigpo` + `advantage_mode: episode_level`，L298-332 的 GiGPO 分支也需要类似处理。当前只用 GRPO 则无影响。

3. **向后兼容**：`advantage_mode=None`（默认）保持当前行为，零破坏性。

4. **Logging 路径**：`step_independent` 在 `is_turn_level_mode` 判断中不被包含（L654, L1178），现有 logging 逻辑不受影响。

---
