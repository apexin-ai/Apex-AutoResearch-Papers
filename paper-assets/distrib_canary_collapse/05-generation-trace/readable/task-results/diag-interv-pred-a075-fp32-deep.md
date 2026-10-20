# diag interv pred a075 fp32 deep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_interv_pred_a075_fp32_deep_20260518T231703_result.json`
- **Structured JSON:** [`7748466aaabd7250a1e9.json`](../../sessions/77/7748466aaabd7250a1e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过，实验正常运行：

- **tmux session** `interv_pred_a075_s42_fp32` 存在
- **PID 63323** 存活，CPU 136%，运行 5min+
- **cuda:4** 占用 2494 MiB
- **日志** 显示模型加载成功，正在 Generation 0 (baseline) 的 synthetic data 生成阶段

## 诊断总结

| 项目 | 结果 |
|---|---|
| **报告的问题** | EXIT_CODE=127 反复失败 |
| **根因 1 (EXIT_CODE=127)** | 首次提交未激活 conda → `python: command not found`。旧日志 `~/runs/interv_pred_a075_s42_fp32.log` (54 bytes) 记录了这个错误 |
| **根因 2 (真正的崩溃)** | 后续 Worker 修复了 conda 问题，实验跑到 Gen 1 metrics 时崩溃：`np.linalg.eigvalsh(cov)` → `LinAlgError: Eigenvalues did not converge`。Gen 1 训练末期已出现 `loss=0, grad_norm=nan`（模型坍缩导致协方差矩阵病态） |
| **根因 3 (Worker 误判)** | 之前的 Worker 看到进程启动就报告"已修复"，但没等够时间验证（进程在 Gen 1 metrics 阶段才崩溃，约 10-15 分钟后） |
| **修复** | 1) `metrics.py` `compute_effective_rank`: 添加 NaN/Inf 前置检查 + eigvalsh→SVD fallback + 空特征值 guard。2) 通过 tmux 重新提交，确保 conda 激活。3) Kill 了使用旧代码的 v2 进程 |
| **当前状态** | PID 63323 在 cuda:4 上正常运行，Gen 0 进行中 |

---
