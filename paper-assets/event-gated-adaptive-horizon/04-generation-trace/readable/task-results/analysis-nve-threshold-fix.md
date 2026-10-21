# analysis nve threshold fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve-threshold-fix_20260517T124824_result.json`
- **Structured JSON:** [`1818d045553847519769.json`](../../sessions/18/1818d045553847519769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

**`nve_threshold_sensitivity.json` 已更新：**
- 添加 exp_008e_v3_s2（NVE 3.78x @105K, label=0, IRD failure mode）
- 12 experiments (3 pos / 9 neg)
- Threshold 1.5x: accuracy=11/12=0.917, precision=3/4=0.75, recall=1.0, F1=6/7=0.857
- AUROC = 25/27 = 0.926

**发现的额外问题：论文 AUROC=0.933 是错的。**
- 论文 B2 task 用 8 个非 baseline 实验 (3 pos / 5 neg)，声称 AUROC=0.933=14/15
- 实际 exp_008e_v3_s2 (3.78) 高于两个 positive (1.619, 1.528)，产生 2 个 discordant pairs
- 正确 AUROC = 13/15 = 0.867

**"7/8" vs "11/12" 口径差异：**

| 口径 | 实验数 | Pos/Neg | Accuracy @1.5x | AUROC |
|------|--------|---------|-----------------|-------|
| 非 baseline (论文 B2) | 8 | 3/5 | 7/8=0.875 | 0.867 |
| 全部实验 (JSON) | 12 | 3/9 | 11/12=0.917 | 0.926 |

详细说明见 `artifacts/analysis/nve_sensitivity_audit_note.md`。

---
