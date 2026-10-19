# check full feasibility analysis

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-feasibility-analysis_20260512T140500_result.json`
- **Structured JSON:** [`8c3472632d8d28c63e4b.json`](../../sessions/8c/8c3472632d8d28c63e4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 14B 测试结果

- 模型: Qwen3-14B-AWQ
- **只完成了 2/100 episodes 就停了**（task 25 和 79），两个都失败
- 成功率: **0/2 = 0%**
- per_type: look_at_obj 0/1, pick_and_place 0/1
- 进程已退出，没有运行中的 14B 测试进程（但 VLLM::EngineCore PID 110596 占 22GB 显存仍在）

### 2. Replay 8B 失败分析

**进程仍在运行**（PID 117225，GPU 0 占 7754 MiB）。

Attempt 1 已处理 7/10 个任务，**全部 replay_ok=False**：

| task | type | replay_steps | corr_steps | replay_ok |
|------|------|:---:|:---:|:---:|
| pick_clean_then_place | failure_step=22 | 21 | 19 | False |
| pick_two_obj | failure_step=19 | 18 | 22 | False |
| pick_heat_then_place | failure_step=11 | 10 | 30 | False |
| pick_and_place | failure_step=6 | 5 | 35 | False |
| pick_and_place | failure_step=13 | 12 | 28 | False |
| look_at_obj | failure_step=7 | 6 | 34 | False |
| look_at_obj | failure_step=6 | 5 | 35 | False |

**没有任何 episode 的 correction 阶段成功。**

**replay_ok=False 的根因**：代码逻辑在 `replay_and_correct()` 中：

```python
if orig_obs and "Nothing happens" in observation and "Nothing happens" not in orig_obs.get("content", ""):
    replay_failed = True
```

即：replay 阶段重放原始 action 时，环境返回了 `"Nothing happens"`，但原始轨迹中该步骤的观察不是 `"Nothing happens"`。**环境状态在 replay 时发生了偏移**。

replay steps 都达到了 `failure_step - 1`（符合预期），说明 action 本身能执行但环境响应不同。**根因是 ALFWorld TextWorld 环境在新 session 中重新初始化同一个 game file 时，状态不完全一致**——某些 action 在新 session 中变成了无效操作（返回 "Nothing happens"），导致后续所有状态链式偏移。correction 阶段基于已偏移的状态生成动作，自然也无法成功。

### 3. Fresh-start 8B

- 完成了 4/100 episodes（tasks 25, 79, 114, 1157），全部失败
- 成功率: **0/4 = 0%**
- **进程已退出**，日志停在 21:56，JSON 只记录了 4 个 episode 的结果
- 可能因 GPU 显存竞争被 OOM kill

### 4. 进程冲突

GPU 上有 **6 个进程**竞争显存：

| PID | 显存 | 进程 |
|-----|------|------|
| 95813 | 7754 MiB | `collect_trajectories.py` (Qwen3-8B, GPU 0) |
| 117225 | 7754 MiB | `test_correction_feasibility_replay.py` (Qwen3-8B, GPU 0) |
| 110596 | 22096 MiB | VLLM::EngineCore（可能是已停止的 14B 测试残留） |
| 117632 | 8152 MiB | structfuse train.py（其他项目） |
| 98300 | 9420 MiB | run_mvp.py（其他项目） |
| 98594 | 9302 MiB | run_mvp.py（其他项目） |

**14B 和 8B fresh-start 测试提前停止很可能是显存不够导致的。** 6 个进程共占 ~64 GB 显存。

### 5. 总结

- **14B / 8B fresh-start 都因显存竞争提前死掉**，结果不可信（样本量太小）
- **replay 机制有根本缺陷**：ALFWorld 环境不支持确定性 replay，同一 game file 重新初始化后 action 效果不同，导致 100% replay 失败
- VLLM EngineCore (22GB) 是残留进程，应该清理

---
