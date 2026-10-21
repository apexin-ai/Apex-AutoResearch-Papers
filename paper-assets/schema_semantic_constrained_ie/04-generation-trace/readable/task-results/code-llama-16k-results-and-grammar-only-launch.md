# code llama 16k results and grammar only launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_16k_results_and_grammar_only_launch_20260518T030611_result.json`
- **Structured JSON:** [`f8dd166606612a518c86.json`](../../sessions/f8/f8dd166606612a518c86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完毕。汇总结果：

---

## Llama 16K (constrained_full) 结果

**Violation Check** (215 parsed / 31 parse failures):
| 指标 | 违规数 | 违规率 |
|------|--------|--------|
| ET (Entity Type) | 0 | 0.0% |
| EV (Event Vocab) | 0 | 0.0% |
| RoV (Role Vocab) | 0 | 0.0% |
| AC (Arg Constraint) | 159 | 3.4% |
| CF (Cross-Field) | 655 | 15.5% |
| **Go/No-go (RoV+AC)** | — | **3.41%** |

**Eval F1** (215 evaluated / 31 parse failures):
| 指标 | Precision | Recall | F1 |
|------|-----------|--------|----|
| Entity | 0.3890 | 0.1155 | **0.1781** |
| Trigger ID | 0.0865 | 0.0717 | **0.0784** |
| Argument | 0.0105 | 0.0115 | **0.0110** |

## Llama grammar_only 启动确认

- PID: 521758
- GPU: cuda:1, 16348MiB 占用
- tmux session: `llama_grammar_only`
- 模型加载完成，已开始推理

---
