# ssh api judges restore workers10

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_api_judges_restore_workers10_20260524T015352_result.json`
- **Structured JSON:** [`237cb234a09c24491a54.json`](../../sessions/23/237cb234a09c24491a54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 报告

### 重启前进度
| Judge | 已完成 | 总数 | 速率 |
|-------|--------|------|------|
| Sonnet | 640 | 16646 | 0.3 items/s |
| Gemini | 240 | 17175 | 0.1 items/s |
| DeepSeek | 170 | 17261 | 0.1 items/s |
| Qwen3 | 170 | 17058 | 0.1 items/s |

### 重启后 PID（--workers 10）
| Judge | PID |
|-------|-----|
| Sonnet | 506658 |
| Gemini | 506876 |
| DeepSeek | 506930 |
| Qwen3 | 506990 |

### 6 个 collect.py 全部运行中
- 4 API judges: `--workers 10` ✓
- LLaMA local (PID 503734): `--workers 4` ✓
- Qwen72B local (PID 505793): `--workers 4` ✓

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 73885 MiB | 65% |
| 1 | 90109 MiB | 100% |
| 2 | 90195 MiB | 100% |
| 3 | 0 MiB | 0% |

GPU 0-2 被 local judges 的 vLLM 占用，GPU 3 空闲。API judges 不占 GPU。

---
