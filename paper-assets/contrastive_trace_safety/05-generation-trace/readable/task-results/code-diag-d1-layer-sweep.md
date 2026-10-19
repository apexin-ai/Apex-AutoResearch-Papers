# code diag d1 layer sweep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diag_d1_layer_sweep_20260516T192941_result.json`
- **Structured JSON:** [`b278df42e4d291504588.json`](../../sessions/b2/b278df42e4d291504588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D1 Layer Sweep 完成

### 结果汇总

| Idx | Layer | Step Acc | F1     | Cross Rate | Lead Mean | Lead Median |
|-----|-------|----------|--------|------------|-----------|-------------|
| 0   | 12    | 0.8033   | 0.6379 | 0.3023     | 6.46      | 6.00        |
| 1   | 13    | 0.8082   | 0.6452 | 0.3023     | 8.85      | 8.00        |
| **2**   | **14**    | **0.8114**   | **0.6455** | 0.1860     | 8.38      | 6.00        |
| 3   | 15    | 0.7869   | 0.6086 | 0.2326     | 13.50     | 7.00        |
| 4   | 16    | 0.8000   | 0.6236 | 0.2093     | 9.78      | 8.00        |
| 5   | 17    | 0.8054   | 0.6419 | 0.1860     | 6.38      | 5.00        |
| 6   | 18    | 0.7978   | 0.6256 | 0.2093     | 8.67      | 5.00        |
| 7   | 19    | 0.7924   | 0.6340 | 0.3023     | 8.00      | 6.00        |
| 8   | 20    | 0.7831   | 0.6202 | 0.2791     | 10.00     | 6.50        |
| 9   | 21    | 0.7946   | 0.6357 | 0.3023     | 11.38     | 5.00        |
| 10  | 22    | 0.7902   | 0.6323 | 0.3023     | 7.85      | 6.00        |
| 11  | 23    | 0.8044   | 0.6504 | 0.3256     | 8.07      | 6.00        |
| 12  | 24    | 0.7978   | 0.6366 | 0.2791     | 8.33      | 7.00        |

### 结论

**Signal MODERATE** — 结论标记为 `negative`（未达 85% 阈值）。

- **Best layer**: 14 (acc=0.8114, F1=0.6455)
- **Default layer 20**: acc=0.7831，略低于平均
- 所有层 accuracy 集中在 78.3%-81.1%，层选择对性能影响很小（~3pp）
- 瓶颈不在 layer 选择，而在 probe 容量——线性 probe 不足以充分捕获 commitment signal
- Crossing rate 仅 19-33%，说明 k=5 连续阈值较严格

Registry 已更新为 DONE，artifact 已注册。

---
