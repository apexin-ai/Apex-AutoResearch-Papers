# eval collect ckpt8000 and chain

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-ckpt8000-and-chain_20260523T024941_result.json`
- **Structured JSON:** [`3c7610c927060ce50738.json`](../../sessions/3c/3c7610c927060ce50738.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部启动完毕。汇报：

---

## 结果汇报

### 1. ACT s2 ckpt-8000 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.2465** |
| ToF | 0.1436 |
| NoF | 0.8674 |

**SYCONScore 0.2465 > vanilla 0.1335**，ckpt-8000 通过。ACT s2 全部 16/16 trajectory 完成评估。

### 2. reduced-lora ckpt-4500 结果（已有）

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.2707** |
| ToF | 0.1602 |
| NoF | 0.8729 |

### 3. 链式启动的 eval 任务

| GPU | 任务 | PID |
|-----|------|-----|
| GPU0 | reduced-lora ckpt-5000 eval | 156229 |
| GPU2 | reduced-lora ckpt-3500 eval | 157352 |
| GPU3 | reduced-lora ckpt-4000 eval | 156793 |

### 4. reduced-lora 训练进度

- 当前 step: **5130**，loss=0.000203
- 可用 checkpoints: 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, **5000**
- checkpoint-5500 尚未产出
- 输出目录: `/root/autodl-tmp/outputs/exp-004-reduced-lora/`

### 5. GPU 状态 (westd-28034)

| GPU | 状态 | 任务 |
|-----|------|------|
| GPU0 | 47%, 16.7GB | rl-ckpt5000 eval |
| GPU1 | 44%, 21.8GB | reduced-lora 训练 (step 5130) |
| GPU2 | 运行中 | rl-ckpt3500 eval |
| GPU3 | 48%, 16.7GB | rl-ckpt4000 eval |

### 6. 备注

- **s2 ckpt-2500** 仅存在于 westd-29046（`/root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-2500`），29046 双 GPU 均在忙（80%/75%），暂无法 eval。需等 29046 GPU 释放或将 checkpoint 拷贝到 28034。

---
