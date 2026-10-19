# diag 28034 gpu and eval results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_28034-gpu-and-eval-results_20260522T220009_result.json`
- **Structured JSON:** [`2ba3ffe5bdeabfb2b504.json`](../../sessions/2b/2ba3ffe5bdeabfb2b504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 全部仍在运行中，均未完成。以下是当前状态：

```
GPU状态:
- GPU0: PID 133996 — eval exp-004-s2-v2-ckpt6000 (运行 19min, 17660MiB/32607MiB, 42%)
- GPU1: PID 30011  — training run_exp004_reduced_lora.py (运行 5h20m, 21768MiB/32607MiB, 61%)
- GPU2: PID 134523 — eval exp-004-s2-v2-ckpt5500 (运行 19min, 17660MiB/32607MiB, 39%)
- GPU3: PID 131250 — eval exp-003-gs8-ckpt500-verified (运行 43min, 16874MiB/32607MiB, 44%)

Eval 结果:
- ACT s2 ckpt-5500: 仍在运行 (260/362, ~72%, 预计 ~6min 后完成)
- ACT s2 ckpt-6000: 仍在运行 (300/362, ~83%, 预计 ~4min 后完成)
- gs8 ckpt-500 verify: 仍在运行 (200/362, ~55%, 预计 ~35min 后完成，速度较慢)

额外发现:
- GPU1 在跑 exp004_reduced_lora 训练（已跑 5h20m）
- /tmp/eval_reduced_lora_ckpt500_v2.log 已完成，结果在:
  eval_results/exp-004-reduced-lora-ckpt500_preset_eval.json
- gs8 eval 速度明显慢于另两个（batch_size 相同但每 20 样本耗时 ~4min vs ~1.2min），
  可能是与 GPU1 训练共享 PCIe 带宽导致
```

ckpt-5500 和 ckpt-6000 的 eval 再等几分钟就能出结果，gs8 还需要约半小时。要等它们完成后再来收集结果吗？

---
