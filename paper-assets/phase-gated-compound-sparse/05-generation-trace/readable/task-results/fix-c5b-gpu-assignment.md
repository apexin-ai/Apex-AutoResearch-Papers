# fix c5b gpu assignment

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c5b_gpu_assignment_20260514T180158_result.json`
- **Structured JSON:** [`8f5aa7473e18a12692ee.json`](../../sessions/8f/8f5aa7473e18a12692ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 根因：`run_c5b_pilot.py:581` 覆盖了 `CUDA_VISIBLE_DEVICES`

启动命令：`CUDA_VISIBLE_DEVICES=3 bash run_c5b_pilot.sh 0`

执行链路：
- `run_c5b_pilot.sh` 接收参数 `0`，设 `GPU=0`，传 `--gpu 0` 给 Python
- **`run_c5b_pilot.py:581`**：`os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` → 将 shell 级别的 `CVD=3` 覆盖为 `0`
- 结果：进程跑在 **物理 GPU 0**，不是预期的 GPU 3

`profiling/run_mitigation_pilot.py:573` 有同样的逻辑，是代码来源。

### 2. c5b 实际在 GPU 0

```
PID 153367 → GPU-183f7d18 = GPU 0（与 c2_n500_deepseek imp 条件 PID 130124 共享）
```

GPU 0 显存占用：c2 imp 33374 MiB + c5b 20888 MiB = 54262 MiB（96GB 卡不爆显存，但算力争抢）

### 3. c2 throughput 受影响

| GPU | 条件 | 进度 | 平均速率 |
|-----|------|------|----------|
| GPU 0（共享）| c2 imp | 471/500 s015 | **~63s/problem** |
| GPU 1（独占）| c2 rand | 496/500 s015 | **~41s/problem** |

GPU 0 比 GPU 1 慢 **~54%**。c2 imp 还剩 ~1530 problems（s015 剩 29 + s020/s025/s030 各 500），如果继续共享，额外耗时约 9.5 小时。

### 4. c5b 进度

s025 阶段 12/30，s030 尚未开始。总进度 12/60 = 20%。

### 建议修复方案

**Kill c5b，修复后重启到 GPU 3：**

1. Kill PID 153367
2. 修复 `run_c5b_pilot.sh`：改为 `bash run_c5b_pilot.sh 3`（或直接去掉 shell 级 `CUDA_VISIBLE_DEVICES`，让 Python 内部的 `--gpu 3` 生效）
3. 重启：`nohup bash run_c5b_pilot.sh 3 &`
4. 损失 s025 前 12 个 problem 的进度（~10 分钟重跑），换来 c2 imp 恢复正常速率 + c5b 独占 GPU 3

是否执行？

---
