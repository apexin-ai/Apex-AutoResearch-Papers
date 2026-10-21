# investigate val metric granularity

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_val_metric_granularity_20260517T053227_result.json`
- **Structured JSON:** [`e099550679896c76691a.json`](../../sessions/e0/e099550679896c76691a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。结论如下：

## 调查结论

### 问题确认

- **`val-env/AlfworldSG/success`（主 metric）: per-episode，两种模式相同，可比。**
  
  关键代码路径：
  - `es_manager.get_rollout_states()` (es_manager.py:300): `success = float(status.terminated and not status.truncated)` — 每个 env 实例一个值
  - `ctx_manager._compute_metrics(env_outputs)` (ctx_manager.py:444): `np.sum(value) / self.env_nums[tag]` — 除以总 episode 数 (32)
  - 与 `context_window_mode` 无关，因为 `env_outputs` 始终是 per-episode 粒度

- **`val-core/unknown/reward/mean@N`: 不可比！**
  - step_independent: N=1600 (32 eps × ~50 windows)
  - full: N=32 (32 episodes)
  - 且存在长度偏差：失败 episode 跑满 50 步 → 产生更多 windows → 在 mean 中权重更大

### 根本原因

`_build_step_independent_samples` 把每个 episode 展开为多个 windows 用于训练 batch（ctx_manager.py:1040-1130），但 `_compute_metrics`（ctx_manager.py:430-480）始终基于原始 `env_outputs`（per-episode）计算。两条路径是分离的：

```python
# ctx_manager.py:1247 - step_independent 模式结尾
llm_inputs.meta_info = {"metrics": self._compute_metrics(env_outputs, response_length)}
#                                                       ↑ 这是 per-episode 的原始 list
```

而 `val-core` 的问题出在 `_validate()` (agent_trainer.py:655):
```python
result = self.val_reward_fn(test_batch, return_dict=True)  # test_batch.batch_size = 1600 windows
scores = reward_tensor.sum(-1).cpu().tolist()  # 1600 个 per-window scores
sample_scores.extend(scores)  # 喂给 process_validation_metrics
```

NaiveRewardManager (naive.py:50) 发现 `rm_scores` 存在就直接返回，而 `rm_scores` 在 step_independent 下是 per-window 的 normalized episode reward。

### Episode-level Success 提取方案

**不需要任何修复。** `val-env/AlfworldSG/success` 已经是 episode-level 的，可以直接用于 h-sweep 对比。

在 W&B 中，所有实验都有 `val-env/AlfworldSG/success` 指标，它在所有 context_window_mode 下语义一致 = `成功 episode 数 / 32`。

### val-core 偏差量化

假设 success rate = 15% (5/32)，典型场景：
- 5 成功 eps × ~12 windows = 60 windows, score=10
- 27 失败 eps × 50 windows = 1350 windows, score=0
- `val-core/reward/mean@1410` ≈ 0.43
- 对比 full 模式 `val-core/reward/mean@32` = 1.56

差 ~3.6x，纯粹因为 episode 长度加权。

### 建议方案

**方案 A（推荐）：无需代码改动，直接用 `val-env/AlfworldSG/success` 做 h-sweep 对比。**

理由：
1. 这个 metric 已经是 episode-level，两种模式语义一致
2. 早停逻辑也用的这个 metric（agent_trainer.py:1641）
3. 无需修改正在跑的 h=2 seed 1

**方案 B（可选优化）：** 给 `val-core` 加 episode-level 聚合选项。修改 `_validate()` 中 step_independent 分支，按 `episode_ids` group 后取 max score per episode 再算 mean。改动量约 15 行。但当前实验不需要。

---
