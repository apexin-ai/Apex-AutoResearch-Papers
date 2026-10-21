# ssh check 34887 and collect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_34887_and_collect_20260520T134805_result.json`
- **Structured JSON:** [`856662ce79fe82a43f5f.json`](../../sessions/85/856662ce79fe82a43f5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 型号 | 温度 | 功耗 | 显存 | 利用率 | 进程 |
|-----|------|------|------|------|--------|------|
| cuda:0 | RTX PRO 6000 Black (98GB) | 82°C | 606W/600W | 45.8/97.9 GB | 100% | PID 212473 — s123 eval |
| cuda:1 | RTX PRO 6000 Black (98GB) | 48°C | 242W/600W | 45.8/97.9 GB | 65% | PID 215424 — s456 eval |

### Mistral KL30 s123 (GPU 0)

- **训练**: 完成。Step 1000/1000, loss=0.0996, kl_norm=0.0996, sparsity=0.281, lambda=5000
- **Checkpoint**: `checkpoints/mistral_kl30_s123/predictor_kl_normalized.pt` (152MB, 20:53)
- **Eval**: 进行中 — MMLU loglikelihood **31%** (12657/40168), ~19.4 it/s
  - arc_challenge, winogrande 已完成
  - MMLU 剩余 ~24 min, 之后还有 gsm8k (~25 min), hellaswag, piqa
  - **预计完成**: ~50-60 min

### Mistral KL30 s456 (GPU 1)

- **训练**: 完成。Step 1000/1000, loss=0.1050, kl_norm=0.1050, sparsity=0.281, lambda=5000
- **Checkpoint**: `checkpoints/mistral_kl30_s456/predictor_kl_normalized.pt` (152MB, 21:23)
- **Eval**: 进行中 — GSM8K generate_until **28%** (369/1319), ~1.14 s/it
  - arc_challenge, winogrande, mmlu 已完成
  - GSM8K 剩余 ~18 min, 之后还有 hellaswag, piqa
  - **预计完成**: ~30 min

### 结果

两个 eval 目录 (`mistral_kl30_s123_eval/`, `mistral_kl30_s456_eval/`) 均为空——results.json 在全部 7 个 task 跑完后才写入。s456 预计先完成（~22:20），s123 约 22:50。

---
