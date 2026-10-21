# code exp16 llama datagen run

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-llama-datagen-run_20260519T143719_result.json`
- **Structured JSON:** [`155856c52102acaaab87.json`](../../sessions/15/155856c52102acaaab87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已成功启动：

| 任务 | tmux session | GPU | 状态 |
|------|-------------|-----|------|
| Jailbreak (crescendo) | `exp16_llama_jailbreak_gen` | cuda:0 (15.5GB) | 模型已加载，从第 3 条续传（248 remaining） |
| Benign | `exp16_llama_benign_gen` | cuda:1 | 模型加载中，250 条 |

Jailbreak 脚本正确识别了 2 条已有数据并从第 3 条续传。benign 输出到 `data/cross_llm/benign_llama.jsonl`。预计 ~4 小时完成。

---
