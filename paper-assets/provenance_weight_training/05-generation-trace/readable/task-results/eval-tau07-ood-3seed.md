# eval tau07 ood 3seed

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau07_ood_3seed_20260520T010256_result.json`
- **Structured JSON:** [`f65e3b226bf1ca33ef3b.json`](../../sessions/f6/f65e3b226bf1ca33ef3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 OOD eval 全部完成。汇总如下：

## τ=0.7 OOD Results (3-seed)

| Eval Set | τ=0.7 s42 | τ=0.7 s123 | τ=0.7 s456 | τ=0.7 Mean±Std | τ=0.8 Mean | Uniform Mean | Δ(0.7−0.8) | Δ(0.7−Uni) |
|----------|-----------|------------|------------|----------------|------------|--------------|------------|------------|
| OpenWebText | 18.348 | 18.348 | 18.344 | **18.347±0.003** | 18.370 | 18.375 | **-0.023** | **-0.028** |
| Wikipedia   | 15.331 | 15.345 | 15.315 | **15.330±0.015** | 15.355 | 15.359 | **-0.025** | **-0.029** |

τ=0.7 在两个 OOD 数据集上均优于 τ=0.8 和 Uniform baseline——OWT 低 ~0.02-0.03 ppl，Wiki 低 ~0.03 ppl。3-seed 方差极小，结果稳定。

---
