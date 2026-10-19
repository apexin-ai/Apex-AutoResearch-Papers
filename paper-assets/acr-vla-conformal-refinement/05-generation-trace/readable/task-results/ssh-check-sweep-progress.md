# ssh check sweep progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-sweep-progress_20260520T015045_result.json`
- **Structured JSON:** [`adca137fb800dd520169.json`](../../sessions/ad/adca137fb800dd520169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实验仍在运行中，无 JSON 输出。进度汇总（每个实验 10 tasks，每 task 10 rollouts）：

### bjb2-28827（6 个实验）
| 实验 | 完成 tasks |
|------|-----------|
| p75-seed42 | **7/10** |
| p75-seed43 | 6/10 |
| p50-seed42 | 6/10 |
| p90-seed43 | **7/10** |
| p90-seed44 | 6/10 |
| p25-seed43 | 5/10 |

### bjb1-32546（4 个实验）
| 实验 | 完成 tasks |
|------|-----------|
| **p75-seed44** | **8/10** ← 最快 |
| p90-seed42 | 7/10 |
| p50-seed44 | 7/10 |
| p25-seed42 | 6/10 |

### bjb2-40593（1 个实验）
| 实验 | 完成 tasks |
|------|-----------|
| p25-seed44 | 2/10 ← 最慢 |

**最快的是 bjb1 上的 p75-seed44（8/10）**，还剩 2 个 tasks（~20 rollouts），预计很快完成。bjb2-28827 上的 p75-seed42 和 p90-seed43 紧随其后（7/10）。bjb2-40593 上只跑了 1 个实验且进度最慢（2/10）。

总计 11 个实验在跑，整体完成度约 60-80%。

---
