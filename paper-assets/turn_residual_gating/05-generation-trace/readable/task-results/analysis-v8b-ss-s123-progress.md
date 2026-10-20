# analysis v8b ss s123 progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v8b_ss_s123_progress_20260521T131054_result.json`
- **Structured JSON:** [`2e2c342b865ed63c06c6.json`](../../sessions/2e/2e2c342b865ed63c06c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v8b SS s123 训练状态:**

| 指标 | 值 |
|------|-----|
| 进程 | PID 221735 运行中，已运行 8h 42m |
| GPU | 83% 利用率，30,977 MiB 显存 |
| 当前位置 | Epoch 2, Step 3900 (microstep) |
| 总进度 | 19,900 / 24,000 microsteps = **82.9%** |
| 预计剩余 | ~1h 48m |

**训练指标正常：**
- L_NTP: 0.68 ~ 1.11（正常波动）
- L_GAR: 极小（≤0.005），L_DIV: 0
- Gate mean: ~0.92-0.96，稳定
- SS ratio: 0.500，scheduled sampling 正常运行

相比上次检查（~19,700, 82.1%），推进了约 200 microsteps，速度正常。预计再 ~1h48m 完成。

---
