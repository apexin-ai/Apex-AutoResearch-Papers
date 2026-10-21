# code llama beam scierc 551

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_beam_scierc_551_20260517T025416_result.json`
- **Structured JSON:** [`050d8e69ef0563e040b6.json`](../../sessions/05/050d8e69ef0563e040b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已启动，汇报状态：

**运行中 - Llama SciERC Beam Search 551 docs**

| 项目 | 值 |
|------|-----|
| Model | Llama-3.1-8B-Instruct (ZS) |
| Path | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct` |
| Decoding | beam_size=4, full_s1 |
| Dataset | SciERC 551 docs |
| PID | 406047 |
| tmux session | `llama_beam` |
| Output | `outputs/llama_scierc_beam_full_s1_551.jsonl` |
| Log | `outputs/llama_scierc_beam_full_s1_551.log` |
| GPU | cuda:0, 16.5GB used, 82% util |
| Progress | 14/551 processed (~2.5 min elapsed) |
| ETA | ~50 min |

预计运行约 50 分钟。完成后需运行 violation_checker + F1 eval 收集最终结果。

---
