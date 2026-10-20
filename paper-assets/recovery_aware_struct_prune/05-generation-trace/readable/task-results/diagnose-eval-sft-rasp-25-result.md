# diagnose eval sft rasp 25 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_rasp_25_result_20260516T191443_result.json`
- **Structured JSON:** [`910b28bf8d0ffdfd81e7.json`](../../sessions/91/910b28bf8d0ffdfd81e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **52.99%** (699/1319) |
| Stderr | ±1.37% |
| EOS rate | 91.8% (108 truncated) |
| Mode | greedy (T=0) |

Registry 已更新为 DONE/success。westb cuda:0 已释放，无进程占用。

对比 20% sparsity 结果（RASP 57% vs Standard 64%），25% sparsity 下 RASP post-SFT 降至 53%，gap 在扩大。等 eval_sft_standard_25 完成后可做完整对比。

---
