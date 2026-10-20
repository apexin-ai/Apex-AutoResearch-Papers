# status 41312 gpu audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_41312-gpu-audit_20260516T184851_result.json`
- **Structured JSON:** [`1f4d4a331ee371c74c1b.json`](../../sessions/1f/1f4d4a331ee371c74c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### GPU 占用（4x H800 98GB）

| GPU | PID | 进程 | 显存占用 | GPU利用率 |
|-----|-----|------|---------|-----------|
| 0 | 324550 | threshold_q07_seed42 (resume from ckpt-2000) | 75GB/98GB | 61% |
| 1 | 316988 | rho02_uniform_seed42 | 75GB/98GB | 100% |
| 2 | 326280 | batch_adaptive_tau_rho04_seed42 | 75GB/98GB | 74% |
| 3 | 325202 | threshold_q03_seed42 | 75GB/98GB | 99% |

**空闲 GPU: 无，4卡全满。**

### 当前运行实验进度

| 实验 | step_metrics 行数 | 当前 step | 目标 tokens | 状态 |
|------|-------------------|-----------|-------------|------|
| rho02_uniform_seed42 | 20,000 | 4999 | 200M | 运行中 |
| threshold_q07_seed42 | 24,940 | 5999 | 200M | 运行中 (resumed from ckpt-2000) |
| threshold_q03_seed42 | 16,000 | 3999 | 200M | 运行中 |
| batch_adaptive_tau_rho04_seed42 | 16,000 | 3999 | 200M | 运行中 |

每个实验 batch_size=4, grad_accum=4, max_length=2048 → 每 step 约 32K tokens → 200M tokens ≈ 6250 steps。

**预估完成度：**
- threshold_q07: ~96% (5999/6250)
- rho02_uniform: ~80% (4999/6250)
- threshold_q03: ~64% (3999/6250)
- batch_adaptive_tau_rho04: ~64% (3999/6250)

### hybrid / llama3b

**hybrid_rho04、hybrid_rho06：不存在。** 服务器上没有任何 hybrid 相关的 step_metrics 或进程。

**llama3b：不存在。** 服务器上没有任何 llama3b 相关的 step_metrics 或进程。

### 磁盘

| 挂载点 | 容量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 250G | 206G | 45G | 83% |

---
