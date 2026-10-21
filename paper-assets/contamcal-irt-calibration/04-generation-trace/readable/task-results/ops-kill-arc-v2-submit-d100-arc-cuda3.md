# ops kill arc v2 submit d100 arc cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_arc_v2_submit_d100_arc_cuda3_20260516T213340_result.json`
- **Structured JSON:** [`d2859345d228f311fc19.json`](../../sessions/d2/d2859345d228f311fc19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动并正在运行：

- **PID 874940** 在 GPU 3 上运行（560MiB，正在加载模型）
- 日志显示已识别 1172 个 ARC items，正在进行 embedding 编码（s1_embedding 阶段）
- tmux session: `exp002_llama_d100_arc`

汇总：
1. PID 870622 已 kill，cuda:3 已释放
2. 确认无已有 ARC signals 产出
3. Llama-3.2-3B_d100_s42 ARC signals 任务已提交，正常运行中

---
