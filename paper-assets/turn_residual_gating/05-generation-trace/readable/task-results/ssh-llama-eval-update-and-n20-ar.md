# ssh llama eval update and n20 ar

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama_eval_update_and_n20_ar_20260522T074856_result.json`
- **Structured JSON:** [`63f6d459a9f659ed47ec.json`](../../sessions/63/63f6d459a9f659ed47ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 正在运行，模型已加载，开始 Base + GAR-ours AR eval。

**eval_llama_lora_only_s42 结果汇总：**

| | GAR-ours (mid) | GAR-dongre (mid) | PPL |
|---|---|---|---|
| **TF** (N=50, T=4) | nGAR=11.80 | nGAR=0.83 | 2.60 |
| **AR** (N=5, T=10) | raw=0.062, nGAR=0.61 | raw=0.023, nGAR=0.25 | 1.32 |

Registry 已更新（status=DONE, conclusion=success, metrics 完整）。

**eval_llama_ar_n20 已提交：**
- 6 个 eval（3 条件 × 2 GAR variant），N=20, T=4, ar-from-fixed
- PID=312592, tmux=eval_llama_ar_n20, GPU=cuda:0
- 预计运行 ~1-2 小时（每个 eval ~10-20 min，6 个串行）

---
