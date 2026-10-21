# ops falcon3 d100 s123 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-d100-s123-eval_20260523T003029_result.json`
- **Structured JSON:** [`3eb667e3e495bc029edd.json`](../../sessions/3e/3eb667e3e495bc029edd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

| 项目 | 状态 |
|------|------|
| Adapter 存在 + lora_alpha=32 | ✓ |
| evaluate.py md5 匹配 | ✓ |
| GPU 0 空闲确认 (C001/C002) | ✓ |
| CUDA_VISIBLE_DEVICES=0 显式设置 (C004) | ✓ |
| PID | **750911** |
| GPU 占用 | 15603MiB / 24564MiB, 96% util |
| tmux session | `falcon3_eval_s123` |
| Registry | `eval_falcon3_d100_s123` → RUNNING |
| 预计完成 | ~12 min（MMLU ~20 it/s + ARC） |

---
