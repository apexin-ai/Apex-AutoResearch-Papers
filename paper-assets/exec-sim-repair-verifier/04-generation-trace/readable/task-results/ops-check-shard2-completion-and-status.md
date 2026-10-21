# ops check shard2 completion and status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-shard2-completion-and-status_20260516T053030_result.json`
- **Structured JSON:** [`58e0748498c0d88fad20.json`](../../sessions/58/58e0748498c0d88fad20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 组件 | 状态 | 进度 | 备注 |
|------|------|------|------|
| **shard2** (idx 7680-9783) | **DONE** | 2104/2104 (100%) | acc=66.54%, f1_macro=54.2%, unparseable=1568 |
| **shard3** (idx 6200-7679) | RUNNING (PID 453335) | 1464/1480 (98.9%) | 即将完成 |
| **v3** (idx 0-?) | 需确认 | 7720 行 | 进程状态未查 |
| **shard4** | DONE | 688/688 | 已知完成 |
| **DeepSeek 下载** | **DONE** | — | PID 464106 已退出，模型文件齐全 (safetensors ×2 + config + tokenizer) |

**GPU 利用率：**
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 21133 MiB | 88% |
| 1 | 0 MiB | 0% |
| 2 | 0 MiB | 0% |
| 3 | 21133 MiB | 88% |

GPU 0 和 3 在跑 shard3（及可能的 v3），GPU 1 和 2 空闲。shard3 还差 ~16 条，预计几分钟内完成。DeepSeek 模型已下载完毕可用。Registry 已将 shard2 标记为 DONE/success。

---
