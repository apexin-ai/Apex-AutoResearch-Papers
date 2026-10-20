# infra confirm eval readiness

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_confirm_eval_readiness_20260520T221829_result.json`
- **Structured JSON:** [`35c9426296012cb79e70.json`](../../sessions/35/35c9426296012cb79e70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 汇报

**westd-10894 — vanilla auto-eval monitor**
- 进程存活：PID 226828，正常运行
- PID 映射正确：`(100203, 97847, 225562)` 对应 vanilla_s0/s1/s2
- 3 个训练进程均在运行中，每 5 分钟检查一次，最近一次检查 06:18
- eval_results 目录可写，已有中期 eval 结果（`vanilla_s0_midtrain_20r.json`, `vanilla_s1_midtrain.json`）
- 状态：✅ 正常

**westd-34685 — occ eval 脚本**
- 脚本存在且可执行
- PID 映射正确：`(27667, 28827, 29970)` → occ_s0/s1/s2，GPU 0/1/2
- **已修复两处问题**：
  - `--num_trials_per_task 20` → `--num_rollouts 20`
  - 删除了不存在的 `--gpu_id 0` 参数
- eval_results 目录已存在
- 状态：✅ 就绪，未启动（按要求）

---
