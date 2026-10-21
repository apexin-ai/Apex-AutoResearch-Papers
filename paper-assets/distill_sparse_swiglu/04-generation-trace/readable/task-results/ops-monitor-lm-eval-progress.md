# ops monitor lm eval progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor_lm_eval_progress_20260515T231946_result.json`
- **Structured JSON:** [`a6d261e421c9c4fa46de.json`](../../sessions/a6/a6d261e421c9c4fa46de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 0 — lm_eval_kl_s42 (PID 171565, 运行 16m39s)
- **当前阶段**: loglikelihood requests 87% (48845/56168)，速度 ~225 it/s
- **已完成**: arc_challenge, winogrande, mmlu 的 tokenization 预处理
- **当前**: 正在执行合并 loglikelihood 批次（arc+winogrande+mmlu），约 30s 完成
- **待执行**: gsm8k generate_until（~1319 items，~1 it/s ≈ 22min）
- **预估剩余**: ~22-25 分钟
- GPU 利用率 97%，显存 29.8GB/96GB，正常

### GPU 1 — lm_eval_dense (PID 163723, 运行 31m27s)
- **已完成**: arc_challenge ✓, winogrande ✓ (acc=0.7814, 86s), mmlu ✓
- **当前阶段**: gsm8k generate_until 32% (425/1319)，已跑 7m02s，速度 ~1.1 it/s
- **预估剩余**: ~13-15 分钟
- GPU 利用率 91%，显存 29.8GB/96GB，正常

### 异常检查
- 两个进程均存活（状态 Rl+/Rl），无异常
- 无错误日志（仅有 HF_TOKEN 警告和 git repo 警告，不影响评估）
- 两张 GPU 均满载运行

### 结论
- **GPU 1 (dense) 将在约 15 分钟后释放**，先于 GPU 0 完成
- GPU 0 (kl_s42) 约 25 分钟后完成
- 结果文件尚未写入 `results/lm_eval/` 目录（均在运行中，完成后才写）

---
