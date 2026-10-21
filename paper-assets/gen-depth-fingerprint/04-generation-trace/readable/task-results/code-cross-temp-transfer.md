# code cross temp transfer

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-temp-transfer_20260517T124518_result.json`
- **Structured JSON:** [`601ce4fb22a0fd86589d.json`](../../sessions/60/601ce4fb22a0fd86589d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

| Condition | Binary F1 | 3-class F1 |
|-----------|-----------|------------|
| 0.7→0.7 (baseline) | 0.9471 | 0.7888 |
| 0.7→1.0 (cross-temp) | 0.9001 | 0.7225 |
| 1.0→1.0 (baseline) | 0.9107 | 0.7257 |
| 1.0→0.7 (cross-temp) | 0.9581 | 0.7913 |

**Cross-temp deltas:**
- 0.7-trained → test on 1.0: binary -4.7pp, 3-class -6.6pp
- 1.0-trained → test on 0.7: binary +4.7pp, 3-class +6.6pp

**关键发现：** 性能变化几乎完全来自 qwen3-1.7b fold。其他 5 个 generator 的数据在两个温度数据集中相同，per-gen F1 不变。qwen3-1.7b 的 3-class F1 从 within-temp 的 ~0.81 / ~0.42 降到 cross-temp 的 ~0.42 / ~0.81，说明温度变化主要影响该 generator 的 depth signal 强度，但 LOGO 整体平均仍保持 >0.72 (3-class) 和 >0.90 (binary)。

脚本：`cross_temp_transfer.py`，结果：`results/cross_temp_transfer.json`，已注册 artifact。

---
