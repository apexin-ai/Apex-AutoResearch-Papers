# ops gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260515T193650_result.json`
- **Structured JSON:** [`aad3b6948e5c48669c3f.json`](../../sessions/aa/aad3b6948e5c48669c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### GPU 利用率
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 71,595 / 97,887 MiB (73%) | 100% |
| cuda:1 | 41,191 / 97,887 MiB (42%) | 100% |

### deepseek_exception_only_seed123 (cuda:0)
- **进度**: 341/444 (77%)
- **已用时间**: ~1h17m
- **当前速度**: ~13.8s/it
- **预估剩余**: ~24 min

### vota_seed456 (cuda:1)
- **进度**: 217/444 (49%)
- **已用时间**: ~1h05m
- **当前速度**: ~17.3s/it
- **预估剩余**: ~65 min

两个实验均正常运行，GPU 利用率 100%。deepseek 实验预计约 25 分钟完成，vota 实验约 1 小时后完成。

---
