# diagnosis read all eval results 0520T18

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_read-all-eval-results-0520T18_20260520T165350_result.json`
- **Structured JSON:** [`07f89397a7d6f2317dda.json`](../../sessions/07/07f89397a7d6f2317dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
=== exp-003 eval (d027, 28034) ===
ckpt-1000: ToF=0.0387, NoF=0.9448, SYCONScore=0.0743
ckpt-2000: ToF=0.0442, NoF=0.9834, SYCONScore=0.0846
ckpt-3000: ToF=0.0497, NoF=0.9724, SYCONScore=0.0946
ckpt-4000: ToF=0.0608, NoF=0.9669, SYCONScore=0.1144
ckpt-5000: ToF=0.0608, NoF=0.9669, SYCONScore=0.1144  ← 与 ckpt-4000 完全一致
ckpt-5500: eval 正在跑（GPU 0，已运行 ~33min）

=== exp-003-s2 eval ===
ckpt-500:  结果文件未找到（28034 上无 s2 eval 结果）
ckpt-1000: 结果文件未找到
ckpt-1500: 结果文件未找到
→ s2 的 eval 尚未启动

=== 28034 GPU ===
GPU 0: 48% util, 16884/32607 MiB — 跑 exp-003 ckpt-5500 eval
GPU 1: 0%, 2/32607 MiB — 空闲
GPU 2: 0%, 2/32607 MiB — 空闲
GPU 3: 0%, 2/32607 MiB — 空闲

=== 29046 exp-003-s2 训练 ===
已有 checkpoint: 500, 1000, 1500（无 2000）
训练进度: step 1821/8000, epoch 40.22, reward ~0.48
```

注意 ckpt-5000 和 ckpt-4000 的指标完全相同，可能是模型已饱和或 eval 有问题值得确认。28034 有 3 张空闲 GPU 可以并行跑 s2 的 ckpt-500/1000/1500 eval。

---
