# code plan018 implement

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan018-implement_20260517T181712_result.json`
- **Structured JSON:** [`ad80163b54cd13c606ba.json`](../../sessions/ad/ad80163b54cd13c606ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

### 1. agent_trainer.py 改动（4 处）

| 位置 | 改动 |
|------|------|
| L172 签名 | 新增 `advantage_mode=None` 参数 |
| L288 step_independent overlay | 新增 `if advantage_mode == "episode_level"` 分支，调用 `compute_episode_returns` 替代 `compute_step_discounted_returns` |
| L984 第一调用处 | 传入 `advantage_mode=getattr(self.config.algorithm, 'advantage_mode', None)` |
| L1569 第二调用处 | 同上 |

### 2. config/_alfworld_factorial_h2_episode_adv.yaml

- `algorithm.advantage_mode: "episode_level"` (新参数)
- `agent_proxy.context_window_mode: "step_independent"`, `step_independent_history_length: 2`
- `n_gpus_per_node: 4`, `CUDA_VISIBLE_DEVICES: "0,1,2,3"` (westd-47453 4卡)
- `val.env_groups: 134`, `tags: ["AlfworldOOD"]` (valid_unseen)

### 3. Dry-run 结果

- bjb1: Config 加载成功，`advantage_mode: episode_level` 正确读取
- bjb1: `from ragen.trainer.agent_trainer import compute_advantage` 无报错
- westd: Import OK，`advantage_mode` 参数存在于签名中

### 4. 同步确认

两台服务器均已独立 patch 完成（互不可达，分别执行相同脚本）。向后兼容：`advantage_mode=None`（默认）走原有 `compute_step_discounted_returns` 路径。

---
