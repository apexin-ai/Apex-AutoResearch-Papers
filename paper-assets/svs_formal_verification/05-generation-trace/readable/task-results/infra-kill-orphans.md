# infra kill orphans

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_orphans_20260514T134156_result.json`
- **Structured JSON:** [`ed5ba9f0d77981cb5773.json`](../../sessions/ed/ed5ba9f0d77981cb5773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 项目 | 状态 |
|------|------|
| 孤儿进程 54409, 54411 | **已清理** |
| v2 rescorer PID 61828 | **已结束**（进程不存在） |
| mvp_003 进度 | **44 条** gold_label 已写入 results_partial.json |
| mvp_003 PID 37622 | **运行中**，已跑 3h51m，CPU 0.6% |

当前活跃 Python 进程：
- **vLLM server** (PID 33091) — DeepSeek-R1-Distill-Qwen-14B，端口 8001，双卡 tensor-parallel
- **mvp_003 主进程** (PID 37622) — `svs_pipeline.run_mvp`，含 forkserver 子进程
- **jupyter-lab** (PID 937) + **tensorboard** (PID 939) — 系统服务
- 若干 multiprocessing forkserver/resource_tracker 子进程（属于 mvp_003）

v2 rescorer 已自行退出，mvp_003 仍在正常推理中。

---
