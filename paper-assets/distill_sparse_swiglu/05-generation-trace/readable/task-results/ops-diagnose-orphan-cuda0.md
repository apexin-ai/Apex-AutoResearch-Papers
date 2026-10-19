# ops diagnose orphan cuda0

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_orphan_cuda0_20260516T052126_result.json`
- **Structured JSON:** [`203e0ce2a931b514e31d.json`](../../sessions/20/203e0ce2a931b514e31d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### PID 207957 (bench_mistral_kl50_s42)
**已死亡**，无需 kill。进程不存在，cuda:0 上无残留。

### GPU 状态

| GPU | 显存 | 利用率 | 温度 | 功耗 | 进程 |
|-----|------|--------|------|------|------|
| cuda:0 | **0 MiB** / 97887 MiB | 100%* | 44°C | 99W | 无 |
| cuda:1 | 90947 MiB / 97887 MiB | 100% | 65°C | 450W | PID 205598 (python train.py) |

*cuda:0 显示 100% utilization 但 0 进程 0 显存，属于驱动计数器残留，不影响使用。**cuda:0 当前空闲可用。**

### bce_isocompute_v3_s42 训练进度 (cuda:1)
- **当前 step: 2400 / 2700**（88.9%）
- 速度: 1.05s/step，**预计 ~5 分钟后完成**
- 最新指标: loss=0.6359, bce=0.6349, reg=0.0011, sparsity=0.511
- Loss 从 0.666 → 0.636 平稳下降，sparsity 稳定在 ~0.51
- PID 205597 (bash) + 205598 (python) 均存活，运行 43 分钟

---
