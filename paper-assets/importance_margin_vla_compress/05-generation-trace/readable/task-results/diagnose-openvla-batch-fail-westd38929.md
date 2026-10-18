# diagnose openvla batch fail westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_openvla_batch_fail_westd38929_20260521T070441_result.json`
- **Structured JSON:** [`7d10c586cf926cb44d60.json`](../../sessions/7d/7d10c586cf926cb44d60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：AutoDL 容器级重启**，不是 OOM / CUDA 错误 / 代码问题。

核心证据：4 个实验日志全部无错误截断 + dmesg 被清空 + jupyter/tensorboard 在实验死亡后 1 分钟重启 + uptime 148 天未变（宿主机没重启，是容器重启）。

**实际需要重跑的只有 2 个**：
- `eval_openvla_random_k03` — 无完整结果
- `eval_openvla_l2norm_k07` — 无完整结果

另外 l2norm k05 (SR=39.2%) 和 l2norm k03 (SR=25.0%) 已有先前完整结果。

`eval_openvla_sc_m128_object_seed42_v2` (PID 188248) 也已死亡，Registry 仍标 RUNNING 需更新。

GPU 当前完全空闲（0 MiB / 96 GB），可立即重试。

---
