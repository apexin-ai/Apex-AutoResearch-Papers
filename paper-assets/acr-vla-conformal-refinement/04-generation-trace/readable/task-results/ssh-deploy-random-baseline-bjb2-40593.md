# ssh deploy random baseline bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-random-baseline-bjb2-40593_20260517T120446_result.json`
- **Structured JSON:** [`0b9b8a7276a8db2a0e59.json`](../../sessions/0b/0b9b8a7276a8db2a0e59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

## 结果汇总

**evaluate.py 修改（已有 random mode？）**：没有，需要新增。

**代码修改内容**：
1. `--mode` choices 中添加 `"random_selection"`（行 67）
2. 新增 `select_action_random()` 函数（行 222-237）：从 K 个 candidates 中 `np.random.randint` 随机选 1 个，返回 7D action
3. rollout 调度处（行 343）添加 `elif args.mode == "random_selection"` 分支

**部署结果**：
- PID: **395256**
- GPU 0 占用: 5884 MiB
- 参数: `--mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 10`
- 输出文件: `logs/eval_object_random_selection_seed42.json`
- 日志: 模型加载完成，已开始加载 LIBERO object 环境（10 tasks）

---
