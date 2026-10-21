# ops check westd38929 gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd38929-gpu_20260520T143134_result.json`
- **Structured JSON:** [`52f2eacd8dc8ccc2fb65.json`](../../sessions/52/52f2eacd8dc8ccc2fb65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. GPU 状态（4×RTX PRO 6000 Blackwell 96GB）

| GPU | PID | k 值 | 显存 | GPU 利用率 | 运行时间 | 状态 |
|-----|--------|------|------|-----------|---------|------|
| 0 | 787425 | 0.5 | 15,961 MiB | 69% | 1h37m | **存活 (Rl)** |
| 1 | 788043 | 0.3 | 16,089 MiB | 68% | 1h36m | **存活 (Rl)** |
| 2 | 796062 | 0.9 | 15,961 MiB | 64% | 1h14m | **存活 (Rl)** |
| 3 | 796839 | 0.95 | 15,961 MiB | 69% | 1h13m | **存活 (Rl)** |

### 2. 各 k 值当前进度

**k=0.5 (GPU 0)** — Task 4/10, Ep 10/50
- T1: 56% (28/50) ✓ | T2: 14% (7/50) ✓ | T3: 38% (19/50) ✓ | T4: 进行中

**k=0.3 (GPU 1)** — Task 4/10, 刚开始
- T1: 42% (21/50) ✓ | T2: 6% (3/50) ✓ | T3: 28% (14/50) ✓ | T4: 进行中

**k=0.9 (GPU 2)** — Task 3/10, Ep 40/50
- T1: 66% (33/50) ✓ | T2: 58% (29/50) ✓ | T3: 进行中 (25/40)

**k=0.95 (GPU 3)** — Task 3/10, Ep 30/50
- T1: 48% (24/50) ✓ | T2: 52% (26/50) ✓ | T3: 进行中 (24/30)

### 3. 结果 JSON

尚无 D108 l2norm 结果 JSON 输出。目录中现有的 `xvla_prune_k*.json` 是之前 xvla 实验的结果。

### 预计剩余时间

以 ~1.8 eps/min 估算，每个 k 值共 500 episodes (10 tasks × 50 eps)：
- k=0.5 / k=0.3：已完成 ~30-32%，剩余 **~3h**
- k=0.9 / k=0.95：已完成 ~26-28%，剩余 **~3.3h**

---
