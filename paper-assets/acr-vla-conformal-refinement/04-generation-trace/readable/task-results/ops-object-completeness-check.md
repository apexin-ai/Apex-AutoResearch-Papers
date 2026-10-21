# ops object completeness check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_object-completeness-check_20260521T184957_result.json`
- **Structured JSON:** [`61b6ca5c79af99121524.json`](../../sessions/61/61b6ca5c79af99121524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总：

---

## 结果

### 1. bjb2-40593 残留进程清理
PID 872656 已 kill，GPU 已完全释放（0 MiB, 0% util）。

### 2. bjb1-32546 precompute 状态
无 precompute 进程运行，所有 shard 已完成。

### 3. 各 shard partial 文件统计

| Shard | 文件数 | save_every | 覆盖范围 | 样本数 | 状态 |
|-------|--------|-----------|----------|--------|------|
| **0** | 71 (bjb2) / 65 (bjb1-18228) | 100 (+部分500重叠) | 0–6900 | **6,900** | **不完整** (被kill中断) |
| 1 | 15 | 500 | 0–7251 | 7,251 | 完整 |
| 2 | 15 | 500 | 0–7251 | 7,251 | 完整 |
| 3 | 15 | 500 | 0–7251 | 7,251 | 完整 |
| 4 | 15 | 500 | 0–7251 | 7,251 | 完整 |
| 5 | 73 | 100 | 0–7251 | 7,251 | 完整 |
| 6 | 41 | 100→500 | 0–7251 | 7,251 | 完整 |
| 7 | 73 | 100 | 0–7251 | 7,251 | 完整 |
| 8 | 73 | 100 | 0–7251 | 7,251 | 完整 |
| 9 | 73 | 100 | 0–7251 | 7,251 | 完整 |

### 4. 总样本数估算

- Shard 1–9 全部完整：9 × 7,251 = **65,259**
- Shard 0 缺尾部：**6,900**（缺 ~351 samples，进程被 kill 中断）
- **可用总计：72,159 / ~72,510 = 99.5%**

### 5. 是否需要 retrain

**不需要。** rsync + merge 后可达 72,159 samples（99.5%），远超 98% 阈值。shard0 仅缺 ~351 samples（0.5%），对训练影响可忽略。

---
