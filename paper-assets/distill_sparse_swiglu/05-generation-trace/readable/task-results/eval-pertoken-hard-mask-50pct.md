# eval pertoken hard mask 50pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pertoken_hard_mask_50pct_20260517T083639_result.json`
- **Structured JSON:** [`310136af095bd1183776.json`](../../sessions/31/310136af095bd1183776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**d_b=256 per-token hard mask PPL = 8.5862**

完整退化分解：

| 配置 | WikiText-2 PPL |
|------|---------|
| Dense | 6.12 |
| Per-token hard (d_b=256) | **8.59** |
| Per-token hard (d_b=128) | 9.22 |
| Global hard (d_b=256, teal_global) | 11.79 |
| TEAL vanilla (magnitude, global) | 23.31 |

d_b=256 per-token (8.59) 确实优于 d_b=128 (9.22)，符合预期。退化链：Dense → Per-token hard 贡献 +2.47 PPL（predictor 误差），Per-token → Global hard 贡献 +3.20 PPL（token 间分配不均），Global hard → TEAL vanilla 贡献 +11.52 PPL（magnitude 选择能力差距）。

---
