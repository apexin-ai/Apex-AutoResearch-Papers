# infra verify and launch eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-and-launch-eval_20260515T194348_result.json`
- **Structured JSON:** [`3465330ebc5098282daf.json`](../../sessions/34/3465330ebc5098282daf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**状态**：
- SmolVLM2 processor 缓存已修复（HF cache 完整，含 processor_config.json 等所有文件）
- 之前的 eval（v2/v1）全部失败——每个 suite 都 crash 在 `Can't load processor for SmolVLM2`
- 新版 eval（v3/v2）已由另一个 Worker 在 03:38 启动，**当前正在运行**

**双 GPU eval 进度**：

| Experiment | GPU | PID | Script | 当前进度 | 早期 SR |
|---|---|---|---|---|---|
| mvp1_baseline_std | cuda:1 | 109421 | run_eval_std_v3.sh | libero_spatial task 0/10 done | **82%** |
| mvp1_baseline_plus | cuda:0 | 109494 | run_eval_plus_v2.sh | libero_spatial task 0/10 done | **98%** |

**预估完成时间**：每个 task 约 8 分钟 × 10 tasks × 4 suites ≈ 5-6 小时，预计 CST ~09:30 完成。

---
