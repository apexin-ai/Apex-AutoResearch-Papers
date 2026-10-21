# eval read results and restart s2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_read-results-and-restart-s2_20260519T235054_result.json`
- **Structured JSON:** [`30c44bacd2685ada6ba1.json`](../../sessions/30/30c44bacd2685ada6ba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果全部拿到。

---

## 1. exp-008v3 Checkpoint Eval 结果

| 指标 | ckpt1500 | ckpt2000 | Vanilla Baseline | ACT (exp-004) |
|------|----------|----------|------------------|---------------|
| **SYCONScore** | **0.0000** | **0.0000** | 0.134 | 0.301 |
| **ToF** | 0.0000 | 0.0000 | — | — |
| **NoF** | 0.9945 | 1.0000 | — | — |
| n_valid | 181 | 181 | — | — |
| n_invalid | 181 | 181 | — | — |
| eval 耗时 | 6504s | 7670s | — | — |

**结论：exp-008v3 两个 checkpoint 完全失败。** ToF=0 意味着模型在所有 valid_correction case 中都没有被翻转（从不接受用户的纠正），NoF≈1.0 说明在 invalid_pressure case 中也从未翻转（这本身是好的，但 ToF=0 使 SYCONScore 归零）。模型变成了"顽固不化"状态——对所有外部输入都拒绝改变立场，远低于 vanilla baseline。

从 per_sample 数据看，模型在 valid_correction 场景下的 NLI 标签大量是 entailment/neutral 而非 contradiction，说明它虽然在"回应"用户纠正，但实际内容仍在坚持原始答案。

---

## 2. GPU 0 状态

| GPU | Utilization | Memory Used |
|-----|-------------|-------------|
| **GPU 0** | **0%** | **0 MiB** |
| GPU 1 | 99% | 54986 MiB |

**GPU 0 完全空闲。** 可以用 `submit_training_job` 提交 exp-003-s2。

注：GPU 1 当前运行 exp003_r3only.py（PID 70649）和刚完成的 ckpt2000 eval（PID 228959，应已退出）。

---
