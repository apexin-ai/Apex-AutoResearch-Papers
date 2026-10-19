# fix spatial add n collection

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_spatial-add-n-collection_20260515T175002_result.json`
- **Structured JSON:** [`b9298a6009a6d510ba1a.json`](../../sessions/b9/b9298a6009a6d510ba1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Dry-run 完成，端到端 pipeline 验证通过：**

| 步骤 | 状态 |
|------|------|
| `_add_N` 任务发现 | 208 tasks, 0 skipped |
| BDDL 加载 + 环境创建 | load_errors=0 |
| π₀ rollout (220 steps × 2 tasks) | 正常运行 |
| (obs, action) 收集 | 正常 |
| 日志/统计 | 正常输出 |

2 个 dry-run episode 都是 FAIL（正常——加了干扰物体后 pi0 base 成功率本来就会下降，这正是训练数据要覆盖的场景）。full run 在 208 tasks × 3 eps = 624 rollouts 中会有足够的成功 episodes。

**修改总结：**
- `collect_expert_demos.py` spatial 模式默认从 `perturb_region_info()` 切换为 `_add_N` distractor-object 任务
- 新增 `--spatial_mode add_n|perturb_region` 参数，默认 `add_n`
- 新增 `discover_add_n_tasks()` 函数从 benchmark 发现 208 个 `_add_N` 任务
- 新增 `collect_spatial_add_n()` 函数，208 tasks × 3 eps = 624 rollouts
- `FileNotFoundError` 单独捕获，记录 `load_errors` 但不中断
- 旧 `perturb_region` 代码保留为 `--spatial_mode perturb_region` 备选

---
