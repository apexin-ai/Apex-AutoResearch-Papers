# diag gemma2 mmlu s0 eval completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-mmlu-s0-eval-completion_20260520T223248_result.json`
- **Structured JSON:** [`9d47d737c82bc1fd7522.json`](../../sessions/9d/9d47d737c82bc1fd7522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Eval 仍在运行，尚未完成。**

已完成的结果：
| Dosage | 5-shot Accuracy | Sweep 内置 | 匹配？ |
|--------|----------------|-----------|--------|
| d000 | 64.88% | 64.88% | ✓ 完全一致 |
| d005 | 64.14% | 64.14% | ✓ 完全一致 |
| d025 | 运行中 (49%) | 64.91% | — |
| d050 | 未开始 | 63.09% | — |

cuda:1 当前 89% 利用率、24GB 显存占用，eval 进程正常运行中。预估 d025 还需约 10 分钟完成，d050 需要再加约 20 分钟。

进程并未退出，cron 检测可能误报。等全部完成后再更新 registry。

---
