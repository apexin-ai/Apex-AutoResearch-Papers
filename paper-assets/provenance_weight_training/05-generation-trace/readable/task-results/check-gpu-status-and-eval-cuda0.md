# check gpu status and eval cuda0

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_and_eval_cuda0_20260521T171631_result.json`
- **Structured JSON:** [`a2ce96887f06923f7a50.json`](../../sessions/a2/a2ce96887f06923f7a50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## 1. 4 GPU 状态表

| GPU | 实验 | Step/Total | PID | GPU Memory | Util |
|-----|------|-----------|-----|------------|------|
| cuda:0 | dr_epoch_matched_indep_lr_v2_seed42 | **2533/2533 ✅** | — (已结束) | 0 MiB / 98 GB | 0% |
| cuda:1 | bs16_adaptive_tau07_seed42 | 5247/6103 (86%) | 613357 | 90 GB | 100% |
| cuda:2 | bs16_uniform_seed42 | 4744/6103 (78%) | 620568 | 90 GB | 100% |
| cuda:3 | detect_remove_q05_v2_seed42 | 1415/6103 (23%) | 629325 | 46 GB | 100% |

## 2. cuda:0 Eval 结果 (dr_epoch_matched_indep_lr_v2_seed42)

| Metric | D&R v2 | uniform_epoch_matched | Δ |
|--------|--------|----------------------|---|
| **Holdout PPL** | **17.6505** | 18.0621 | **−0.412** |
| **OOD OWT PPL** | **18.2611** | 18.6497 | **−0.389** |
| **OOD Wiki PPL** | **15.1938** | 15.5110 | **−0.317** |

## 3. 解读

**D&R v2 在所有 3 个 eval 上都显著优于 uniform epoch-matched baseline。**

- Holdout PPL: −0.412（−2.3%）
- OWT PPL: −0.389（−2.1%）
- Wiki PPL: −0.317（−2.0%）

结论：**D&R filtering 在公平 LR 对比下仍有实质性优势，epoch confound 假说不成立。** 在相同步数 (2533) 和独立 LR schedule 下，D&R 过滤后的数据（q≤0.5, 86.4% real）训练出的模型一致优于全量 uniform 数据，说明 D&R 的增益来自数据质量提升而非训练 schedule 差异。

---
