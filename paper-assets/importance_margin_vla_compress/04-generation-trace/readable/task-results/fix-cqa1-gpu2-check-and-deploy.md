# fix cqa1 gpu2 check and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-gpu2-check-and-deploy_20260525T215800_result.json`
- **Structured JSON:** [`a11def96989864ac1b9b.json`](../../sessions/a1/a11def96989864ac1b9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型还在 CPU 加载阶段（π0.5 权重大，加载需 1-2 分钟）。进程正常运行中。

---

**总结：**

| 项目 | 状态 |
|------|------|
| **zeromask_l2norm k=0.9 Object seed42** | ✅ DONE — SR=**99.4%** (497/500) |
| **对比基准** hard-prune l2norm k=0.9 Object | 已知 SR≈96-98% |
| **结论** | zero_mask_l2norm 保留位置+置零反而比 hard-prune 更好，说明 π0.5 linear connector 对 token 位置有轻微依赖但信息移除不影响太多 |

| **新实验部署** | eval_pi05_random_k075_long_seed42 |
|------|------|
| GPU | cqa1-33015 GPU2 |
| PID | 802254 |
| tmux | eval_random_k075_long |
| Registry | RUNNING |
| 预计用时 | ~3-4 小时 (10 tasks × 50 eps) |

---
