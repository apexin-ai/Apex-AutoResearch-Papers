# monitor exp015 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp015-progress_20260514T131318_result.json`
- **Structured JSON:** [`aa983bcb72cfd3d478c7.json`](../../sessions/aa/aa983bcb72cfd3d478c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp015 训练状态报告

### 进程状态
- PID 334692 alive，ELAPSED 15:45 min
- 日志：`/root/runs/cost-verify-agent-rl/exp015.log`，1685 行
- 日志最后修改时间 21:05:24，当前 21:08:35（约 3 分钟前更新）

### 当前进度：**Step 1/30 完成，Step 2 进行中**

仅检测到 **step 0 (初始验证)** 的指标输出。Step 1 已完成（Training Progress 1/30 [05:37<2:43:06, 337.47s/it]），但 step 1 训练指标尚未打印到日志（test_freq=20 推测训练步指标只在 val/save freq 触发时输出）。

### Step 0 (初始验证) 指标
```
Step 0 (val): success=0.0%, action_is_valid=85.83%, pass@1=0.0%, 
              num_actions=30.0, response_length=2797.5,
              reward/best@4=0.0, reward/worst@4=0.0
```

### 训练步指标
**无**。日志中目前不存在 `step:1`、`pg_loss`、`grad_norm`、`reward_mean` 等训练指标的实际数值输出。仅看到 `compute_policy_loss` 函数调用栈。

### exp014c stale Worker 影响排查 ✓ 安全

- `env.py:203` 存在 `success_gated_bonus` 代码，但**整段被 `if self.config.valid_action_bonus > 0`（line 202）包裹**
- `config.py`: 默认 `valid_action_bonus = 0.0`、`success_gated_bonus = False`
- exp015 config (`_alfworld_exp015_sparse_stable.yaml`) 未覆盖以上字段
- exp015 config 使用 `tags: ["AlfworldSG"]`（非 AlfworldSG_SuccessGated）
- **结论**：exp014c 的 success_gated_bonus 代码路径对 exp015 完全无影响（dead code path）

### Kill 判断
**当前不触发**。Step 6 还需 ≈25 分钟（每步 337s × 5 步）。需稍后再查。

### 建议
约 25-30 分钟后再次检查日志以获取 step 6 指标。下次检查关键看：
- step:N 训练指标是否开始打印（若 step 5 仍无输出，需排查日志写入异常）
- step 6 时 pg_loss=0 且 success=0% → 触发 kill

---
