# ops westd 34887 gpu check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-34887-gpu-check_20260518T061334_result.json`
- **Structured JSON:** [`6c720d2cff6f9c71ddda.json`](../../sessions/6c/6c720d2cff6f9c71ddda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 型号 | 显存占用 | GPU Util | 温度 | 功耗 |
|-----|------|---------|----------|------|------|
| cuda:0 | RTX PRO 6000 Black | 66988 / 97887 MiB | 64% | 48°C | 235W/600W |
| cuda:1 | RTX PRO 6000 Black | 67569 / 97887 MiB | 100% | 80°C | 581W/600W |

### 实验状态

**1. kl50_s123_uniform_eval (cuda:0, PID 3143)**
- 命令: `src/benchmark_eval.py`, tasks=wikitext2,arc_challenge,winogrande,mmlu,gsm8k
- 配置: TEAL global sparsity 50%, uniform allocation, checkpoint=kl_50pct_s123
- 进度: 正在跑 `generate_until` 请求，281/1319 (21%)，速度 ~1.13s/it，预计当前 task 剩余约 20 分钟。前面几个小 benchmark 已完成。

**2. kl50_s456_train (cuda:1, PID 2589)**
- 命令: `src/train.py`, seed=456, kl_normalized loss, 1000 steps
- 进度: **step 730/1000** (73%)，剩余 270 steps
- 训练指标 (step 730): loss=0.324, sparsity=0.492 (接近目标 0.5), constraint=0.0 (已满足), tau=0.343, lr=2.06e-04
- 训练稳定，loss 在 0.28-0.36 之间波动，sparsity 收敛于 0.48-0.50

注意：用户提供的 PID 100563 与实际 PID 2589 不符，可能进程重启过。cmdline 显示 `--gpu 0`，但 nvidia-smi 显示在 GPU 1 上，推测有 `CUDA_VISIBLE_DEVICES` 重映射。

---
