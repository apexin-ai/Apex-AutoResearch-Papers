# deploy westd41074 gpu3 k085 object postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074-gpu3-k085-object-postfix_20260524T022430_result.json`
- **Structured JSON:** [`231c0bbb93345adbb4b2.json`](../../sessions/23/231c0bbb93345adbb4b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

**收割 eval_pi05_random_k085_goal_seed43 (post-fix)**
| Seed | SR | Episodes |
|------|-----|----------|
| 42 | 51.6% | 500 |
| 43 | 52.2% | 500 |
| **均值** | **51.9%** | — |

Baseline 88% → random k=0.85 造成 ~36pp 下降，Wilson CI 95% ≈ [47.8%, 56.5%]。Registry 已更新为 negative。

**已部署 eval_pi05_random_k085_object_seed42_postfix**
- PID: **450953**，westd-41074 GPU 3
- 模型加载成功，CPU RNG fix 已生效（`Device for randperm: cpu`）
- random mode, k=0.85, libero_object, 50eps/task, seed=42
- Registry 状态: RUNNING
- 预计运行 ~90 分钟

---
