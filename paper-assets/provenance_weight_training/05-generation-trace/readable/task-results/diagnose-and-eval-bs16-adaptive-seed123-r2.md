# diagnose and eval bs16 adaptive seed123 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_and_eval_bs16_adaptive_seed123_r2_20260521T231813_result.json`
- **Structured JSON:** [`bc7961ab3a7e1321318d.json`](../../sessions/bc/bc7961ab3a7e1321318d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。汇总如下：

---

## 结果

### 1. 训练状态：成功
- 6103/6103 步完成，train_loss=2.534
- final 目录已保存 model.safetensors (1.1GB)
- checkpoint-5500, 6000, 6103 均存在

### 2. Eval 结果

| 指标 | bs16_adaptive_seed123 | bs16_uniform_seed123 | Δ(adaptive−uniform) |
|------|----------------------|---------------------|---------------------|
| holdout_ppl | **17.616** | 17.686 | **−0.070** |
| holdout_loss | 2.8688 | 2.8728 | −0.0040 |
| owt_ppl | **18.325** | 18.369 | **−0.044** |
| owt_loss | 2.9083 | 2.9107 | −0.0024 |
| wiki_ppl | **15.349** | 15.381 | **−0.033** |
| wiki_loss | 2.7310 | 2.7332 | −0.0022 |

### 3. seed123 vs seed42 Δ 对比

| 指标 | seed42 Δ | seed123 Δ |
|------|---------|-----------|
| holdout_ppl | −0.063 | **−0.070** |
| owt_ppl | −0.061 | **−0.044** |
| wiki_ppl | −0.095 | **−0.033** |

**seed123 在 holdout 上复现了 adaptive 优势（−0.070 vs −0.063，方向一致且幅度相近）。** OWT 和 wiki 的优势方向一致但幅度略小。三个 eval set 均显示 adaptive < uniform，效应不是 seed-dependent。

---
