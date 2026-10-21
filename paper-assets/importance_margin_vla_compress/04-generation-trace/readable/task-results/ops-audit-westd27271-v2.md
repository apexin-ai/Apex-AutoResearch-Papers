# ops audit westd27271 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd27271_v2_20260522T054035_result.json`
- **Structured JSON:** [`c0164c88753273b151d9.json`](../../sessions/c0/c0164c88753273b151d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### GPU 状态

| GPU | PID | 实验 | 显存占用 | GPU 利用率 |
|-----|-----|------|----------|-----------|
| 0 | 9470 | `random k=0.95 spatial seed43` | 10,630 / 97,887 MiB | 31% |
| 1 | 9613 | `l2norm k=0.85 spatial seed43` | 10,614 / 97,887 MiB | 28% |

两张 GPU 均被已知实验占用，**无异常进程**。

### 实验进度

libero_spatial 共 10 个 task（T0-T9），每个 50 episodes。

**random k=0.95**（GPU 0）— 7/10 tasks 完成，正在跑 T7 (ep 10/50)，约 **72%**
- 已完成 task 分数：T2=100%, T3=60%, T4=36%, T5=76%, T6=90%
- 累计：278/350 = **79.4%**

**l2norm k=0.85**（GPU 1）— 8/10 tasks 完成，正在跑 T8 (ep 20/50)，约 **82%**
- 已完成 task 分数：T3=78%, T4=62%, T5=84%, T6=96%, T7=90%
- 累计：351/400 = **87.8%**

### 结论

- 两张 GPU 都在正常跑上一轮部署的实验，状态健康
- 预计 random 还需 ~25 min，l2norm 还需 ~15 min 完成
- **空闲 GPU：0 张**

---
