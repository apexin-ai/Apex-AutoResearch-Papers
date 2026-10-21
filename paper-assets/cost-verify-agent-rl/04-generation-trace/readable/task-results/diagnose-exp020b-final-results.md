# diagnose exp020b final results

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020b-final-results_20260515T005413_result.json`
- **Structured JSON:** [`1074e4315d58f024f9db.json`](../../sessions/10/1074e4315d58f024f9db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp020b GRPO 训练状态汇总

### 1. 进程状态：**正在运行**

- `train.py` 进程活跃（PID 385982），启动时间 06:12 UTC
- Ray GCS server + 多个 `ray::IDLE` worker + `ray::TaskRunner.run` + 2× `ray::WorkerDict` 均在运行
- 无 error/OOM/killed

### 2. GPU 使用

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 100% | 48857 MiB |
| 1 | 100% | 48769 MiB |

### 3. 训练进度：**21/30 steps (70%)**

当前在 step 21，已运行约 2h36m，预计剩余 ~1h11m。

### 4. 逐步 metrics（关键指标）

| Step | train success | val success | pg_loss | ppo_kl | entropy | grad_norm | critic/score/mean |
|------|--------------|-------------|---------|--------|---------|-----------|-------------------|
| 0 (init val) | — | 0.0 | — | — | — | — | — |
| 1 | **0.1875** | — | 6.39e-5 | 9.30e-5 | 0.107 | 2.777 | 1.875 |
| 20 | **0.125** | **0.0** | -6.71e-4 | 0.00918 | 0.045 | 5.577 | 1.25 |

**观察：**
- train success 从 step 1 的 18.75% 下降到 step 20 的 12.5%
- val success 始终为 **0.0**（4 个 val 环境全部失败）
- entropy 从 0.107 下降到 0.045（策略在坍缩）
- ppo_kl 从 ~0 增长到 0.0092（策略偏离 reference 中）
- pass@16 (train) 始终为 1.0（说明多样性足够，至少有解，只是 greedy/平均太差）

### 5. Checkpoints

```
/root/autodl-tmp/checkpoints/exp020b/
├── global_step_5/   (空目录)
├── global_step_10/  (actor/)
├── global_step_15/  (actor/)
├── global_step_20/  (actor/ — 含 model .pt, optimizer .pt, huggingface config)
└── latest_checkpointed_iteration.txt → "20"
```

每 5 步保存一次，最新 checkpoint 为 step 20，包含完整的 FSDP sharded model + optimizer state。

### 6. 错误

**无任何 error/exception/OOM/traceback。** 训练运行完全正常。

---

### 结论

训练**仍在运行中**，尚未跑完 30 步（当前 21/30）。预计约 1 小时后完成。但 **val success rate 为 0，train success rate 也在下降（18.75% → 12.5%），entropy 持续降低** — 模型正在经历策略坍缩，GRPO 训练效果不佳。

---
