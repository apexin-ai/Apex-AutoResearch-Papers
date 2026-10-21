# run openvla spatial untrained cuda1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_openvla_spatial_untrained_cuda1_20260522T091143_result.json`
- **Structured JSON:** [`74b88e48b6ca30861541.json`](../../sessions/74/74b88e48b6ca30861541.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，两卡并行运行：

| GPU | 进程 | 任务 | PID |
|-----|------|------|-----|
| cuda:0 | trained CF（Phase 6） | `libero_spatial_full_pipeline.py --conditions trained --only-counterfactual` | 645141 |
| cuda:1 | untrained 6-phase | `spatial_untrained_only.py` → `--conditions untrained` | 646058 |

操作总结：
- 杀掉了 resume 脚本（PID 645140），trained CF 子进程（645141）reparent 到 init 继续运行
- untrained pipeline 已在 cuda:1 启动，正在跑 Phase 1 extraction（Task 1/10 进行中）
- 结果输出到 `/root/autodl-tmp/vla-ssd/results/libero_spatial_untrained/`
- 日志：`/tmp/spatial_untrained_cuda1.log`

---
