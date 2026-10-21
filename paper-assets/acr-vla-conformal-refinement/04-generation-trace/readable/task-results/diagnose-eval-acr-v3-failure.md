# diagnose eval acr v3 failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-acr-v3-failure_20260514T202026_result.json`
- **Structured JSON:** [`6fe7a7bbc4b133d077db.json`](../../sessions/6f/6fe7a7bbc4b133d077db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。写报告。

## 诊断报告

### 结论：进程未崩溃，是监控误报

**两个 eval 进程仍在正常运行**，没有任何崩溃。

### 证据

| 项目 | eval-acr-spatial-v3 | eval-acr-object-v3 |
|------|---------------------|---------------------|
| 实际 PID | 197062 (子进程，session ID = 197057) | 197808 (子进程，session ID = 197803) |
| 进程状态 | **R (running)** | **R (running)** |
| 内存 RSS | 9.6 GB | 10.6 GB |
| GPU 显存 | 3575 MiB (cuda:0) | 1450 MiB (cuda:3) + 1873 MiB (cuda:0 EGL) |
| 已完成 | 5/10 tasks, 1/50 success (2%) | 5/10 tasks, 0/50 success (0%) |
| 日志行数 | 31 行（正常，每完成一个 task 输出几行） | 31 行 |
| 最后日志更新 | 04:17（几分钟前） | 04:03 |

### 根因："反复死亡"是监控误判

1. **evaluate.py 中没有任何 wandb 集成** — `grep -rn "wandb" evaluate.py` 返回空。脚本从未调用 `wandb.init()` 或 `wandb.log()`。
2. 监控系统检测不到 W&B heartbeat/metrics → 判定为"进程死亡"。实际上进程一直在跑。
3. 日志文件只有 31 行不是因为重启截断，而是 evaluate.py 本身输出稀疏（每完成一个 task 才输出 2-3 行）。

### 进程启动方式

父进程 (PID 197061) 命令：
```
timeout 86400 env bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl ... python -u src/evaluate.py ..."
```

24 小时 timeout wrapper，没有自动重启机制。进程启动以来一直在连续运行。

### 对 v4 eval 的影响

- **无影响**。崩溃从未发生，环境和 GPU 状态正常。
- GPU 0 较拥挤（12.9 GB / 24.5 GB，4 个 python 进程），GPU 1-3 负载轻。
- v3 eval 预计还需 ~3-4 小时完成剩余 4-5 个 tasks。

### 建议

1. **给 evaluate.py 加 W&B logging** — 否则后续 eval 都会被监控误判。至少需要 `wandb.init()` + 每完成一个 task 时 `wandb.log({"task_success_rate": ...})`。
2. **v3 eval 让它跑完** — 进程正常，不需要干预。虽然用的是旧 CRM v2 checkpoint（未归一化），结果可以作为 ablation baseline。
3. **v4 eval 可以直接启动** — 确保 evaluate.py 先加上 W&B 集成，并分配到空闲 GPU（避开 GPU 0）。

---
