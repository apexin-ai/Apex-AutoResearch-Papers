# infra mistral folio data dedup check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mistral-folio-data-dedup-check_20260522T104516_result.json`
- **Structured JSON:** [`d15763377f0a89afe359.json`](../../sessions/d1/d15763377f0a89afe359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 数据状态

| Seed | 路径 | 文件数 | 状态 | SC | SICA | Δ (SICA−SC) |
|------|------|--------|------|------|------|-------------|
| **123** | `exp052_mistral_folio204_seed123/` | 204 + results.json | **完整** ✓ | 53.92% (110/204) | 57.35% (117/204) | **+3.43%** |
| **456** | `exp053_mistral_folio204_seed456/` | 204 + results.json | **完整** ✓ | 56.37% (115/204) | 55.88% (114/204) | **−0.49%** |
| **789** | — | 0 | **不存在** ✗ | — | — | — |

### PID 575732 状态

脚本 `multiseed_mistral_folio_cuda3.sh` 按 123→456→789 顺序跑。当前正在重跑 seed 123，进度 **9/204**，ETA ~96 min。seed 123 和 456 已有完整数据，这两轮是重复计算（浪费约 **2.5 小时 GPU**），但 **seed 789 确实还没有数据**。

### 建议

**不应直接 kill**——seed 789 还需要跑。但当前脚本会先浪费 ~2.5h 重跑 123+456。更优方案：kill 当前进程，另起一个只跑 seed 789 的脚本。是否执行？

---
