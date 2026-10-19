# ops registry and data cleanup

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-and-data-cleanup_20260512T171821_result.json`
- **Structured JSON:** [`820b173b0b9588c8388f.json`](../../sessions/82/820b173b0b9588c8388f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. v5_cuda0 数据残留：**无残留，无需清理**

- 文件 Birth time = 00:52:15（被 kill 的 GPU3 进程创建了目录和空文件）
- PID 266200 在 00:58:56 启动，代码第 407 行用 **`open(output_file, "w")`**（覆盖写），启动时清空了整个文件
- 当前 25 行 = PID 266200 自己写的 25 条 task（log 对得上），无脏数据

### 2. Seed 参数：**脚本无 seed 参数**

- `collect_trajectories.py` 没有 `seed`/`random`/`shuffle` 任何一个关键词
- argparse 参数只有：`model_name, output_dir, split, temperature, max_steps, max_new_tokens, gpu, num_tasks, part_num, part_idx`
- task 顺序由 ALFWorld 环境的 `task_gen` 迭代器决定（顺序遍历 game files），**两卡跑的是完全相同的 task 序列**（都是 task 0-249）
- temperature=0.7 引入采样随机性，所以同一 task 两卡的轨迹不完全一样，但 **task 分布完全重叠**。如果目的是收集更多样的数据，应该用 `--part_num 2 --part_idx 0/1` 做分片

### 3. 两卡进度

| | v5_cuda0 (PID 266200) | v5_cuda1 (PID 263025) |
|---|---|---|
| 启动时间 | 00:58:56 | 00:48:20 |
| 已完成 | 25/250 tasks | 35/250 tasks |
| 成功率 | ~60.9% (14/23 at log) | ~50.0% (17/34 at log) |
| 当前速率 | ~1.2 tasks/min | ~1.1 tasks/min |

### 4. 预计完成时间

- cuda0：剩余 225 tasks，约 **187 min ≈ 3.1h**，预计 ~04:20 完成
- cuda1：剩余 215 tasks，约 **195 min ≈ 3.3h**，预计 ~04:10 完成

### 关键问题

两卡跑相同 task 序列（task 0-249），没有分片。如果需要去重合并，500 条变 250 条（每个 task 有两个不同轨迹版本）。如果原意是覆盖 500 个不同 task，需要现在加 `--part_num 2 --part_idx` 重启。

---
