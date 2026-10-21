# code 14b rsft eval launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-rsft-eval-launch_20260520T205016_result.json`
- **Structured JSON:** [`ee934a979eae59bcadd6.json`](../../sessions/ee/ee934a979eae59bcadd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

14B RSFT eval 已启动。

| 项目 | 值 |
|---|---|
| **PID** | 53413 (python), 53407 (bash wrapper) |
| **GPU** | cuda:0, 32503 MiB / 97887 MiB |
| **进度** | 985 docs, ~5s/doc |
| **预估完成** | ~82 min (~1.4h) |
| **输出目录** | `/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval/` |
| **日志** | `/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval.log` |
| **Registry** | `plan017_14b_rsft_eval` → RUNNING |

Nested LoRA 加载确认：base(Qwen3-14B) → merge SFT(checkpoint-144) → load RSFT adapter。与 4B/8B 流程一致。

---
