# deploy westd41074 gpu2 gpu3 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu2_gpu3_seed43_20260527T125829_result.json`
- **Structured JSON:** [`aa6353723da5e0232240.json`](../../sessions/aa/aa6353723da5e0232240.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

## 汇总

| GPU | 实验 | 状态 | PID | 备注 |
|-----|------|------|-----|------|
| GPU2 | `eval_pi05_random_k09_long_seed43_strict_w41` | **RUNNING** | 610959 | 已启动，正在执行 Task 0（random k=0.9, 230/256 tokens kept） |
| GPU3 | `eval_pi05_l2norm_k095_long_seed43_strict_w41` | **QUEUED** (cascade) | — | 等待 PID 608185 (attention k=0.7 seed42) 结束后自动启动 |

Cascade 脚本每 60s 轮询 PID 608185，结束后 10s 内自动启动 L2norm k=0.95 seed43。GPU3 实验启动后需要将 registry 状态从 QUEUED → RUNNING。

---
