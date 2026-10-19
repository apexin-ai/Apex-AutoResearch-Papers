# ops bjb2 28827 cuda2 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-28827-cuda2-check_20260515T191450_result.json`
- **Structured JSON:** [`88dc3a4a9a3b9ab6b326.json`](../../sessions/88/88dc3a4a9a3b9ab6b326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 全局状态

| GPU | 内存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 5200/24564 MiB | 21% | PID 105947 — perdof norm=0.03 object (registry job 105938) |
| 1 | 5200/24564 MiB | 18% | PID 109655 — perdof norm=0.05 object (job 109650) |
| **2** | **20722/24564 MiB** | **98%** | **4 个进程挤在一起（见下）** |
| **3** | 6239/24564 MiB | 19% | PID 130113 — obsonly norm=0.3 spatial b2 (运行 ~4min) |
| 4 | 5200/24564 MiB | 18% | PID 101616 — obs_only norm=0.05 object (job 101610) |
| 5 | 5200/24564 MiB | 19% | PID 103034 — obs_only norm=0.3 object (job 103028) |

### cuda:2 详情 — **不空闲，严重超载**

| PID | 运行时间 | 内存 | 任务 |
|-----|---------|------|------|
| 127581 | ~17min | 5645 MiB | perdof norm=0.3 object r2（重跑） |
| 131689 | ~2min | 6221 MiB | obsonly norm=0.3 spatial b3 |
| 132825 | ~1.6min | 6221 MiB | obsonly norm=0.3 spatial b4 |
| 134541 | ~47s | 2359 MiB | obsonly norm=0.3 spatial b2 |

4 个进程共吃 ~20.4 GB，GPU 利用率 98%。这些应该是刚通过 tmux session 提交的新任务。

### cuda:3 详情
- PID 130113 — obsonly norm=0.3 spatial b2 (eval_mag_obsonly_norm03_b2.json)，运行 ~4min，6.2 GB

### 关键 PID 生死

| PID | 状态 | 说明 |
|-----|------|------|
| 115384 | **DEAD** | eval-mag-perdof-norm03-object (原始 registry job) |
| 118886 | **DEAD** | perdof norm=0.3 手动提交 |
| 127570 | **DEAD** | eval-mag-perdof-norm0p3-object-r2 (已 kill) |
| 105938 | ALIVE | perdof norm=0.03 object, cuda:0, task 1/10 rollout 5/10 |
| 109650 | ALIVE | perdof norm=0.05 object, cuda:1, task 1/10 已完成(0% sr) |
| 101610 | ALIVE | obs_only norm=0.05 object, cuda:4, task 2/10 |
| 103028 | ALIVE | obs_only norm=0.3 object, cuda:5, task 2/10 |

### perdof norm=0.3 部分结果
- **无 JSON 结果文件**（logs/ 下零个 .json）
- 原始 115384 的日志 (eval_object_perdof_norm03.log) 只跑到 task 1 的 rollout 5/10 就挂了
- PID 127581 是新的 r2 重跑，在 cuda:2 上刚启动 ~17min

### Tmux sessions
```
eval-mag-obsonly-norm03-b2   (03:11:50)
eval-mag-obsonly-norm03-b3   (03:14:52)  ← 之前报 duplicate 的 session，实际存在且在运行
eval-mag-obsonly-norm03-b4   (03:14:00)
eval-mag-perdof-norm003-object (00:47:40)
```

### 问题
**cuda:2 上塞了 4 个 eval 进程**（1 个 perdof r2 + 3 个 obsonly spatial b2/b3/b4），总内存 20.4 GB / 98% 利用率。这些进程互相争抢 GPU 会严重拖慢速度，可能需要把其中一些迁移到别的 GPU 或 kill 掉重新分配。

---
