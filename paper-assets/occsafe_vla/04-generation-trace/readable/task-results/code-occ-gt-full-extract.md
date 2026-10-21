# code occ gt full extract

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_occ-gt-full-extract_20260520T072219_result.json`
- **Structured JSON:** [`e962b2ede6abe8553e3d.json`](../../sessions/e9/e962b2ede6abe8553e3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总状态：

**已启动：**
- Tasks 0-8：9 个并行 nohup 进程正在提取全部 50 demos
- Task 9：自动监控脚本（PID 55214），下载完成后自动启动提取

**时间估算：**
- 并发帧速率 ~1.65s/帧（比单进程慢 28%）
- 每任务约 50 demos × ~100 帧 × 1.65s ≈ 8,250s ≈ **~2.3 小时**
- 启动于 15:23，预计 **17:40 左右完成**（CST）
- Task 9 下载约还需 20-25 分钟，之后单独提取 ~2 小时

**进度监控命令：**
```bash
bash /tmp/check_extract_progress.sh
```

或单个任务详情：
```bash
tail -20 /tmp/extract_logs/task_0.log
```

**完成检查：**
```bash
# 查看已完成的 demo 数量
for i in $(seq 0 9); do
    echo "task_$i: $(grep -c 'BEV shape' /tmp/extract_logs/task_${i}.log 2>/dev/null)/50 demos"
done
```

**无代码修改** — 现有脚本已支持 `--task_id` + 默认全量 demo，直接并行启动 10 个实例即可。

---
