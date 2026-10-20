# analysis math500 table compilation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math500_table_compilation_20260521T200734_result.json`
- **Structured JSON:** [`0c1ce3520e5d024e65c0.json`](../../sessions/0c/0c1ce3520e5d024e65c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/_project/report/math500_2048_full_table.md`（`art_20260521_598c93`）。

**现状汇总**:

**有结果的 cell（5个）**:
| 配置 | Accuracy |
|------|----------|
| Dense GRPO | 69.0% |
| CKA-only 20% GRPO | 29.2% |
| Standard 20% SFT | 25.8% |
| CKA-only 25% GRPO | 18.4% (inline) |
| Standard 25% SFT | 13.0% |

**进行中（2个）**: CKA-only 20% SFT (v6)、Standard 25% SFT (2048)

**P0 缺失（需要立即补跑）**:
1. **GRPO Standard 20%** — checkpoint 在，没有 MATH-500 eval
2. **GRPO RASP 20%** — v3 failed（服务器释放），需要 v4
3. **SFT RASP 20%** — checkpoint 在，没有 MATH-500 eval

**Cross-benchmark**: MATH/GSM ratio 在 0.31–0.45 之间，MATH-500 对剪枝模型的打击远大于 GSM8K。CKA-only 20% GRPO 的 ratio 最高（0.454），说明 CKA-only 在难题上的保留能力相对更好。

---
