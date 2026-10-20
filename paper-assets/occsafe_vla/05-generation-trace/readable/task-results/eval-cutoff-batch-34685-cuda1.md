# eval cutoff batch 34685 cuda1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cutoff_batch_34685_cuda1_20260527T163924_result.json`
- **Structured JSON:** [`d86df4e6f4cd1e52788d.json`](../../sessions/d8/d86df4e6f4cd1e52788d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成，结果如下：

## 汇总

**两台服务器上所有 cutoff/reverse_cutoff 50K checkpoint：**

| 服务器 | checkpoint 目录 | eval 状态 |
|--------|----------------|-----------|
| westd-10894 | cutoff_15k_s1 | cutoff_15k_s1_eval ✓ (CAR=0.76) |
| westd-34685 | cutoff_25k_s1_v2 | cutoff_25k_s1_v2_eval ✓ (CAR=0.788) |

**所有 12 个已成功的 eval 均已有结果，无需重跑。**

**唯一的缺口：`reverse_cutoff_s2_v2_eval`**（训练成功但 eval failed），但 checkpoint 目录 `/root/autodl-tmp/checkpoints/reverse_cutoff_s2_v2` 在 westd-10894 和 westd-34685 上均已被删除，无法重新 eval。

没有"磁盘上有 50K checkpoint 但完全没 eval 记录"的实验。

**结论：无 eval 可跑。** `reverse_cutoff_s2_v2` 如果需要补数据，需要重新训练。

---
