# ops check 3tasks status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_3tasks_status_20260520T053359_result.json`
- **Structured JSON:** [`b418dc11a2d783053371.json`](../../sessions/b4/b418dc11a2d783053371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 任务 1: SNR full curve — **已完成**
- PID 175225 已退出
- 结果文件已生成：`snr_full_1000steps_results.json`（77KB，May 20 12:54）
- KL 和 BCE 两组数据完整，14 个 snapshot steps（0→1000）
- KL SNR 轨迹：1.3e-5 → 6.1e-4（peak@100）→ 稳定在 2~6e-4 → 最终 8.8e-4
- BCE SNR 轨迹：7.0e-5 → 上升到 5.1e-3（peak@600）→ 最终 2.0e-3
- KL sparsity 从 0.41 收敛到 ~0.30；BCE sparsity 从 0.50 收敛到 ~0.30

### 任务 2: KL 40% retrain+eval — **失败**
- PID 187509 已退出
- **原因：wandb API key 未配置**，`wandb.init()` 抛 `UsageError: No API key configured`
- Checkpoint 未生成（`predictor_kl_normalized.pt` 不存在）
- 需要先在服务器上 `wandb login` 或设置 `WANDB_API_KEY` 环境变量后重跑

### 任务 3: westd-41718 — **空闲**
- GPU 0: 0 MiB / 0% util
- GPU 1: 0 MiB / 0% util
- 无 python 训练进程

---
