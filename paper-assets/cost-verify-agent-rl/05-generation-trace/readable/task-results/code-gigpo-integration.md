# code gigpo integration

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gigpo_integration_20260515T201405_result.json`
- **Structured JSON:** [`70d803d34895367a9a8c.json`](../../sessions/70/70d803d34895367a9a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡各占用 ~51GB/98GB。exp027 正在运行，dry run 暂时不可行——会导致 GPU OOM 冲突。

## 完成报告

### 修改文件

| 文件 | 变更 | LOC |
|------|------|-----|
| `ragen/trainer/core_algos.py` | 新增 GiGPO 核心函数 (to_hashable, are_similar, build_step_group, gigpo_episode_norm_reward, gigpo_step_norm_reward, compute_gigpo_outcome_advantage) | +215 |
| `ragen/trainer/agent_trainer.py` | 新增 advantage_type/gigpo_config 参数传递，GiGPO 分支逻辑，metrics 日志 | +45 |
| `config/_alfworld_exp028_gigpo.yaml` | exp028 配置，基于 exp027 + `advantage_type: gigpo` | +102 (新文件) |
| `tests/test_gigpo.py` | 17 个单元测试 | +283 (新文件) |

### 单元测试结果
**17/17 passed** (4.99s)，覆盖:
- `to_hashable`: 基本类型、numpy、嵌套结构、字典
- `build_step_group`: 精确匹配分组、跨任务隔离、单步组、全同组、空 batch
- `gigpo_step_norm_reward`: 归一化计算、单例组、mask 应用
- `gigpo_episode_norm_reward`: 轨迹去重
- `compute_gigpo_outcome_advantage`: 组合 advantage、w=0 退化、单例组
- GRPO/GiGPO 一致性: 有限性验证

### Dry run
**暂不可行**。exp027 (PID 789790) 占用 cuda:0+cuda:1 各 ~51GB，启动 dry run 会 OOM。等 exp027 完成或空闲时再跑。

### exp028 config 路径
`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp028_gigpo.yaml`

### 关键设计决策
- GiGPO 通过 `algorithm.advantage_type: "gigpo"` 激活，默认 `"grpo"` 保持向后兼容
- 仅在 `context_window_mode == "step_independent"` 时生效（与现有 step-level 基础设施复用）
- `anchor_obs` 缺失时自动 fallback 到 GRPO step advantage 并打 warning
- GiGPO metrics (`step_group_avg_size`, `step_advantage_magnitude`, `episode_advantage_magnitude`) 自动记录到 W&B

### 风险
- `anchor_obs` 的文本内容质量直接影响分组效果。如果 ALFWorld 返回的 observation 过于相似或过于不同，step grouping 可能退化
- `enable_similarity: false`（默认精确匹配）是保守选择；如果 ALFWorld observation 有微小变化，可能需要开启 fuzzy matching

---
