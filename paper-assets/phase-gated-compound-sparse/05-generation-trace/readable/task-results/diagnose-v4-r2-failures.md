# diagnose v4 r2 failures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4_r2_failures_20260513T234353_result.json`
- **Structured JSON:** [`d83868f95982cab84c2a.json`](../../sessions/d8/d83868f95982cab84c2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验 registry 已更新。

## 诊断结论

| 项目 | 详情 |
|------|------|
| **根因** | GPU OOM — `compute_dense_forward_with_importance()` (interaction_index.py:302) 使用 `output_attentions=True` 对完整序列做 forward，同时在 GPU 上物化全部 28 层的 attention 矩阵 |
| **内存估算** | ~1700 token 序列：28 层 × 28 头 × 1700² × 2B ≈ 4.5 GB attention + ~14 GB 模型权重 → 超出单卡 VRAM |
| **为何静默** | 进程被 SIGKILL（系统 OOM killer），无法捕获，stderr 缓冲区未刷新 |
| **为何 random 正常** | random 方法调用 `compute_dense_ce_losses()` 不使用 `output_attentions=True`，不物化 attention 矩阵 |
| **error_type** | code |
| **修复方向** | 逐层 hook 提取 importance（前向传播时即时计算每层 Frobenius norm / cumulative attention，不存储完整 attention tensor） |

`mvp_v4_random_r2` 仍在运行中（PID 32187, elapsed 15 min, 已完成 13/50 问题）。

---
