# diag exp039 040 dir mapping

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp039-040-dir-mapping_20260518T222737_result.json`
- **Structured JSON:** [`08a467c462c73347cb7f.json`](../../sessions/08/08a467c462c73347cb7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 目录 ↔ Registry 映射表

| Registry exp_id | 实际目录名 | tmux session | 模型 | 端口 | GPU |
|---|---|---|---|---|---|
| **exp-039** | `exp032_qwen25_14b_pw600` | `exp032` | Qwen2.5-14B-Instruct | 8000 | GPU 0 |
| **exp-040** | `exp033_qwen3_14b_pw600_nonthinking` | `exp033` | Qwen3-14B (thinking=false) | 8001 | GPU 1 |

另外发现 GPU 2-3 上还跑着两个额外实验（`exp049b`/`exp050b`），都是 Mistral-7B-Instruct-v0.3 跑 LogiQA。

### 当前进度

| 实验 | 已完成 | 总数 | 进度 | 运行时长 | 预估剩余 |
|---|---|---|---|---|---|
| exp032 (Qwen2.5-14B) | 263 | 600 | 43.8% | ~4h44m | ~6h |
| exp033 (Qwen3-14B) | 162 | 600 | 27.0% | ~4h43m | ~12.8h |

两个实验均在正常运行中（HTTP 200，GPU 100% 利用率）。exp033 比 exp032 慢约一倍，Qwen3-14B 即使关了 thinking 推理速度仍然较慢。

---
