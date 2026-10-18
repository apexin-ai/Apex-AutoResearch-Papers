# deploy cqa1 gpu3 openvla profiling

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu3-openvla-profiling_20260525T203134_result.json`
- **Structured JSON:** [`893415d721469575fe69.json`](../../sessions/89/893415d721469575fe69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动。

**状态确认：**
- GPU3: 14891 MiB / 62% utilization — 模型已加载
- 模型: OpenVLA 7.5B, **256 vision tokens**, RTX 4090 D
- tmux session: `profiling_openvla_latency` 运行中
- 日志: `~/runs/importance_margin_vla_compress/profiling_openvla_latency.log`
- k=1.0 warmup 阶段已开始，单步 ~153ms（warmup step 3）

**配置：**
- 4 个 k 点: 1.0 / 0.9 / 0.7 / 0.5
- 每个 k 点 220 步（20 warmup + 200 measure）
- 统计: median + P5/P95
- 输出: `results/profiling_latency_openvla.json`

预计总运行时间约 15-20 分钟（880 步 × ~150ms）。

---
