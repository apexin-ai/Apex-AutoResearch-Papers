# check seed47 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed47_status_20260529T015749_result.json`
- **Structured JSON:** [`9357b39f19ab0ac3b3c6.json`](../../sessions/93/9357b39f19ab0ac3b3c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 seed47 bonus 实验已完成，exit code 均为 0。

**注意**：cqa1-33015 上实际运行的实验名与预期不同——实际是 `l2norm_k0.75`、`random_k0.70`、`random_k0.75`（而非 `l2norm_k0.5`、`attn_k0.75`、`attn_k0.7`）。

## 状态表

| exp_id | server | status | success_rate | elapsed | notes |
|--------|--------|--------|-------------|---------|-------|
| pi05_l2norm_k0.75_seed47 | cqa1-33015 | ✅ Done (exit 0) | **71.0%** | 221 min | completed 2026-05-28T20:48 UTC |
| pi05_random_k0.70_seed47 | cqa1-33015 | ✅ Done (exit 0) | **59.0%** | 228 min | completed 2026-05-28T20:55 UTC |
| pi05_random_k0.75_seed47 | cqa1-33015 | ✅ Done (exit 0) | **62.4%** | 228 min | completed 2026-05-28T20:55 UTC |
| pi05_l2norm_k0.70_seed47 | westd-41074 | ✅ Done (exit 0) | **62.0%** | 156 min | completed 2026-05-28T19:44 UTC |

实验名与你预期的 3 个（l2norm_k0.5, attn_k0.75, attn_k0.7）不同——实际提交的是 l2norm_k0.75、random_k0.70、random_k0.75。可能提交时实验配置做了调整。

---
