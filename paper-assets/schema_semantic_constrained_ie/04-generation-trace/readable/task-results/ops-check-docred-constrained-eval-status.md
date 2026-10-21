# ops check docred constrained eval status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-docred-constrained-eval-status_20260516T020406_result.json`
- **Structured JSON:** [`a599a13f07d6acce7232.json`](../../sessions/a5/a599a13f07d6acce7232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. w5_llama_docred_lora_constrained_eval
| 项目 | 值 |
|------|-----|
| **状态** | RUNNING |
| **进度** | **387/998** (38.8%) |
| **运行时间** | 1h37m |
| **PID** | 317464 (wrapper), 317469 (GPU) — 均存活 |
| **GPU** | cuda:0, 86% util, 16825/97887 MiB |
| **速率** | ~4.0 docs/min (~15s/doc) |
| **预计剩余** | ~2.5h (约 04:40 UTC 完成) |
| **输出文件** | `/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl` |
| **异常** | 3 个 FAIL（#51, #52, #297）— 超时 ~66s，E=0 R=0 |

### 2. w5_qwen_docred_lora_constrained_eval
| 项目 | 值 |
|------|-----|
| **状态** | RUNNING |
| **进度** | **28/998** (2.8%) |
| **运行时间** | ~10m |
| **PID** | 321568 — 存活 |
| **GPU** | cuda:1, 84% util, 17193/97887 MiB |
| **速率** | ~2.8 docs/min (~21s/doc) |
| **预计剩余** | ~5h46m (约 07:55 UTC 完成) |
| **输出文件** | `/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl` |
| **异常** | 暂无，刚启动不久 |

两个实验均正常运行，进度符合预期。Qwen 比 Llama 慢约 40%（21s vs 15s per doc）。

---
