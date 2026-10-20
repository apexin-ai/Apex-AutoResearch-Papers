# code p0 contamination 60 datagen

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0_contamination_60_datagen_20260515T193111_result.json`
- **Structured JSON:** [`075d8b0be189fea25cea.json`](../../sessions/07/075d8b0be189fea25cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出摘要：**

| 项目 | 值 |
|------|------|
| 文件 | `/root/provenance_weight_training/data/scored_data_60.jsonl` (907MB) |
| 行数 | 371,499（与 scored_data.jsonl 一致） |
| Synthetic (depth=1) | 222,900 (60.00%) |
| Human (depth=0) | 148,599 (40.00%) |
| q_score | mean=0.6243, std=0.3703, median=0.7753 |
| 对比原始 | 原始 mean=0.5987, median=0.7049（ρ=0.6 的 mean/median 更高，符合预期：更多 synthetic → 更高 q_score） |
| 脚本 | `scripts/prepare_rho06_data.py`（已更新，支持固定总行数模式） |

---
