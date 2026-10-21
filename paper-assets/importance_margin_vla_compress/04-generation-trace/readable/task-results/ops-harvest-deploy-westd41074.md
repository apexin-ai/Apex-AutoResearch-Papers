# ops harvest deploy westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-deploy-westd41074_20260524T070425_result.json`
- **Structured JSON:** [`f25689ff54ab1f06ba1a.json`](../../sessions/f2/f25689ff54ab1f06ba1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验都在加载模型，正常启动。

---

## 收割结果汇总

| 实验 | GPU | SR | 对比 |
|------|-----|-----|------|
| L2norm k=0.925 Goal seed42 v3 | 0 | **89.8%** | > baseline (88.4%), L2norm graceful degradation 极好 |
| Random k=0.85 Spatial seed42 v3 | 2 | **60.2%** | 与 v2 (60.8%) 一致，baseline=78% → -17.8pp |
| L2norm k=0.85 Spatial seed42 v3 | 3 | **88.4%** | > baseline (78%) → **+10.4pp**，importance margin vs random = **+28.2pp** |

关键发现：L2norm k=0.85 Spatial 的 88.4% **超过了 baseline 78%**，移除 15% token 后性能反而提升。Random 同参数仅 60.2%，importance margin 达 28.2pp。

## 新实验部署

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval_pi05_random_k0925_object_seed42_postfix (PID 827992) | RUNNING |
| 1 | eval_pi05_random_k0925_goal_seed42_v3 (PID 828073) | RUNNING |
| 2 | eval_pi05_random_k095_spatial_seed42_postfix_v2 (PID 828215) | RUNNING |
| 3 | 空闲（L2norm k=0.85 Spatial v3 有效，无需 v4；无 pending 实验） | IDLE |

---
