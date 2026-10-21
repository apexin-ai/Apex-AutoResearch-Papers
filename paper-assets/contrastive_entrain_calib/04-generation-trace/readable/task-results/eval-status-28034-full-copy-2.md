# eval status 28034 full

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_status-28034-full_20260522T133703_result.json`
- **Structured JSON:** [`08328b24e86896fcf601.json`](../../sessions/08/08328b24e86896fcf601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
4× GPU 全部空闲（0% 利用率，2 MiB/32607 MiB）

### 进程状态
**无任何 Python 训练/eval 进程在运行。** 仅有系统服务（supervisord, tensorboard, jupyter-lab）。

### Eval 结果

| 实验 | Checkpoint | ToF | NoF | SYCONScore | 耗时 |
|------|-----------|-----|-----|------------|------|
| exp-002v3 | ckpt-500 | 0.0000 | 1.0000 | **0.0000** | 1229s |
| exp-002v3 | ckpt-1000 | 0.0000 | 1.0000 | **0.0000** | 1320s |
| exp-002v3 | ckpt-1500 | 0.0000 | 1.0000 | **0.0000** | 1282s |
| exp-002v3 | ckpt-2000 | 0.0000 | 1.0000 | **0.0000** | 1200s |
| exp-003-s2 | ckpt-7500 | 0.0608 | 0.9669 | **0.1144** | 4407s |

所有 eval 样本 n=362（181 valid + 181 invalid）。

### 关键发现
- **exp-002v3 全部 4 个 checkpoint 的 SYCONScore = 0**，ToF=0 / NoF=1，模型完全没学到 sycophancy 区分能力（LoRA: `exp002v3_dcgrpo_scaled_cosine`）
- **exp-003-s2 ckpt-7500 SYCONScore = 0.1144**，有微弱信号（ToF=0.0608, NoF=0.9669），LoRA 来自 `checkpoints_r3only_s2`
- **exp-004-s2-ckpt2000** 目录为空，未产出结果
- 所有 eval 已完成，GPU 空闲，无正在运行的进程

---
