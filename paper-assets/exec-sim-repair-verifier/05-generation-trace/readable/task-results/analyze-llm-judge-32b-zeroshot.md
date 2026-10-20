# analyze llm judge 32b zeroshot

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llm-judge-32b-zeroshot_20260512T082016_result.json`
- **Structured JSON:** [`b9d51bdb2299b1f38fd4.json`](../../sessions/b9/b9d51bdb2299b1f38fd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

**结论：SUCCESS** — Fine-tuned 4B 的 Pareto 优势得到确认。

| 指标 | 32B zero-shot | 8B zero-shot | Fine-tuned 4B |
|------|:---:|:---:|:---:|
| Accuracy | 71.69% | 64.4% | **88.41%** |
| Fail P / R / F1 | 64.4 / 92.4 / 75.9 | 57.9 / 95.8 / 72.2 | ~88.4 / ~88.4 / **88.40** |
| Pass P / R / F1 | 88.1 / 52.4 / 65.7 | 90.0 / 35.1 / 50.5 | ~88.4 / ~88.4 / **88.41** |
| Traj. accuracy | 99.1% | — | — |

关键发现：
- 8B→32B（4x 参数量）仅提升 7.3pp accuracy，距 fine-tuned 4B 仍差 16.7pp
- Zero-shot 模型存在系统性 FAIL 偏向（fail recall>92%, pass recall<53%），fine-tuning 消除了这一偏差
- Wall clock 471s，0.13 GPU-hours

---
