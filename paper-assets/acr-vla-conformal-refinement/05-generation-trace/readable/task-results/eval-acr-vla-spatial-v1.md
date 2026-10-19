# eval acr vla spatial v1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acr-vla-spatial-v1_20260513T225211_result.json`
- **Structured JSON:** [`bb6725a4e2c6633638eb.json`](../../sessions/bb/bb6725a4e2c6633638eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常。CRM 已加载（337,438 params），10 个 spatial tasks 已加载，rollouts 正在运行。

**启动摘要：**

| 项目 | 值 |
|------|-----|
| 实验 ID | `eval-acr-spatial-v1` |
| 服务器 | bjb1-18228, GPU 1 (RTX 4090) |
| 模式 | `acr_vla` (SmolVLA K=10 → CGS → CRM correction) |
| 基准 | LIBERO spatial, 10 tasks × 10 rollouts |
| CRM | crm_best.pt, 337K params |
| tmux session | `eval-acr-spatial-v1` |
| 日志 | `/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log` |
| 结果 JSON | `/root/autodl-tmp/eval_results/eval-acr-spatial-v1.json` |

进程已进入 rollout 阶段。可用 `tail /root/autodl-tmp/eval_results/eval-acr-spatial-v1.log` 跟踪进度。

---
