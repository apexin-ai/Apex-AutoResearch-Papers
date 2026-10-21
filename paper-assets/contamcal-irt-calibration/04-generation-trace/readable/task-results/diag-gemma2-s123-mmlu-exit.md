# diag gemma2 s123 mmlu exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-s123-mmlu-exit_20260520T133133_result.json`
- **Structured JSON:** [`cf0836ca55e3f0a5753d.json`](../../sessions/cf/cf0836ca55e3f0a5753d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Gemma-2 s123 MMLU** — 5/5 完成，registry 已标记 DONE：

| Dosage | Accuracy | vs d000 |
|--------|----------|---------|
| d000 | 0.6584 | — |
| d005 | 0.6581 | -0.03pp |
| d025 | 0.6302 | -2.82pp |
| d050 | 0.6674 | +0.90pp |
| d100 | 0.6733 | **+1.49pp** |

s42 是 +3.76pp，s123 只 +1.49pp，且 d025 有 -2.82pp 的 dip（非单调）。

**Qwen-14B s123 MMLU** — 已提交到 westd-29999 cuda:2，tmux session `eval_qwen14b_s123_mmlu` 运行中，模型已加载（28731 MiB）。

---
