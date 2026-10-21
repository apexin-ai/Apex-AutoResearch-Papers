# analysis cwm eval final results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-eval-final-results_20260514T120624_result.json`
- **Structured JSON:** [`814374f9270fb425f3a2.json`](../../sessions/81/814374f9270fb425f3a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前状态汇报

### GPU 使用
| GPU | 任务 | VRAM |
|-----|------|------|
| 0 | CWM seed123 eval | 13.0/32.6 GB |
| 1 | CWM v12 eval | 13.0/32.6 GB |
| 2 | CWM 8B train | 31.5/32.6 GB |
| 3 | CLS 8B seed123 train | 23.6/32.6 GB |

### CWM Eval 进度（仍在跑）
| 模型 | 进度 | running_acc | 剩余 | ETA |
|------|------|-------------|-------|-----|
| CWM v12 | 6296/9784 (64.3%) | 57.8% | ~3488 samples | ~02:10 AM May 15 |
| CWM seed123 | 6216/9784 (63.5%) | 58.8% | ~3568 samples | ~02:20 AM May 15 |

速率约 9.5 samples/min，还需 **~6 小时**完成。

### 8B 训练进度
| 模型 | 进度 | 速率 | ETA |
|------|------|------|-----|
| CWM 8B (seed42) | 988/6633 (14.9%) | ~12.3s/step | ~May 15 15:00 |
| CLS 8B (seed123) | 1800/6633 (27.1%) | ~8.2s/step | ~May 15 07:10 |

CLS 8B 刚完成 step 1800 的 eval checkpoint，eval_loss = **0.2101**。

---

CWM eval 距离完成还有约 6 小时，不适合轮询等待。需要我设置定时检查（比如明早自动查结果并执行 4 项分析），还是你稍后手动触发？

---
