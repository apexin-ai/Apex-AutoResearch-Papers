# code prepare line rerun

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_line_rerun_20260514T200454_result.json`
- **Structured JSON:** [`9798ba3c1b3d249b0cdf.json`](../../sessions/97/9798ba3c1b3d249b0cdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码修改完毕，dry-run 验证通过。以下是完整报告。

---

## 报告

### 1. 重复 PID 调查结论

- **PID 60414**：已不存在（进程已结束）
- **PID 60524**：仍在运行，是当前唯一的 scoring 进程
- **PID 60518**（60524 的父进程）：`bash -c rm -f phase2_line_scores.json && ... nohup python run_phase2_scoring.py --mode line --max-segments 200 --max-concurrent 5`

**结论：无 race condition。** PID 60414 是更早的一次运行（已结束），60524 启动时先 `rm -f` 删除了旧输出文件再重新开始。日志中的重复编号是两次独立运行写入同一 log 文件导致的。当前只有 60524 在跑，快完成了（36/36 youtube-dl_5 是最后一个）。

### 2. 代码修改清单

**teacher_scorer.py — score_segment 方法重写**
- 原来：1 次 retry（仅限 NoneType），其它异常直接 fallback
- 改为：**3 次 retry + exponential backoff（1s/2s/4s）**，覆盖 NoneType 和所有 API 异常
- 3 次重试仍失败则 fallback 为 `label="drop"`, `confidence=0.0`，记录 warning
- NoneType 不会导致整个 instance 失败

**run_phase2_scoring.py — 三项修改**

| 修改 | 原来 | 改后 |
|------|------|------|
| 截断逻辑 | `max_segments_per_instance=200` 参数 + 截断代码 | **完全移除**，不再截断 |
| `--max-segments` 参数 | 存在 | **移除** |
| 每 instance 记录字段 | `num_segments_original` / `num_segments_scored` / `truncated` | `total_segments` / `scored_segments`（无截断时两者相等） |
| EXCLUDED_INSTANCES | `{"fastapi_3", "fastapi_5"}`（已正确） | 不变，fastapi_1/2 自动纳入 |

**dry-run 验证结果：** 38 instances，62,322 total segments（之前 36 instances，~3,635 segments 因 max_segments=200 截断）。

### 3. 重跑命令

```bash
# 1. 等当前进程 60524 结束（或确认已结束）
ps -p 60524 -o pid= 2>/dev/null && echo "STILL RUNNING" || echo "DONE"

# 2. 启动全量重跑
cd /root/trace_distill_repair
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 清理旧结果
rm -f /root/trace_distill_repair/pipeline_output/phase2_line_scores.json

# 全量 line scoring（无截断，并发=5）
nohup python run_phase2_scoring.py --mode line --max-concurrent 5 \
  > /tmp/phase2_line_scoring_v2.log 2>&1 &
echo "PID=$!"
```

### 4. 风险评估

| 指标 | 值 |
|------|-----|
| 总 segments | 62,322 |
| 之前截断后的量 | ~3,635（仅 5.8%） |
| **增量 API 调用** | ~58,687 |
| 每段耗时（实测） | ~1.6 秒 |
| **估计耗时** | ~27 小时 |
| API 费用 | DeepSeek V4 Flash 自托管端点（47.94.22.126），无直接费用，但需服务器持续运行 |

**主要风险：**
- **youtube-dl 5 个实例占 87.7%**（54,652 segments），单个最大 13,449 segments。若 API 端点不稳定，这些大实例最易受影响（retry 逻辑已覆盖）
- 耗时 ~27 小时，需确保服务器和 API 端点在此期间稳定运行
- 建议写 log 到 `/tmp/phase2_line_scoring_v2.log`（不同于原来的文件名）以避免混淆

---
