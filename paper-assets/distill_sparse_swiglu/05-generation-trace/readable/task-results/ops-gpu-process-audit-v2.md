# ops gpu process audit v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_process_audit_v2_20260516T002401_result.json`
- **Structured JSON:** [`ab8aac1ce1d7d2792038.json`](../../sessions/ab/ab8aac1ce1d7d2792038.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 (2026-05-16)

### GPU 占用

| GPU | 型号 | 显存占用 | GPU 利用率 | 进程 |
|-----|------|----------|-----------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 21.3 / 97.9 GB (22%) | 92% | 1 个进程 |
| cuda:1 | RTX PRO 6000 Blackwell | 74.2 / 97.9 GB (76%) | 94% | 4 个进程 |

### 进程明细

| PID | GPU | 显存 | 运行时间 | 任务 |
|-----|-----|------|---------|------|
| 181121 | cuda:0 | 21.2 GB | 19 min | `eval_benchmark.py --condition mistral_dense --tasks lm_eval` |
| 174850 | cuda:1 | 21.3 GB | 50 min | `eval_benchmark.py --condition mistral_kl_s42 --tasks lm_eval` |
| 179918 | cuda:1 | 16.4 GB | 32 min | `lm_eval_sparse.py --predictor kl_normalized --sparsity 0.5` |
| 182573 | cuda:1 | 18.3 GB | 11 min | `diag_hflm.py` |
| 182747 | cuda:1 | 18.3 GB | 10 min | `diag_hflm.py` |

### lm_eval_kl_s42 官方结果 (已完成，保存在 plan_007/)

| arc_challenge | winogrande | mmlu | gsm8k |
|---------------|-----------|------|-------|
| 0.3771 | 0.6156 | 0.2591 | 0.0121 |

耗时 3010s，EXIT_CODE=129。PID 179918 是一次重跑，输出目录 `lm_eval_kl_s42/` 尚未创建，仍在运行中。

### Mistral lm-eval 进度

- **Mistral dense** (PID 181121): gsm8k generate_until **9%** (113/1319)，~1.1s/it，预计还需 ~22 min
- **Mistral KL s42** (PID 174850): gsm8k generate_until **49%** (645/1319)，~2.5s/it，预计还需 ~28 min
- 输出目录 `plan_009_mistral/` 目前为空

### 空闲状况

**无空闲 GPU。** cuda:0 利用率 92% 但显存余量大 (76 GB 空闲)；cuda:1 显存接近饱和 (24 GB 空闲)，跑着 4 个进程。两个 `diag_hflm.py` 进程各占 18 GB，来源不明——可能需要确认是否是预期任务。

---
