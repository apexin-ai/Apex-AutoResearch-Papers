# collect ckpt1000 val8192 and submit test

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_ckpt1000-val8192-and-submit-test_20260515T013555_result.json`
- **Structured JSON:** [`eeeac16fa769994cb647.json`](../../sessions/ee/eeeac16fa769994cb647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 结果

### 1. ckpt-1000 val@8192 最终结果
| 指标 | 值 |
|------|-----|
| **Accuracy** | **88.23%** |
| **F1 macro** | **82.72%** |
| F1 fail | 73.0% (P=81.8%, R=65.8%) |
| F1 pass | 92.5% (P=89.8%, R=95.3%) |
| Unparseable | 9/9335 |

**远超 val-best 阈值 85%，比 ckpt-600 的 85.00% 高出 3.23pp。**

### 2. test@8192 已提交
- **tmux session**: `cls8b-s42-ckpt1000-test8192-eval`
- **PID**: 312975
- **GPU**: cuda:0 (空闲，0 MiB → 已开始加载模型)
- **test 集**: 9784 instances
- **Registry**: RUNNING
- 预计耗时 ~35min（按 val 的 9335 samples / 34min 推算）

### 3. s42 resume 新 checkpoint
| Checkpoint | 生成时间 |
|-----------|---------|
| checkpoint-800 | 06:34 |
| **checkpoint-1000** | 07:15 |
| **checkpoint-1200** | 07:56 |
| **checkpoint-1400** | 08:38 |
| **checkpoint-1600** | 09:19 |

训练仍在继续，每 ~40min 出一个 checkpoint。1200/1400/1600 均为新产出。

### 4. GPU 占用
| GPU | 状态 |
|-----|------|
| cuda:0 | → test@8192 eval (刚启动) |
| cuda:1 | 27.3 GB occupied (PID 295794) |
| cuda:2 | 30.7 GB occupied (PID 266816) |
| cuda:3 | 30.9 GB occupied (PID 266449) |

---
