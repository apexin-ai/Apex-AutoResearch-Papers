# ssh training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-progress-check_20260521T180213_result.json`
- **Structured JSON:** [`50b72a375d767c94cf04.json`](../../sessions/50/50b72a375d767c94cf04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### 1. Qwen s123 训练 (GPU 0, PID 4271)
- **状态**: 存活，运行 20h23m
- **进度**: step ~6000/6633 (90%)，正在跑 step 6000 的 eval（5936/9335 样本）
- **ETA**: ~2h（含 eval 时间）
- **GPU 0**: 98%, 30553/32607 MiB

### 2. Qwen s456 训练 (GPU 3, PID 4561)
- **状态**: 存活，运行 20h22m
- **进度**: step 6150/6633 (92.7%)，~12s/step
- **ETA**: ~1.5h
- **GPU 3**: 97%, 25559/32607 MiB

### 3. DS s123 训练 (GPU 2, PID 28200)
- **状态**: 存活，运行 13h38m
- **进度**: 最新 checkpoint 8418/12627 (67%)。按 ~8s/step 推算，当前约 step ~10200 (81%)
- **ETA**: ~5-6h
- **GPU 2**: 99%, 20501/32607 MiB
- 注：输出目录实为 `checkpoints_deepseek_cwm_repo_s123_v2/`（非 v3），日志为 `deepseek-cwm-repo-s123-train-v2.log`

### 4. DS s456 e3 eval (GPU 1, PID 63490)
- **状态**: 存活，运行 4h15m
- **进度**: 3324/9784 样本 (34%)，~13 样本/min
- **ETA**: ~8.3h
- **GPU 1**: 85%, 30427/32607 MiB

---

Qwen 两个种子预计 1.5-2h 内完成，DS s123 训练约 5-6h，DS s456 eval 最慢约 8h。全部 4 GPU 满载运行。

---
