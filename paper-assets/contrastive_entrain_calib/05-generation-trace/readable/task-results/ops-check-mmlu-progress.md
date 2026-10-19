# ops check mmlu progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-mmlu-progress_20260524T061634_result.json`
- **Structured JSON:** [`353843f74ebd20e141b7.json`](../../sessions/35/353843f74ebd20e141b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. MMLU/GSM8K Eval (GPU0)

| 模型 | MMLU (5-shot) | GSM8K (5-shot) | 状态 |
|------|-------------|----------------|------|
| **Vanilla Qwen3-8B** | **0.7493** | **0.8764** (strict) / 0.8832 (flex) | ✅ 完成 |
| **ACT s1 ckpt8000** | **0.7356** (-1.37%) | 510/1319 (38.7%) 进行中 | ⏳ GSM8K ~1h20m 剩余 |
| **R3-only s1 ckpt6500** | — | — | ⏸ 未开始 |

当前正在跑 ACT s1 的 GSM8K，之后还要跑 R3-only 的 MMLU + GSM8K。无报错。

ACT s1 的 MMLU 比 vanilla 下降了 1.37%（0.7493 → 0.7356），各子类均有小幅下降（humanities -1.5%, other -1.5%, social_sci -1.6%, stem -0.8%）。

### 2. exp-003-len512-v3 (GPU1)

| 指标 | 值 |
|------|-----|
| 进度 | **2136/8000** (26.7%) |
| 最新 checkpoint | checkpoint-2000 (May 24 12:32) |
| 速度 | ~46.5s/step |
| 剩余 | 5864 steps × 46.5s ≈ **75.7h (~3.15天)** |
| 预计完成 | **~May 27 18:00** |

下一个 checkpoint-2500 预计约 4.7h 后（~18:55 今天）。

### GPU 状态
- GPU0: 100% util, 35.7/97.9 GB (eval)
- GPU1: 95% util, 41.3/97.9 GB (training)

---
