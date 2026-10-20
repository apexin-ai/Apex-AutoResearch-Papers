# infra status check all servers

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-check-all-servers_20260519T111808_result.json`
- **Structured JSON:** [`fa32f8857cd304fa8fde.json`](../../sessions/fa/fa32f8857cd304fa8fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

**实际 RUNNING: 6 个 | FINISHED: 2 个**（Registry 显示 10 个 RUNNING 不准确）

### westd-25068
| 实验 | 模型 | GPU | 状态 | 进度 |
|------|------|-----|------|------|
| exp-062 | Gemma-27B | cuda:3 | RUNNING | 80/204 (39%) |
| exp-065 | Qwen2.5-7B | cuda:0 | RUNNING | 262/600 (44%) |
| exp-066 | Qwen2.5-14B | cuda:1 | RUNNING | 198/204 (97%) 即将完成 |
| exp-067 | Mistral-7B | - | **FINISHED** | 结果文件已生成 (314KB) |

空闲: **cuda:2**

### westd-16639
| 实验 | 模型 | GPU | 状态 | 进度 |
|------|------|-----|------|------|
| exp-048 | LLaMA-8B | cuda:3 | RUNNING | 419/600 (70%) |
| exp-063 | LLaMA-8B | - | **FINISHED** | SICA=61.8%, SC=66.2%, 结果文件已生成 (300KB) |
| exp-064 | DeepSeek-R1-8B | cuda:2 | RUNNING | 52/204 (25%) |
| exp-068 | Qwen3-14B | cuda:1 | RUNNING | 11/200 (6%) 刚启动 |

空闲: **cuda:0**

额外发现：westd-25068 还有旧 tmux session（exp033/034/035_run, model_dl_25068），无 GPU 占用，可清理。

报告已写入 `artifacts/status_check_20260519.md`。

---
