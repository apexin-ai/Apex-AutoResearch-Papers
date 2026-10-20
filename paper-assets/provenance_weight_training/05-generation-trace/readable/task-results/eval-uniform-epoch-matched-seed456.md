# eval uniform epoch matched seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_uniform_epoch_matched_seed456_20260522T111446_result.json`
- **Structured JSON:** [`1c47f9c23c246d2a34b2.json`](../../sessions/1c/1c47f9c23c246d2a34b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，registry 已更新为 DONE/success。

## 结果汇总

| 数据集 | seed456 PPL | seed42 PPL | 差异 |
|--------|-------------|------------|------|
| holdout | 18.068 | 18.062 | +0.006 (+0.03%) |
| owt | 18.660 | 18.650 | +0.010 (+0.05%) |
| wiki | 15.515 | 15.511 | +0.004 (+0.03%) |

**两个 seed 的结果高度一致**，差异 <0.1%，确认 uniform epoch-matched baseline 的 PPL 非常稳定。

**与 D&R epoch-matched 对比**：
- holdout: uniform 2-seed avg ≈ 18.065 vs D&R 3-seed avg ≈ 17.654 → uniform 高 **2.3%**
- owt: uniform ≈ 18.655 vs D&R ≈ 18.28 → uniform 高 **2.1%**
- wiki: uniform ≈ 15.513 vs D&R ≈ 15.19 → uniform 高 **2.1%**

**结论确认：在公平 LR schedule (independent linear) 下，uniform epoch-matched 在全部三个评估集上 PPL 均显著高于 D&R epoch-matched（约 2%），且跨 seed 高度稳定。**

---
