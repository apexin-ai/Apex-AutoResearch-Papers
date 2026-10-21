# ops seed43 result check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed43-result-check_20260518T115032_result.json`
- **Structured JSON:** [`5de8e7394b0ded87e640.json`](../../sessions/5d/5de8e7394b0ded87e640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### gpt2xl_seed43_001 (GPU1, PID 868749)

| 阶段 | 状态 |
|---|---|
| depth_0 生成 (5000) | 完成 |
| depth_0 LoRA 训练 | 完成 |
| depth_1 生成 (5000) | 完成 |
| depth_1 LoRA 训练 | 完成 |
| depth_2 生成 (5000) | 完成 |
| depth_2 LoRA 训练 | 完成 (loss=1.326, 3 epochs, 681s) |
| **depth_3 生成 (5000)** | **进行中: 3230/5000 (64.6%)** |

- 原始 PID 857779 已结束，当前新进程 PID 868749 (15.6GB VRAM, 70% util)
- 无 summary.json，预计 depth_3 生成完后还需训练 depth_3 LoRA + 后续 pipeline 步骤

### qwen25_14b_scale_002 (GPU0, PID 806751)

| 阶段 | 状态 |
|---|---|
| 模型下载 | 完成 (8/8 shards, 下载错误已恢复) |
| depth_0 生成 (5000) | 完成 |
| depth_1 生成 (5000) | 完成 |
| depth_1 LoRA 训练 | 完成 (loss=0.339, 3 epochs, 2429s) |
| depth_2 生成 (5000) | 完成 |
| **depth_2 LoRA 训练** | **进行中: 894/939 steps (95%), ~2min 剩余** |

- GPU0 满载: 34.7GB VRAM, 100% util, 80°C, 603W
- 训练速度 ~2.5s/step，即将完成 d2 训练，之后进入 d3 生成阶段
- 14B 比 GPT2-XL 慢约 3.5x（单步 2.5s vs 0.7s）

---
