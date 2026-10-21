# run bootstrap parallel optimize and restart

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_bootstrap_parallel_optimize_and_restart_20260522T201139_result.json`
- **Structured JSON:** [`c83ceb18c89e14f61fe7.json`](../../sessions/c8/c83ceb18c89e14f61fe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 session 均已启动并运行：

- **bootstrap_cuda0**: openvla/goal/trained 正在加载模型，GPU 0 即将开始
- **bootstrap_cuda1**: tracvla/goal/trained 正在特征提取 (300/5000 samples)，GPU 1 占用 57%/8.9GB

任务分布：
- cuda0: openvla (4 suites × 2 conditions = 8) + nora (2 suites × 2 conditions = 4) = **12 conditions**
- cuda1: tracvla (4 suites × 2 conditions) = **8 conditions**
- 总计 **20 conditions**，每个 1000 bootstrap iterations，multiprocessing 并行化 (100 workers)

---
