# ssh check jsd and 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_jsd_and_34887_20260520T161023_result.json`
- **Structured JSON:** [`dbda0a0618a9d59d2114.json`](../../sessions/db/dbda0a0618a9d59d2114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 实验 | GPU | Step | Loss | Sparsity | Lambda | Tau | 状态 |
|------|-----|------|------|----------|--------|-----|------|
| **JSD 30% s42** | cuda:0 (75GB/98GB, 100%) | **500/1000** | 0.0352 | 0.289 | 1310.72 | 0.550 | 正常 |
| **Reverse KL 30% s42** | cuda:1 (71GB/98GB, 100%) | **510/1000** | 0.2002 | 0.301 | 5000.00 | 0.541 | 正常 |

**关键观察**：

- **Sparsity**：两个实验都稳定在 0.28–0.31 范围，接近 target=0.3，constraint≈0，约束满足良好
- **Lambda**：JSD 的 lambda 在 300–2600 间振荡（PID 控制还在调节）；Reverse KL 已触及 lambda_max=5000 并稳定
- **Loss**：JSD loss ~0.035 远低于 Reverse KL ~0.20，符合 JSD 量纲更小的预期
- **进度**：两者约 50% 完成，Reverse KL 比 JSD 快约 10 步，预计还需数小时

---
