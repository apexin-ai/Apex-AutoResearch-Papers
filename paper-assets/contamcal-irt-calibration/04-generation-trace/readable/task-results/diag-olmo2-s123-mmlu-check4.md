# diag olmo2 s123 mmlu check4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-s123-mmlu-check4_20260520T123200_result.json`
- **Structured JSON:** [`41f279733ea8ae407a9b.json`](../../sessions/41/41f279733ea8ae407a9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**OLMo-2 s123 MMLU 结果（5/5 完成）：**

| Dosage | Accuracy |
|--------|----------|
| d000 | 55.66% |
| d005 | 56.14% |
| d025 | 54.97% |
| d050 | 55.92% |
| d100 | 55.11% |
| **Δ(d100-d000)** | **-0.55pp** |

模式：flat/noisy，无明显 contamination benefit，与 OLMo-2 s42 一致。Registry 已更新为 success。

**Gemma-2 s123 MMLU eval 已提交：**
- 服务器 westd-29999, cuda:2, tmux session `eval_gemma2_s123_mmlu`
- PID 343616, 正在加载 d000_s123 模型
- 预计 ~50min 完成 5 个 dosage

---
