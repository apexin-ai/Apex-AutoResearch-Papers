# urgent threshold q03 datagen submit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_threshold-q03-datagen-submit_20260516T053531_result.json`
- **Structured JSON:** [`368b0b99b2eb21f27ae4.json`](../../sessions/36/368b0b99b2eb21f27ae4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**detect_remove_baseline_seed42 最终指标：**
- train_loss: **11.003**
- epoch: 0.64, runtime: 3h40m, EXIT_CODE=0

**过滤数据集：**
| 阈值 | 样本数 | 占比 |
|------|--------|------|
| q≤0.3 | 116,935 | 31.5% |
| q≤0.7 | 184,908 | 49.8% |

**threshold_q03_seed42 已提交：**
- PID: **298800**
- GPU: **cuda:3**
- 日志: `~/runs/provenance_weight_training/threshold_q03_seed42.log`
- timeout: 6h

q07 脚本已就绪，待分配 GPU 即可提交。

---
