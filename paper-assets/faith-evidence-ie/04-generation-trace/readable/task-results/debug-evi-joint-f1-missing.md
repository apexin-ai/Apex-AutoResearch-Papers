# debug evi joint f1 missing

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_evi_joint_f1_missing_20260515T235451_result.json`
- **Structured JSON:** [`3498a8461b18169b2e4d.json`](../../sessions/34/3498a8461b18169b2e4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 根因分析

`compute_evi_f1_joint` 方法后来才加入 evaluator.py，`evaluate()` 方法调用了它。**之前跑的 18 个 eval 用的是旧版 evaluator，不包含 joint 计算**，所以 metrics.json 里没有 `evi_f1_joint` 字段。

## 补算结果

已从 predictions.json 重新计算并写入所有 18 个缺失目录的 metrics.json。验证：
- 15 个已有 joint 的方法，重算值与原值完全一致（0 mismatch）
- joint ≤ conditional 对所有方法成立

## 汇总表（论文关注的 RSFT-CED 方法）

| Method | Cond Evi-F1 | Joint Evi-F1 | Rel F1 |
|--------|------------|-------------|--------|
| rsft_r1 | 0.8187 | 0.3468 | 0.4449 |
| rsft_r2a | 0.8108 | 0.3509 | 0.4494 |
| rsft_r2b | 0.8128 | 0.3490 | 0.4493 |
| rsft_r2b_maxtok1536 | 0.8102 | 0.3488 | 0.4504 |
| rsft_s43 | 0.8156 | **0.3711** | **0.4683** |
| rsft_s44 | 0.8087 | **0.3713** | 0.4655 |

Joint Evi-F1 与 Rel F1 高度正相关（rel_f1 越高，FN 越少，joint 越接近 conditional），符合预期。

脚本位于 `/root/autodl-tmp/scripts/recompute_joint_evi_f1.py`，支持 `--dry-run`。

---
