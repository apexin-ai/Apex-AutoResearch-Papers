# urgent home ckpt600 val4096 result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_home-ckpt600-val4096-result_20260514T140057_result.json`
- **Structured JSON:** [`d8553a6e8afc1fbaf79b.json`](../../sessions/d8/d8553a6e8afc1fbaf79b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果汇总

### ckpt-600 val@4096 指标
| 指标 | 值 |
|------|-----|
| accuracy | 79.18% |
| f1_macro | 70.73% |
| fail_f1 | 55.00% |
| pass_f1 | 86.45% |
| fail_recall | 52.75% |
| unparseable | 1406 (15.1%) |
| gap_vs_majority | +3.3pp |

### val@4096 对比：ckpt-600 vs ckpt-400

| 指标 | ckpt-600 | ckpt-400 | 差异 |
|------|----------|----------|------|
| accuracy | 79.18% | **82.57%** | -3.39pp |
| f1_macro | 70.73% | **71.24%** | -0.51pp |
| fail_f1 | **55.00%** | 53.18% | +1.82pp |
| fail_recall | **52.75%** | 41.00% | +11.75pp |

### 排序一致性

| 评估设置 | 更优 checkpoint |
|----------|----------------|
| test@2048 | **ckpt-600** (80.73% vs 75.05%) |
| val@4096 | **ckpt-400** (82.57% vs 79.18%) |

**排序不一致。** val@4096 偏好 ckpt-400（accuracy 更高，因为 pass-biased 策略在高 pass-rate val set 上受益），而 test@2048 偏好 ckpt-600。值得注意的是 ckpt-600 的 fail_recall 高很多（52.75% vs 41%），说明 ckpt-600 更均衡，ckpt-400 靠牺牲 fail_recall 换 accuracy。

### GPU 状态
home-1x5090 cuda:0 空闲（0% 利用率，0 MiB 显存），等待分配下一任务。

---
