# diagnose extract r4 step30 40 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_extract-r4-step30-40-check_20260514T172912_result.json`
- **Structured JSON:** [`5591693e4a17be1e3257.json`](../../sessions/55/5591693e4a17be1e3257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

270 秒后回来检查 checkpoint-30。目前观察：
- extract_r4 从 step 10 起已陷入 mode collapse（frac_zero_std=0.8, f1=0）
- 模型只优化 format_reward（从 0.17→0.29），完全放弃了 f1_reward
- grad_norm 虽从 0.005 回升到 0.198，但未转化为 f1 改善
- 与 ced_kl001_r4 相比，ced 在 step 20 时 frac 已降到 0.1 且 f1=0.003 开始恢复，而 extract_r4 在 step 20 仍是 frac=0.8/f1=0，情况明显更差

---
