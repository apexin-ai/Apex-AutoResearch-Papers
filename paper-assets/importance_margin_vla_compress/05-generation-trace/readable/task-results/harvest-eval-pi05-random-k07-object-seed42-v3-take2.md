# harvest eval pi05 random k07 object seed42 v3 take2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_random_k07_object_seed42_v3_take2_20260523T230523_result.json`
- **Structured JSON:** [`40a9f4e4dd835bcb2183.json`](../../sessions/40/40a9f4e4dd835bcb2183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/failed。无活跃 cron 需要删除。

## 报告

**eval_pi05_random_k07_object_seed42_v3** — 失败，需要 v4 重试。

| 项目 | 值 |
|------|-----|
| SR | **无结果**（未完成） |
| 进度 | T0 ep=30/50 (87%)，仅完成 0/10 tasks |
| 崩溃方式 | 静默终止，无 error/traceback |
| v2→v3 改进 | tokenizer 网络问题已修复（TRANSFORMERS_OFFLINE=1 生效），模型加载成功 |
| 崩溃原因推测 | 4 GPU 均占用 ~10GB，可能因资源争用被 OOM killer 终止 |
| vs pre-fix 69.4% | 无法对比 |

**GPU 状态**（cqa1-33015）：
- GPU 0: 10314 MiB, 23%
- GPU 1: 10140 MiB, 22%
- GPU 2: 10264 MiB, 35%
- GPU 3: 10211 MiB, 19%

GPU 2 当前仍有 ~10GB 占用，**不空闲**——4 个 GPU 均被其他进程占用。如需重试 v4，需等当前任务完成或选择其他时段。

---
