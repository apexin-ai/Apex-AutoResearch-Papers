# ops check a1 rerun and collect cuda3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_a1_rerun_and_collect_cuda3_20260522T200618_result.json`
- **Structured JSON:** [`3bd3a18d05ace5217959.json`](../../sessions/3b/3bd3a18d05ace5217959.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 诊断结果

### 1. 失败原因
**Registry 误判**。Health check 用 `tmux:eval_a1_obj_rerun` 格式校验 PID，不匹配 `[a-zA-Z0-9_-]+` 正则，连续 5 次 SSH check 失败后自动标记 failed。**进程本身从未中断**，当前 PID 931014 仍在 GPU:3 运行。

### 2. Rerun 进度
- 启动时间：05-23 02:30
- 当前进度：Task 2 (milk) ep 100/200
- 预计完成：~05:10（约 1h 后）
- 参数：4 tasks × 200 episodes，共 800 episodes

### 3. GPU:3 状态
在用，8550MiB / 97887MiB，24% 利用率。

### 4. Fake Safety 分析（已有 50 eps/task 数据）

| 模型 | CAR | Safe Eps | Fake Safe | Fake Safe Rate |
|------|-----|----------|-----------|----------------|
| A1/LoRA Baseline (M025 corrupted, 数据相同) | 90.0% | 180/200 | 178/180 | **98.9%** |
| Baseline Full-FT | 83.0% | 166/200 | 165/166 | **99.4%** |

几乎所有 safe episodes 的 `max_displacement < 0.1mm`（多数 < 1μm）。机器人本质上是 frozen/action-collapsed，而非真正避障。M025 bug 确认：A1 和 LoRA baseline 文件数据完全相同。

### 5. 待办
Rerun 完成后（~05:10），需检查输出文件 `a1_rerun_v11_eval_safelibero_object_all_levelII_best_lora_baseline_seed0.json` 并重新做 200 eps 的 displacement 分析。

---
